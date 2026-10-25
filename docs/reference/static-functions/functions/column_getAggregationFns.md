---
id: column_getAggregationFns
title: column_getAggregationFns
---

```ts
function column_getAggregationFns<TFeatures, TData, TValue>(column): readonly ResolvedAggregationFn<TFeatures, TData>[];
```

定義元: [features/row-aggregation/rowAggregationFeature.utils.ts:225](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.utils.ts#L225)

列の単一または複数の集計オプションを解決し、検証します。

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

## 戻り値 {#returns}

readonly [`ResolvedAggregationFn`](../../index/interfaces/ResolvedAggregationFn.md)\<`TFeatures`, `TData`\>[]
