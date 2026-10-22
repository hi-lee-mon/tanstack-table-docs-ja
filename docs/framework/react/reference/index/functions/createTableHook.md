---
id: createTableHook
title: createTableHook
---

```ts
function createTableHook<TFeatures, TTableComponents, TCellComponents, THeaderComponents>(__namedParameters): CreateTableHookResult<TFeatures, TTableComponents, TCellComponents, THeaderComponents>;
```

定義元: [src/createTableHook.tsx:692](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L692)

コンポーネントを組み合わせて使うための、コンポーネントがあらかじめ結び付けられたカスタムテーブルフックを作成します。

TanStack Form の `createFormHook` に相当するテーブル版です。次のことができます。
- 機能・行モデル・デフォルトのオプションを一度だけ定義し、すべてのテーブルで共有する
- 再利用できるテーブル・セル・ヘッダーのコンポーネントを登録する
- 登録したコンポーネントの中から、コンテキスト経由でテーブル・セル・ヘッダーのインスタンスにアクセスする
- App ラッパーコンポーネントを備えた拡張テーブルを返す `useAppTable` フックを得る
- 機能があらかじめ結び付けられた `createAppColumnHelper` 関数を得る

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TTableComponents {#ttablecomponents}

`TTableComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

### TCellComponents {#tcellcomponents}

`TCellComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

### THeaderComponents {#theadercomponents}

`THeaderComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

## パラメーター {#parameters}

### \_\_namedParameters {#namedparameters}

[`CreateTableHookOptions`](../type-aliases/CreateTableHookOptions.md)\<`TFeatures`, `TTableComponents`, `TCellComponents`, `THeaderComponents`\>

## 戻り値 {#returns}

[`CreateTableHookResult`](../interfaces/CreateTableHookResult.md)\<`TFeatures`, `TTableComponents`, `TCellComponents`, `THeaderComponents`\>

## 例 {#example}

```tsx
// hooks/table.ts
export const {
  useAppTable,
  createAppColumnHelper,
  useTableContext,
  useCellContext,
  useHeaderContext,
} = createTableHook({
  features: tableFeatures({
    rowPaginationFeature,
    rowSortingFeature,
    columnFilteringFeature,
    paginatedRowModel: createPaginatedRowModel(),
    sortedRowModel: createSortedRowModel(),
    filteredRowModel: createFilteredRowModel(),
    sortFns,
    filterFns,
  }),
  tableComponents: { PaginationControls, RowCount },
  cellComponents: { TextCell, NumberCell },
  headerComponents: { SortIndicator, ColumnFilter },
})

// Create column helper with TFeatures already bound
const columnHelper = createAppColumnHelper<Person>()

// components/table-components.tsx
function PaginationControls() {
  const table = useTableContext() // TFeatures already known!
  return <table.Subscribe selector={(s) => s.pagination}>...</table.Subscribe>
}

// features/users.tsx
function UsersTable({ data }: { data: Person[] }) {
  const table = useAppTable({
    columns,
    data, // TData inferred from Person[]
  })

  return (
    <table.AppTable>
      <table>
        <thead>
          {table.getHeaderGroups().map(headerGroup => (
            <tr key={headerGroup.id}>
              {headerGroup.headers.map(h => (
                <table.AppHeader header={h} key={h.id}>
                  {(header) => (
                    <th>
                      <table.FlexRender header={h} />
                      <header.SortIndicator />
                    </th>
                  )}
                </table.AppHeader>
              ))}
            </tr>
          ))}
        </thead>
        <tbody>
          {table.getRowModel().rows.map(row => (
            <tr key={row.id}>
              {row.getAllCells().map(c => (
                <table.AppCell cell={c} key={c.id}>
                  {(cell) => <td><cell.TextCell /></td>}
                </table.AppCell>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
      <table.PaginationControls />
    </table.AppTable>
  )
}
```
