---
id: row_getParentRows
title: row_getParentRows
---

```ts
function row_getParentRows<TFeatures, TData>(row): Row<TFeatures, TData>[];
```

定義元: [core/rows/coreRowsFeature.utils.ts:208](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.utils.ts#L208)

この行の祖先の連なりを、ルートから直接の親まで集めます。

現在の行は含みません。親を持たない行は空の配列を返します。

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
const ancestors = row_getParentRows(row)
```
