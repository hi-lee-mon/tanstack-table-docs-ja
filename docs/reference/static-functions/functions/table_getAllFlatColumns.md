---
id: table_getAllFlatColumns
title: table_getAllFlatColumns
---

```ts
function table_getAllFlatColumns<TFeatures, TData>(table): Column<TFeatures, TData, unknown>[];
```

定義元: [core/columns/coreColumnsFeature.utils.ts:171](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.utils.ts#L171)

グループ列と末端の列を含め、テーブルのすべての列を平坦化します。

データを持つ末端の列に加えて、親の列（グループ列）も含める必要がある場合に使ってください。

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
const flatColumns = table_getAllFlatColumns(table)
```
