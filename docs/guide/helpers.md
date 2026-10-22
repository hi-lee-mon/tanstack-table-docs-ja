---
title: ヘルパーガイド
---

TanStack Table には、TypeScript の型推論を効かせながらテーブルの設定を書くための、小さなヘルパー関数がいくつか用意されています。ヘルパー自体が動作を追加するわけではありません。機能の組み合わせ・行の型・列定義・テーブルオプション・名前付きの関数レジストリの間の関係を、TypeScript が保てるようにするためのものです。

よく使うヘルパーは次のとおりです。

- `tableFeatures` - テーブルの静的な機能の組み合わせと、機能に関係するスロットを定義します
- `tableOptions` - 再利用できるテーブルオプションを組み立てるときに型推論を保ちます
- `createColumnHelper` - 厳密に型付けされた列定義を作成します

これらのヘルパーは、すべてのフレームワークのアダプターと `@tanstack/table-core` からエクスポートされています。

## `tableFeatures` {#tablefeatures}

テーブルで使う機能を宣言するには `tableFeatures()` を使います。v9 では機能はオプトイン（明示的に有効にする）方式です。そのため、このヘルパーに渡すオブジェクトによって、テーブル・列・行・ヘッダー・セルにどの機能の API と状態のスライスが存在するかが決まります。

コアの動作だけが必要な基本的なテーブルでは、空のオブジェクトを渡します。

```ts
import { tableFeatures } from '@tanstack/react-table'

const features = tableFeatures({})
```

テーブルに追加の動作が必要な場合は、機能のオブジェクトと行モデルのファクトリーを追加します。

```ts
import {
  columnFilteringFeature,
  createFilteredRowModel,
  createSortedRowModel,
  filterFn_includesString,
  rowSortingFeature,
  sortFn_alphanumeric,
  sortFn_text,
  tableFeatures,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnFilteringFeature,
  rowSortingFeature,
  filteredRowModel: createFilteredRowModel(),
  sortedRowModel: createSortedRowModel(),
  filterFns: { includesString: filterFn_includesString },
  sortFns: { alphanumeric: sortFn_alphanumeric, text: sortFn_text },
})
```

> [!NOTE]
> 組み込みのレジストリ全体（`filterFns`、`sortFns`、`aggregationFns`）を、これらのスロットにスプレッドで展開することも引き続きできます。ただし、組み込みの関数がすべてバンドルに含まれてしまうため、非推奨です。使う関数だけを慣例的な文字列キーで登録するか、登録はせずに列オプションの `filterFn`、`sortFn`、`aggregationFn` に関数を直接渡してください。文字列キー（デフォルトの `'auto'` を含む）で解決されるのは、登録済みの関数だけです。

`features` は参照が変わらないようにしてください。たいていのアプリでは、コンポーネントの外か、共有のテーブル設定のコードで定義します。`typeof features` はテーブルの型のあちこちで使われるため、features が変わらなければ、列ヘルパー・列定義・共有オプションも再利用しやすくなります。

### `tableFeatures` に入れるもの {#what-goes-in-tablefeatures}

`tableFeatures()` は、テーブルが作成される前に組み込まれるものを静的に設定する場所です。

- `rowSortingFeature`、`columnFilteringFeature`、独自の機能などの機能オブジェクト
- `createSortedRowModel()` や `createFilteredRowModel()` などの行モデルのファクトリー
- `filterFns`、`sortFns`、`aggregationFns` などの関数レジストリ
- `tableMeta` や `columnMeta` などの型専用のスロット（通常は `metaHelper` で宣言します）

`metaHelper()` は、`tableFeatures()` で型専用の meta スロットを宣言するときに便利です。`{} as MyMeta` と書くのと同じですが、意図がより明確になり、lint ルールによって型アサーションが誤って取り除かれることも防げます。

```ts
import {
  metaHelper,
  rowSortingFeature,
  tableFeatures,
} from '@tanstack/react-table'

type MyTableMeta = {
  updateData: (rowIndex: number, columnId: string, value: unknown) => void
}

type MyColumnMeta = {
  align?: 'left' | 'right'
}

const features = tableFeatures({
  rowSortingFeature,
  tableMeta: metaHelper<MyTableMeta>(),
  columnMeta: metaHelper<MyColumnMeta>(),
})
```

`tableMeta`、`columnMeta`、`metaHelper` について詳しくは、[テーブルと列の meta ガイド](./table-and-column-meta)を参照してください。

関数レジストリのキーは、テーブルや列のオプションで参照できる有効な文字列になります。

