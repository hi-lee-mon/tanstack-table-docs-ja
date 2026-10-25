---
id: column_getSize
title: column_getSize
---

```ts
function column_getSize<TFeatures, TData, TValue>(column): number;
```

定義元: [features/column-sizing/columnSizingFeature.utils.ts:66](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.utils.ts#L66)

列の現在の幅（ピクセル）を求めます。

確定した `state.columnSizing[column.id]`、`columnDef.size`、組み込みの既定の幅の順に優先されます。結果は最小幅と最大幅の間に収められます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### column {#column}

[`Column_Internal`](../../index/interfaces/Column_Internal.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

`number`

## 例 {#example}

```ts
const width = column_getSize(column)
```
