---
id: table_setColumnPinning
title: table_setColumnPinning
---

```ts
function table_setColumnPinning<TFeatures, TData>(table, updater): void;
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:295](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L295)

列の固定のアップデーターを、テーブルの固定の変更ハンドラーに通します。

アップデーターには、次の `{ start, end }` の状態か、前の状態を受け取る関数を指定できます。インスタンスの `table.setColumnPinning` と同じ動作です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### updater {#updater}

[`Updater`](../../index/type-aliases/Updater.md)\<[`ColumnPinningState`](../../index/interfaces/ColumnPinningState.md)\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setColumnPinning(table, (old) => ({ ...old, start: ['select'] }))
```
