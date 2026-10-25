---
id: row_getCanPin
title: row_getCanPin
---

```ts
function row_getCanPin<TFeatures, TData>(row): boolean;
```

定義元: [features/row-pinning/rowPinningFeature.utils.ts:214](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.utils.ts#L214)

この行を固定できるかどうかを判定します。

`options.enableRowPinning` には、真偽値か行の述語関数を指定できます。既定値は `true` です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const canPin = row_getCanPin(row)
```
