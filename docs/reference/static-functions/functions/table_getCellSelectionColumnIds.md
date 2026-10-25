---
id: table_getCellSelectionColumnIds
title: table_getCellSelectionColumnIds
---

```ts
function table_getCellSelectionColumnIds<TFeatures, TData>(table): string[];
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:1329](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L1329)

選択範囲と交わるすべての列の ID を返します。

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
const columnIds = table_getCellSelectionColumnIds(table)
```
