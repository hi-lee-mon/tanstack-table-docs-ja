---
id: row_getIsGrouped
title: row_getIsGrouped
---

```ts
function row_getIsGrouped<TFeatures, TData>(row): boolean;
```

定義元: [features/column-grouping/columnGroupingFeature.utils.ts:187](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.utils.ts#L187)

この行がグループ行として作られたかどうかを判定します。

グループ行は `groupingColumnId` を持ちます。ふつうの末端の行は持ちません。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row_Core`](../../index/interfaces/Row_Core.md)\<`TFeatures`, `TData`\> & [`ExtractFeatureMapTypes`](../../index/type-aliases/ExtractFeatureMapTypes.md)\<`TFeatures`, [`Row_FeatureMap`](../../index/interfaces/Row_FeatureMap.md)\<`TFeatures`, `TData`\>\> & `Partial`\<[`Row_ColumnGrouping`](../../index/interfaces/Row_ColumnGrouping.md)\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const isGrouped = row_getIsGrouped(row)
```
