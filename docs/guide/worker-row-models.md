---
title: Worker 行モデルガイド（実験的）
---

> ⚠️ **実験的な機能です。** `experimental-worker-plugin` エントリーポイントは、フィードバックを集めるために公開している概念実証です。API はどのリリースでも変更・削除される可能性があり、意図的に安定版の API からは外しています。おそらく、極端なユースケースにしか向きません。おおまかな目安として、**クライアントで 100,000 行以上**を処理するのでなければ、使わないでください。その規模のテーブルの多くは、まずサーバーサイドでの処理（`manual*` オプション）、ページネーション、仮想化で対応したほうがうまくいきます。

## 何をするのか {#what-it-does}

Worker プラグインは、行モデルの中でも重い処理の段階（フィルタリング、集計付きのグループ化、ソート）を専用の Web Worker に移します。そのため、重い再計算がメインスレッドをブロックすることはありません。テーブルのコードは通常のテーブルとほぼ同じままで、`manual*` フラグも `postMessage` の呼び出しも要りません。Worker の中では、本物の行モデルのパイプラインを持つヘッドレスな「シャドウテーブル」が動き、結果をコンパクトな形で返します（transferable なインデックスの並び、またはグループ化が有効なときはシリアライズした行ツリー）。再計算の途中でもテーブルは直前の行をレンダーし続け、結果が届いた時点で更新されます。

## 検討すべき場面 {#when-to-consider-it}

- データセット全体がクライアントにあり（ローカルファーストのアプリ、オフラインキャッシュ、分析用のグリッドなど）、サーバーでは処理できない。
- 行数と比較関数のコストを掛け合わせると、1フレームの予算を超える。基本的なソートならおよそ 10 万行以上、重いカスタムのフィルター関数やソート関数ならそれより少ない行数が目安です。
- 再計算の間も UI が操作できる状態でなければならない（入力しながらのフィルター、仮想化したスクロール、アニメーションなど）。

データをサーバー側でページネーションしている場合や、クライアントサイドの処理が数ミリ秒で終わる場合は、このプラグインは複雑さを増やすだけです。

## クイックスタート {#quick-start}

必要なものは3つです。1つ目は、両方のスレッドが import する共有モジュールです。この中のものはすべて、スレッドをまたいで持ち運べなければなりません。使えるのは `accessorKey` の列（またはこのモジュール内で定義したアクセサー）と、`sortFns`/`filterFns`/`aggregationFns` のレジストリにある関数です。アプリの状態を閉じ込めたクロージャーは使えません。

```ts
// tableConfig.ts (imported by BOTH the app and the worker)
import {
  columnFilteringFeature,
  createColumnHelper,
  createFilteredRowModel,
  createPaginatedRowModel,
  createSortedRowModel,
  filterFns,
  rowPaginationFeature,
  rowSortingFeature,
  sortFns,
  tableFeatures,
} from '@tanstack/react-table'
import { workerRowModelsFeature } from '@tanstack/react-table/experimental-worker-plugin'

export const sharedFeatures = tableFeatures({
  rowSortingFeature,
  columnFilteringFeature,
  rowPaginationFeature,
  workerRowModelsFeature,
  // these sync row models run inside the worker's shadow table
  filteredRowModel: createFilteredRowModel(),
  sortedRowModel: createSortedRowModel(),
  paginatedRowModel: createPaginatedRowModel(), // pagination stays on main
  sortFns,
  filterFns,
})

const columnHelper = createColumnHelper<typeof sharedFeatures, Person>()
export const columns = columnHelper.columns([
  /* accessorKey columns, named fns, custom fns declared in this module */
])
```

2つ目は、Worker のエントリーファイルです。Worker 側のコードはこれで全部です。

```ts
// table.worker.ts
import { initTableWorker } from '@tanstack/react-table/experimental-worker-plugin'
import { columns, sharedFeatures } from './tableConfig'

initTableWorker({ features: sharedFeatures, columns })
```

3つ目に、アプリ側で、Worker に任せる段階を Worker で動くものに差し替えます。`new Worker(new URL(...))` の式は自分のコードの中に書く必要があります。そうしないと、バンドラーが Worker のファイルを見つけてバンドルできません。

