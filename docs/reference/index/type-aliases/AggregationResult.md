---
id: AggregationResult
title: AggregationResult
---

```ts
type AggregationResult<TOption, TFeatures> = TOption extends ReadonlyArray<infer TEntry> ? { [TKey in AggregationEntryId<TEntry>]: AggregationResultOfRef<AggregationEntryDefinition<Extract<TEntry, TKey | { id: TKey }>>, TFeatures> } : AggregationResultOfRef<TOption, TFeatures>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:184](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L184)

集計オプションが返す、単一またはキー付きの結果の型を推論します。

## 型パラメーター {#type-parameters}

### TOption {#toption}

`TOption`

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md) = `any`
