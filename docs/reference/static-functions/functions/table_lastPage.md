---
id: table_lastPage
title: table_lastPage
---

```ts
function table_lastPage<TFeatures, TData>(table): void;
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:377](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L377)

テーブルを、わかっている最後のページに移動します。

ページ数が不明、0、有限でない場合は移動できる最後のページがないので、その場合は何もしません。

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
table_lastPage(table)
```
