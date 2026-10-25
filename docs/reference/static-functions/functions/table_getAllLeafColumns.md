---
id: table_getAllLeafColumns
title: table_getAllLeafColumns
---

```ts
function table_getAllLeafColumns<TFeatures, TData>(table): Column<TFeatures, TData, unknown>[];
```

定義元: [core/columns/coreColumnsFeature.utils.ts:217](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.utils.ts#L217)

すべての末端の列を、現在のテーブルの順で集めます。

列の並べ替えの機能は、結果を返す前に、集めた末端の列を並べ替えられます。

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
const leafColumns = table_getAllLeafColumns(table)
```
