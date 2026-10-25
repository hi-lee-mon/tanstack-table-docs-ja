---
id: column_getIndex
title: column_getIndex
---

```ts
function column_getIndex<TFeatures, TData, TValue>(column, position?): number;
```

定義元: [features/column-ordering/columnOrderingFeature.utils.ts:81](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.utils.ts#L81)

表示中の固定領域の中で、この列のインデックスを探します。

`'start'`、`'center'`、`'end'` を渡すとその領域の中を探します。位置を省略すると、表示中の末端の列全体を探します。

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
const index = column_getIndex(column, 'center')
```
