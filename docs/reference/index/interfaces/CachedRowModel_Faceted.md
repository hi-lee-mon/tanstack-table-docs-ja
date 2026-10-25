---
id: CachedRowModel_Faceted
title: CachedRowModel_Faceted
---

定義元: [features/column-faceting/columnFacetingFeature.types.ts:50](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L50)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### facetedMinMaxValues? {#facetedminmaxvalues}

```ts
optional facetedMinMaxValues?: Record<string, () => [number, number] | undefined>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:55](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L55)

***

### facetedRowModels? {#facetedrowmodels}

```ts
optional facetedRowModels?: Record<string, () => RowModel<TFeatures, TData>>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:54](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L54)

***

### facetedUniqueValues? {#faceteduniquevalues}

```ts
optional facetedUniqueValues?: Record<string, () => Map<any, number>>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:56](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L56)

***

### globalFacetedMinMaxValues? {#globalfacetedminmaxvalues}

```ts
optional globalFacetedMinMaxValues?: () => [number, number] | undefined;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:58](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L58)

#### 戻り値 {#returns}

\[`number`, `number`\] \| `undefined`

***

### globalFacetedRowModel? {#globalfacetedrowmodel}

```ts
optional globalFacetedRowModel?: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:57](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L57)

#### 戻り値 {#returns-1}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

***

### globalFacetedUniqueValues? {#globalfaceteduniquevalues}

```ts
optional globalFacetedUniqueValues?: () => Map<any, number>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:59](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L59)

#### 戻り値 {#returns-2}

`Map`\<`any`, `number`\>
