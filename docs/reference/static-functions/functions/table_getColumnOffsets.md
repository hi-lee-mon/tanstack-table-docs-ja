---
id: table_getColumnOffsets
title: table_getColumnOffsets
---

```ts
function table_getColumnOffsets<TFeatures, TData>(table): ColumnOffsetsByPosition;
```

定義元: [features/column-sizing/columnSizingFeature.utils.ts:126](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.utils.ts#L126)

表示中のすべての末端の列について、先頭からと後ろからのオフセットのマップを作ります。固定領域ごとと、表示中の全列について1回ずつ計算します。

この結果をテーブル単位で1つメモ化しておくことで、すべての `column.getStart()` と `column.getAfter()` の呼び出しが O(1) で引けます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`ColumnOffsetsByPosition`](../../index/interfaces/ColumnOffsetsByPosition.md)

## 例 {#example}

```ts
const offsets = table_getColumnOffsets(table)
const startOffset = offsets.start.starts[column.id]
```
