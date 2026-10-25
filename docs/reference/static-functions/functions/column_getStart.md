---
id: column_getStart
title: column_getStart
---

```ts
function column_getStart<TFeatures, TData, TValue>(column, position?): number;
```

定義元: [features/column-sizing/columnSizingFeature.utils.ts:181](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.utils.ts#L181)

固定領域の先頭の端から、この列までのオフセットを計算します。

値は、指定した `'start'`、`'center'`、`'end'` の領域で前にある、表示中のすべての末端の列の幅の合計です。

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

### position? {#position}

  \| [`ColumnPinningPosition`](../../index/type-aliases/ColumnPinningPosition.md)
  \| `"center"`

## 戻り値 {#returns}

`number`

## 例 {#example}

```ts
const startOffset = column_getStart(column, 'start')
```
