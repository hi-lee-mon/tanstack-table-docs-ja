---
id: table_getPageOptions
title: table_getPageOptions
---

```ts
function table_getPageOptions<TFeatures, TData>(table): number[];
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:228](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L228)

現在のページ数で使える、0始まりのページ番号を作ります。

ページ数が不明か0なら空の配列を返します。そうでなければ、結果は `[0, 1, ...pageCount - 1]` です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`number`[]

## 例 {#example}

```ts
const pageIndexes = table_getPageOptions(table)
```
