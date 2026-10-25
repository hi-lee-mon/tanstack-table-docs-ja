---
id: table_getAllFlatColumnsById
title: table_getAllFlatColumnsById
---

```ts
function table_getAllFlatColumnsById<TFeatures, TData>(table): Record<string, Column<TFeatures, TData, unknown>>;
```

定義元: [core/columns/coreColumnsFeature.utils.ts:191](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.utils.ts#L191)

テーブルの平坦化したすべての列について、ID で引けるマップを作ります。

グループ列と末端の列を含みます。同じ ID の列があれば、後ろの列が前のエントリーを置き換えます。

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
const columnsById = table_getAllFlatColumnsById(table)
```
