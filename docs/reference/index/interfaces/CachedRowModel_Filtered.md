---
id: CachedRowModel_Filtered
title: CachedRowModel_Filtered
---

定義元: [features/column-filtering/columnFilteringFeature.types.ts:308](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L308)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### filteredRowModel {#filteredrowmodel}

```ts
filteredRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:312](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L312)

#### 戻り値 {#returns}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>
