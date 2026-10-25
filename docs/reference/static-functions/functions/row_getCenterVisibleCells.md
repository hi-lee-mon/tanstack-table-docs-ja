---
id: row_getCenterVisibleCells
title: row_getCenterVisibleCells
---

```ts
function row_getCenterVisibleCells<TFeatures, TData>(row): Cell<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:204](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L204)

列が先頭にも末尾にも固定されていない、表示中のセルを集めます。

結果は、中央の列について、行の表示中のセルの順を保ちます。

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
const centerCells = row_getCenterVisibleCells(row)
```
