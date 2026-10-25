---
id: column_getFilterFn
title: column_getFilterFn
---

```ts
function column_getFilterFn<TFeatures, TData, TValue>(column):
  | FilterFn<TFeatures, TData>
  | undefined;
```

定義元: [features/column-filtering/columnFilteringFeature.utils.ts:109](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.utils.ts#L109)

列に設定されたフィルター関数を解決します。

`columnDef.filterFn` が関数ならそのまま返し、`'auto'` なら `column_getAutoFilterFn` に任せ、文字列ならテーブルのフィルター関数のレジストリから探します。

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

  \| [`FilterFn`](../../index/interfaces/FilterFn.md)\<`TFeatures`, `TData`\>
  \| `undefined`

## 例 {#example}

```ts
const filterFn = column_getFilterFn(column)
```
