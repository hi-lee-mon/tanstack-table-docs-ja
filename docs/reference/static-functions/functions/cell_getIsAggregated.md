---
id: cell_getIsAggregated
title: cell_getIsAggregated
---

```ts
function cell_getIsAggregated<TFeatures, TData, TValue>(cell): boolean;
```

定義元: [features/row-aggregation/rowAggregationFeature.utils.ts:478](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.utils.ts#L478)

合成されたグループ行について、`cell.getIsAggregated()` を実装します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### cell {#cell}

[`Cell`](../../index/type-aliases/Cell.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

`boolean`
