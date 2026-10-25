---
id: cell_getSelectionEdges
title: cell_getSelectionEdges
---

```ts
function cell_getSelectionEdges<TFeatures, TData, TValue>(cell): CellSelectionEdges;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:625](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L625)

このセルのどの辺が選択範囲の外周に接しているかを返します。

その方向の隣のセルがどの範囲にも含まれていなければ、その辺は外周です。これにより、使う側は、任意の長方形を合わせた形の周りに1本の枠線を描けます。

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

[`CellSelectionEdges`](../../index/interfaces/CellSelectionEdges.md)

## 例 {#example}

```ts
const { top, right, bottom, left } = cell_getSelectionEdges(cell)
```
