---
id: ColumnDef_FeatureMap
title: ColumnDef_FeatureMap
---

定義元: [types/ColumnDef.ts:132](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L132)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](../type-aliases/CellData.md)

## プロパティ {#properties}

### cellSelectionFeature {#cellselectionfeature}

```ts
cellSelectionFeature: ColumnDef_CellSelection;
```

定義元: [types/ColumnDef.ts:137](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L137)

***

### cellSpanningFeature {#cellspanningfeature}

```ts
cellSpanningFeature: ColumnDef_CellSpanning<TFeatures, TData, TValue>;
```

定義元: [types/ColumnDef.ts:138](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L138)

***

### columnFilteringFeature {#columnfilteringfeature}

```ts
columnFilteringFeature: ColumnDef_ColumnFiltering<TFeatures, TData>;
```

定義元: [types/ColumnDef.ts:139](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L139)

***

### columnGroupingFeature {#columngroupingfeature}

```ts
columnGroupingFeature: ColumnDef_ColumnGrouping<TFeatures, TData>;
```

定義元: [types/ColumnDef.ts:140](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L140)

***

### columnPinningFeature {#columnpinningfeature}

```ts
columnPinningFeature: ColumnDef_ColumnPinning;
```

定義元: [types/ColumnDef.ts:141](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L141)

***

### columnResizingFeature {#columnresizingfeature}

```ts
columnResizingFeature: ColumnDef_ColumnResizing;
```

定義元: [types/ColumnDef.ts:142](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L142)

***

### columnSizingFeature {#columnsizingfeature}

```ts
columnSizingFeature: ColumnDef_ColumnSizing;
```

定義元: [types/ColumnDef.ts:143](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L143)

***

### columnVisibilityFeature {#columnvisibilityfeature}

```ts
columnVisibilityFeature: ColumnDef_ColumnVisibility;
```

定義元: [types/ColumnDef.ts:144](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L144)

***

### globalFilteringFeature {#globalfilteringfeature}

```ts
globalFilteringFeature: ColumnDef_GlobalFiltering;
```

定義元: [types/ColumnDef.ts:145](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L145)

***

### rowAggregationFeature {#rowaggregationfeature}

```ts
rowAggregationFeature: ColumnDef_RowAggregation<TFeatures, TData, TValue>;
```

定義元: [types/ColumnDef.ts:146](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L146)

***

### rowSortingFeature {#rowsortingfeature}

```ts
rowSortingFeature: ColumnDef_RowSorting<TFeatures, TData>;
```

定義元: [types/ColumnDef.ts:147](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L147)
