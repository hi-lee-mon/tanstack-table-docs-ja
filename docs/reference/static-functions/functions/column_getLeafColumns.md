---
id: column_getLeafColumns
title: column_getLeafColumns
---

```ts
function column_getLeafColumns<TFeatures, TData, TValue>(column): Column<TFeatures, TData, TValue>[];
```

定義元: [core/columns/coreColumnsFeature.utils.ts:46](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.utils.ts#L46)

この列の下にある末端の列を集めます。

グループ列は、順序付きの子孫を返します。グループ列でない列は、その列自身だけを含む配列を返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### column {#column}

[`Column`](../../index/type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

[`Column`](../../index/type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>[]

## 例 {#example}

```ts
const leafColumns = column_getLeafColumns(column)
```
