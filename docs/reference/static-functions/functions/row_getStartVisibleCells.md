---
id: row_getStartVisibleCells
title: row_getStartVisibleCells
---

```ts
function row_getStartVisibleCells<TFeatures, TData>(row): Cell<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:229](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L229)

先頭領域に固定された列について、表示中のセルを集めます。

セルは `state.columnPinning.start` の順で返され、`cell.position = 'start'` が付きます。

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
const startCells = row_getStartVisibleCells(row)
```
