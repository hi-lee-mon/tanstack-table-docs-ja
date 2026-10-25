---
id: Table_RowAggregation
title: Table_RowAggregation
---

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:295](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L295)

`rowAggregationFeature` が追加するテーブルの API です。

## プロパティ {#properties}

### \_aggregateColumnValue {#_aggregatecolumnvalue}

```ts
_aggregateColumnValue: <TFeatures, TData>(args) => unknown;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:303](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L303)

**`Internal`**

列に設定された集計を、行の集合に対して実行します。グループ化済み行モデルはこれを通して集計するので、`rowAggregationFeature` なしでグループ化するテーブルには、集計の実行器がバンドルされません。

深さで選んだ行の最前線に対して、設定されたすべての集計を実行します。

#### 型パラメーター {#type-parameters}

##### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

#### パラメーター {#parameters}

##### args {#args}

###### column {#column}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>

###### groupingRow? {#groupingrow}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

###### maxDepth? {#maxdepth}

`number`

###### rows {#rows}

readonly [`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>[]

###### subRows? {#subrows}

readonly [`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>[]

###### uniqueRows? {#uniquerows}

`boolean`

`rows` が1つの行ツリーの別々のノード（テーブル自身の行モデルが作った行）であることを示します。これにより、ID の重複を防ぐ確認を省いて最前線を選べます。呼び出し側が渡す行の配列では、これを指定しないでください。

#### 戻り値 {#returns}

`unknown`
