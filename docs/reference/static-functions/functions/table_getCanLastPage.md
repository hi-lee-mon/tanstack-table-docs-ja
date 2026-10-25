---
id: table_getCanLastPage
title: table_getCanLastPage
---

```ts
function table_getCanLastPage<TFeatures, TData>(table): boolean;
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:299](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L299)

現在のページより後ろに、わかっている有限の最後のページがあるかどうかを判定します。

ページ数が不明（`-1`）、0、有限でない場合は、移動できる最後のページはありません。

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
const canGoToLastPage = table_getCanLastPage(table)
```
