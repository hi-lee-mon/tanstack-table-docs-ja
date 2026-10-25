---
id: CachedRowModel_All
title: CachedRowModel_All
---

定義元: [types/RowModel.ts:32](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/RowModel.ts#L32)

## 継承元 {#extends}

- `Partial`\<[`CachedRowModel_Core`](CachedRowModel_Core.md)\<`TFeatures`, `TData`\> & [`CachedRowModel_Expanded`](CachedRowModel_Expanded.md)\<`TFeatures`, `TData`\> & [`CachedRowModel_Faceted`](CachedRowModel_Faceted.md)\<`TFeatures`, `TData`\> & [`CachedRowModel_Filtered`](CachedRowModel_Filtered.md)\<`TFeatures`, `TData`\> & [`CachedRowModel_Grouped`](CachedRowModel_Grouped.md)\<`TFeatures`, `TData`\> & [`CachedRowModel_Paginated`](CachedRowModel_Paginated.md)\<`TFeatures`, `TData`\> & [`CachedRowModel_Sorted`](CachedRowModel_Sorted.md)\<`TFeatures`, `TData`\>\>

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

## プロパティ {#properties}

### coreRowModel? {#corerowmodel}

```ts
optional coreRowModel?: () => RowModel<TFeatures, TData>;
```

定義元: [core/row-models/coreRowModelsFeature.types.ts:24](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/row-models/coreRowModelsFeature.types.ts#L24)

#### 戻り値 {#returns}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from}

```ts
Partial.coreRowModel
```

***

### expandedRowModel? {#expandedrowmodel}

```ts
optional expandedRowModel?: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:146](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L146)

#### 戻り値 {#returns-1}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-1}

```ts
Partial.expandedRowModel
```

***

### facetedMinMaxValues? {#facetedminmaxvalues}

```ts
optional facetedMinMaxValues?: Record<string, () => [number, number] | undefined>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:55](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L55)

#### 継承元のメンバー {#inherited-from-2}

```ts
Partial.facetedMinMaxValues
```

***

### facetedRowModels? {#facetedrowmodels}

```ts
optional facetedRowModels?: Record<string, () => RowModel<TFeatures, TData>>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:54](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L54)

#### 継承元のメンバー {#inherited-from-3}

```ts
Partial.facetedRowModels
```

***

### facetedUniqueValues? {#faceteduniquevalues}

```ts
optional facetedUniqueValues?: Record<string, () => Map<any, number>>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:56](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L56)

#### 継承元のメンバー {#inherited-from-4}

```ts
Partial.facetedUniqueValues
```

***

### filteredRowModel? {#filteredrowmodel}

```ts
optional filteredRowModel?: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:312](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L312)

#### 戻り値 {#returns-2}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-5}

```ts
Partial.filteredRowModel
```

***

### globalFacetedMinMaxValues? {#globalfacetedminmaxvalues}

```ts
optional globalFacetedMinMaxValues?: () => [number, number] | undefined;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:58](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L58)

#### 戻り値 {#returns-3}

\[`number`, `number`\] \| `undefined`

#### 継承元のメンバー {#inherited-from-6}

```ts
Partial.globalFacetedMinMaxValues
```

***

### globalFacetedRowModel? {#globalfacetedrowmodel}

```ts
optional globalFacetedRowModel?: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:57](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L57)

#### 戻り値 {#returns-4}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-7}

```ts
Partial.globalFacetedRowModel
```

***

### globalFacetedUniqueValues? {#globalfaceteduniquevalues}

```ts
optional globalFacetedUniqueValues?: () => Map<any, number>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:59](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L59)

#### 戻り値 {#returns-5}

`Map`\<`any`, `number`\>

#### 継承元のメンバー {#inherited-from-8}

```ts
Partial.globalFacetedUniqueValues
```

***

### groupedRowModel? {#groupedrowmodel}

```ts
optional groupedRowModel?: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:161](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L161)

#### 戻り値 {#returns-6}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-9}

```ts
Partial.groupedRowModel
```

***

### paginatedRowModel? {#paginatedrowmodel}

```ts
optional paginatedRowModel?: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:152](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L152)

#### 戻り値 {#returns-7}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-10}

```ts
Partial.paginatedRowModel
```

***

### sortedRowModel? {#sortedrowmodel}

```ts
optional sortedRowModel?: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:308](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L308)

#### 戻り値 {#returns-8}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-11}

```ts
Partial.sortedRowModel
```
