---
id: column_getAutoAggregationFn
title: column_getAutoAggregationFn
---

```ts
function column_getAutoAggregationFn<TFeatures, TData, TValue>(column):
  | AggregationFnDef<TFeatures, TData, any, any>
  | undefined;
```

定義元: [features/row-aggregation/rowAggregationFeature.utils.ts:183](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.utils.ts#L183)

最初のコア行から推論した `sum` または `extent` の定義を返します。

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

  \| [`AggregationFnDef`](../../index/interfaces/AggregationFnDef.md)\<`TFeatures`, `TData`, `any`, `any`\>
  \| `undefined`