```ts
// App.tsx
import {
  createTableWorker,
  createWorkerRowModel,
} from '@tanstack/react-table/experimental-worker-plugin'
import { columns, sharedFeatures } from './tableConfig'

const tableWorker = createTableWorker({
  createWorker: () =>
    new Worker(new URL('./table.worker.ts', import.meta.url), {
      type: 'module',
    }),
})

const features: typeof sharedFeatures = {
  ...sharedFeatures,
  filteredRowModel: createWorkerRowModel(tableWorker, 'filtered'),
  sortedRowModel: createWorkerRowModel(tableWorker, 'sorted'),
}

// then a completely normal table:
const table = useTable({ features, columns, data })
```

ローディング表示には `table.state.workerRowModels.isPending` を読みます。同じ状態には `lastComputeMs` と `lastRoundTripMs` もあり、所要時間を確認できます。結果が届くと、通常のテーブルの状態の仕組みを通じて再レンダーされます。

このプラグインのエントリーは、すべてのフレームワークアダプター（`@tanstack/react-table/experimental-worker-plugin`、`@tanstack/octane-table/experimental-worker-plugin`、`@tanstack/vue-table/experimental-worker-plugin` など）と `@tanstack/table-core/experimental-worker-plugin` から利用できます。また、完全にツリーシェイク可能なので、import しないアプリにはまったく含まれません。

## Worker に任せられる段階と組み合わせ方 {#offloadable-stages-and-composition}

`createWorkerRowModel(tableWorker, stage)` には `'filtered'`、`'grouped'`、`'sorted'`、`'expanded'` のいずれかを渡せます。1つのテーブルのすべての段階は1つの Worker を共有し、状態が変わるたびのやり取りも1往復で済みます。入力が変わっていない段階は丸ごとスキップされます。

Worker に任せる段階は、パイプラインの先頭から途切れずに並んでいなければなりません（filtered、grouped、sorted、expanded の順）。`filtered` だけを任せるのは問題ありません。後続の同期的な段階が、その結果を通常どおり受け取るからです。しかし、フィルタリングをメインスレッドで動かしたまま `sorted` を任せると、フィルターが黙って素通りされてしまいます。このような食い違いがあると、開発モードで警告が出ます。実際には、`expanded` は決して任せないでください（開閉のたびに変わるためです）。また、ページネーションはメインスレッドに残してください（現在のページを切り出すだけだからです）。

## 制約と挙動 {#constraints-and-behavior}

- 今のところ、**平坦な元データのみ**に対応しています（`getSubRows` は使えません）。
- **処理に影響するテーブルのオプション**（たとえば独自の `globalFilterFn`）は、テーブルのフックに渡すだけでなく、共有の設定として `initTableWorker` にも渡す必要があります。
- **グループの集計**を使うには、共有の機能セットに `rowAggregationFeature` と `columnGroupingFeature` の両方が必要です。集計は Worker の中で先行して計算されますが、対象は `aggregationFn` または `aggregatedCell` を明示的に指定した列だけです。それ以外の列では、グループ行の `getValue()` は `undefined` を返します。
- **複数の集計結果**は、キー付きのオブジェクトとして受け渡されます。カスタムの集計結果は、ブラウザーの構造化複製アルゴリズム（structured clone）が扱える値でなければなりません。
- `column.getAggregationValue(options?)` による**総計と、呼び出し側が選んだ行の合計**は、メインスレッドで計算されます。現在の Worker が引き受けるのは行モデルの段階であり、任意の集計リクエストではありません。
- **SSR** は追加の設定なしで動きます。サーバー上（`Worker` グローバルがない環境）では、テーブルは未処理の行をレンダーし、ハイドレーション後にクライアントが処理を引き継ぎます。
- **Worker が失敗した場合**（読み込めない、または例外を投げた場合）、プラグインはエラーをログに出し、直前の結果を画面に残したまま更新を止めます。結果がまだ出ていない段階は、その段階の手前のモデルにフォールバックします。
- 今のところ、**Worker を自動で終了させる仕組みはありません**。手動の抜け道（escape hatch）として `tableWorker.terminate()` があり、次に読み取るときに自動で復旧します。
- 行選択、展開、ページネーションはメインスレッドの状態であり、このプラグインの影響を受けません。非常に大きなグループに対する選択は、引き続きメインスレッド上で行数に比例してコストが増えます。

ソート、フィルタリング、集計付きのグループ化、行選択を備えた完全な SSR アプリについては、[Web Worker 行モデルのサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/web-worker-row-models)を参照してください。
