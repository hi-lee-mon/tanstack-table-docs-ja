---
id: table_getCoreRowModel
title: table_getCoreRowModel
---

```ts
function table_getCoreRowModel<TFeatures, TData>(table): RowModel<TFeatures, TData>;
```

定義元: [core/row-models/coreRowModelsFeature.utils.ts:18](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/row-models/coreRowModelsFeature.utils.ts#L18)

テーブルの、加工前のコア行モデルを求めます。

ファクトリーはテーブルごとに1回だけ、`features` オプションの `coreRowModel` スロットか、組み込みの `createCoreRowModel()` から作られ、以降の呼び出しで使い回されます。

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
const coreRows = table_getCoreRowModel(table)
```
