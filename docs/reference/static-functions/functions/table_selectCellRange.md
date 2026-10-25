---
id: table_selectCellRange
title: table_selectCellRange
---

```ts
function table_selectCellRange<TFeatures, TData>(
   table,
   range,
   opts?): void;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:776](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L776)

replace、include、exclude のいずれかの意味で、長方形を選択します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### range {#range}

[`CellSelectionRange`](../../index/interfaces/CellSelectionRange.md)

### opts? {#opts}

[`SelectCellRangeOptions`](../../index/interfaces/SelectCellRangeOptions.md)

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_selectCellRange(table, range, { mode: 'exclude' })
```
