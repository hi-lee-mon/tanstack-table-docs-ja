---
id: ColumnDef_RowAggregation
title: ColumnDef_RowAggregation
---

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:219](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L219)

`rowAggregationFeature` が追加する列定義のオプションです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](../type-aliases/CellData.md) = [`CellData`](../type-aliases/CellData.md)

## プロパティ {#properties}

### aggregatedCell? {#aggregatedcell}

```ts
optional aggregatedCell?: ColumnDefTemplate<ReturnType<Cell<TFeatures, TData, TValue>["getContext"]>>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:225](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L225)

グループ行の集計済みセルを描画するレンダラーです。

***

### aggregationFn? {#aggregationfn}

```ts
optional aggregationFn?: AggregationFnOption<TFeatures, TData, TValue>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:232](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L232)

単一の結果にするなら集計の参照を1つ、キー付きの結果オブジェクトにするなら配列を指定します。配列に入れるインラインの定義には、明示的な `id` が必要です。

***

### getAggregationValue? {#getaggregationvalue}

```ts
optional getAggregationValue?: (context) =>
  | AggregationValueResult<unknown>
  | undefined;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:244](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L244)

この列について、あらかじめ計算した集計値を渡せます（省略可能）。
`{ value }` を返すと要求を処理済みにします（`{ value: undefined }` も含みます）。`undefined` を返すと、ローカルの集計にフォールバックします。

#### パラメーター {#parameters}

##### context {#context}

[`AggregationValueContext`](AggregationValueContext.md)\<`TFeatures`, `TData`, `TValue`\>

#### 戻り値 {#returns}

  \| [`AggregationValueResult`](AggregationValueResult.md)\<`unknown`\>
  \| `undefined`

***

### maxAggregationDepth? {#maxaggregationdepth}

```ts
optional maxAggregationDepth?: number;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:238](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L238)

グループ化した集計とキャッシュされる既定の合計で使う、サブ行の相対的な深さの最大値です。
`0` は渡されたルートの行、`1` はその直下のサブ行を選び、以降も同様です。既定値は `0` です。
