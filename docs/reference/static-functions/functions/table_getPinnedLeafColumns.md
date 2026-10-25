---
id: table_getPinnedLeafColumns
title: table_getPinnedLeafColumns
---

```ts
function table_getPinnedLeafColumns<TFeatures, TData>(table, position):
  | Column<TFeatures, TData, unknown>[]
  | Column_Internal<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:759](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L759)

指定した固定領域の末端の列を求めます。

`'start'`、`'center'`、`'end'` を渡すとその区分を、`false` を渡すと区分けせずにすべての末端の列を読み取ります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### position {#position}

  \| [`ColumnPinningPosition`](../../index/type-aliases/ColumnPinningPosition.md)
  \| `"center"`

## 戻り値 {#returns}

  \| [`Column`](../../index/type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]
  \| [`Column_Internal`](../../index/interfaces/Column_Internal.md)\<`TFeatures`, `TData`, `unknown`\>[]

## 例 {#example}

```ts
const columns = table_getPinnedLeafColumns(table, 'center')
```
