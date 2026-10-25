---
id: table_getCanNextPage
title: table_getCanNextPage
---

```ts
function table_getCanNextPage<TFeatures, TData>(table): boolean;
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:269](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L269)

現在のページ番号を先に進められるかどうかを判定します。

`pageCount` が `-1` なのは、呼び出し側が総ページ数を知らないことを意味するので、`true` を返します。ページ数が `0` なら `false` を返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const canGoForward = table_getCanNextPage(table)
```
