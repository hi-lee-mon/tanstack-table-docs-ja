---
id: header_getSize
title: header_getSize
---

```ts
function header_getSize<TFeatures, TData, TValue>(header): number;
```

定義元: [features/column-sizing/columnSizingFeature.utils.ts:280](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.utils.ts#L280)

末端のヘッダーから、ヘッダーの描画時の幅を計算します。

グループヘッダーは、子孫のすべての末端の列の幅を合計します。末端のヘッダーは、その列の現在の幅を使います。

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
const width = header_getSize(header)
```
