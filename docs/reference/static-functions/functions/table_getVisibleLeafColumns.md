---
id: table_getVisibleLeafColumns
title: table_getVisibleLeafColumns
---

```ts
function table_getVisibleLeafColumns<TFeatures, TData>(table): Column<TFeatures, TData, unknown>[];
```

定義元: [features/column-visibility/columnVisibilityFeature.utils.ts:244](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.utils.ts#L244)

末端の列を、現在表示されているものに絞り込みます。

これは、行を描画するコードの多くが、固定に応じて区分けする前に使う列のリストです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`Column`](../../index/type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

## 例 {#example}

```ts
const columns = table_getVisibleLeafColumns(table)
```
