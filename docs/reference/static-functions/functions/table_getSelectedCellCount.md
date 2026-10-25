---
id: table_getSelectedCellCount
title: table_getSelectedCellCount
---

```ts
function table_getSelectedCellCount<TFeatures, TData>(table): number;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:1232](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L1232)

選択されているセルの数を返します。

正規化された、互いに重ならない、除外を差し引いた領域に対して、長方形の計算を行います。
セルごとの `enableCellSelection` 述語関数がある場合は、1つずつ数える必要があります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`number`

## 例 {#example}

```ts
const count = table_getSelectedCellCount(table)
```
