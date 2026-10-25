---
id: Cell_RowAggregation
title: Cell_RowAggregation
---

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:283](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L283)

`rowAggregationFeature` が追加する、セルのインスタンス API です。

## プロパティ {#properties}

### getIsAggregated {#getisaggregated}

```ts
getIsAggregated: () => boolean;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:285](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L285)

このセルが合成されたグループ行で集計値を表示しているかどうかです。

#### 戻り値 {#returns}

`boolean`
