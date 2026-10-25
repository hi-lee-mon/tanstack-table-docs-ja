---
id: table_getCanPreviousPage
title: table_getCanPreviousPage
---

```ts
function table_getCanPreviousPage<TFeatures, TData>(table): boolean;
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:251](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L251)

現在のページ番号を前に戻せるかどうかを判定します。

最初のページはページ番号 `0` なので、前のページに移動できるのは、ページ番号が正の場合だけです。

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
const canGoBack = table_getCanPreviousPage(table)
```
