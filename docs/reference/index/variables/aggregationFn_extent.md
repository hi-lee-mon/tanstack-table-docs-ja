---
id: aggregationFn_extent
title: aggregationFn_extent
---

```ts
const aggregationFn_extent: AggregationFnDef<any, any, unknown, [RangeValue | undefined, RangeValue | undefined]>;
```

定義元: [features/row-aggregation/aggregationFns.ts:180](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/aggregationFns.ts#L180)

選ばれた行から、数値または Date の最小値と最大値を求めます。
入力が空なら `[undefined, undefined]` を返し、以前の組み込みの結果の形を保ちます。
