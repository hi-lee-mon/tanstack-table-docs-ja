---
id: row_getIsPinned
title: row_getIsPinned
---

```ts
function row_getIsPinned<TFeatures, TData>(row): RowPinningPosition;
```

定義元: [features/row-pinning/rowPinningFeature.utils.ts:236](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.utils.ts#L236)

この行の現在の固定領域を読み取ります。

`state.rowPinning.top` にある行は `'top'`、`bottom` にある行は `'bottom'`、固定されていない行は `false` を返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`RowPinningPosition`](../../index/type-aliases/RowPinningPosition.md)

## 例 {#example}

```ts
const position = row_getIsPinned(row)
```
