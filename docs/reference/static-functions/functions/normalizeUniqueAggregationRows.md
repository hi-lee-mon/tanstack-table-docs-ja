---
id: normalizeUniqueAggregationRows
title: normalizeUniqueAggregationRows
---

```ts
function normalizeUniqueAggregationRows<TFeatures, TData>(rows, maxDepth?): readonly Row<TFeatures, TData>[];
```

定義元: [features/row-aggregation/rowAggregationFeature.utils.ts:139](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.utils.ts#L139)

1つの行ツリーの別々のノードである行（テーブル自身が作る行モデル）のための、最前線の選び方です。
`normalizeAggregationRows` の ID の重複を防ぐ確認を省き（重ならない部分木で同じ行を2回たどることはないため）、子孫を持つ行がなければ `rows` をそのまま返します。そのため、既定の `maxDepth: 0` の場合は、集計ごとのコストがかかりません。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### rows {#rows}

readonly [`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>[]

### maxDepth? {#maxdepth}

`number` = `0`

## 戻り値 {#returns}

readonly [`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>[]
