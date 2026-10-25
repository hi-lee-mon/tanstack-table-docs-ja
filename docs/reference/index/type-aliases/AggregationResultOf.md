---
id: AggregationResultOf
title: AggregationResultOf
---

```ts
type AggregationResultOf<TDefinition> = TDefinition extends AggregationFnDef<any, any, any, infer TResult> ? TResult : unknown;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:146](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L146)

集計定義が返す結果の型を取り出します。

## 型パラメーター {#type-parameters}

### TDefinition {#tdefinition}

`TDefinition`
