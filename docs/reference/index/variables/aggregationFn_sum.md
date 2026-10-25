---
id: aggregationFn_sum
title: aggregationFn_sum
---

```ts
const aggregationFn_sum: AggregationFnDef<any, any, unknown, number>;
```

定義元: [features/row-aggregation/aggregationFns.ts:52](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/aggregationFns.ts#L52)

選ばれた行の数値の値を合計します。数値でない値は 0 として扱います。以前の API と同じく、`NaN` は数値なので、合計にもそのまま伝わります。
