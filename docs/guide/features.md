---
title: 機能ガイド
---

## `features` オプションが必須である理由 {#why-the-features-option-is-required}

TanStack Table v9 では、各テーブルが使う機能を明示的に宣言するために、`features` オプションが必須です。以前のバージョンでは、TanStack Table の機能を増やすことに慎重でした。新しい機能を1つ足すたびに、それを必要とするアプリケーションがごく一部であっても、すべてのユーザーのコードが増えるおそれがあったからです。この制約はライブラリを小さく保つのに役立ちましたが、既存の機能をどこまで拡張できるか、新しい機能をどれだけ提供できるかを制限してもいました。

v9 のプラグインアーキテクチャは、この制約を取り除きます。各機能はそれぞれ拡張できるようになり、TanStack Table はすべてのコードをあらゆるアプリケーションに含めることなく、より多くの機能を提供できます。全機能を含めた場合のバンドルサイズは v8 の約 14 kB から v9 では約 25 kB に増えましたが、必要な機能だけを登録すれば、ほとんどのユーザーはより小さなバンドルで済むはずです。TanStack Table の機能をおよそ半分使うアプリケーションなら、残りの半分を配布する必要はもうありません。

TanStack Table v9 は、プラグインアーキテクチャを土台にした、ヘッドレスでツリーシェイク可能なライブラリです。テーブルには、テーブル・列・ヘッダー・行・セルを作るのに必要な少数のコア機能が常に含まれます。ソート・フィルタリング・ページネーション・選択・列幅などのその他の機能は、オプトイン（明示的に有効にする）方式です。

各機能は、それぞれの状態・オプション・デフォルト値・ライフサイクルフック・API を、テーブルとその関連オブジェクトに追加します。登録した機能オブジェクトは、TypeScript の型にも反映されます。登録していない機能の API は、テーブル・列・行・ヘッダー・セルに現れません。

## `tableFeatures` で機能を選ぶ {#choose-your-features-with-tablefeatures}

どのテーブルも、静的な機能の組み合わせを `tableFeatures()` で宣言します。コアの動作だけが必要なテーブルでは、空の機能オブジェクトを使います。

```ts
import { tableFeatures, useTable } from '@tanstack/react-table'

const features = tableFeatures({})

function Table() {
  const table = useTable({
    features,
    columns,
    data,
  })

  // render the table...
}
```

そのテーブルに必要なオプションの機能だけをインポートして登録します。

```ts
import {
  columnFilteringFeature,
  rowPaginationFeature,
  rowSortingFeature,
  tableFeatures,
  useTable,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnFilteringFeature,
  rowSortingFeature,
  rowPaginationFeature,
})
```

機能オブジェクトは、できるだけコンポーネントの外で定義してください。これは静的な設定です。参照を安定させておけば、テーブルの構造を作り直さずに済みます。また、共有する列定義やヘルパーが、再利用できる1つの `typeof features` 型を使えるようになります。

`tableFeatures()` は、スロット同士の関係も検証します。たとえば、`sortedRowModel` には `rowSortingFeature` が必要で、`globalFilteringFeature` には `columnFilteringFeature` が必要です。前提となる機能が足りないと、必要な機能の名前を示す型エラーになります。

## 機能・行モデル・関数はそれぞれ別のもの {#features-row-models-and-functions-are-separate}

機能は状態と API を追加しますが、それだけではクライアントサイドのデータ処理を行いません。クライアントサイドの行モデルは任意です。TanStack Table にブラウザーでデータを処理させたい場合にだけ、対応する行モデルのファクトリーを追加します。その処理をサーバーが行う場合は、状態と API のために機能は残し、クライアントサイドの行モデルは省きます。

次の例では、クライアントサイドのフィルタリング・ソート・ページネーションを有効にしています。

```ts
import {
  columnFilteringFeature,
  createFilteredRowModel,
  createPaginatedRowModel,
  createSortedRowModel,
  filterFn_includesString,
  rowPaginationFeature,
  rowSortingFeature,
  sortFn_alphanumeric,
  tableFeatures,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnFilteringFeature,
  rowSortingFeature,
  rowPaginationFeature,
  filteredRowModel: createFilteredRowModel(),
  sortedRowModel: createSortedRowModel(),
  paginatedRowModel: createPaginatedRowModel(),
  filterFns: { includesString: filterFn_includesString },
  sortFns: { alphanumeric: sortFn_alphanumeric },
})
```

それぞれの部品には、別々の役割があります。

