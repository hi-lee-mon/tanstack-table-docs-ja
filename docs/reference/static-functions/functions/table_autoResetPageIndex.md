---
id: table_autoResetPageIndex
title: table_autoResetPageIndex
---

```ts
function table_autoResetPageIndex<TFeatures, TData>(table): void;
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:40](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L40)

ページの内容を変える変更でページ 0 に戻すべきときに、ページ番号をリセットします。

リセットは、`autoResetAll`、`autoResetPageIndex`、またはクライアントサイドでのページネーションの既定の動作が許可する場合に実行されます。手動のページネーションでは、リセットのオプションで明示的に有効にしない限り実行されません。

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
table_autoResetPageIndex(table)
```
