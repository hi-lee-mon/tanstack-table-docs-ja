---
id: AggregationValueResult
title: AggregationValueResult
---

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:323](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L323)

集計値の上書きを処理済みとして示します。

## 型パラメーター {#type-parameters}

### TResult {#tresult}

`TResult` = `unknown`

## プロパティ {#properties}

### value {#value}

```ts
value: TResult;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:325](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L325)

渡された値です。`undefined` でも処理済みの結果として扱われます。
