---
id: column_getIsPinned
title: column_getIsPinned
---

```ts
function column_getIsPinned<TFeatures, TData, TValue>(column): ColumnPinningPosition;
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:143](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L143)

この列の現在の固定領域を読み取ります。

グループ列は、その領域に固定された末端の列があれば `'start'` または `'end'` を返します。固定されていない列は `false` を返します。

`start` と `end` は論理的な位置です。LTR の言語やレイアウトでは、ふつう `start` は左、`end` は右にあたります。RTL の言語やレイアウトでは、ふつう `start` は右、`end` は左にあたります。

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

[`ColumnPinningPosition`](../../index/type-aliases/ColumnPinningPosition.md)

## 例 {#example}

```ts
const position = column_getIsPinned(column)
```
