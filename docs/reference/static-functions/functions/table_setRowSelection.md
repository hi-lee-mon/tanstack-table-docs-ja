---
id: table_setRowSelection
title: table_setRowSelection
---

```ts
function table_setRowSelection<TFeatures, TData>(table, updater): void;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:46](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L46)

行選択のアップデーターを、テーブルの選択の変更ハンドラーに通します。

アップデーターには、次の選択のマップか、前のマップを受け取る関数を指定できます。インスタンスの `table.setRowSelection` と同じ動作です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### updater {#updater}

[`Updater`](../../index/type-aliases/Updater.md)\<[`RowSelectionState`](../../index/type-aliases/RowSelectionState.md)\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setRowSelection(table, (old) => ({ ...old, [rowId]: true }))
```
