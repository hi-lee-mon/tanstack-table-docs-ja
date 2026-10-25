---
id: constructHeader
title: constructHeader
---

```ts
function constructHeader<TFeatures, TData, TValue>(
   table,
   column,
options): Header<TFeatures, TData, TValue>;
```

定義元: [core/headers/constructHeader.ts:31](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/constructHeader.ts#L31)

正規化されたテーブルの内部データからヘッダーのインスタンスを作成します。

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

### column {#column}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>

### options {#options}

#### depth {#depth}

`number`

#### id? {#id}

`string`

#### index {#index}

`number`

#### isPlaceholder? {#isplaceholder}

`boolean`

#### placeholderId? {#placeholderid}

`string`

## 戻り値 {#returns}

[`Header`](../type-aliases/Header.md)\<`TFeatures`, `TData`, `TValue`\>
