---
id: table_getDefaultColumnDef
title: table_getDefaultColumnDef
---

```ts
function table_getDefaultColumnDef<TFeatures, TData>(table): Partial<ColumnDef<TFeatures, TData, unknown>>;
```

定義元: [core/columns/coreColumnsFeature.utils.ts:76](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.utils.ts#L76)

組み込み、機能、利用者の列定義の既定値をマージします。

組み込みの既定値はヘッダーと代わりのセルのレンダラーを提供し、機能の既定値は機能ごとの列オプションを追加できます。最後に `options.defaultColumn` が優先されます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`Partial`\<[`ColumnDef`](../../index/type-aliases/ColumnDef.md)\<`TFeatures`, `TData`, `unknown`\>\>

## 例 {#example}

```ts
const defaultColumn = table_getDefaultColumnDef(table)
```
