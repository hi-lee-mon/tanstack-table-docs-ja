---
id: column_getGroupedIndex
title: column_getGroupedIndex
---

```ts
function column_getGroupedIndex<TFeatures, TData, TValue>(column): number;
```

定義元: [features/column-grouping/columnGroupingFeature.utils.ts:106](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.utils.ts#L106)

順序付きのグループ化の状態の中で、この列の位置を探します。

列がグループ化されていなければ、結果は `-1` です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### column {#column}

[`Column_Internal`](../../index/interfaces/Column_Internal.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

`number`

## 例 {#example}

```ts
const index = column_getGroupedIndex(column)
```
