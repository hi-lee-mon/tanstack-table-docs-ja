---
title: 仮想化（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React のサンプルを参照してください。

- [列の仮想化](https://tanstack.com/table/latest/docs/framework/react/examples/virtualized-columns)
- [行の仮想化](https://tanstack.com/table/latest/docs/framework/react/examples/virtualized-rows)
- [仮想化と無限スクロール](https://tanstack.com/table/latest/docs/framework/react/examples/virtualized-infinite-scrolling)
- [列の仮想化（実験的）](https://tanstack.com/table/latest/docs/framework/react/examples/virtualized-columns-experimental)
- [行の仮想化（実験的）](https://tanstack.com/table/latest/docs/framework/react/examples/virtualized-rows-experimental)

### 仮想化の準備 {#virtualization-setup}

TanStack Table で仮想化を使うための準備は次のとおりです。仮想化は描画の戦略なので、TanStack Table 側に機能や行モデルを追加する必要はありません。

`@tanstack/react-virtual` から React 用の仮想化アダプターをインストールしてインポートします。行・列・テーブルの状態は引き続き TanStack Table が持ち、スクロール位置に対応するインデックスと要素の計測は仮想化ライブラリ（virtualizer）が持ちます。
[TanStack Virtual のテーブルのサンプル](https://tanstack.com/virtual/latest/docs/framework/react/examples/table)も参照してください。

## 仮想化（React）ガイド {#virtualization-react-guide}

TanStack Table のパッケージには、仮想化の API や機能は組み込まれていません。仮想化はテーブルの機能ではなく、描画の戦略です。TanStack Table はどの仮想化ライブラリとも組み合わせられますが、公式のサンプルでは TanStack Virtual を使っています。

TanStack Table と TanStack Virtual は、問題の別々の部分を受け持ちます。

- TanStack Table は、行モデル・列・ヘッダー・セル・列幅・ソート・フィルタリングなどのテーブルの状態を組み立てます。
- TanStack Virtual は、現在のスクロール位置で描画すべき項目のインデックスを決めます。
- あなたが書くテーブルの描画処理は、その仮想インデックスを行・ヘッダー・セルに対応づけます。

### 仮想化を使うべき場面 {#when-to-use-virtualization}

テーブルの行数や列数（またはその両方）が非常に多い場合に仮想化を使います。仮想化では、スクロール領域に見えている項目と、少しの先読み分（overscan）だけを描画するので、DOM を小さく保てます。

仮想化は、サーバーサイドのページネーション・フィルタリング・ソートの代わりにはなりません。クライアントで仮想化する場合でも、データそのものはクライアントに存在している必要があります。データセットが大きすぎてブラウザーに読み込めない場合は、サーバーサイドのデータ操作か無限スクロールを使ってください。

小さなテーブルなら、通常の描画のほうが単純で、たいていはそのほうが適しています。

### TanStack Virtual をインストールする {#install-tanstack-virtual}

React 用の仮想化アダプターをインストールします。

```sh
npm install @tanstack/react-virtual
```

React のサンプルでは、`@tanstack/react-virtual` の `useVirtualizer` を使っています。行・列・ヘッダー・セル・列幅・ソート・フィルタリングなどのテーブルの状態は引き続き TanStack Table が持ち、現在のスクロール位置で描画すべき項目のインデックスは TanStack Virtual が決めます。

テーブル自体は、ほかの v9 のテーブルと同じように準備します。`tableFeatures()` で機能を宣言し、`useTable` でテーブルを作成します。仮想化のためにテーブルの準備を変える必要はありません。

```tsx
import {
  columnSizingFeature,
  rowSortingFeature,
  createSortedRowModel,
  sortFns,
  tableFeatures,
  useTable,
} from '@tanstack/react-table'
import { useVirtualizer } from '@tanstack/react-virtual'

const features = tableFeatures({
  columnSizingFeature,
  rowSortingFeature,
  sortedRowModel: createSortedRowModel(),
  sortFns,
})

const table = useTable({
  features,
  columns,
  data,
})
```

### 基本のパターン {#the-basic-pattern}

仮想化したテーブルの実装は、ほとんどが同じパターンに沿っています。

1. 高さを固定したスクロールコンテナーを作る。
2. スクロールする要素を virtualizer に渡す。
3. 元になるリストとして `table.getRowModel().rows` か `table.getVisibleLeafColumns()` を使う。
4. `count`、`estimateSize`、`overscan`、必要に応じて `measureElement` を設定する。
5. 仮想項目だけを描画する。
6. 仮想オフセットか余白用のパディングを使って、スクロール領域全体の大きさを保つ。

行の仮想化の簡潔な例を示します。

```tsx
const rows = table.getRowModel().rows

const rowVirtualizer = useVirtualizer({
  count: rows.length,
  getScrollElement: () => tableContainerRef.current,
  estimateSize: () => 33,
  overscan: 5,
})

<tbody
  style={{
    height: `${rowVirtualizer.getTotalSize()}px`,
    position: 'relative',
  }}
>
  {rowVirtualizer.getVirtualItems().map(virtualRow => {
    const row = rows[virtualRow.index]

    return (
      <tr
        key={row.id}
        style={{
          position: 'absolute',
          transform: `translateY(${virtualRow.start}px)`,
          width: '100%',
        }}
      >
        {row.getVisibleCells().map(cell => (
          <td key={cell.id}>{/* render cell */}</td>
        ))}
      </tr>
    )
  })}
</tbody>
```

### 行の仮想化 {#virtualized-rows}

[行の仮想化のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/virtualized-rows)では、DOM を小さく保ちながら大量の行を描画する方法を示しています。サンプルは React、Solid、Svelte、Vue、Angular、Lit 向けに用意されています。

要点は、ソート・フィルタリング・グループ化などの行モデルの処理は、引き続き TanStack Table が担うということです。virtualizer は、テーブルの最終的な行モデルを読み取ります。

```tsx
const rows = table.getRowModel().rows
```

行の virtualizer には、`count: rows.length`、行の高さの見積もり、スクロールコンテナー、overscan の値を設定します。`tbody` には `rowVirtualizer.getTotalSize()` で仮想領域全体の高さを与え、描画する各行は `transform: translateY(...)` で絶対配置します。

サンプルでは、表示状態を考慮したセルが必要か、すべてのセルが必要かに応じて、`row.getVisibleCells()` や `row.getAllCells()` などの API で現在の行のセルを描画しています。

公式のサンプルでは、数万〜数十万行といった大規模な生成データを使っています。また、可能な場合は `measureElement` を使って行の高さの動的な変化にも対応しています。ただし Firefox ではテーブルの罫線の高さの計測結果が異なることがあるため、Firefox では行の高さの動的な計測を行いません。

### 列の仮想化 {#virtualized-columns}

[列の仮想化のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/virtualized-columns)では、行と列の両方が大量にある場合の描画方法を示しています。サンプルは React、Solid、Svelte、Vue、Angular、Lit 向けに用意されています。

列の仮想化では、現在表示されている列のリストを使います。

```tsx
const visibleColumns = table.getVisibleLeafColumns()
```

列の virtualizer は、横方向の仮想化に設定します。

```tsx
const columnVirtualizer = useVirtualizer({
  count: visibleColumns.length,
  estimateSize: (index) => visibleColumns[index].getSize(),
  getScrollElement: () => tableContainerRef.current,
  horizontal: true,
  overscan: 3,
})
```

列の仮想化は、行の仮想化とは描画の方法が異なります。列を絶対配置する代わりに、サンプルでは左右に余白用のダミーのセルを追加しています。

```tsx
const virtualColumns = columnVirtualizer.getVirtualItems()
const virtualPaddingLeft = virtualColumns[0]?.start ?? 0
const virtualPaddingRight =
  columnVirtualizer.getTotalSize() -
  (virtualColumns[virtualColumns.length - 1]?.end ?? 0)
```

この余白用のセルが横方向のスクロール幅を保ち、実際にマウントするのは仮想列だけになります。この方法なら行の描画をテーブルらしい形のまま保てるので、行の高さの動的な計測も引き続き機能します。

### 行と列を同時に仮想化する {#virtualized-rows-and-columns-together}

公式の列の仮想化のサンプルでは、行も仮想化しています。これらのサンプルでは次のようになっています。

- 行の virtualizer は、縦方向の配置と本体全体の高さを制御します。
- 列の virtualizer は、ヘッダーやセルの横方向の描画と、左右の余白用のセルを制御します。
- `virtualRow.index` は `rows[virtualRow.index]` に対応します。
- `virtualColumn.index` は `visibleCells[virtualColumn.index]` に対応します。

仮想インデックスは、必ずテーブルが返す現在の行と列のリストに対して使ってください。ソート・フィルタリング・ページネーション・グループ化・列の表示切り替えが変わったら、仮想化する行と列を現在のテーブルの状態から計算し直します。

### 仮想化と無限スクロール {#virtualized-infinite-scrolling}

[仮想化と無限スクロールのサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/virtualized-infinite-scrolling)では、行の仮想化と段階的なデータ取得を組み合わせています。サンプルは React、Solid、Svelte、Vue、Angular、Lit 向けに用意されています。

よくあるパターンは次のとおりです。

1. 1ページ分の行を取得する。
2. 取得したページを平坦化して、テーブルの `data` にする。
3. 読み込み済みの行に対して行の仮想化を使う。
4. テーブルのコンテナーでスクロールイベントを監視する。
5. ユーザーが末尾近くまでスクロールしたら、次のページを取得する。

React のサンプルでは TanStack Query の `useInfiniteQuery` を使っていますが、同じパターンはどのデータ取得の仕組みでも使えます。

```tsx
const { scrollHeight, scrollTop, clientHeight } = scrollElement

if (scrollHeight - scrollTop - clientHeight < 500) {
  fetchNextPage()
}
```

ソートをサーバー側で行う場合は、手動ソートを使ってください。そうすれば、取得するデータが、現在読み込み済みの行だけでなくバックエンドのデータセット全体を反映したものになります。ソートが変わって取得済みのデータセットが置き換わったら、`rowVirtualizer.scrollToIndex(0)` で先頭までスクロールを戻します。

### 行の高さを動的にする {#dynamic-row-heights}

行の高さを動的にすると、内容が折り返したり広がったりする場合に役立ちます。ただし、行の高さが固定の場合よりも複雑になります。

`estimateSize` は、virtualizer が最初に使う見積もりの値として使います。

```tsx
estimateSize: () => 33
```

そのうえで、描画後に `measureElement` で実際の行の高さに合わせて補正します。

```tsx
<tr
  data-index={virtualRow.index}
  ref={node => rowVirtualizer.measureElement(node)}
>
```

各行に `data-index` を設定して、virtualizer が計測結果を正しい項目に対応づけられるようにします。React 以外のアダプターでは、そのアダプターに合った ref・アクション・ディレクティブ・コントローラーを通じて `measureElement` を呼び出してください。

overscan は、計測が落ち着くまでの間に空白の領域が見えるのを防ぐのに役立ちます。すべての行の高さが固定で分かっている場合は、動的な計測を行わず、固定の高さを見積もりの値として使ってください。

### 固定ヘッダーとセマンティックなテーブルのマークアップ {#sticky-headers-and-semantic-table-markup}

サンプルでは引き続きセマンティックなテーブルのタグを使っていますが、仮想的な配置と固定ヘッダーに対応するため、テーブルのレイアウトの CSS を変更しています。

行の高さを動的にした仮想化では、一般的に次の指定が必要です。

```css
table {
  display: grid;
}

thead {
  display: grid;
  position: sticky;
  top: 0;
}

tr {
  display: flex;
}
```

行は相対配置した `tbody` の中で絶対配置し、セルは flex でサイズを決めて `column.getSize()` や `cell.column.getSize()` に合わせられるようにします。これは意図的な設計です。ブラウザー標準のテーブルレイアウトは、個別に配置される高さ可変の仮想行とうまくかみ合いません。

### パフォーマンスのヒント {#performance-tips}

- virtualizer は、仮想化した項目を描画するコンポーネントの近くに置く。
- スクロールのたびにテーブルの本体全体を再レンダーしないようにする。
- 行・列・データの参照は、できるだけ安定させる。
- `overscan` は意図を持って設定する。overscan を増やすと見える空白が減り、減らすと DOM ノードが減る。
- 非常に大きな仮想化テーブルでは、重いセルの描画処理を避ける。
- 本番ビルドでテストする。React の開発モードは遅く、React のサンプルでもその点に触れている。
- UI が許すなら、行のサイズを固定にする。
- 列の仮想化では、`column.getSize()`、`header.getSize()`、`cell.column.getSize()` を一貫して使う。

### React の実験的な仮想化サンプル {#experimental-react-virtualization-examples}

React のサンプルには、[行の仮想化（実験的）](https://tanstack.com/table/latest/docs/framework/react/examples/virtualized-rows-experimental)と[列の仮想化（実験的）](https://tanstack.com/table/latest/docs/framework/react/examples/virtualized-columns-experimental)があります。これらは、スクロール中の React の描画処理を減らすための高度な実験です。

まずは標準のサンプルを使ってください。実験的なサンプルを使うのは、プロファイリングの結果、スクロール中の React の描画処理がボトルネックだと分かった場合だけにしてください。

実験的なサンプルでは、TanStack Virtual の `onChange` コールバックを使って DOM のスタイルを命令的に更新し、スクロール位置が変わるたびに React の描画を通さないようにしています。

実験的な行のサンプルでは、次のことをしています。

- 仮想行のインデックスから DOM の行要素への `rowRefsMap` を保持する。
- `onChange` で `rowRef.style.transform` を更新する。
- スクロール中は、独自の比較関数を渡した `React.memo` で行をメモ化する。

```tsx
onChange: (instance) => {
  instance.getVirtualItems().forEach((virtualRow) => {
    const rowRef = rowRefsMap.current.get(virtualRow.index)
    if (!rowRef) return
    rowRef.style.transform = `translateY(${virtualRow.start}px)`
  })
}
```

実験的な列のサンプルでも、スクロール位置だけに関わる DOM のスタイルを直接書き換えています。

```tsx
tableContainerRef.current?.style.setProperty(
  '--virtual-padding-left',
  `${virtualPaddingLeft}px`,
)

tableContainerRef.current?.style.setProperty(
  '--virtual-padding-right',
  `${virtualPaddingRight}px`,
)

tableBodyRef.current!.style.height = `${instance.getTotalSize()}px`
```

このサンプルは DOM の ref を通じて行の transform を更新し、列の virtualizer がスクロールしている間はヘッダーとセルのコンポーネントをメモ化します。

これらのサンプルは React の通常の描画の流れの外で DOM を更新するため、命令的な更新は `transform`、本体の高さ、余白の幅といった、スクロール位置だけに関わるスタイルに限定してください。業務上の状態・テーブルの状態・データ・ソート・フィルタリング・セルの値には、このパターンを使わないでください。

### サンプルの選び方 {#choosing-an-example}

| 必要なこと                                     | 最初に見るサンプル                                                                   |
| ---------------------------------------- | ---------------------------------------------------------------------------- |
| 行が多く、列は普通                | [行の仮想化](https://tanstack.com/table/latest/docs/framework/react/examples/virtualized-rows)                             |
| 列が多い                             | [列の仮想化](https://tanstack.com/table/latest/docs/framework/react/examples/virtualized-columns)                       |
| 行も列も多い                    | [列の仮想化](https://tanstack.com/table/latest/docs/framework/react/examples/virtualized-columns)                       |
| ユーザーのスクロールに応じてリモートのデータを読み込む   | [仮想化と無限スクロール](https://tanstack.com/table/latest/docs/framework/react/examples/virtualized-infinite-scrolling) |
| プロファイリングを経た React のスクロール性能改善 | [React の実験的なサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/virtualized-rows-experimental)     |

### よくある落とし穴 {#common-pitfalls}

- スクロールコンテナーの高さを固定し忘れる。
- `virtualizer.getVirtualItems().map(...)` ではなく `table.getRowModel().rows.map(...)` で描画してしまう。
- ソート・フィルタリング・ページネーション・グループ化・列の表示切り替えが変わった後も、古い行や列に対して仮想インデックスを使ってしまう。
- 横方向の仮想化で、左右の余白用のセルを忘れる。
- すべての行の高さが固定なのに `measureElement` を使う。
- TanStack Table が仮想化の API を機能として提供していると思い込む。
- クライアントサイドの仮想化と、サーバーサイドのソートやフィルタリングを一貫しない形で混在させる。
