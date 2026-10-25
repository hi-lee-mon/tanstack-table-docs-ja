---
id: header_getStart
title: header_getStart
---

```ts
function header_getStart<TFeatures, TData, TValue>(header): number;
```

定義元: [features/column-sizing/columnSizingFeature.utils.ts:299](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.utils.ts#L299)

ヘッダーグループの先頭から、ヘッダーまでのオフセットを計算します。

オフセットは、1つ前の兄弟ヘッダーの開始位置にその幅を足したものです。グループの最初のヘッダーなら `0` です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### header {#header}

[`Header`](../../index/type-aliases/Header.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

`number`

## 例 {#example}

```ts
const offset = header_getStart(header)
```
