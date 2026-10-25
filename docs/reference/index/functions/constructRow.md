---
id: constructRow
title: constructRow
---

```ts
function constructRow<TFeatures, TData>(
   table,
   id,
   original,
   rowIndex,
   depth,
   subRows?,
parentId?): Row<TFeatures, TData>;
```

定義元: [core/rows/constructRow.ts:31](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/constructRow.ts#L31)

正規化されたテーブルの内部データから行のインスタンスを作成します。

コアのプロパティ、機能のプロトタイプ API、インスタンスデータを結び付けます。これらはテーブルの描画と行モデルの処理で使われます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### id {#id}

`string`

### original {#original}

`TData`

### rowIndex {#rowindex}

`number`

### depth {#depth}

`number`

### subRows? {#subrows}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>[]

### parentId? {#parentid}

`string`

## 戻り値 {#returns}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>
