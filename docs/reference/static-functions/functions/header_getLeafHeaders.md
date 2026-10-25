---
id: header_getLeafHeaders
title: header_getLeafHeaders
---

```ts
function header_getLeafHeaders<TFeatures, TData, TValue>(header): Header<TFeatures, TData, TValue>[];
```

定義元: [core/headers/coreHeadersFeature.utils.ts:35](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.utils.ts#L35)

ヘッダーのツリーをたどり、子孫の末端のヘッダーをすべて集めます。

ヘッダー自身も、その子孫のあとに含まれます。入れ子のヘッダーグループで使う再帰の形と同じです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue`

## パラメーター {#parameters}

### header {#header}

[`Header`](../../index/type-aliases/Header.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

[`Header`](../../index/type-aliases/Header.md)\<`TFeatures`, `TData`, `TValue`\>[]

## 例 {#example}

```ts
const leafHeaders = header_getLeafHeaders(header)
```
