---
id: normalizeAggregationRows
title: normalizeAggregationRows
---

```ts
function normalizeAggregationRows<TFeatures, TData>(rows, maxDepth?): Row<TFeatures, TData>[];
```

定義元: [features/row-aggregation/rowAggregationFeature.utils.ts:108](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.utils.ts#L108)

相対的な深さの最大値までの一意な行を、出てきた順に選びます。
指定した深さより手前で終わる枝からは、その枝でいちばん深い行が入ります。

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

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>[]
