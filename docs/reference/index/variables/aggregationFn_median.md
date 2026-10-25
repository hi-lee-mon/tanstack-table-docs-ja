---
id: aggregationFn_median
title: aggregationFn_median
---

```ts
const aggregationFn_median: AggregationFnDef<any, any, unknown, number | undefined>;
```

定義元: [features/row-aggregation/aggregationFns.ts:281](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/aggregationFns.ts#L281)

数値の行の値の中央値を求めます。`sum` / `min` / `max` / `mean` の集計と同じく、数値でない値は無視します。数値の値が1つも残らなければ `undefined` を返します。
