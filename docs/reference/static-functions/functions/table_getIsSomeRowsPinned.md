---
id: table_getIsSomeRowsPinned
title: table_getIsSomeRowsPinned
---

```ts
function table_getIsSomeRowsPinned<TFeatures, TData>(table, position?): boolean;
```

定義元: [features/row-pinning/rowPinningFeature.utils.ts:93](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.utils.ts#L93)

固定されている行があるかどうかを判定します。

`position` を省略すると両方の領域を判定し、`'top'` / `'bottom'` を渡すと1つの領域だけを調べます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### position? {#position}

[`RowPinningPosition`](../../index/type-aliases/RowPinningPosition.md)

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const hasPinnedRows = table_getIsSomeRowsPinned(table)
```
