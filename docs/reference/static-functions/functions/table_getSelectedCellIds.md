---
id: table_getSelectedCellIds
title: table_getSelectedCellIds
---

```ts
function table_getSelectedCellIds<TFeatures, TData>(table): string[];
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:1174](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L1174)

選択されているすべてのセルの ID を、行優先の順で返します。

重なった範囲に含まれるセルは、最初に出てきた位置で1回だけ返されます。

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
const ids = table_getSelectedCellIds(table)
```
