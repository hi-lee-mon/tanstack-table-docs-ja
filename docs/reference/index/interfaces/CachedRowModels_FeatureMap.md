---
id: CachedRowModels_FeatureMap
title: CachedRowModels_FeatureMap
---

定義元: [types/RowModel.ts:11](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/RowModel.ts#L11)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### columnFacetingFeature {#columnfacetingfeature}

```ts
columnFacetingFeature: CachedRowModel_Faceted<TFeatures, TData>;
```

定義元: [types/RowModel.ts:15](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/RowModel.ts#L15)

***

### columnFilteringFeature {#columnfilteringfeature}

```ts
columnFilteringFeature: CachedRowModel_Filtered<TFeatures, TData>;
```

定義元: [types/RowModel.ts:16](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/RowModel.ts#L16)

***

### columnGroupingFeature {#columngroupingfeature}

```ts
columnGroupingFeature: CachedRowModel_Grouped<TFeatures, TData>;
```

定義元: [types/RowModel.ts:18](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/RowModel.ts#L18)

***

### rowExpandingFeature {#rowexpandingfeature}

```ts
rowExpandingFeature: CachedRowModel_Expanded<TFeatures, TData>;
```

定義元: [types/RowModel.ts:17](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/RowModel.ts#L17)

***

### rowPaginationFeature {#rowpaginationfeature}

```ts
rowPaginationFeature: CachedRowModel_Paginated<TFeatures, TData>;
```

定義元: [types/RowModel.ts:19](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/RowModel.ts#L19)

***

### rowSortingFeature {#rowsortingfeature}

```ts
rowSortingFeature: CachedRowModel_Sorted<TFeatures, TData>;
```

定義元: [types/RowModel.ts:20](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/RowModel.ts#L20)
