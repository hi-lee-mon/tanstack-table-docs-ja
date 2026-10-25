---
id: table_resetColumnPinning
title: table_resetColumnPinning
---

```ts
function table_resetColumnPinning<TFeatures, TData>(table, defaultState?): void;
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:318](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L318)

`columnPinning` を、設定した初期状態か機能の既定値に戻します。

引数なしの場合、`table.initialState.columnPinning` があればそれを複製して戻します。`true` を渡すと、初期状態を無視して、先頭と末尾が空の配列の状態に戻します。

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
table_resetColumnPinning(table)
table_resetColumnPinning(table, true)
```
