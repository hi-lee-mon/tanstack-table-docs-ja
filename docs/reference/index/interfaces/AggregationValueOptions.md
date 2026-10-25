---
id: AggregationValueOptions
title: AggregationValueOptions
---

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:272](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L272)

呼び出し側が列の集計値を要求するときのオプションです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### maxDepth? {#maxdepth}

```ts
optional maxDepth?: number;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:277](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L277)

この要求に限り、列の `maxAggregationDepth` を上書きします。

***

### rows? {#rows}

```ts
optional rows?: readonly Row<TFeatures, TData>[];
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:279](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L279)

既定のグループ化前の行モデルの代わりに集計する行です。
