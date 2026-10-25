---
id: Row_RowAggregation
title: Row_RowAggregation
---

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:289](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L289)

グループの集計を評価する間に使う、行ごとの内部のキャッシュです。

## プロパティ {#properties}

### \_aggregationValuesCache? {#_aggregationvaluescache}

```ts
optional _aggregationValuesCache?: Record<string, unknown>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:291](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L291)

列 ID をキーにした、キャッシュ済みの集計結果です。グループ行で必要になった時点で作られます。
