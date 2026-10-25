---
id: column_getFilterValue
title: column_getFilterValue
---

```ts
function column_getFilterValue<TFeatures, TData, TValue>(column): unknown;
```

定義元: [features/column-filtering/columnFilteringFeature.utils.ts:191](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.utils.ts#L191)

`state.columnFilters` から、この列の現在のフィルター値を読み取ります。

フィルターのエントリーがなければ `undefined` を返します。

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

`unknown`

## 例 {#example}

```ts
const value = column_getFilterValue(column)
```
