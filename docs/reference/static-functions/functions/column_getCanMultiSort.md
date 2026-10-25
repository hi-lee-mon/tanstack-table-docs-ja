---
id: column_getCanMultiSort
title: column_getCanMultiSort
---

```ts
function column_getCanMultiSort<TFeatures, TData, TValue>(column): boolean;
```

定義元: [features/row-sorting/rowSortingFeature.utils.ts:447](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.utils.ts#L447)

この列を複数列ソートの状態に加えられるかどうかを判定します。

列の `enableMultiSort` はテーブルの `enableMultiSort` より優先されます。どちらも指定されていなければ、アクセサー列は既定で複数列ソートできます。

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
const canMultiSort = column_getCanMultiSort(column)
```
