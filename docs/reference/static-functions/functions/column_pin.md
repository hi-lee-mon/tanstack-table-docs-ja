---
id: column_pin
title: column_pin
---

```ts
function column_pin<TFeatures, TData, TValue>(column, position): void;
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:60](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L60)

この列の末端の列 ID を、固定領域に移します。

グループ列を固定すると、その末端の列がすべて固定されます。末端の列 ID はまず両方の領域から取り除かれ、そのあと指定した `'start'` または `'end'` の領域の末尾に追加されます。`false` を渡すと固定を解除し、中央に戻します。

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

### position {#position}

[`ColumnPinningPosition`](../../index/type-aliases/ColumnPinningPosition.md)

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
column_pin(column, 'start')
```
