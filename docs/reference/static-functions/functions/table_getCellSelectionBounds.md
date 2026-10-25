---
id: table_getCellSelectionBounds
title: table_getCellSelectionBounds
---

```ts
function table_getCellSelectionBounds<TFeatures, TData>(table): CellSelectionBounds[];
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:382](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L382)

順序付きの範囲の操作を、互いに重ならない、除外を差し引いた表示順インデックスの長方形に解決します。

これは、セルごとの読み取りがすべて通る唯一のキャッシュです。そのため、インデックスを引くのはセルごとではなく、無効化のたびに1回だけで済みます。
角が解決できなくなった範囲（アンカーの行がフィルターで除かれた場合など）は、端に寄せずに除外されます。そのため、状態には残ったまま選択には何も加えず、フィルターを解除すると元どおりに戻ります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`CellSelectionBounds`](../../index/interfaces/CellSelectionBounds.md)[]

## 例 {#example}

```ts
const bounds = table_getCellSelectionBounds(table)
```
