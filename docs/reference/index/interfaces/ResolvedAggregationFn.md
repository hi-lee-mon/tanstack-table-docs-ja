---
id: ResolvedAggregationFn
title: ResolvedAggregationFn
---

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:208](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L208)

`column.getAggregationFns()` が返す、検証済みの集計のエントリーです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### aggregationFn {#aggregationfn}

```ts
aggregationFn:
  | AggregationFnDef<TFeatures, TData, any, any>
  | undefined;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:213](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L213)

解決済みの定義です。設定が不正な場合は `undefined` です。

***

### id {#id}

```ts
id: string | undefined;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:215](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L215)

複数の結果で使うキーです。単一の結果のインライン定義には id がありません。
