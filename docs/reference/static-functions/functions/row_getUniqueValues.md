---
id: row_getUniqueValues
title: row_getUniqueValues
---

```ts
function row_getUniqueValues<TFeatures, TData>(row, columnId): unknown;
```

定義元: [core/rows/coreRowsFeature.utils.ts:93](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.utils.ts#L93)

列について、ファセットやグループ化に使う値を読み取り、キャッシュします。

列が `getUniqueValues` を定義していれば、その結果を使います。そうでなければ、行のアクセサーの値を要素1つの配列に包みます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

### columnId {#columnid}

`string`

## 戻り値 {#returns}

`unknown`

## 例 {#example}

```ts
const values = row_getUniqueValues(row, 'tags')
```
