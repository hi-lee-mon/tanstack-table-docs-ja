---
id: row_getEndVisibleCells
title: row_getEndVisibleCells
---

```ts
function row_getEndVisibleCells<TFeatures, TData>(row): Cell<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:261](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L261)

末尾領域に固定された列について、表示中のセルを集めます。

セルは `state.columnPinning.end` の順で返され、`cell.position = 'end'` が付きます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`Cell`](../../index/type-aliases/Cell.md)\<`TFeatures`, `TData`, `unknown`\>[]

## 例 {#example}

```ts
const endCells = row_getEndVisibleCells(row)
```
