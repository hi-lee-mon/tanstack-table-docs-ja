---
id: table_setColumnSizing
title: table_setColumnSizing
---

```ts
function table_setColumnSizing<TFeatures, TData>(table, updater): void;
```

定義元: [features/column-sizing/columnSizingFeature.utils.ts:330](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.utils.ts#L330)

確定した列幅のアップデーターを、テーブルの列幅のハンドラーに通します。

アップデーターには、次の幅のマップか、前のマップを受け取る関数を指定できます。インスタンスの `table.setColumnSizing` と同じ動作です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### updater {#updater}

[`Updater`](../../index/type-aliases/Updater.md)\<[`ColumnSizingState`](../../index/type-aliases/ColumnSizingState.md)\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setColumnSizing(table, (old) => ({ ...old, age: 96 }))
```
