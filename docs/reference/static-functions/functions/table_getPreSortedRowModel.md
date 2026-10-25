---
id: table_getPreSortedRowModel
title: table_getPreSortedRowModel
---

```ts
function table_getPreSortedRowModel<TFeatures, TData>(table): RowModel<TFeatures, TData>;
```

定義元: [core/row-models/coreRowModelsFeature.utils.ts:131](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/row-models/coreRowModelsFeature.utils.ts#L131)

ソートの直前の行モデルを読み取ります。

ソートはグループ化のあとに実行されるので、これは `table.getGroupedRowModel()` の別名です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`RowModel`](../../index/interfaces/RowModel.md)\<`TFeatures`, `TData`\>

## 例 {#example}

```ts
const rowsBeforeSorting = table_getPreSortedRowModel(table)
```
