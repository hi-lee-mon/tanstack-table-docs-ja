---
id: column_getCanFilter
title: column_getCanFilter
---

```ts
function column_getCanFilter<TFeatures, TData, TValue>(column): boolean;
```

定義元: [features/column-filtering/columnFilteringFeature.utils.ts:149](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.utils.ts#L149)

このアクセサー列で列フィルタリングが有効かどうかを判定します。

列がアクセサーを持ち、列定義、`enableColumnFilters`、テーブル全体の `enableFilters` オプションのすべてでフィルタリングが有効になっている必要があります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### column {#column}

[`Column_Internal`](../../index/interfaces/Column_Internal.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const canFilter = column_getCanFilter(column)
```
