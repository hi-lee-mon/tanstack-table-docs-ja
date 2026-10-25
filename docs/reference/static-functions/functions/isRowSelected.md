---
id: isRowSelected
title: isRowSelected
---

```ts
function isRowSelected<TFeatures, TData>(row, rowSelection): boolean;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:996](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L996)

現在の行選択の状態で、行 ID が選択されているかどうかを返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

### rowSelection {#rowselection}

[`RowSelectionState`](../../index/type-aliases/RowSelectionState.md)

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const selected = isRowSelected(row)
```
