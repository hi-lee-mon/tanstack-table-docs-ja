---
id: table_getIsSomeRowsSelected
title: table_getIsSomeRowsSelected
---

```ts
function table_getIsSomeRowsSelected<TFeatures, TData>(table): boolean;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:437](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L437)

選択されている行 ID が少なくとも1つあるかどうかを判定します。

すべての行が選択されている場合も、結果は true のままです。

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
const someRowsSelected = table_getIsSomeRowsSelected(table)
```
