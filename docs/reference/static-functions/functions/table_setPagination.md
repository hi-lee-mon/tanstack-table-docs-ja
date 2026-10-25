---
id: table_setPagination
title: table_setPagination
---

```ts
function table_setPagination<TFeatures, TData>(table, updater): void;
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:72](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L72)

ページネーションのアップデーターを、テーブルのページネーションの変更ハンドラーに通します。

アップデーターには、次の状態オブジェクトか、前の `PaginationState` を受け取る関数を指定できます。制御された状態と外部のアトムも、インスタンスの API と同じアップデーターの経路を通ります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### updater {#updater}

[`Updater`](../../index/type-aliases/Updater.md)\<[`PaginationState`](../../index/interfaces/PaginationState.md)\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setPagination(table, (old) => old)
```
