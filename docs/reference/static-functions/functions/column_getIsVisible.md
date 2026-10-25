---
id: column_getIsVisible
title: column_getIsVisible
---

```ts
function column_getIsVisible<TFeatures, TData, TValue>(column): boolean;
```

定義元: [features/column-visibility/columnVisibilityFeature.utils.ts:82](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.utils.ts#L82)

この列が表示されているかどうかを判定します。

末端の列は `state.columnVisibility[column.id]` を読み、エントリーがなければ表示されているものとして扱います。親の列は、子の列が少なくとも1つ表示されていれば表示されているものとします。

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
const visible = column_getIsVisible(column)
```
