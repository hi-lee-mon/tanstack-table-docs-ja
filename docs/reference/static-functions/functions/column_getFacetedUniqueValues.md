---
id: column_getFacetedUniqueValues
title: column_getFacetedUniqueValues
---

```ts
function column_getFacetedUniqueValues<TFeatures, TData, TValue>(column, table): Map<any, number>;
```

定義元: [features/column-faceting/columnFacetingFeature.utils.ts:85](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.utils.ts#L85)

1つの列について、ファセットの一意な値とその出現回数を計算します。

計算は、設定された行モデルのファクトリー `facetedUniqueValues` が担います。ファクトリーが登録されていなければ、空の `Map` を返します。

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

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`Map`\<`any`, `number`\>

## 例 {#example}

```ts
const values = column_getFacetedUniqueValues(column, table)
```
