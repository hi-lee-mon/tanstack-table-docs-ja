---
id: table_moveCellSelection
title: table_moveCellSelection
---

```ts
function table_moveCellSelection<TFeatures, TData>(table, direction): void;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:1007](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L1007)

選択を指定した方向に1つ動かし、1つのセルにまとめます。

何も選択されていない場合は、キーボード操作の起点ができるよう、最初の選択可能なセルを選択します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### direction {#direction}

[`CellSelectionDirection`](../../index/type-aliases/CellSelectionDirection.md)

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_moveCellSelection(table, 'down')
```
