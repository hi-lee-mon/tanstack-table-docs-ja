---
id: TableOptions_All
title: TableOptions_All
---

```ts
type TableOptions_All<TFeatures, TData> = TableOptions_Core<TFeatures, TData> & Partial<TableOptions_RowAggregation & TableOptions_CellSelection<TFeatures, TData> & TableOptions_CellSpanning & TableOptions_ColumnFiltering<TFeatures, TData> & TableOptions_ColumnGrouping & TableOptions_ColumnOrdering & TableOptions_ColumnPinning & TableOptions_ColumnResizing & TableOptions_ColumnSizing & TableOptions_ColumnVisibility & TableOptions_GlobalFiltering<TFeatures, TData> & TableOptions_RowExpanding<TFeatures, TData> & TableOptions_RowPagination & TableOptions_RowPinning<TFeatures, TData> & TableOptions_RowSelection<TFeatures, TData> & TableOptions_RowSorting & TableOptions_PluginFeatureMapTypes<TFeatures, TData>>;
```

定義元: [types/TableOptions.ts:142](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableOptions.ts#L142)

現在のジェネリックな機能の組み合わせにない機能のオプションを、機能のコードが読む必要がある場所で使う、内部用の広いオプションの形です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)
