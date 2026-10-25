---
id: cell_getIsSelected
title: cell_getIsSelected
---

```ts
function cell_getIsSelected<TFeatures, TData, TValue>(cell): boolean;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:557](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L557)

このセルが最終的な選択（除外を差し引いた結果）の中にあるかどうかを判定します。

あえてメモ化していません。`memoDeps` を付けて `assignPrototypeAPIs` で登録すると、セルごとにメモのクロージャーと依存関係の配列が作られ、省ける数回の整数の比較よりもコストがかかるためです。

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
const isSelected = cell_getIsSelected(cell)
```
