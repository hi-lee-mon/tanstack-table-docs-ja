---
id: aggregationFn_mean
title: aggregationFn_mean
---

```ts
const aggregationFn_mean: AggregationFnDef<any, any, unknown, number | undefined>;
```

定義元: [features/row-aggregation/aggregationFns.ts:253](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/aggregationFns.ts#L253)

数値と数値に変換できる行の値を平均します。null や undefined の値と数値でない値は無視します。それ以外の値には、従来どおり単項プラスによる型変換を行います。
