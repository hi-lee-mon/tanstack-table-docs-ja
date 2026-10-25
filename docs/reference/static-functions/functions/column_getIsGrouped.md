---
id: column_getIsGrouped
title: column_getIsGrouped
---

```ts
function column_getIsGrouped<TFeatures, TData, TValue>(column): boolean;
```

定義元: [features/column-grouping/columnGroupingFeature.utils.ts:88](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.utils.ts#L88)

この列 ID が `state.grouping` に含まれているかどうかを判定します。

結果はグループ化の状態を示すだけで、グループ化済み行モデルがもう計算されたかどうかは示しません。

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
const isGrouped = column_getIsGrouped(column)
```
