---
id: AggregationFnDescriptor
title: AggregationFnDescriptor
---

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:114](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L114)

複数の結果を返す集計で、集計の参照に安定したキーを付けます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` = `unknown`

### TResult {#tresult}

`TResult` = `unknown`

## プロパティ {#properties}

### aggregationFn {#aggregationfn}

```ts
aggregationFn: AggregationFnRef<TFeatures, TData, TValue, TResult>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:121](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L121)

実行する定義です。名前付き、自動、インラインのいずれかです。

***

### id {#id}

```ts
id: string;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:123](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L123)

複数の結果を返す集計が返すオブジェクトで使う、安定したキーです。
