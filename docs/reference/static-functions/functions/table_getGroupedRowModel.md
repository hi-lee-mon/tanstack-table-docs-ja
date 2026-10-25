---
id: table_getGroupedRowModel
title: table_getGroupedRowModel
---

```ts
function table_getGroupedRowModel<TFeatures, TData>(table): RowModel<TFeatures, TData>;
```

定義元: [core/row-models/coreRowModelsFeature.utils.ts:105](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/row-models/coreRowModelsFeature.utils.ts#L105)

グループ化でグループ行ができたあとの行モデルを求めます。

`manualGrouping` が有効な場合や、グループ化済み行モデルのファクトリーが登録されていない場合は、グループ化前の行モデルをそのまま返します。

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
const groupedRows = table_getGroupedRowModel(table)
```
