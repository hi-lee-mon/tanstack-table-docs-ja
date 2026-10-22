---
title: 行モデルガイド
---

TanStack Table のいちばん基本的な例を見ると、次のようなコードがあります。

```ts
import { tableFeatures, useTable } from '@tanstack/react-table'

const features = tableFeatures({}) // Core features only

function Component() {
  const table = useTable({
    features,
    columns,
    data,
  })
}
```

v9 では、行モデルのファクトリーは `tableFeatures()` で作る features オブジェクトの上に置きます。コア行モデルは常に自動で含まれます。追加するのは、フィルタリング・ソート・ページネーションなどに必要な行モデルだけです。有効にした機能のコードだけをインポートして使うので、バンドルを小さく保てます。

## 行モデルとは {#what-are-row-models}

行モデルは TanStack Table の内部で動き、フィルタリング・ソート・グループ化・展開・ページネーションといったデータグリッドの機能に必要な形へ、元のデータを変換します。生成されて画面に描画される行は、テーブルに渡した元のデータと必ずしも1対1で対応するわけではありません。ソート・フィルタリング・ページネーションなどが適用されていることがあります。

## 行モデルを設定する {#configuring-row-models}

追加する行モデルは、必要なものだけにしてください。行モデルのファクトリーは、機能オブジェクトと並べて、`tableFeatures()` の呼び出しの中にスロットとして直接渡します。

| スロットのキー        | ファクトリー関数              | 用途                                       |
| --------------------- | ----------------------------- | ------------------------------------------ |
| （自動）              | （なし）                      | コア行モデル（常に含まれる）               |
| `filteredRowModel`    | `createFilteredRowModel()`    | フィルタリング（列フィルター＋グローバルフィルター） |
| `sortedRowModel`      | `createSortedRowModel()`      | ソート                                     |
| `paginatedRowModel`   | `createPaginatedRowModel()`   | ページネーション                           |
| `expandedRowModel`    | `createExpandedRowModel()`    | 行の展開                                   |
| `groupedRowModel`     | `createGroupedRowModel()`     | グループ化（有効にした場合は集計も）       |
| `facetedRowModel`     | `createFacetedRowModel()`     | ファセットによるフィルタリング             |
| `facetedMinMaxValues` | `createFacetedMinMaxValues()` | ファセットフィルター用の最小値・最大値     |
| `facetedUniqueValues` | `createFacetedUniqueValues()` | ファセットフィルター用の一意な値           |

