---
id: table_getPinnedVisibleLeafColumns
title: table_getPinnedVisibleLeafColumns
---

```ts
function table_getPinnedVisibleLeafColumns<TFeatures, TData>(table, position?):
  | Column<TFeatures, TData, unknown>[]
  | Column_Internal<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:864](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L864)

指定した固定領域の、表示中の末端の列を求めます。

`position` を省略すると表示中のすべての末端の列を、`'start'`、`'center'`、`'end'` を渡すと1つの区分を返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### position? {#position}

  \| [`ColumnPinningPosition`](../../index/type-aliases/ColumnPinningPosition.md)
  \| `"center"`

## 戻り値 {#returns}

  \| [`Column`](../../index/type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]
  \| [`Column_Internal`](../../index/interfaces/Column_Internal.md)\<`TFeatures`, `TData`, `unknown`\>[]

## 例 {#example}

```ts
const columns = table_getPinnedVisibleLeafColumns(table, 'start')
```
