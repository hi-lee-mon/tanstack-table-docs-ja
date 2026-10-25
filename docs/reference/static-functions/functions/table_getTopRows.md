---
id: table_getTopRows
title: table_getTopRows
---

```ts
function table_getTopRows<TFeatures, TData>(table): Row<TFeatures, TData>[];
```

定義元: [features/row-pinning/rowPinningFeature.utils.ts:153](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.utils.ts#L153)

上部の領域に固定された、表示する行を求めます。

結果は `state.rowPinning.top` の順で、各行に `position = 'top'` が付きます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>[]

## 例 {#example}

```ts
const rows = table_getTopRows(table)
```