```ts
import {
  createColumnHelper,
  createSortedRowModel,
  rowSortingFeature,
  tableFeatures,
} from '@tanstack/react-table'

type Person = {
  rank: number
}

const features = tableFeatures({
  rowSortingFeature,
  sortedRowModel: createSortedRowModel(),
  sortFns: {
    byRank: (rowA, rowB, columnId) => {
      return rowA.getValue<number>(columnId) - rowB.getValue<number>(columnId)
    },
  },
})

const columnHelper = createColumnHelper<typeof features, Person>()

const columns = columnHelper.columns([
  columnHelper.accessor('rank', {
    sortFn: 'byRank',
  }),
])
```

行モデルのスロットと関数レジストリについて詳しくは、[行モデルガイド](./row-models)を参照してください。

## `tableOptions` {#tableoptions}

TanStack Table のジェネリクスの型推論を保ったまま、再利用できるテーブルオプションのオブジェクトを組み立てたい場合は `tableOptions()` を使います。このヘルパーは実行時には受け取ったオブジェクトをそのまま返します。価値があるのは TypeScript のオーバーロードの部分です。

共有のデフォルト値に役立ちます。

```ts
import { tableFeatures, tableOptions, useTable } from '@tanstack/react-table'

const features = tableFeatures({})

const sharedOptions = tableOptions({
  features,
  defaultColumn: {
    minSize: 80,
    maxSize: 400,
  },
  debugTable: true,
})

const table = useTable({
  ...sharedOptions,
  columns,
  data,
})
```

ラッパーやテーブルのファクトリーが必須のオプションを後から渡す場合にも役立ちます。たとえば、再利用するオプションの断片では `data`、`columns`、`features` を省略しても、残りのテーブルオプションの型を同じ機能の組み合わせと行の型に結び付けたままにできます。

```ts
import {
  createSortedRowModel,
  rowSortingFeature,
  tableFeatures,
  tableOptions,
  useTable,
} from '@tanstack/react-table'

type Person = {
  firstName: string
  lastName: string
  age: number
}

const features = tableFeatures({
  rowSortingFeature,
  sortedRowModel: createSortedRowModel(),
})

const sortableDefaults = tableOptions<typeof features, Person>({
  initialState: {
    sorting: [{ id: 'lastName', desc: false }],
  },
})

const table = useTable({
  features,
  columns,
  data,
  ...sortableDefaults,
})
```

`tableOptions()` は再利用する設定に使ってください。その場限りのテーブルのセットアップであれば、通常はアダプターのテーブル作成関数にオブジェクトを直接渡すだけで十分です。

## `createColumnHelper` {#createcolumnhelper}

`createColumnHelper()` は、列定義を書くための小さなユーティリティ群を作成します。

- `accessor` は、アクセサーのキーまたはアクセサー関数からデータ列を作成します
- `display` は、操作ボタンや選択用の操作部品など、表示専用の列を作成します
- `group` は、入れ子の列を含む親の列を作成します
- `columns` は列定義の配列をラップし、各列の値の型を個別に保ちます

このヘルパーは、機能の組み合わせと行の型の両方で型付けされます。

```ts
import { createColumnHelper, tableFeatures } from '@tanstack/react-table'

type Person = {
  firstName: string
  lastName: string
  age: number
}

const features = tableFeatures({})
const columnHelper = createColumnHelper<typeof features, Person>()

const columns = columnHelper.columns([
  columnHelper.accessor('firstName', {
    header: 'First Name',
  }),
  columnHelper.accessor((row) => row.lastName, {
    id: 'lastName',
    header: 'Last Name',
  }),
  columnHelper.display({
    id: 'actions',
    cell: (info) => `Actions for ${info.row.id}`,
  }),
])
```

実行時には、列ヘルパーは列定義のオブジェクトを返すだけです。主な目的は、アクセサーの値・機能ごとの列オプション・入れ子の列の配列を、場面によっては素のオブジェクトリテラルよりも正確に TypeScript で推論させることです。

列定義には専用のガイドがあり、アクセサー列・表示列・グループ列・ID・描画について詳しく説明しています。[列定義ガイド](./column-defs)を参照してください。

## 各ヘルパーを使う場面 {#when-to-use-each-helper}

`tableFeatures()` は v9 のすべてのテーブルで使ってください。空の `tableFeatures({})` の呼び出しでも、そのテーブルがコア機能だけを使うことをはっきり宣言できます。

`tableOptions()` は、オプションを共有したり、組み合わせたり、複数の段階で渡したりする場合に使います。オプションのオブジェクトを `useTable`、`createTable`、`injectTable`、`TableController`、`constructTable` に直接渡すだけなら不要です。

`createColumnHelper()` は、列の型推論を強く効かせたい場合、特にアクセサーの値・独自機能のオプション・入れ子の列グループで使います。用途によっては素の `ColumnDef` オブジェクトのほうが扱いやすいこともあり、その場合はそれを使ってもかまいません。
