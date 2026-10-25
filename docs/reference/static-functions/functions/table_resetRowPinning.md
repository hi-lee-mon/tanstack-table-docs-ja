---
id: table_resetRowPinning
title: table_resetRowPinning
---

```ts
function table_resetRowPinning<TFeatures, TData>(table, defaultState?): void;
```

定義元: [features/row-pinning/rowPinningFeature.utils.ts:66](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.utils.ts#L66)

`rowPinning` を、設定した初期状態か機能の既定値に戻します。

引数なしの場合、`table.initialState.rowPinning` があればそれを複製して戻します。`true` を渡すと、初期状態を無視して、上部と下部が空の配列の状態に戻します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### defaultState? {#defaultstate}

`boolean`

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_resetRowPinning(table)
table_resetRowPinning(table, true)
```
