---
id: column_getSortFn
title: column_getSortFn
---

```ts
function column_getSortFn<TFeatures, TData, TValue>(column): SortFn<TFeatures, TData>;
```

定義元: [features/row-sorting/rowSortingFeature.utils.ts:215](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.utils.ts#L215)

列に設定されたソート関数を解決します。

`columnDef.sortFn` が関数ならそのまま返し、`'auto'` なら `column_getAutoSortFn` に任せ、文字列ならテーブルのソート関数のレジストリから探します。見つからなければ `basic` を使います。

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

[`SortFn`](../../index/interfaces/SortFn.md)\<`TFeatures`, `TData`\>

## 例 {#example}

```ts
const sortFn = column_getSortFn(column)
```
