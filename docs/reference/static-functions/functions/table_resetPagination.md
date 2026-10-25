---
id: table_resetPagination
title: table_resetPagination
---

```ts
function table_resetPagination<TFeatures, TData>(table, defaultState?): void;
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:92](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L92)

`pagination` を、設定した初期状態か機能の既定値に戻します。

引数なしの場合、`table.initialState.pagination` があればそれを複製して戻します。`true` を渡すと、初期状態を無視して `{ pageIndex: 0, pageSize: 10 }` に戻します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### defaultState? {#defaultstate}

`boolean`

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_resetPagination(table)
table_resetPagination(table, true)
```
