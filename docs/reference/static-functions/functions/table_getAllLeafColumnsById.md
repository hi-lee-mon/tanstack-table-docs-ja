---
id: table_getAllLeafColumnsById
title: table_getAllLeafColumnsById
---

```ts
function table_getAllLeafColumnsById<TFeatures, TData>(table): Record<string, Column<TFeatures, TData, unknown>>;
```

定義元: [core/columns/coreColumnsFeature.utils.ts:240](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.utils.ts#L240)

末端の列だけについて、ID で引けるマップを作ります。

親の列（グループ列）を含まないので、行のセルや、データ列をキーにした機能の状態で使うのに向いています。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`Record`\<`string`, [`Column`](../../index/type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>\>

## 例 {#example}

```ts
const leavesById = table_getAllLeafColumnsById(table)
```
