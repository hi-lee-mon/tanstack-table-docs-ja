---
id: aggregateColumnValue
title: aggregateColumnValue
---

```ts
function aggregateColumnValue<TFeatures, TData>(args): unknown;
```

定義元: [features/row-aggregation/rowAggregationFeature.utils.ts:336](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.utils.ts#L336)

深さで選んだ行の最前線に対して、設定されたすべての集計を実行します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### args {#args}

#### column {#column}

[`Column`](../../index/type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>

#### groupingRow? {#groupingrow}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

#### maxDepth? {#maxdepth}

`number`

#### rows {#rows}

readonly [`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>[]

#### subRows? {#subrows}

readonly [`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>[]

#### uniqueRows? {#uniquerows}

`boolean`

`rows` が1つの行ツリーの別々のノード（テーブル自身の行モデルが作った行）であることを示します。これにより、ID の重複を防ぐ確認を省いて最前線を選べます。呼び出し側が渡す行の配列では、これを指定しないでください。

## 戻り値 {#returns}

`unknown`
