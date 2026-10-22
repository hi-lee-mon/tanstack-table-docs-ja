---
title: テーブルと列のメタガイド
---

テーブルやその列に任意のデータや関数を独自に持たせ、`table` や `column` のインスタンスを使えるところならどこからでも使えるようにしたいことがあります。そのためにあるのが `meta` オプションです。TanStack Table 自体は `meta` を一切読み書きしません。テーブルを通じて独自のコンテキストを受け渡すための置き場所にすぎません。

メタには2種類あります。

- **テーブルのメタ** - `meta` テーブルオプションです。任意のオブジェクトを渡し、`table.options.meta` を通じてどこからでも読み出せます。典型的な使い方は、編集可能なセルに `updateData` 関数を渡すことです。
- **列のメタ** - 列定義の `meta` プロパティです。列を使えるところならどこからでも `column.columnDef.meta` で読み出せます。典型的な使い方は、列のヘッダーがどの種類のフィルター UI をレンダーするかを宣言することです。

## テーブルのメタ {#table-meta}

```ts
const table = useTable({
  features,
  columns,
  data,
  meta: {
    updateData: (rowIndex, columnId, value) => {
      // ...
    },
  },
})

// ...later, anywhere the table is available (e.g. inside a cell component)
table.options.meta?.updateData(rowIndex, columnId, newValue)
```


列のメタは列定義に設定します。どのアダプターでも同じです。

```ts
const columns = columnHelper.columns([
  columnHelper.accessor('age', {
    header: 'Age',
    meta: {
      filterVariant: 'range',
    },
  }),
])

// ...later, anywhere a column is available (e.g. inside a header component)
const variant = column.columnDef.meta?.filterVariant
```

## テーブルごとにメタの型を付ける（推奨） {#typing-meta-per-table-recommended}

デフォルトでは、どちらのメタの型も空のオブジェクトです。型安全にするには、その形を自分で宣言します。v9 からは、`tableFeatures()` の呼び出しの中で型専用の `tableMeta` スロットと `columnMeta` スロットを使い、`metaHelper` ユーティリティでメタの型を**機能のセットごとに**宣言できるようになりました。

まず、必要な形を定義します（これはどのフレームワークでも同じです）。

```ts
interface MyTableMeta {
  updateData: (rowIndex: number, columnId: string, value: unknown) => void
}

interface MyColumnMeta {
  filterVariant?: 'text' | 'range' | 'select'
}
```

次に、それを `features` オブジェクトに宣言します。

```ts
import {
  metaHelper,
  rowSortingFeature,
  tableFeatures,
} from '@tanstack/react-table'

const features = tableFeatures({
  rowSortingFeature,
  tableMeta: metaHelper<MyTableMeta>(),
  columnMeta: metaHelper<MyColumnMeta>(),
})
```


これだけです。この `features` オブジェクトが渡る先（`useTable`、`createColumnHelper`、`ColumnDef`、`Column` など）ではどこでも、メタの型が `typeof features` から推論されます。ジェネリクスを追加で受け渡す必要はありません。

```ts
const columnHelper = createColumnHelper<typeof features, Person>()

columnHelper.accessor('age', {
  meta: {
    filterVariant: 'range', // ✅ type-checked against MyColumnMeta
  },
})

// And both meta surfaces are fully typed wherever you read them:
table.options.meta?.updateData // ✅ (rowIndex, columnId, value) => void
column.columnDef.meta?.filterVariant // ✅ 'text' | 'range' | 'select' | undefined
```

後述する v8 方式の宣言のマージと違い、この方法の範囲は**グローバルではなくテーブルごと**です。この `features` オブジェクトで作ったテーブルだけが、これらのメタの型を持ちます。アプリ内の別々のテーブルで、別々の `features` オブジェクトを使えば、まったく異なるメタの形を宣言できます。

### 型専用スロットの仕組み {#how-the-type-only-slots-work}

`tableMeta` と `columnMeta` のキーは、_ファントム_（型の上にだけ存在する）エントリーです。意味を持つのは TypeScript の型だけです。実行時の値は空のオブジェクトで、テーブルに登録された機能からは取り除かれるため、本物の機能として扱われることはありません。実際のメタの _値_ は、これまでどおりの場所、つまり `meta` テーブルオプションと列定義の `meta` プロパティに渡します。

`metaHelper<MyMeta>()` は、`{}` をメタの型にキャストして返すだけです。キャストを自分で書いてもかまいません。

```ts
const features = tableFeatures({
  rowSortingFeature,
  tableMeta: {} as MyTableMeta,
  columnMeta: {} as MyColumnMeta,
})
```

どちらの書き方も同じ意味ですが、`metaHelper` を使うことをおすすめします。ひと目で型専用だと読み取れるうえ、`@typescript-eslint/no-unnecessary-type-assertion` という lint ルールの誤検知を避けられるからです。このルールは、メタの型がオプショナルなプロパティしか持たないときに `{} as` の書き方を指摘し、自動修正を適用するとメタの型が黙って消えてしまいます。

## フィルターのメタ（`filterMeta` スロット） {#filter-meta-filtermeta-slot}

`filterMeta` スロットを使うと、カスタムのフィルター関数がフィルタリング中に行へ付け加える任意のメタデータの形を宣言できます。とくに役立つのは、フィルター関数が副産物（ランキングのスコアなど）を生み出し、それを列のソート関数やセルのレンダラーで読みたい場合です。

やり方は `tableMeta` や `columnMeta` と同じです。メタのインターフェースを宣言し、`metaHelper` で登録してから、フィルター関数やソート関数に型注釈を付けるときに `TableFeatures` とメタの型を交差させます。

