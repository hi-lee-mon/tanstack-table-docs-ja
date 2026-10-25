---
id: column_getCanResize
title: column_getCanResize
---

```ts
function column_getCanResize<TFeatures, TData, TValue>(column): boolean;
```

定義元: [features/column-resizing/columnResizingFeature.utils.ts:48](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.utils.ts#L48)

この列でリサイズ操作を始められるかどうかを判定します。

`columnDef.enableResizing` とテーブルの `enableColumnResizing` は、どちらも既定値が `true` です。

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
const canResize = column_getCanResize(column)
```
