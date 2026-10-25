---
id: column_getAfter
title: column_getAfter
---

```ts
function column_getAfter<TFeatures, TData, TValue>(column, position?): number;
```

定義元: [features/column-sizing/columnSizingFeature.utils.ts:208](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.utils.ts#L208)

この列の後ろから、固定領域の末尾の端までのオフセットを計算します。

値は、指定した領域で後ろに続く、表示中のすべての末端の列の幅の合計です。

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
const endOffset = column_getAfter(column, 'end')
```