```ts
import {
  metaHelper,
  tableFeatures,
  columnFilteringFeature,
  globalFilteringFeature,
  rowSortingFeature,
  rowPaginationFeature,
  createFilteredRowModel,
  createSortedRowModel,
  createPaginatedRowModel,
  sortFn_alphanumeric,
} from '@tanstack/react-table'
import type {
  FilterFn,
  SortFn,
  RowData,
  TableFeatures,
} from '@tanstack/react-table'
import { rankItem, type RankingInfo } from '@tanstack/match-sorter-utils'

// 1. Define the metadata shape your filter function will attach
interface FuzzyFilterMeta {
  itemRank?: RankingInfo
}

// 2. Intersect with TableFeatures to get a fully typed features surface
type FuzzyFeatures = TableFeatures & { filterMeta: FuzzyFilterMeta }

// 3. Annotate your filter and sort functions against the extended features type
const fuzzyFilter: FilterFn<FuzzyFeatures, RowData> = (
  row,
  columnId,
  value,
  addMeta,
) => {
  const itemRank = rankItem(row.getValue(columnId), value)
  addMeta({ itemRank })
  return itemRank.passed
}

const fuzzySort: SortFn<FuzzyFeatures, Person> = (rowA, rowB, columnId) => {
  let dir = 0
  if (rowA.columnFiltersMeta[columnId]) {
    dir = compareItems(
      rowA.columnFiltersMeta[columnId]?.itemRank!,
      rowB.columnFiltersMeta[columnId]?.itemRank!,
    )
  }
  return dir === 0 ? sortFn_alphanumeric(rowA, rowB, columnId) : dir
}

// 4. Register everything on tableFeatures(), including the filterMeta slot
const features = tableFeatures({
  columnFilteringFeature,
  globalFilteringFeature,
  rowSortingFeature,
  rowPaginationFeature,
  filteredRowModel: createFilteredRowModel(),
  sortedRowModel: createSortedRowModel(),
  paginatedRowModel: createPaginatedRowModel(),
  filterFns: { fuzzy: fuzzyFilter },
  sortFns: { fuzzy: fuzzySort },
  filterMeta: metaHelper<FuzzyFilterMeta>(),
})
```

> [!NOTE]
> 上の `filterFns` スロットと `sortFns` スロットには、このテーブルで使う関数だけを登録しています。パッケージからエクスポートされている組み込みの登録一式（`filterFns`、`sortFns`、`aggregationFns`）を展開してこれらのスロットに入れることもまだできますが、すべての組み込み関数がバンドルに含まれてしまうため非推奨です。代わりに `sortFn_alphanumeric` のような個別の関数をインポートするか、列定義に関数を直接渡してください。

これで、この `features` オブジェクトから作ったテーブルでは、各行の `columnFiltersMeta` の型が `FuzzyFilterMeta` になります。`filterMeta` スロットも、`tableMeta` や `columnMeta` と同じく型専用のファントムエントリーです。`metaHelper<FuzzyFilterMeta>()` は実行時には `{}` を返し、登録された機能からは取り除かれます。

そのまま動く完全な実装は、[React の filters-fuzzy サンプル](https://tanstack.com/table/latest/docs/framework/react/examples/filters-fuzzy) を参照してください。

## 宣言のマージでメタにグローバルに型を付ける（v8 方式） {#typing-meta-globally-with-declaration-merging-v8-style}

モジュール拡張で `TableMeta` と `ColumnMeta` のインターフェースを拡張する v8 のやり方は、v9 でも使えます。v8 からの変更点はジェネリクスの形だけで、どちらのインターフェースでも `TFeatures` が最初の型パラメーターになりました。

```ts
import type { CellData, RowData, TableFeatures } from '@tanstack/react-table'

declare module '@tanstack/react-table' {
  interface TableMeta<TFeatures extends TableFeatures, TData extends RowData> {
    updateData: (rowIndex: number, columnId: string, value: unknown) => void
  }

  interface ColumnMeta<
    TFeatures extends TableFeatures,
    TData extends RowData,
    TValue extends CellData = CellData,
  > {
    filterVariant?: 'text' | 'range' | 'select'
  }
}
```


宣言のマージの欠点は、それが**グローバル**であることです。あるテーブルが実際にそのメタを渡しているかどうかにかかわらず、プロジェクト全体のすべてのテーブルが同じメタの型を持ちます。必要なものが異なるテーブルがたくさんある場合は、先に説明したテーブルごとのスロットのほうが適しています。

2つのやり方は、単純な優先順位で解決されます。`features` オブジェクトが `tableMeta` か `columnMeta` のスロットを宣言していれば、その機能で作ったテーブルにはそのスロットの型が使われ、グローバルに宣言したインターフェースは（マージされずに）_置き換えられ_ ます。機能にスロットを宣言していないテーブルは、宣言のマージで定義したインターフェースを使います。

## 代わりにカスタム機能を使うべきとき {#when-to-use-custom-features-instead}

メタは意図的にシンプルにしてあります。テーブルを通じて持ち回る、型付きの値の入れ物です。デフォルト値を持つ本物のテーブル _オプション_ や、新しい _状態_、テーブルインスタンス上の新しい _API_（`table.toggleDensity()` など）がほしくなったら、代わりに [カスタム機能](../framework/react/guide/custom-features) を書くことを検討してください。カスタム機能は同じ `features` オプションに組み込まれ、同じように `typeof features` から型が推論され、独自のオプション、状態、インスタンスメソッドを宣言できます。メタは、そうしたことをするためには作られていません。
