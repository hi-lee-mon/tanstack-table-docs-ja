---
id: row_getAllCells
title: row_getAllCells
---

```ts
function row_getAllCells<TFeatures, TData>(row): Cell<TFeatures, TData, unknown>[];
```

定義元: [core/rows/coreRowsFeature.utils.ts:235](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.utils.ts#L235)

この行の末端の列ごとに、セルを1つずつ作ります。

結果は `table.getAllLeafColumns()` の順で、非表示の列も含みます。表示に関係する API が、あとでこのリストを絞り込みます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`Cell`](../../index/type-aliases/Cell.md)\<`TFeatures`, `TData`, `unknown`\>[]

## 例 {#example}

```ts
const cells = row_getAllCells(row)
```
