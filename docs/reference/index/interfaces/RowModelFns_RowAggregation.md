---
id: RowModelFns_RowAggregation
title: RowModelFns_RowAggregation
---

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:81](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L81)

テーブルの機能の組み合わせが持つ、集計定義のレジストリです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### aggregationFns {#aggregationfns}

```ts
aggregationFns: Record<string, AggregationFnDef<TFeatures, TData, any, any>>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:85](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L85)
