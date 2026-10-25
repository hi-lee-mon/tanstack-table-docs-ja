---
id: RowModelFns_All
title: RowModelFns_All
---

定義元: [types/RowModelFns.ts:25](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/RowModelFns.ts#L25)

## 継承元 {#extends}

- `Partial`\<[`RowModelFns_ColumnFiltering`](RowModelFns_ColumnFiltering.md)\<`TFeatures`, `TData`\> & [`RowModelFns_RowAggregation`](RowModelFns_RowAggregation.md)\<`TFeatures`, `TData`\> & [`RowModelFns_RowSorting`](RowModelFns_RowSorting.md)\<`TFeatures`, `TData`\>\>

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### aggregationFns? {#aggregationfns}

```ts
optional aggregationFns?: Record<string, AggregationFnDef<TFeatures, TData, any, any>>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:85](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L85)

#### 継承元のメンバー {#inherited-from}

```ts
Partial.aggregationFns
```

***

### filterFns? {#filterfns}

```ts
optional filterFns?: Record<string, FilterFn<TFeatures, TData>>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:57](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L57)

#### 継承元のメンバー {#inherited-from-1}

```ts
Partial.filterFns
```

***

### sortFns? {#sortfns}

```ts
optional sortFns?: Record<string, SortFn<TFeatures, TData>>;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:29](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L29)

#### 継承元のメンバー {#inherited-from-2}

```ts
Partial.sortFns
```
