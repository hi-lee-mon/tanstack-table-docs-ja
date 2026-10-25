---
id: cell_getColSpan
title: cell_getColSpan
---

```ts
function cell_getColSpan<TFeatures, TData, TValue>(cell): number;
```

定義元: [features/cell-spanning/cellSpanningFeature.utils.ts:395](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.utils.ts#L395)

このセルが結合する列の数を返します。

結合しない場合は `1`、他のセルの列の結合に覆われている場合は `0` です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### cell {#cell}

[`Cell`](../../index/type-aliases/Cell.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

`number`

## 例 {#example}

```ts
const colSpan = cell_getColSpan(cell)
```
