---
id: table_firstPage
title: table_firstPage
---

```ts
function table_firstPage<TFeatures, TData>(table): void;
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:359](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L359)

テーブルを最初のページに移動します。

`table_setPageIndex(table, 0)` を手軽に呼ぶためのラッパーです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_firstPage(table)
```
