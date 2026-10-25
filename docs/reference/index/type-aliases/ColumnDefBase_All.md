---
id: ColumnDefBase_All
title: ColumnDefBase_All
---

```ts
type ColumnDefBase_All<TFeatures, TData, TValue> = ColumnDefBase_Core<TFeatures, TData, TValue> & Partial<ColumnDef_RowAggregation<TFeatures, TData, TValue> & ColumnDef_CellSelection & ColumnDef_CellSpanning<TFeatures, TData, TValue> & ColumnDef_ColumnVisibility & ColumnDef_ColumnPinning & ColumnDef_ColumnFiltering<TFeatures, TData> & ColumnDef_GlobalFiltering & ColumnDef_RowSorting<TFeatures, TData> & ColumnDef_ColumnGrouping<TFeatures, TData> & ColumnDef_ColumnSizing & ColumnDef_ColumnResizing>;
```

定義元: [types/ColumnDef.ts:160](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L160)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](CellData.md) = [`CellData`](CellData.md)
