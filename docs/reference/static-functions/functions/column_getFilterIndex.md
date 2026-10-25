---
id: column_getFilterIndex
title: column_getFilterIndex
---

```ts
function column_getFilterIndex<TFeatures, TData, TValue>(column): number;
```

定義元: [features/column-filtering/columnFilteringFeature.utils.ts:211](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.utils.ts#L211)

順序付きの `state.columnFilters` 配列の中で、この列の位置を探します。

列に有効なフィルターがなければ、結果は `-1` です。

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
const index = column_getFilterIndex(column)
```
