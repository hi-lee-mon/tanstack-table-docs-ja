---
title: 組み立て可能なテーブル（createTableHook）ガイド
---

`createTableHook` は、アプリ専用のテーブルファクトリーを作成します。共有する機能・行モデル・テーブルオプションの既定値を一度だけ定義しておき、個々の React テーブルは、そのテーブル固有の列とデータだけで作成できます。

同じ API で、再利用できるテーブル・セル・ヘッダーのコンポーネントを登録することもできますが、コンポーネントの登録は任意です。まずは共有するオプションと機能から始めてください。再利用できるコンポーネントは、アプリでテーブル UI の部品を統一したくなったときにだけ追加すれば十分です。

## サンプル {#examples}

- [基本的な useAppTable](https://tanstack.com/table/latest/docs/framework/react/examples/basic-use-app-table) - `createTableHook` の最小構成のセットアップ。
- [組み立て可能なテーブル](https://tanstack.com/table/latest/docs/framework/react/examples/composable-tables) - `src/hooks/table.ts` と再利用できるコンポーネントを共有する、より機能の多い Users テーブルと Products テーブル。

## 共有する機能とオプションから始める {#start-with-shared-features-and-options}

アプリ用のテーブルフックを1つ作り、そこに機能のセット・行モデル・共有の既定値をまとめます。この例では、`useAppTable` で作るすべてのテーブルでソートが使えるようにしています。

```tsx
import {
  createSortedRowModel,
  createTableHook,
  rowSortingFeature,
  sortFns,
  tableFeatures,
} from '@tanstack/react-table'

const features = tableFeatures({
  rowSortingFeature,
  sortedRowModel: createSortedRowModel(),
  sortFns,
})

const { useAppTable, createAppColumnHelper } = createTableHook({
  features,
  debugTable: true,
  enableSortingRemoval: false,
})
```

`createTableHook` に渡したオプションは、`useAppTable` で作るすべてのテーブルの既定値になります。`features` オプションは戻り値の列ヘルパーにも結び付けられるので、列定義の側でもソートの API が使えることが型として分かります。

## アプリ用の列を作成する {#create-app-columns}

行の型ごとに列ヘルパーを1つ作成します。ヘルパーはすでにアプリの機能のセットに結び付いているので、各テーブルの列定義で `typeof features` を引き回す必要はありません。

```tsx
type Person = {
  firstName: string
  lastName: string
  age: number
  visits: number
}

const columnHelper = createAppColumnHelper<Person>()

const columns = columnHelper.columns([
  columnHelper.accessor('firstName', {
    cell: (info) => info.getValue(),
  }),
  columnHelper.accessor((row) => row.lastName, {
    id: 'lastName',
    header: () => <span>Last Name</span>,
    cell: (info) => <i>{info.getValue()}</i>,
  }),
  columnHelper.accessor('age', {
    header: 'Age',
  }),
  columnHelper.accessor('visits', {
    header: 'Visits',
  }),
])
```

## テーブルを作成する {#create-a-table}

各テーブルは `useAppTable` で作成します。`columns` や `data` などテーブル固有の入力は呼び出し側で渡し、共有の機能と既定値はフックから提供されます。

```tsx
function UsersTable({ data }: { data: Person[] }) {
  const table = useAppTable(
    {
      key: 'users-table',
      columns,
      data,
    },
    (state) => ({ sorting: state.sorting }),
  )

  // render with the table instance
}
```

## 通常のテーブル API でレンダーする {#render-with-the-normal-table-apis}

単体の `useTable` で作ったテーブルと同じテーブルインスタンスの API で、テーブルをレンダーできます。この簡単な方法なら、`AppTable`、`AppCell`、`AppHeader` や、登録したコンポーネントは必要ありません。

```tsx
return (
  <table>
    <thead>
      {table.getHeaderGroups().map((headerGroup) => (
        <tr key={headerGroup.id}>
          {headerGroup.headers.map((header) => (
            <th
              key={header.id}
              onClick={header.column.getToggleSortingHandler()}
            >
              {header.isPlaceholder ? null : (
                <table.FlexRender header={header} />
              )}
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
              <table.FlexRender cell={cell} />
            </td>
          ))}
        </tr>
      ))}
    </tbody>
  </table>
)
```

## 共有の既定値をテーブルごとに上書きする {#override-shared-defaults-per-table}

`useAppTable` に渡したオプションは、`createTableHook` の既定値を上書きします。別のアプリ用フックを作らずに、一部のテーブルだけ動作を変えたいときに使います。

```tsx
const table = useAppTable(
  {
    key: 'sortable-users-table',
    columns,
    data,
    enableSortingRemoval: true,
  },
  (state) => ({ sorting: state.sorting }),
)
```

## 任意: 再利用できるコンポーネント {#optional-reusable-components}

より機能の多い composable-tables のサンプルでは、`createTableHook` をコンポーネントの登録先（レジストリ）としても使っています。複数のテーブルで、同じツールバーの操作部品、セルの描画部品、ヘッダーの描画部品、フッターの描画部品を共有したいときに使います。

### コンポーネントレジストリのセットアップ {#component-registry-setup}

組み立て可能なテーブルのサンプルでは、共有の設定を `src/hooks/table.ts` に置いています。

```tsx
import {
  columnFilteringFeature,
  createFilteredRowModel,
  createPaginatedRowModel,
  createSortedRowModel,
  createTableHook,
  filterFns,
  rowPaginationFeature,
  rowSortingFeature,
  sortFns,
  tableFeatures,
} from '@tanstack/react-table'

import {
  PaginationControls,
  RowCount,
  TableToolbar,
} from '../components/table-components'
import {
  CategoryCell,
  NumberCell,
  PriceCell,
  ProgressCell,
  RowActionsCell,
  StatusCell,
  TextCell,
} from '../components/cell-components'
import {
  ColumnFilter,
  FooterColumnId,
  FooterSum,
  SortIndicator,
} from '../components/header-components'

const features = tableFeatures({
  columnFilteringFeature,
  rowPaginationFeature,
  rowSortingFeature,
  sortedRowModel: createSortedRowModel(),
  filteredRowModel: createFilteredRowModel(),
  paginatedRowModel: createPaginatedRowModel(),
  sortFns,
  filterFns,
})

export const {
  createAppColumnHelper,
  useAppTable,
  useTableContext,
  useCellContext,
  useHeaderContext,
} = createTableHook({
  features,
  getRowId: (row) => row.id,
  tableComponents: {
    PaginationControls,
    RowCount,
    TableToolbar,
  },
  cellComponents: {
    TextCell,
    NumberCell,
    StatusCell,
    ProgressCell,
    RowActionsCell,
    PriceCell,
    CategoryCell,
  },
  headerComponents: {
    SortIndicator,
    ColumnFilter,
    FooterColumnId,
    FooterSum,
  },
})
```

### 返されるヘルパー {#returned-helpers}

| ヘルパー | 用途 |
| --- | --- |
| `useAppTable` | 共有の機能（行モデルのファクトリーを含む）・既定値・登録したコンポーネントを備えたテーブルを作成します。 |
| `createAppColumnHelper` | `TFeatures` と登録したコンポーネントの型があらかじめ結び付いた列ヘルパーを作成します。 |
| `useTableContext` | 登録したテーブルコンポーネントの中で、現在のテーブルを読み取ります。 |
| `useCellContext` | 登録したセルコンポーネントの中で、現在のセルを読み取ります。 |
| `useHeaderContext` | 登録したヘッダーコンポーネントの中で、現在のヘッダー・フッターを読み取ります。 |

> [!IMPORTANT]
> `useTableContext`、`useCellContext`、`useHeaderContext` は、（上の例のように）`createTableHook` を呼び出したのと同じモジュールからインポートしてください。これらのフックには `TFeatures` と登録したコンポーネントのマップに基づく型が付いているので、`table.PaginationControls`、`cell.TextCell`、`header.SortIndicator` などの値にも型が付きます。詳しい説明と、スコープ付きコンテキストという抜け道（escape hatch）については、[テーブルコンテキストガイド](./table-context)を参照してください。

### コンポーネントを使う列 {#component-columns}

行の型ごとに列ヘルパーを1つ作成します。ヘルパーはすでにアプリのテーブル設定に結び付いているので、列定義から、登録したセルやヘッダーのコンポーネントを直接参照できます。

```tsx
const personColumnHelper = createAppColumnHelper<Person>()

const columns = useMemo(
  () =>
    personColumnHelper.columns([
      personColumnHelper.accessor('firstName', {
        header: 'First Name',
        footer: (props) => props.column.id,
        cell: ({ cell }) => <cell.TextCell />,
      }),
      personColumnHelper.accessor('age', {
        header: 'Age',
        footer: (props) => props.column.id,
        cell: ({ cell }) => <cell.NumberCell />,
      }),
      personColumnHelper.display({
        id: 'actions',
        header: 'Actions',
        cell: ({ cell }) => <cell.RowActionsCell />,
      }),
    ]),
  [],
)
```

登録したセルコンポーネントは内部で `useCellContext()` を使い、登録したヘッダー・フッターのコンポーネントは `useHeaderContext()` を使います。

### コンポーネントを使ったテーブルのレンダー {#component-table-rendering}

各テーブルは `useAppTable` で作成します。`key`、`columns`、`data` などテーブル固有のオプションを渡すと、共有の `features`、`getRowId`、コンポーネントのレジストリはフックから提供されます。

```tsx
const table = useAppTable(
  {
    key: 'users-table',
    columns,
    data,
    debugTable: true,
  },
  (state) => state,
)
```

返されるテーブルには、ラッパーとして `AppTable`、`AppHeader`、`AppCell`、`AppFooter` が含まれます。このサンプルでは `AppTable` にセレクターを渡し、そのテーブルが使う状態のスライスをレンダー側で購読できるようにしています。

```tsx
<table.AppTable
  selector={(state) => ({
    pagination: state.pagination,
    sorting: state.sorting,
    columnFilters: state.columnFilters,
  })}
>
  {({ sorting, columnFilters }) => (
    <div className="table-container">
      <table.TableToolbar title="Users Table" onRefresh={refreshData} />

      <table>
        <thead>
          {table.getHeaderGroups().map((headerGroup) => (
            <tr key={headerGroup.id}>
              {headerGroup.headers.map((h) => (
                <table.AppHeader header={h} key={h.id}>
                  {(header) => (
                    <th onClick={header.column.getToggleSortingHandler()}>
                      <header.FlexRender />
                      <header.SortIndicator />
                      <header.ColumnFilter />
                    </th>
                  )}
                </table.AppHeader>
              ))}
            </tr>
          ))}
        </thead>
        <tbody>
          {table.getRowModel().rows.map((row) => (
            <tr key={row.id}>
              {row.getAllCells().map((c) => (
                <table.AppCell cell={c} key={c.id}>
                  {(cell) => (
                    <td>
                      <cell.FlexRender />
                    </td>
                  )}
                </table.AppCell>
              ))}
            </tr>
          ))}
        </tbody>
      </table>

      <table.PaginationControls />
      <table.RowCount />
    </div>
  )}
</table.AppTable>
```

### コンポーネントレジストリを再利用する {#reusing-the-component-registry}

このサンプルでは、同じ `createAppColumnHelper` から `personColumnHelper` と `productColumnHelper` の両方を作成し、同じ `useAppTable` ファクトリーで Users テーブルと Products テーブルをレンダーしています。データと列は各テーブルが持ち、テーブルの土台とコンポーネントの決まりごとはアプリ用フックが持ちます。

### スコープ付きコンテキスト {#scoped-contexts}

登録したコンポーネントは、現在のテーブル・セル・ヘッダーを React のコンテキストから読み取ります。初期設定では `createTableHook` が共有のコンテキストでこれをつないでくれるので、意識する必要はありません。異なるテーブル設定を入れ子にしていて、それぞれのコンテキストを分離する必要がある場合は、`createTableHookContexts` でスコープ付きコンテキストを作成し、`createTableHook` に渡してください。詳しい説明とサンプルは[テーブルコンテキストガイド](./table-context)を参照してください。

## このパターンを使う場面 {#when-to-use-this-pattern}

複数のテーブルで機能・行モデル・オプションの既定値・決まりごとを共有したい場合は、`createTableHook` を使います。1回きりのテーブルなら、単体の `useTable` API を使います。コンポーネントのレジストリは、アプリで再利用できるテーブル UI の部品を統一したい場合にだけ追加してください。
