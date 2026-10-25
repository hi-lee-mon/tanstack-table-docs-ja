---
id: CustomAggregationFns
title: CustomAggregationFns
---

```ts
type CustomAggregationFns<TFeatures, TData> = Record<string, AggregationFnDef<TFeatures, TData, any, any>>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:89](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L89)

機能の組み合わせに登録された、名前付きのコンテキストベースの集計定義です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)