- 機能オブジェクトは、状態・オプション・イベントハンドラー・インスタンスの API を提供します。
- 行モデルは、クライアントサイドのフィルタリング・グループ化・ソート・展開・ページネーション・ファセットを行います。
- 関数のレジストリは、名前付きのフィルター・ソート・集計の実装を提供します。

使う関数だけを登録してください。関数を個別にインポートすれば、ツリーシェイキングが効きます。組み込みの関数レジストリ全体を展開すると、そのレジストリのすべての実装が含まれます。列のオプションに直接渡した関数は、名前で登録する必要はありません。

サーバーサイドで処理する場合は、状態と API のために機能は残し、クライアントサイドの行モデルは省いて、該当する場合は対応する `manual*` オプションを設定します。こうしたデータの流れの選び方については、[行モデルガイド](./row-models)と[クライアントサイドとサーバーサイドのガイド](./client-side-vs-server-side)を参照してください。

## すべての標準機能を使う {#using-every-stock-feature}

`stockFeatures` は、オプションの機能をすべてまとめたものです。プロトタイプや共有の互換レイヤー、実際にほとんどの機能を使うテーブルで便利です。

```ts
import { stockFeatures, tableFeatures } from '@tanstack/react-table'

const features = tableFeatures({
  ...stockFeatures,
})
```

これはまとめて全部をインポートするので、すべての標準機能のコードが含まれます。バンドルサイズやツリーシェイキングが重要な場合は、機能を個別にインポートしてください。また、`stockFeatures` はクライアントサイドの行モデルや関数のレジストリを追加しません。必要な場合は別途追加してください。

## 標準機能 {#stock-features}

- `cellSelectionFeature`: [セル選択](../framework/react/guide/cell-selection) は、セル範囲の選択状態と API を追加します。
- `cellSpanningFeature`: [セル結合](../framework/react/guide/cell-spanning) は、セルが複数の行や列にまたがれるようにします。
- `columnFacetingFeature`: [ファセット](../framework/react/guide/column-faceting) は、フィルタリング UI のために一意な値・範囲・件数を導き出します。
- `columnFilteringFeature`: [列フィルタリング](../framework/react/guide/column-filtering) は、列ごとにフィルタリングし、列フィルターの状態を提供します。
- `columnGroupingFeature`: [グループ化](../framework/react/guide/grouping) は、列の値で行をグループ化します。
- `columnOrderingFeature`: [列の並べ替え](../framework/react/guide/column-ordering) は、列の順序を制御します。
- `columnPinningFeature`: [列の固定](../framework/react/guide/column-pinning) は、列をテーブルの左端または右端に固定します。
- `columnResizingFeature`: [列幅の変更](../framework/react/guide/column-resizing) は、列幅を変える操作を追加します。列幅の機能を土台にしています。
- `columnSizingFeature`: [列幅](../framework/react/guide/column-sizing) は、列の幅の情報を保持して公開します。
- `columnVisibilityFeature`: [列の表示切り替え](../framework/react/guide/column-visibility) は、列を表示したり隠したりします。
- `globalFilteringFeature`: [グローバルフィルタリング](../framework/react/guide/global-filtering) は、複数の列にまたがって行をフィルタリングします。列フィルタリングの機能を土台にしています。
- `rowAggregationFeature`: [集計](../framework/react/guide/aggregation) は、行の集まりに対して合計などの集計値を計算します。
- `rowExpandingFeature`: [展開](../framework/react/guide/expanding) は、展開された行と表示されるサブ行を制御します。
- `rowPaginationFeature`: [ページネーション](../framework/react/guide/pagination) は、ページの状態、ページ移動の API、任意のクライアントサイドのページネーションを提供します。
- `rowPinningFeature`: [行の固定](../framework/react/guide/row-pinning) は、行をテーブルの上端または下端に固定します。
- `rowSelectionFeature`: [行選択](../framework/react/guide/row-selection) は、選択された行の状態と API を管理します。
- `rowSortingFeature`: [ソート](../framework/react/guide/sorting) は、ソートの状態と、任意のクライアントサイドでの行の並べ替えを管理します。

これらが `stockFeatures` に含まれる機能です。あいまい検索フィルターは、フィルタリングとソートの機能を組み合わせて作るレシピです。また、仮想化はテーブルの機能ではなく、TanStack Virtual が提供します。

独自のプラグインを作って型を付ける方法は、フレームワークごとの[カスタムプラグインのガイド](../framework/react/guide/custom-features)を参照してください。
