---
id: column_getAggregationValue
title: column_getAggregationValue
---

```ts
function column_getAggregationValue<TFeatures, TData, TValue>(column, options?): ColumnAggregationValue<TFeatures>;
```

定義元: [features/row-aggregation/rowAggregationFeature.utils.ts:415](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.utils.ts#L415)

`column.getAggregationValue(options?)` と、その既定のキャッシュを実装します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### column {#column}

[`Column_Internal`](../../index/interfaces/Column_Internal.md)\<`TFeatures`, `TData`, `TValue`\>

### options? {#options}

[`AggregationValueOptions`](../../index/interfaces/AggregationValueOptions.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`ColumnAggregationValue`](../../index/type-aliases/ColumnAggregationValue.md)\<`TFeatures`\>
