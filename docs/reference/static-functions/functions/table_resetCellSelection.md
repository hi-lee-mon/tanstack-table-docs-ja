---
id: table_resetCellSelection
title: table_resetCellSelection
---

```ts
function table_resetCellSelection<TFeatures, TData>(table, defaultState?): void;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:80](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L80)

`cellSelection` を、設定した初期状態か機能の既定値に戻します。

引数なしの場合、`table.initialState.cellSelection` があればそれを複製して戻します。`true` を渡すと、初期状態を無視して空の選択に戻します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### defaultState? {#defaultstate}

`boolean`

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_resetCellSelection(table, true)
```
