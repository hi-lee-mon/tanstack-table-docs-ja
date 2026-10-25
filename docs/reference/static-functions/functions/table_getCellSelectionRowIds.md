---
id: table_getCellSelectionRowIds
title: table_getCellSelectionRowIds
---

```ts
function table_getCellSelectionRowIds<TFeatures, TData>(table): string[];
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:1292](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L1292)

選択範囲と交わるすべての行の ID を返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`string`[]

## 例 {#example}

```ts
const rowIds = table_getCellSelectionRowIds(table)
```
