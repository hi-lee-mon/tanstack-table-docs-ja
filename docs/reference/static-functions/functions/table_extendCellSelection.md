---
id: table_extendCellSelection
title: table_extendCellSelection
---

```ts
function table_extendCellSelection<TFeatures, TData>(table, direction): void;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:1044](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L1044)

アンカーを固定したまま、アクティブな範囲を指定した方向に1つ広げます。

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
table_extendCellSelection(table, 'right')
```
