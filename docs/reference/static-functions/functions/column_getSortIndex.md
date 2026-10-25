---
id: column_getSortIndex
title: column_getSortIndex
---

```ts
function column_getSortIndex<TFeatures, TData, TValue>(column): number;
```

定義元: [features/row-sorting/rowSortingFeature.utils.ts:491](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.utils.ts#L491)

順序付きの `state.sorting` 配列の中で、この列の位置を探します。

列がソートされていなければ、結果は `-1` です。

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
const index = column_getSortIndex(column)
```
