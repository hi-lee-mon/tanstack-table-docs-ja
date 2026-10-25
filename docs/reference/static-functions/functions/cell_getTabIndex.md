---
id: cell_getTabIndex
title: cell_getTabIndex
---

```ts
function cell_getTabIndex<TFeatures, TData, TValue>(cell): number;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:605](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L605)

ローヴィング tabindex のために、フォーカスされたセルでは `0`、それ以外では `-1` を返します。

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

`number`

## 例 {#example}

```ts
const tabIndex = cell_getTabIndex(cell)
```
