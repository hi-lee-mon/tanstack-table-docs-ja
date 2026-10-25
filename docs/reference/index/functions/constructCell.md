---
id: constructCell
title: constructCell
---

```ts
function constructCell<TFeatures, TData, TValue>(
   column,
   row,
table): Cell<TFeatures, TData, TValue>;
```

定義元: [core/cells/constructCell.ts:32](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/constructCell.ts#L32)

正規化されたテーブルの内部データからセルのインスタンスを作成します。

コアのプロパティ、機能のプロトタイプ API、インスタンスデータを結び付けます。これらはテーブルの描画と行モデルの処理で使われます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### column {#column}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>

### row {#row}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

### table {#table}

[`Table_Internal`](../interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`Cell`](../type-aliases/Cell.md)\<`TFeatures`, `TData`, `TValue`\>
