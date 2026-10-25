---
id: table_getStartLeafColumns
title: table_getStartLeafColumns
---

```ts
function table_getStartLeafColumns<TFeatures, TData>(table): Column_Internal<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:684](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L684)

先頭の領域に固定された末端の列を求めます。

結果は `state.columnPinning.start` の順で、もう末端の列に対応しない古い ID は読み飛ばします。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`Column_Internal`](../../index/interfaces/Column_Internal.md)\<`TFeatures`, `TData`, `unknown`\>[]

## 例 {#example}

```ts
const columns = table_getStartLeafColumns(table)
```
