---
id: table_getEndLeafHeaders
title: table_getEndLeafHeaders
---

```ts
function table_getEndLeafHeaders<TFeatures, TData>(table): Header<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:639](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L639)

末尾の固定領域について、末端のヘッダーを集めます。

末尾の平坦なヘッダーのリストから、親のヘッダーを取り除きます。

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
const headers = table_getEndLeafHeaders(table)
```
