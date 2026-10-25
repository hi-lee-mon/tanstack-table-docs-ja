---
id: row_getGroupingValue
title: row_getGroupingValue
---

```ts
function row_getGroupingValue<TFeatures, TData>(row, columnId): any;
```

定義元: [features/column-grouping/columnGroupingFeature.utils.ts:205](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.utils.ts#L205)

列について、この行のグループ化の値を読み取り、キャッシュします。

`columnDef.getGroupingValue` を渡した場合は、そちらが優先されます。そうでなければ、ふつうの行のアクセサーの値を使います。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row_Core`](../../index/interfaces/Row_Core.md)\<`TFeatures`, `TData`\> & [`ExtractFeatureMapTypes`](../../index/type-aliases/ExtractFeatureMapTypes.md)\<`TFeatures`, [`Row_FeatureMap`](../../index/interfaces/Row_FeatureMap.md)\<`TFeatures`, `TData`\>\> & `Partial`\<[`Row_ColumnGrouping`](../../index/interfaces/Row_ColumnGrouping.md)\>

### columnId {#columnid}

`string`

## 戻り値 {#returns}

`any`

## 例 {#example}

```ts
const groupValue = row_getGroupingValue(row, 'status')
```
