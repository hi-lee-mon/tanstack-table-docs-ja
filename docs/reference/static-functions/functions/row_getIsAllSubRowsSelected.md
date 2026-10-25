---
id: row_getIsAllSubRowsSelected
title: row_getIsAllSubRowsSelected
---

```ts
function row_getIsAllSubRowsSelected<TFeatures, TData>(row): boolean;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:606](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L606)

選択可能な子孫がすべて選択されているかどうかを判定します。

選択可能な子孫を持たない行は false を返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const allChildrenSelected = row_getIsAllSubRowsSelected(row)
```
