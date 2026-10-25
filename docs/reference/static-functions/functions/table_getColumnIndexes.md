---
id: table_getColumnIndexes
title: table_getColumnIndexes
---

```ts
function table_getColumnIndexes<TFeatures, TData>(table): ColumnIndexes;
```

定義元: [features/column-ordering/columnOrderingFeature.utils.ts:45](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.utils.ts#L45)

表示中の固定領域ごとに、列 ID からインデックスへのレコードを作ります。

4つの領域を1回の走査でまとめて作るので、列ごとに走査しなくても、1つのメモのエントリーですべての `column_getIndex` の検索をまかなえます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`ColumnIndexes`](../../index/interfaces/ColumnIndexes.md)

## 例 {#example}

```ts
const indexes = table_getColumnIndexes(table)
```
