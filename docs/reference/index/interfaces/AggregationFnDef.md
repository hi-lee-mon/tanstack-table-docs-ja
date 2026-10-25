---
id: AggregationFnDef
title: AggregationFnDef
---

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:63](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L63)

コンテキストベースの集計定義と、省略可能なグループ結果のマージ処理です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md) = `any`

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

### TValue {#tvalue}

`TValue` = `unknown`

### TResult {#tresult}

`TResult` = `unknown`

## プロパティ {#properties}

### aggregate {#aggregate}

```ts
aggregate: (context) => TResult;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:70](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L70)

選ばれた `rows` から直接、結果を計算します。

#### パラメーター {#parameters}

##### context {#context}

[`AggregationContext`](AggregationContext.md)\<`TFeatures`, `TData`, `TValue`\>

#### 戻り値 {#returns}

`TResult`

***

### merge? {#merge}

```ts
optional merge?: (context) => TResult;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:75](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L75)

計算済みの直下のサブ行の結果を組み合わせます。省略した場合、入れ子のグループ化では、グループで選ばれた行に対して `aggregate` を実行します。

#### パラメーター {#parameters-1}

##### context {#context-1}

[`AggregationMergeContext`](AggregationMergeContext.md)\<`TFeatures`, `TData`, `TValue`, `TResult`\>

#### 戻り値 {#returns-1}

`TResult`
