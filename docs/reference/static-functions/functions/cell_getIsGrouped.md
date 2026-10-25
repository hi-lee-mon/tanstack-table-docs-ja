---
id: cell_getIsGrouped
title: cell_getIsGrouped
---

```ts
function cell_getIsGrouped<TFeatures, TData, TValue>(cell): boolean;
```

定義元: [features/column-grouping/columnGroupingFeature.utils.ts:243](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.utils.ts#L243)

このセルがグループ行でグループ化の基準になった列を表しているかどうかを判定します。

ふつうは、このセルがグループの値と展開の操作部品を描画します。

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
const isGroupedCell = cell_getIsGrouped(cell)
```
