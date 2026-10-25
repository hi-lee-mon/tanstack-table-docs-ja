---
id: table_getCenterTotalSize
title: table_getCenterTotalSize
---

```ts
function table_getCenterTotalSize<TFeatures, TData>(table): number;
```

定義元: [features/column-sizing/columnSizingFeature.utils.ts:432](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.utils.ts#L432)

固定されていない表示中の末端の列の幅を合計します。

中央の領域が空なら `0` を返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`number`

## 例 {#example}

```ts
const width = table_getCenterTotalSize(table)
```
