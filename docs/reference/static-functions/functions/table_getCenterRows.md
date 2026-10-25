---
id: table_getCenterRows
title: table_getCenterRows
---

```ts
function table_getCenterRows<TFeatures, TData>(table): Row<TFeatures, TData>[];
```

定義元: [features/row-pinning/rowPinningFeature.utils.ts:189](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.utils.ts#L189)

上部にも下部にも固定されていない行を求めます。

現在の行モデルを、`state.rowPinning.top` と `state.rowPinning.bottom` で絞り込みます。

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
const rows = table_getCenterRows(table)
```
