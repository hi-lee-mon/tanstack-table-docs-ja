---
id: table_getPaginatedRowModel
title: table_getPaginatedRowModel
---

```ts
function table_getPaginatedRowModel<TFeatures, TData>(table): RowModel<TFeatures, TData>;
```

定義元: [core/row-models/coreRowModelsFeature.utils.ts:240](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/row-models/coreRowModelsFeature.utils.ts#L240)

ページネーションで現在のページの行を切り出したあとの行モデルを求めます。

`manualPagination` が有効な場合や、ページ分割済み行モデルのファクトリーが登録されていない場合は、ページ分割前の行モデルを返します。ページネーションは、データがテーブルに届く前に済んでいるものとみなすためです。

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
const pageRows = table_getPaginatedRowModel(table)
```
