---
title: useLegacyTable で段階的に移行する
---

`useLegacyTable` フックは、内部では v9 を使いながら v8 形式の API を受け付ける互換レイヤーです。段階的に移行する必要があるチームや、コードベースが大きく、すぐには全面的な移行が難しい場合に役立ちます。

> [!WARNING]
> `useLegacyTable` は**非推奨**であり、移行中の一時的な補助としてのみ使うことを想定しています。デフォルトですべての機能を含むため、ツリーシェイク可能な v9 の API を使う場合よりもバンドルが大きくなります。パフォーマンスの向上とバンドルの縮小のために、`useTable` への移行を計画してください。

## `useLegacyTable` を使う場面 {#when-to-use-uselegacytable}

- 既存の v8 のコードベースがあり、依存関係をアップグレードする必要がある
- テーブルを1つずつ、段階的に移行したい
- v9 との互換性は必要だが、まだ全面的に移行する時間がない

## 基本的な使い方 {#basic-usage}

```tsx
import { useState } from 'react'
import { flexRender } from '@tanstack/react-table'
import {
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  legacyCreateColumnHelper,
  useLegacyTable,
} from '@tanstack/react-table/legacy'
import type {
  ColumnFiltersState,
  PaginationState,
  SortingState,
} from '@tanstack/react-table'
import type {
  LegacyColumn,
  LegacyColumnDef,
  LegacyRow,
} from '@tanstack/react-table/legacy'

interface Person {
  name: string
  email: string
  age: number
}

const columnHelper = legacyCreateColumnHelper<Person>()

const columns: LegacyColumnDef<Person>[] = [
  columnHelper.accessor('name', { header: 'Name' }),
  columnHelper.accessor('email', { header: 'Email' }),
  columnHelper.accessor('age', { header: 'Age' }),
  columnHelper.display({ id: 'actions', header: 'Actions' }),
]

function MyTable({ data }: { data: Person[] }) {
  const [sorting, setSorting] = useState<SortingState>([])
  const [columnFilters, setColumnFilters] = useState<ColumnFiltersState>([])
  const [pagination, setPagination] = useState<PaginationState>({
    pageIndex: 0,
    pageSize: 10,
  })

  // useLegacyTable accepts the v8-style API
  const table = useLegacyTable({
    columns,
    data,
    getCoreRowModel: getCoreRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    state: { sorting, columnFilters, pagination },
    onSortingChange: setSorting,
    onColumnFiltersChange: setColumnFilters,
    onPaginationChange: setPagination,
  })

  return (
    <table>
      <thead>
        {table.getHeaderGroups().map((headerGroup) => (
          <tr key={headerGroup.id}>
            {headerGroup.headers.map((header) => (
              <th key={header.id}>
                {flexRender(
                  header.column.columnDef.header,
                  header.getContext(),
                )}
                {header.column.getCanFilter() ? (
                  <Filter column={header.column} />
                ) : null}
              </th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody>
        {table.getRowModel().rows.map((row) => (
          <tr key={row.id}>
            {row.getAllCells().map((cell) => (
              <td key={cell.id}>
                {cell.column.id === 'actions' ? (
                  <RowActions row={row} />
                ) : (
                  flexRender(cell.column.columnDef.cell, cell.getContext())
                )}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  )
}

function Filter({ column }: { column: LegacyColumn<Person> }) {
  return (
    <input
      value={(column.getFilterValue() as string) ?? ''}
      onChange={(e) => column.setFilterValue(e.target.value)}
      placeholder="Filter..."
    />
  )
}

function RowActions({ row }: { row: LegacyRow<Person> }) {
  return <button onClick={() => console.log(row.original)}>Edit</button>
}
```

## 型ヘルパー {#type-helpers}

`useLegacyTable` を使うときは、TypeScript で正しく型付けするために次の型ヘルパーを使います。

| 型                                  | 説明                                                            |
| ----------------------------------- | --------------------------------------------------------------- |
| `LegacyColumnDef<TData>`            | 列定義の型（v8 の `ColumnDef<TData>` に相当）                   |
| `LegacyColumn<TData>`               | 列インスタンスの型                                              |
| `LegacyRow<TData>`                  | 行インスタンスの型                                              |
| `LegacyCell<TData>`                 | セルインスタンスの型                                            |
| `LegacyTable<TData>`                | テーブルインスタンスの型                                        |
| `legacyCreateColumnHelper<TData>()` | StockFeatures があらかじめ結び付けられた列ヘルパー。TData だけを指定すればよい |

