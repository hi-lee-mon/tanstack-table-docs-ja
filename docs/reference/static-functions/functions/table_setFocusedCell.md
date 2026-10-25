---
id: table_setFocusedCell
title: table_setFocusedCell
---

```ts
function table_setFocusedCell<TFeatures, TData>(
   table,
   rowId,
   columnId): void;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:754](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L754)

選択を、指定した座標の1つのセルにまとめます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### rowId {#rowid}

`string`

### columnId {#columnid}

`string`

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setFocusedCell(table, '3', 'firstName')
```
