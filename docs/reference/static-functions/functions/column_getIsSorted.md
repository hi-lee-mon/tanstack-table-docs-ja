---
id: column_getIsSorted
title: column_getIsSorted
---

```ts
function column_getIsSorted<TFeatures, TData, TValue>(column): false | SortDirection;
```

定義元: [features/row-sorting/rowSortingFeature.utils.ts:470](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.utils.ts#L470)

この列の現在のソートの向きを読み取ります。

列がソートされていなければ `false` を、そうでなければ `state.sorting` にある列のエントリーに応じて `'asc'` か `'desc'` を返します。

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

`false` \| [`SortDirection`](../../index/type-aliases/SortDirection.md)

## 例 {#example}

```ts
const direction = column_getIsSorted(column)
```
