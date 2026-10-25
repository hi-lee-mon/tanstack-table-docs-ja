---
id: CachedRowModel_Grouped
title: CachedRowModel_Grouped
---

定義元: [features/column-grouping/columnGroupingFeature.types.ts:157](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L157)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### groupedRowModel {#groupedrowmodel}

```ts
groupedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:161](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L161)

#### 戻り値 {#returns}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>
