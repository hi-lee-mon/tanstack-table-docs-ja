---
id: table_setRowPinning
title: table_setRowPinning
---

```ts
function table_setRowPinning<TFeatures, TData>(table, updater): void;
```

定義元: [features/row-pinning/rowPinningFeature.utils.ts:43](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.utils.ts#L43)

行の固定のアップデーターを、テーブルの行の固定の変更ハンドラーに通します。

アップデーターには、次の `{ top, bottom }` の状態か、前の状態を受け取る関数を指定できます。インスタンスの `table.setRowPinning` と同じ動作です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### updater {#updater}

[`Updater`](../../index/type-aliases/Updater.md)\<[`RowPinningState`](../../index/interfaces/RowPinningState.md)\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setRowPinning(table, (old) => ({ ...old, top: [rowId] }))
```
