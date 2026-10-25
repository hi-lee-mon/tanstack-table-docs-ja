---
id: column_getIsFirstColumn
title: column_getIsFirstColumn
---

```ts
function column_getIsFirstColumn<TFeatures, TData, TValue>(column, position?): boolean;
```

定義元: [features/column-ordering/columnOrderingFeature.utils.ts:115](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.utils.ts#L115)

この列が固定領域の中で表示中の最初の列かどうかを判定します。

`position` の意味は `column_getIndex` と同じです。

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

`boolean`

## 例 {#example}

```ts
const isFirst = column_getIsFirstColumn(column, 'start')
```
