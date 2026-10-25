---
id: table_getSelectedRowIds
title: table_getSelectedRowIds
---

```ts
function table_getSelectedRowIds<TFeatures, TData>(table): string[];
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:339](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L339)

選択されているすべての行の ID を返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`string`[]

## 例 {#example}

```ts
const selectedRowIds = table_getSelectedRowIds(table)
```
