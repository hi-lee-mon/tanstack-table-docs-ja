---
id: table_setPageIndex
title: table_setPageIndex
---

```ts
function table_setPageIndex<TFeatures, TData>(table, updater): void;
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:117](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L117)

`pagination.pageIndex` を更新し、わかっているページの範囲に収めます。

ページ数が不明（`undefined` か `-1`）なら、0以上のどのページ番号でも指定できます。ページ数がわかっていれば、インデックスを `0` から `pageCount - 1` の間に収めます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### updater {#updater}

[`Updater`](../../index/type-aliases/Updater.md)\<`number`\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setPageIndex(table, (old) => old)
```
