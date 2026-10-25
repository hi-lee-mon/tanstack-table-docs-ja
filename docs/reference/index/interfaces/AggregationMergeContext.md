---
id: AggregationMergeContext
title: AggregationMergeContext
---

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:50](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L50)

入れ子のグループ結果をマージするときに追加で使える値です。

## 継承元 {#extends}

- [`AggregationContext`](AggregationContext.md)\<`TFeatures`, `TData`, `TValue`\>

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue`

### TResult {#tresult}

`TResult`

## プロパティ {#properties}

### column {#column}

```ts
column: Column<TFeatures, TData, TValue>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:21](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L21)

値を集計している列です。

#### 継承元のメンバー {#inherited-from}

[`AggregationContext`](AggregationContext.md).[`column`](AggregationContext.md#column)

***

### columnId {#columnid}

```ts
columnId: string;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:23](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L23)

`column.id` の別名です。

#### 継承元のメンバー {#inherited-from-1}

[`AggregationContext`](AggregationContext.md).[`columnId`](AggregationContext.md#columnid)

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

#### 継承元のメンバー {#inherited-from-2}

[`AggregationContext`](AggregationContext.md).[`getValue`](AggregationContext.md#getvalue)

***

### groupingRow? {#groupingrow}

```ts
optional groupingRow?: Row<TFeatures, TData>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:39](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L39)

この結果を受け取る、合成されたグループ行です。ルートでの集計や、呼び出し側が行を渡した集計では、このプロパティはありません。
グループ化した集計でグループの階層を区別したいときは、この行の `depth` で判別できます。

#### 継承元のメンバー {#inherited-from-3}

[`AggregationContext`](AggregationContext.md).[`groupingRow`](AggregationContext.md#groupingrow)

***

### maxDepth {#maxdepth}

```ts
maxDepth: number;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:25](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L25)

`rows` を選ぶときに使う、サブ行の相対的な深さの最大値です。

#### 継承元のメンバー {#inherited-from-4}

[`AggregationContext`](AggregationContext.md).[`maxDepth`](AggregationContext.md#maxdepth)

***

### rows {#rows}

```ts
rows: readonly Row<TFeatures, TData>[];
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:44](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L44)

`maxDepth` で選ばれた一意な行です。`maxDepth` より手前で終わる枝からは、その枝でいちばん深い行が入ります。

#### 継承元のメンバー {#inherited-from-5}

[`AggregationContext`](AggregationContext.md).[`rows`](AggregationContext.md#rows)

***

### subRowResults {#subrowresults}

```ts
subRowResults: readonly TResult[];
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:57](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L57)

直下のサブ行のグループごとに出た結果です。サブ行の順に並びます。

***

### subRows {#subrows}

```ts
subRows: readonly Row<TFeatures, TData>[];
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:59](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L59)

`subRowResults` に対応する、直下のサブ行のグループです。

#### 上書き元 {#overrides}

[`AggregationContext`](AggregationContext.md).[`subRows`](AggregationContext.md#subrows)

***

### table {#table}

```ts
table: Table<TFeatures, TData>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:46](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L46)

列と行を持つテーブルです。

#### 継承元のメンバー {#inherited-from-6}

[`AggregationContext`](AggregationContext.md).[`table`](AggregationContext.md#table)
