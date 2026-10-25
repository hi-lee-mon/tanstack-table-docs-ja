---
id: table_getIsSomePageRowsSelected
title: table_getIsSomePageRowsSelected
---

```ts
function table_getIsSomePageRowsSelected<TFeatures, TData>(table): boolean;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:455](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L455)

現在のページにある選択可能な行が、少なくとも1つ選択されているかどうかを判定します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const somePageRowsSelected = table_getIsSomePageRowsSelected(table)
```
