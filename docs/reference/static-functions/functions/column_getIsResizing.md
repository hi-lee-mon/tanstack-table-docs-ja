---
id: column_getIsResizing
title: column_getIsResizing
---

```ts
function column_getIsResizing<TFeatures, TData, TValue>(column): boolean;
```

定義元: [features/column-resizing/columnResizingFeature.utils.ts:69](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.utils.ts#L69)

この列が現在リサイズ中の対象の列かどうかを判定します。

値は `state.columnResizing.isResizingColumn` から読み取ります。

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
const isResizing = column_getIsResizing(column)
```
