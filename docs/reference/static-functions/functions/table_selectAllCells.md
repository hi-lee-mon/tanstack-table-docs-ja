---
id: table_selectAllCells
title: table_selectAllCells
---

```ts
function table_selectAllCells<TFeatures, TData>(table): void;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:826](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L826)

テーブル内の選択できるすべてのセルを、1つの範囲として選択します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_selectAllCells(table)
```
