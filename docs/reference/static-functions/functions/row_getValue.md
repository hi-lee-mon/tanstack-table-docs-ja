---
id: row_getValue
title: row_getValue
---

```ts
function row_getValue<TFeatures, TData>(row, columnId): unknown;
```

定義元: [core/rows/coreRowsFeature.utils.ts:63](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.utils.ts#L63)

列について、この行の値を読み取り、キャッシュします。

値は列のアクセサーが作ります。列がない場合や、アクセサーを持たない表示用の列の場合は `undefined` を返します。

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
const firstName = row_getValue(row, 'firstName')
```
