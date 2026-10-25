---
id: table_getSortedRowModel
title: table_getSortedRowModel
---

```ts
function table_getSortedRowModel<TFeatures, TData>(table): RowModel<TFeatures, TData>;
```

定義元: [core/row-models/coreRowModelsFeature.utils.ts:150](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/row-models/coreRowModelsFeature.utils.ts#L150)

ソートを適用したあとの行モデルを返します。

`manualSorting` が有効な場合や、ソート済み行モデルのファクトリーが登録されていない場合は、ソート前の行モデルを返します。ソート済みのデータは呼び出し側が渡すものとみなすためです。

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
const sortedRows = table_getSortedRowModel(table)
```
