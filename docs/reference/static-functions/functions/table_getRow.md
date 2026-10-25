---
id: table_getRow
title: table_getRow
---

```ts
function table_getRow<TFeatures, TData>(
   table,
   rowId,
searchAll?): Row<TFeatures, TData>;
```

定義元: [core/rows/coreRowsFeature.utils.ts:321](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.utils.ts#L321)

現在の行モデルか全体の行モデルから、ID で行を探します。

既定では `table.getRowModel()` を探します。`searchAll` を渡すと、まずページネーション前の行モデルを探し、見つからなければコア行モデルを探します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### rowId {#rowid}

`string`

### searchAll? {#searchall}

`boolean`

## 戻り値 {#returns}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 例 {#example}

```ts
const row = table_getRow(table, rowId, true)
```
