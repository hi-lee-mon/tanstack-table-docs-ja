---
id: table_getFlatHeaders
title: table_getFlatHeaders
---

```ts
function table_getFlatHeaders<TFeatures, TData>(table): Header<TFeatures, TData, unknown>[];
```

定義元: [core/headers/coreHeadersFeature.utils.ts:127](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.utils.ts#L127)

すべてのヘッダーグループのヘッダーを、1つの配列に平坦化します。

結果には親のヘッダーとプレースホルダーのヘッダーも含まれ、ヘッダーグループの上から下への順に並びます。

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
const flatHeaders = table_getFlatHeaders(table)
```
