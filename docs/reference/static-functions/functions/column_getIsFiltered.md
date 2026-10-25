---
id: column_getIsFiltered
title: column_getIsFiltered
---

```ts
function column_getIsFiltered<TFeatures, TData, TValue>(column): boolean;
```

定義元: [features/column-filtering/columnFilteringFeature.utils.ts:173](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.utils.ts#L173)

この列が現在 `state.columnFilters` にエントリーを持つかどうかを判定します。

これはフィルターの状態があるかどうかを示すだけで、フィルターが実際に行を除いているかどうかは示しません。

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
const isFiltered = column_getIsFiltered(column)
```
