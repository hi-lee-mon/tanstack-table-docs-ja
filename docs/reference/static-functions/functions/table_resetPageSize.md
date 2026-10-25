---
id: table_resetPageSize
title: table_resetPageSize
---

```ts
function table_resetPageSize<TFeatures, TData>(table, defaultState?): void;
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:175](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L175)

`pagination.pageSize` だけをリセットします。

引数なしの場合、`table.initialState.pagination?.pageSize` か `10` を使います。`true` を渡すと、常にページサイズを `10` に戻します。

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
table_resetPageSize(table)
table_resetPageSize(table, true)
```