ファクトリー関数は、もう `filterFns`・`sortFns`・`aggregationFns` を引数として受け取りません。これらの関数マップは、features オブジェクトにそれぞれ名前付きのスロットとして登録します（後述の[関数のレジストリ](#function-registries)を参照してください）。

使う行モデルごとに、対応する機能オブジェクトも `tableFeatures()` に追加する必要があります。たとえば次のようにします。

```ts
import {
  tableFeatures,
  useTable,
  columnFilteringFeature,
  rowSortingFeature,
  rowPaginationFeature,
  createFilteredRowModel,
  createSortedRowModel,
  createPaginatedRowModel,
  filterFn_includesString,
  sortFn_alphanumeric,
  sortFn_text,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnFilteringFeature,
  rowSortingFeature,
  rowPaginationFeature,
  filteredRowModel: createFilteredRowModel(),
  sortedRowModel: createSortedRowModel(),
  paginatedRowModel: createPaginatedRowModel(),
  filterFns: { includesString: filterFn_includesString },
  sortFns: { alphanumeric: sortFn_alphanumeric, text: sortFn_text },
})

const table = useTable({
  features,
  columns,
  data,
})
```

> [!NOTE]
> 組み込みのレジストリ全体（`filterFns`・`sortFns`・`aggregationFns`）を、これらのスロットにスプレッドで展開して渡すこともまだできます。ただし、組み込みの関数がすべてバンドルに含まれてしまうため非推奨です。使う関数だけを慣例の文字列キーで登録するか、`filterFn`・`sortFn`・`aggregationFn` の列オプションに関数を直接渡して登録自体を省いてください。文字列キー（デフォルトの `'auto'` を含む）で解決されるのは、登録済みの関数だけです。

## 関数のレジストリ {#function-registries}

`tableFeatures()` は、`filterFns`・`sortFns`・`aggregationFns` という3つの名前付きのレジストリのスロットを受け付けます。各スロットはオブジェクトで、そのキーが列定義やテーブルオプションの `filterFn`・`sortFn`・`globalFilterFn`・`aggregationFn` に指定できる、完全に型安全な文字列値になります。コストがかかるのは、登録した関数の分だけです。

```ts
import {
  tableFeatures,
  columnFilteringFeature,
  createFilteredRowModel,
} from '@tanstack/react-table'

const myFuzzyFilter: FilterFn<typeof features, Person> = (
  row,
  columnId,
  value,
  addMeta,
) => {
  // ...
  return true
}

const features = tableFeatures({
  columnFilteringFeature,
  filteredRowModel: createFilteredRowModel(),
  filterFns: { fuzzy: myFuzzyFilter },
})

// 'fuzzy' is now a valid type-safe value for filterFn in column defs:
const columnHelper = createColumnHelper<typeof features, Person>()

columnHelper.accessor('name', { filterFn: 'fuzzy' })
```

ソートとグループ化でも同じパターンが使えます。

- `sortFns: { myCustomSort }` とすると、列定義の `sortFn` に `'myCustomSort'` を指定できるようになります。
- `aggregationFns: { myAgg }` とすると、列定義の `aggregationFn` に `'myAgg'` を指定できるようになります。

組み込みの関数を文字列の名前で使うには、関数を個別にインポートし（`filterFn_includesString`、`sortFn_alphanumeric`、`aggregationFn_sum` など）、慣例のキーで登録します。たとえば `filterFns: { includesString: filterFn_includesString }` のようにします。列オプションが関数を直接受け付ける場合は、登録をすべて省き、インポートした関数をそのまま `filterFn`・`sortFn`・`aggregationFn` の値として渡すこともできます。

## 行モデルをカスタマイズ・フォークする {#customizefork-row-models}

TanStack Table が提供する行モデルをそのまま使う必要はありません。特定の行モデルを高度にカスタマイズしたい場合は、カスタマイズしたい行モデルの[ソースコード](https://github.com/TanStack/table/tree/main/packages/table-core/src/features)を遠慮なくコピーし、必要に合わせて書き換えてください。各行モデルのファクトリーは対応する機能と同じ場所にあり（例: `row-sorting/createSortedRowModel.ts`）、コア行モデルは [`core/row-models`](https://github.com/TanStack/table/tree/main/packages/table-core/src/core/row-models) にあります。

## 行モデルを使う {#using-row-models}

テーブルインスタンスを作成したら、必要な行モデルにはすべてテーブルインスタンスから直接アクセスできます。自分でインポートした行モデル以外にも、さらに多くの派生した行モデルが用意されています。

通常の描画であれば、おそらく `table.getRowModel()` メソッドだけで足ります。この行モデルは、どの機能を有効・無効にしているかに応じて、他の行モデルをすべて、あるいは必要なものだけ使うからです。その他の行モデルはすべて、テーブル内で行われているデータ変換を「掘り下げて」調べたいときに使えます。

## テーブルインスタンスで使える行モデル {#available-row-models-on-table-instance}

- **`getRowModel`** - テーブルの行のマークアップを描画するのに使うべき、メインの行モデルです。他のすべての行モデルを使って、テーブルの行の描画に使う最終的な行モデルを生成します。

- `getCoreRowModel` - テーブルに渡された元のデータを1対1で写しただけの、基本的な行モデルを返します。

- `getFilteredRowModel` - 列フィルタリングとグローバルフィルタリングを反映した行モデルを返します。
- `getPreFilteredRowModel` - 列フィルタリングとグローバルフィルタリングを適用する前の行モデルを返します。

- `getGroupedRowModel` - グループ化を適用し、サブ行を作成した行モデルを返します。`rowAggregationFeature` も登録されている場合は、それらのグループ化された行について、設定された集計値が計算されます。
- `getPreGroupedRowModel` - グループ化する前の行モデルを返します。そのルートの行は、総計を求める `column.getAggregationValue()` がデフォルトで使う行の集合です。`maxAggregationDepth` を使えば、より深い階層を対象にできます。

- `getSortedRowModel` - ソートを適用した行モデルを返します。
- `getPreSortedRowModel` - ソートを適用する前の行モデルを返します（行は元の順序のままです）。

- `getExpandedRowModel` - サブ行の展開・非表示を反映した行モデルを返します。
- `getPreExpandedRowModel` - ルート階層の行だけを含み、展開されたサブ行を含まない行モデルを返します。ソートは反映されたままです。

- `getPaginatedRowModel` - ページネーションの状態に基づき、現在のページに表示すべき行だけを含む行モデルを返します。
- `getPrePaginatedRowModel` - ページネーションを適用していない行モデルを返します（すべての行を含みます）。

- `getSelectedRowModel` - 選択されたすべての行の行モデルを返します（ただし、テーブルに渡されたデータだけに基づきます）。getCoreRowModel の後に実行されます。
- `getPreSelectedRowModel` - 行選択を適用する前の行モデルを返します（getCoreRowModel をそのまま返すだけです）。
- `getGroupedSelectedRowModel` - グループ化した後の、選択された行の行モデルを返します。getSortedRowModel の後に実行されます。getSortedRowModel は getGroupedRowModel の後に、getGroupedRowModel は getFilteredRowModel の後に実行されます。
- `getFilteredSelectedRowModel` - 列フィルタリングとグローバルフィルタリングを適用した後の、選択された行の行モデルを返します。getFilteredRowModel の後に実行されます。

## 行モデルの実行順序 {#the-order-of-row-model-execution}

TanStack Table が内部で行をどう処理しているかを知っておくと、裏で何が起きているかをよりよく理解でき、問題に遭遇したときのデバッグにも役立ちます。

内部では、それぞれの機能が有効になっている場合、次の順序で各行モデルがデータに適用されます。

`getCoreRowModel` -> `getFilteredRowModel` -> `getGroupedRowModel` -> `getSortedRowModel` -> `getExpandedRowModel` -> `getPaginatedRowModel` -> `getRowModel`

対応する機能が無効になっている場合や、`"manual*"` 系のテーブルオプションでオフにされている場合は、その段階では代わりに `getPre*RowModel` が使われます。

上のとおり、データはまずフィルタリングされ、次にグループ化、ソート、展開され、最後の段階としてページネーションが適用されます。

## 行モデルのデータ構造 {#row-model-data-structure}

各行モデルは、行を3つの便利な形式で提供します。

1. `rows` - 行の配列です。
2. `flatRows` - 行の配列ですが、すべてのサブ行が最上位に平坦化されています。
3. `rowsById` - 行のオブジェクトで、各行がその `id` をキーとして格納されています。`id` を使って行を高速に検索したいときに便利です。

```ts
console.log(table.getRowModel().rows) // array of rows
console.log(table.getRowModel().flatRows) // array of rows, but all sub-rows are flattened into the top level
console.log(table.getRowModel().rowsById['row-id']) // object of rows, where each row is keyed by its `id`
```