### `legacyCreateColumnHelper` を使う {#using-legacycreatecolumnhelper}

`createColumnHelper` の代わりに `legacyCreateColumnHelper` を使います。StockFeatures があらかじめ結び付けられているため、指定が必要なのは `TData` だけです。

```tsx
import { legacyCreateColumnHelper } from '@tanstack/react-table/legacy'
import type { LegacyColumnDef } from '@tanstack/react-table/legacy'

const columnHelper = legacyCreateColumnHelper<Person>()

const columns: LegacyColumnDef<Person>[] = [
  columnHelper.accessor('name', { header: 'Name' }),
  // ...
]
```

## v8 との API の違い {#api-differences-from-v8}

`useLegacyTable` は v8 との互換性を目指していますが、いくつか違いがあります。

### 行モデルの関数 {#row-model-functions}

`get*RowModel()` 関数は `@tanstack/react-table/legacy` からインポートします。

```tsx
import {
  getCoreRowModel,
  getFilteredRowModel,
  getSortedRowModel,
  getPaginationRowModel,
  getExpandedRowModel,
  getGroupedRowModel,
  getFacetedRowModel,
  getFacetedMinMaxValues,
  getFacetedUniqueValues,
} from '@tanstack/react-table/legacy'
```

### ソート関数の名前変更 {#sorting-function-renames}

v9 では、ソート関連の API の名前が変わっている点に注意してください。列定義でカスタムのソート関数を使っている場合は次のとおりです。

| v8          | v9       |
| ----------- | -------- |
| `sortingFn` | `sortFn` |

組み込みのソートについてはレガシーテーブルのアダプターが内部で対応しますが、カスタムのソート関数を定義している場合は、この名前変更に気をつけてください。

## 注意点と制限 {#caveats-and-limitations}

### バンドルサイズ {#bundle-size}

`useLegacyTable` は、v8 と同じくデフォルトで**すべての機能**を含みます。つまり、次のようになります。

- ツリーシェイキングの恩恵を受けられない
- 各機能が v8 から大きくなっており、そのすべてを抱えることになるため、バンドルサイズは v8 より**かなり大きく**なる
- v9 の API がツリーシェイク可能になっているのは、全員のバンドルを肥大化させずに TanStack Table が機能を追加していけるようにするためです。ある機能のコストを負担するのは、その機能をオプトインしたユーザーだけです
- バンドルサイズが気になる場合は、完全な v9 の API への移行を優先してください

### 非推奨 {#deprecation}

`useLegacyTable` は非推奨であり、将来のメジャーバージョンで削除されます。移行を楽にするためだけに存在しています。それを踏まえて移行のスケジュールを立ててください。

### 状態全体の購読のみ {#full-state-subscription-only}

`useLegacyTable` は常にテーブルの状態全体を購読します。そのため、v8 と同じく、テーブルを作成したコンポーネントは状態が変わるたびに再レンダーされます。v9 の細かい単位での描画の最適化（範囲を絞った `useTable` のセレクター）は、レガシーのフックでは使えません。

### `createTableHook` とは連携できない {#no-createtablehook-integration}

`useLegacyTable` は `createTableHook` と組み合わせて使えません。再利用できるテーブル設定を作りたい場合は、完全な v9 の API に移行してください。

## 移行の手順 {#migration-path}

完全な v9 の API に移行する準備ができたら、次の手順で進めます。

1. `useLegacyTable` を `useTable` に置き換える
2. `tableFeatures()` を使って `features` を定義する
3. `get*RowModel()` オプションを `rowModels` に変換する
4. 型を `Legacy*` から標準の v9 の型に更新する

詳しい手順は[メインの移行ガイド](./migrating.md)を参照してください。

## 例 {#example}

動作する実装は [Basic useLegacyTable の例](https://tanstack.com/table/latest/docs/framework/react/examples/basic-use-legacy-table)を参照してください。
