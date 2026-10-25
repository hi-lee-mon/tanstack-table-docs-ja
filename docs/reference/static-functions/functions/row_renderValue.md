---
id: row_renderValue
title: row_renderValue
---

```ts
function row_renderValue<TFeatures, TData>(row, columnId): any;
```

定義元: [core/rows/coreRowsFeature.utils.ts:131](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.utils.ts#L131)

列について、描画できる行の値を返します。

アクセサーの値が null や undefined の場合は、代わりにテーブルの `renderFallbackValue` を使います。

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

`any`

## 例 {#example}

```ts
const value = row_renderValue(row, 'firstName')
```
