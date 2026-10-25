---
id: row_getLeafRows
title: row_getLeafRows
---

```ts
function row_getLeafRows<TFeatures, TData>(row): Row<TFeatures, TData>[];
```

定義元: [core/rows/coreRowsFeature.utils.ts:148](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.utils.ts#L148)

この行の子孫のツリーを、末端の行に平坦化します。

行自身は含まず、入れ子の `subRows` だけをたどります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>[]

## 例 {#example}

```ts
const descendants = row_getLeafRows(row)
```
