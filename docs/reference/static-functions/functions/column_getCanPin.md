---
id: column_getCanPin
title: column_getCanPin
---

```ts
function column_getCanPin<TFeatures, TData, TValue>(column): boolean;
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:112](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L112)

この列か、その末端の列のいずれかを固定できるかどうかを判定します。

列の `enablePinning` とテーブルの `enableColumnPinning` は、どちらも既定値が `true` です。少なくとも1つの末端の列が固定を許可している必要があります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### column {#column}

[`Column_Internal`](../../index/interfaces/Column_Internal.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const canPin = column_getCanPin(column)
```
