---
id: table_getIsSomeColumnsPinned
title: table_getIsSomeColumnsPinned
---

```ts
function table_getIsSomeColumnsPinned<TFeatures, TData>(table, position?): boolean;
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:343](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L343)

固定されている列があるかどうかを判定します。

`position` を省略すると両側を判定し、`'start'` / `'end'` を渡すと1つの固定領域だけを調べます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### position? {#position}

[`ColumnPinningPosition`](../../index/type-aliases/ColumnPinningPosition.md)

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const hasPinnedColumns = table_getIsSomeColumnsPinned(table)
```
