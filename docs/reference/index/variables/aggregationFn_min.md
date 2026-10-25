---
id: aggregationFn_min
title: aggregationFn_min
---

```ts
const aggregationFn_min: AggregationFnDef<any, any, unknown, RangeValue | undefined>;
```

定義元: [features/row-aggregation/aggregationFns.ts:81](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/aggregationFns.ts#L81)

選ばれた行から、数値または Date の最小値を求めます。無効な型の値は無視します。`NaN` は、従来の数値の初期値の動作を保ちます。
