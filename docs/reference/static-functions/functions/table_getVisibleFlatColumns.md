---
id: table_getVisibleFlatColumns
title: table_getVisibleFlatColumns
---

```ts
function table_getVisibleFlatColumns<TFeatures, TData>(table): Column<TFeatures, TData, unknown>[];
```

定義元: [features/column-visibility/columnVisibilityFeature.utils.ts:222](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.utils.ts#L222)

平坦な列のリストを、表示中の列に絞り込みます。

親の列（グループ列）は、`column_getIsVisible` が表示中とみなす場合に含まれます。

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
const columns = table_getVisibleFlatColumns(table)
```
