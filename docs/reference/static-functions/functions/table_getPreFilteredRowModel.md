---
id: table_getPreFilteredRowModel
title: table_getPreFilteredRowModel
---

```ts
function table_getPreFilteredRowModel<TFeatures, TData>(table): RowModel<TFeatures, TData>;
```

定義元: [core/row-models/coreRowModelsFeature.utils.ts:42](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/row-models/coreRowModelsFeature.utils.ts#L42)

列フィルタリングとグローバルフィルタリングの直前の行モデルを読み取ります。

フィルタリングは行モデルを導き出す最初の段階なので、現在これは `table.getCoreRowModel()` の別名です。

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
const rowsBeforeFiltering = table_getPreFilteredRowModel(table)
```
