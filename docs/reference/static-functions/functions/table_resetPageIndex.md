---
id: table_resetPageIndex
title: table_resetPageIndex
---

```ts
function table_resetPageIndex<TFeatures, TData>(table, defaultState?): void;
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:151](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L151)

`pagination.pageIndex` だけをリセットします。

引数なしの場合、`table.initialState.pagination?.pageIndex` か `0` を使います。`true` を渡すと、常にページ番号を `0` に戻します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### defaultState? {#defaultstate}

`boolean`

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_resetPageIndex(table)
table_resetPageIndex(table, true)
```
