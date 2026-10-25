---
id: AggregationContext
title: AggregationContext
---

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:15](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L15)

1つの集計を評価する間に使える値とテーブルのオブジェクトです。

## 継承先 {#extended-by}

- [`AggregationMergeContext`](AggregationMergeContext.md)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` = `unknown`

## プロパティ {#properties}

### column {#column}

```ts
column: Column<TFeatures, TData, TValue>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:21](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L21)

値を集計している列です。

***

### columnId {#columnid}

```ts
columnId: string;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:23](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L23)

`column.id` の別名です。

***

### getValue {#getvalue}

```ts
getValue: (row) => TValue;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:33](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L33)

`rows` のうち1行から、この列の値を読み取ります。

#### パラメーター {#parameters}

##### row {#row}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns}

`TValue`

***

### groupingRow? {#groupingrow}

```ts
optional groupingRow?: Row<TFeatures, TData>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:39](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L39)

この結果を受け取る、合成されたグループ行です。ルートでの集計や、呼び出し側が行を渡した集計では、このプロパティはありません。
グループ化した集計でグループの階層を区別したいときは、この行の `depth` で判別できます。

***

### maxDepth {#maxdepth}

```ts
maxDepth: number;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:25](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L25)

`rows` を選ぶときに使う、サブ行の相対的な深さの最大値です。

***

### rows {#rows}

```ts
rows: readonly Row<TFeatures, TData>[];
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:44](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L44)

`maxDepth` で選ばれた一意な行です。`maxDepth` より手前で終わる枝からは、その枝でいちばん深い行が入ります。

***

### subRows? {#subrows}

```ts
optional subRows?: readonly Row<TFeatures, TData>[];
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:31](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L31)

グループ化した集計での、直下のサブ行です。ルートでの集計や、呼び出し側が行を渡した集計では、このプロパティはありません。
末端のグループ階層ではデータの行そのもの、入れ子の階層ではサブ行のグループになります。

***

### table {#table}

```ts
table: Table<TFeatures, TData>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:46](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L46)

列と行を持つテーブルです。
