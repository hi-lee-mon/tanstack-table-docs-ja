---
id: table_getStartFlatHeaders
title: table_getStartFlatHeaders
---

```ts
function table_getStartFlatHeaders<TFeatures, TData>(table): Header<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:529](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L529)

先頭に固定されたヘッダーグループのヘッダーを、すべて平坦化します。

親のヘッダーとプレースホルダーのヘッダーも含みます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`Header`](../../index/type-aliases/Header.md)\<`TFeatures`, `TData`, `unknown`\>[]

## 例 {#example}

```ts
const headers = table_getStartFlatHeaders(table)
```
