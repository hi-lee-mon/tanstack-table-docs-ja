---
id: table_setColumnVisibility
title: table_setColumnVisibility
---

```ts
function table_setColumnVisibility<TFeatures, TData>(table, updater): void;
```

定義元: [features/column-visibility/columnVisibilityFeature.utils.ts:266](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.utils.ts#L266)

列の表示のアップデーターを、テーブルの表示の変更ハンドラーに通します。

アップデーターには、次の表示のマップか、前のマップを受け取る関数を指定できます。インスタンスの `table.setColumnVisibility` と同じ動作です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### updater {#updater}

[`Updater`](../../index/type-aliases/Updater.md)\<[`ColumnVisibilityState`](../../index/type-aliases/ColumnVisibilityState.md)\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setColumnVisibility(table, (old) => ({ ...old, age: false }))
```
