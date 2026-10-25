---
id: AggregationValueContext
title: AggregationValueContext
---

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:307](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L307)

列レベルの集計値プロバイダーに渡される値です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](../type-aliases/CellData.md) = [`CellData`](../type-aliases/CellData.md)

## プロパティ {#properties}

### column {#column}

```ts
column: Column<TFeatures, TData, TValue>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:313](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L313)

値が要求された列です。

***

### maxDepth {#maxdepth}

```ts
maxDepth: number;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:315](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L315)

この要求で使う、サブ行の相対的な深さの最大値です。

***

### rows? {#rows}

```ts
optional rows?: readonly Row<TFeatures, TData>[];
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:317](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L317)

呼び出し側が渡した行です。既定の行モデルを使う場合は `undefined` です。

***

### table {#table}

```ts
table: Table<TFeatures, TData>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:319](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L319)

列を持つテーブルです。
