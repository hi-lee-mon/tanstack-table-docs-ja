---
id: constructColumn
title: constructColumn
---

```ts
function constructColumn<TFeatures, TData, TValue>(
   table,
   columnDef,
   depth,
parent?): Column<TFeatures, TData, TValue>;
```

定義元: [core/columns/constructColumn.ts:35](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/constructColumn.ts#L35)

正規化されたテーブルの内部データから列のインスタンスを作成します。

コアのプロパティ、機能のプロトタイプ API、インスタンスデータを結び付けます。これらはテーブルの描画と行モデルの処理で使われます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### columnDef {#columndef}

[`ColumnDef`](../type-aliases/ColumnDef.md)\<`TFeatures`, `TData`, `TValue`\>

### depth {#depth}

`number`

### parent? {#parent}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>
