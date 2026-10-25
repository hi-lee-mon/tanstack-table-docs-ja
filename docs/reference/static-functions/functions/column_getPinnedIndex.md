---
id: column_getPinnedIndex
title: column_getPinnedIndex
---

```ts
function column_getPinnedIndex<TFeatures, TData, TValue>(column): number;
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:179](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L179)

固定領域の中で、この列のインデックスを探します。

固定されていない列は `0` を返します。固定された列は、`state.columnPinning.start` または `state.columnPinning.end` の中での位置を返します。

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

## 戻り値 {#returns}

`number`

## 例 {#example}

```ts
const index = column_getPinnedIndex(column)
```
