---
id: table_setColumnOrder
title: table_setColumnOrder
---

```ts
function table_setColumnOrder<TFeatures, TData>(table, updater): void;
```

定義元: [features/column-ordering/columnOrderingFeature.utils.ts:160](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.utils.ts#L160)

列の並び順のアップデーターを、テーブルの列の並び順の変更ハンドラーに通します。

アップデーターには、次の順序付きの ID 配列か、前の配列を受け取る関数を指定できます。インスタンスの `table.setColumnOrder` と同じ動作です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### updater {#updater}

[`Updater`](../../index/type-aliases/Updater.md)\<[`ColumnOrderState`](../../index/type-aliases/ColumnOrderState.md)\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setColumnOrder(table, ['firstName', 'lastName', 'age'])
```
