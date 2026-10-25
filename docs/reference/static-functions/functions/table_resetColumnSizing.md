---
id: table_resetColumnSizing
title: table_resetColumnSizing
---

```ts
function table_resetColumnSizing<TFeatures, TData>(table, defaultState?): void;
```

定義元: [features/column-sizing/columnSizingFeature.utils.ts:354](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.utils.ts#L354)

`columnSizing` を、設定した初期状態か機能の既定値に戻します。

引数なしの場合、`table.initialState.columnSizing` があればそれを複製して戻します。`true` を渡すと、初期状態を無視して `{}` に戻します。

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
table_resetColumnSizing(table)
table_resetColumnSizing(table, true)
```
