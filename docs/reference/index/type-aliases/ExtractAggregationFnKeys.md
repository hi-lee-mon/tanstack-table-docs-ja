---
id: ExtractAggregationFnKeys
title: ExtractAggregationFnKeys
---

```ts
type ExtractAggregationFnKeys<TFeatures> = IsAny<TFeatures> extends true ?
  | keyof AggregationFns
  | BuiltInAggregationFn : TFeatures extends object ? Extract<keyof TAggregationFns, string> : keyof AggregationFns;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:95](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L95)

機能の組み合わせの集計レジストリで使える、文字列の名前です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)
