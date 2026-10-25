---
id: table_setCellSelection
title: table_setCellSelection
---

```ts
function table_setCellSelection<TFeatures, TData>(table, updater): void;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:57](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L57)

セル選択のアップデーターを、テーブルの選択の変更ハンドラーに通します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### updater {#updater}

[`Updater`](../../index/type-aliases/Updater.md)\<[`CellSelectionState`](../../index/type-aliases/CellSelectionState.md)\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setCellSelection(table, (old) => old.slice(0, -1))
```
