---
id: table_getFilteredRowModel
title: table_getFilteredRowModel
---

```ts
function table_getFilteredRowModel<TFeatures, TData>(table): RowModel<TFeatures, TData>;
```

定義元: [core/row-models/coreRowModelsFeature.utils.ts:61](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/row-models/coreRowModelsFeature.utils.ts#L61)

列フィルタリングとグローバルフィルタリングのあとの行モデルを求めます。

`manualFiltering` が有効な場合や、フィルター済み行モデルのファクトリーが登録されていない場合は、フィルタリング前の行モデルを返します。フィルタリングはテーブルの外で行われるものとみなすためです。

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
const filteredRows = table_getFilteredRowModel(table)
```
