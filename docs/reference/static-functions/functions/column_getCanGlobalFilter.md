---
id: column_getCanGlobalFilter
title: column_getCanGlobalFilter
---

```ts
function column_getCanGlobalFilter<TFeatures, TData, TValue>(column): boolean;
```

定義元: [features/global-filtering/globalFilteringFeature.utils.ts:20](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/global-filtering/globalFilteringFeature.utils.ts#L20)

このアクセサー列がグローバルフィルタリングの対象かどうかを判定します。

列がアクセサーを持ち、列、テーブル、そして指定されていれば `getColumnCanGlobalFilter` の判定に通る必要があります。

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
const canGlobalFilter = column_getCanGlobalFilter(column)
```
