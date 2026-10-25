---
id: table_getEndVisibleLeafColumns
title: table_getEndVisibleLeafColumns
---

```ts
function table_getEndVisibleLeafColumns<TFeatures, TData>(table): Column_Internal<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:820](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L820)

末尾の領域に固定された、表示中の末端の列を求めます。

末尾の固定順を適用したあとで、非表示の固定された列を取り除きます。

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
const columns = table_getEndVisibleLeafColumns(table)
```
