---
id: table_getGroupedSelectedRowModel
title: table_getGroupedSelectedRowModel
---

```ts
function table_getGroupedSelectedRowModel<TFeatures, TData>(table):
  | RowModel<TFeatures, TData>
  | {
  flatRows: never[];
  rows: never[];
  rowsById: Record<string, unknown>;
};
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:306](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L306)

グループ化済み行モデルから、選択された行を含む行モデルを作ります。

選択されている行 ID がなければ、行をたどらずに空の行モデルを返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

  \| [`RowModel`](../../index/interfaces/RowModel.md)\<`TFeatures`, `TData`\>
  \| \{
  `flatRows`: `never`[];
  `rows`: `never`[];
  `rowsById`: `Record`\<`string`, `unknown`\>;
\}

## 例 {#example}

```ts
const selectedRows = table_getGroupedSelectedRowModel(table)
```
