---
id: column_getCanGroup
title: column_getCanGroup
---

```ts
function column_getCanGroup<TFeatures, TData, TValue>(column): boolean;
```

定義元: [features/column-grouping/columnGroupingFeature.utils.ts:65](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.utils.ts#L65)

この列をグループ化に使えるかどうかを判定します。

列とテーブルの両方でグループ化が有効で、かつ列がアクセサーを持つか `getGroupingValue` を渡している必要があります。

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
const canGroup = column_getCanGroup(column)
```
