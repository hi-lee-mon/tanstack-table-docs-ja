---
id: row_pin
title: row_pin
---

```ts
function row_pin<TFeatures, TData>(
   row,
   position,
   includeLeafRows?,
   includeParentRows?): void;
```

定義元: [features/row-pinning/rowPinningFeature.utils.ts:287](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.utils.ts#L287)

行を固定、または固定を解除します。

省略可能なフラグを使うと、行の固定の状態を更新するときに、親の行や末端の行も含められます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

### position {#position}

[`RowPinningPosition`](../../index/type-aliases/RowPinningPosition.md)

### includeLeafRows? {#includeleafrows}

`boolean`

### includeParentRows? {#includeparentrows}

`boolean`

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
row_pin(row, 'top')
```
