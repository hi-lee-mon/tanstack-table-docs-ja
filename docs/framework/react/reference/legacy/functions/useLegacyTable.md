---
id: useLegacyTable
title: useLegacyTable
---

```ts
function useLegacyTable<TData>(options): LegacyReactTable<TData>;
```

定義元: [src/useLegacyTable.ts:405](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L405)

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## パラメーター {#parameters}

### options {#options}

[`LegacyTableOptions`](../type-aliases/LegacyTableOptions.md)\<`TData`\>

v8 形式のレガシーなテーブルオプション

## 戻り値 {#returns}

[`LegacyReactTable`](../type-aliases/LegacyReactTable.md)\<`TData`\>

状態全体を購読し、`getState()` メソッドを備えたテーブルインスタンス

## 非推奨 {#deprecated}

このフックは、TanStack Table v8 から移行するための互換レイヤーとして提供されています。

代わりに、新しい `useTable` フックを使い、`features` オプションを明示的に指定してください。

```tsx
// New v9 API
const features = tableFeatures({
  columnFilteringFeature,
  rowSortingFeature,
  rowPaginationFeature,
  filteredRowModel: createFilteredRowModel(),
  sortedRowModel: createSortedRowModel(),
  paginatedRowModel: createPaginatedRowModel(),
  filterFns,
  sortFns,
})

const table = useTable({
  features,
  columns,
  data,
})
```

v8 からの主な違いは次のとおりです。
- 機能はツリーシェイク可能です。使うものだけをインポートします
- 行モデルと関数のレジストリは、`features` オプションで明示的に渡します
- 細かい単位で再レンダーしたいときは `table.Subscribe` を使います
- 状態には、第2引数で選択したうえで `table.state` からアクセスします
