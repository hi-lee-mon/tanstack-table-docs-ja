---
id: table_getTotalSize
title: table_getTotalSize
---

```ts
function table_getTotalSize<TFeatures, TData>(table): number;
```

定義元: [features/column-sizing/columnSizingFeature.utils.ts:393](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.utils.ts#L393)

テーブルのヘッダー行全体の、描画時の幅を合計します。

主となるヘッダーグループの、先頭・中央・末尾の列をすべて含みます。

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
const width = table_getTotalSize(table)
```
