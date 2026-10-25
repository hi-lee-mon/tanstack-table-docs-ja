---
id: ColumnAggregationValue
title: ColumnAggregationValue
---

```ts
type ColumnAggregationValue<TFeatures> =
  | RegisteredAggregationResult<TFeatures>
  | Record<string, RegisteredAggregationResult<TFeatures> | undefined>
  | undefined;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:202](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L202)

列の正確なオプションがわからないときに使う、公開用の既定の結果のユニオンです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)
