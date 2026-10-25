---
id: table_autoResetCellSelection
title: table_autoResetCellSelection
---

```ts
function table_autoResetCellSelection<TFeatures, TData>(table): void;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:110](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L110)

`data` が変わったあとに、セル選択のリセットを予約します。

範囲は行 ID と列 ID で保存されます。そのため、これがないと、データを差し替えたときに選択がもう存在しない行を指したままになったり、新しいデータが同じ ID を使うたびに気づかないうちにセルが選択し直されたりします。
リセットは `autoResetAll` か `autoResetCellSelection` が許可する場合に実行され、既定では有効です。

空ではなく `initialState.cellSelection` に戻すので、最初の行モデルの計算では何も起きません。`table_autoResetExpanded` と同じ動作です。

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
table_autoResetCellSelection(table)
```
