---
id: column_getCanHide
title: column_getCanHide
---

```ts
function column_getCanHide<TFeatures, TData, TValue>(column): boolean;
```

定義元: [features/column-visibility/columnVisibilityFeature.utils.ts:114](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.utils.ts#L114)

この列を非表示にできるかどうかを判定します。

`columnDef.enableHiding` とテーブルの `enableHiding` は、どちらも既定値が `true` です。

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
const canHide = column_getCanHide(column)
```
