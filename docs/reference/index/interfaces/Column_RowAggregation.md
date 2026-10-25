---
id: Column_RowAggregation
title: Column_RowAggregation
---

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:250](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L250)

`rowAggregationFeature` が追加する列のインスタンス API です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getAggregationFns {#getaggregationfns}

```ts
getAggregationFns: () => readonly ResolvedAggregationFn<TFeatures, TData>[];
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:255](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L255)

設定された、単一または複数の集計定義を解決します。

#### 戻り値 {#returns}

readonly [`ResolvedAggregationFn`](ResolvedAggregationFn.md)\<`TFeatures`, `TData`\>[]

***

### getAggregationValue {#getaggregationvalue}

```ts
getAggregationValue: <TResult>(options?) => TResult;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:263](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L263)

既定のグループ化前の行モデル、または呼び出し側が渡した行の配列に対して、この列を集計します。`options.maxDepth` は列の `maxAggregationDepth` を上書きします。行を明示的に渡した呼び出しは、意図的にキャッシュしません。

#### 型パラメーター {#type-parameters-1}

##### TResult {#tresult}

`TResult` = [`ColumnAggregationValue`](../type-aliases/ColumnAggregationValue.md)\<`TFeatures`\>

#### パラメーター {#parameters}

##### options? {#options}

[`AggregationValueOptions`](AggregationValueOptions.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns-1}

`TResult`

***

### getAutoAggregationFn {#getautoaggregationfn}

```ts
getAutoAggregationFn: () =>
  | AggregationFnDef<TFeatures, TData, any, any>
  | undefined;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:267](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L267)

最初の行が数値なら `sum` を、Date なら `extent` を推論します。

#### 戻り値 {#returns-2}

  \| [`AggregationFnDef`](AggregationFnDef.md)\<`TFeatures`, `TData`, `any`, `any`\>
  \| `undefined`
