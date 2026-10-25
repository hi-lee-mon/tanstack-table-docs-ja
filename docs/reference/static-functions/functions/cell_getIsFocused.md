---
id: cell_getIsFocused
title: cell_getIsFocused
---

```ts
function cell_getIsFocused<TFeatures, TData, TValue>(cell): boolean;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:581](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L581)

このセルがアクティブなセルかどうかを判定します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### cell {#cell}

[`Cell`](../../index/type-aliases/Cell.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const isFocused = cell_getIsFocused(cell)
```
