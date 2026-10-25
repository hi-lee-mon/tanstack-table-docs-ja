---
id: AggregationFnOption
title: AggregationFnOption
---

```ts
type AggregationFnOption<TFeatures, TData, TValue> =
  | AggregationFnRef<TFeatures, TData, TValue, any>
| ReadonlyArray<AggregationFnListItem<TFeatures, TData, TValue>>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:137](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L137)

単一の集計の参照か、キー付きのオブジェクトを作るリストです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` = `unknown`
