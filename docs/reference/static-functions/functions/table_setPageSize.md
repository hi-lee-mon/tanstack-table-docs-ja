---
id: table_setPageSize
title: table_setPageSize
---

```ts
function table_setPageSize<TFeatures, TData>(table, updater): void;
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:198](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L198)

現在の先頭の行を保ったまま、`pagination.pageSize` を更新します。

新しいサイズは最小でも `1` に収められます。また、それまでページの先頭にあった行が表示に残るよう、`pageIndex` を計算し直します。

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
table_setPageSize(table, (old) => old)
```
