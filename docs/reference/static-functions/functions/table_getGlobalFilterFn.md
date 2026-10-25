---
id: table_getGlobalFilterFn
title: table_getGlobalFilterFn
---

```ts
function table_getGlobalFilterFn<TFeatures, TData>(table):
  | FilterFn<TFeatures, TData>
  | undefined;
```

定義元: [features/global-filtering/globalFilteringFeature.utils.ts:61](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/global-filtering/globalFilteringFeature.utils.ts#L61)

グローバルフィルタリングで使うフィルター関数を解決します。

`options.globalFilterFn` が関数ならそのまま返し、`'auto'` なら `table_getGlobalAutoFilterFn` に任せ、文字列ならテーブルのフィルター関数のレジストリから探します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

  \| [`FilterFn`](../../index/interfaces/FilterFn.md)\<`TFeatures`, `TData`\>
  \| `undefined`

## 例 {#example}

```ts
const filterFn = table_getGlobalFilterFn(table)
```
