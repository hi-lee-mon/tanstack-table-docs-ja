---
id: table_getLeafHeaders
title: table_getLeafHeaders
---

```ts
function table_getLeafHeaders<TFeatures, TData>(table): Header<TFeatures, TData, unknown>[];
```

定義元: [core/headers/coreHeadersFeature.utils.ts:153](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.utils.ts#L153)

現在のヘッダーのツリーから、末端のヘッダーだけを集めます。

親のヘッダー（グループヘッダー）は読み飛ばすので、表示中の末端の列ごとに1つのヘッダーを描画するのに向いています。

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
const leafHeaders = table_getLeafHeaders(table)
```
