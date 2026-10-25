---
id: column_getCanSort
title: column_getCanSort
---

```ts
function column_getCanSort<TFeatures, TData, TValue>(column): boolean;
```

定義元: [features/row-sorting/rowSortingFeature.utils.ts:424](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.utils.ts#L424)

このアクセサー列をソートの対象にできるかどうかを判定します。

列がアクセサーを持ち、列定義とテーブルのオプションの両方でソートが有効になっている必要があります。

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

`boolean`

## 例 {#example}

```ts
const canSort = column_getCanSort(column)
```
