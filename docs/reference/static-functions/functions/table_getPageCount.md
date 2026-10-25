---
id: table_getPageCount
title: table_getPageCount
---

```ts
function table_getPageCount<TFeatures, TData>(table): number;
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:401](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L401)

現在のページネーションの状態でのページ数を求めます。

手動のページネーションでは `options.pageCount` が優先されます。そうでなければ、`table_getRowCount(table)` と現在の `pageSize` から計算します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`number`

## 例 {#example}

```ts
const pages = table_getPageCount(table)
```
