---
id: AggregationFnRef
title: AggregationFnRef
---

```ts
type AggregationFnRef<TFeatures, TData, TValue, TResult> =
  | "auto"
  | ExtractAggregationFnKeys<TFeatures>
| AggregationFnDef<TFeatures, TData, TValue, TResult>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:103](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L103)

登録された名前、自動推論、インラインの集計定義のいずれかです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` = `unknown`

### TResult {#tresult}

`TResult` = `unknown`
