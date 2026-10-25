---
id: column_getFacetedMinMaxValues
title: column_getFacetedMinMaxValues
---

```ts
function column_getFacetedMinMaxValues<TFeatures, TData, TValue>(column, table): [number, number] | undefined;
```

定義元: [features/column-faceting/columnFacetingFeature.utils.ts:19](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.utils.ts#L19)

1つの列について、数値のファセットの最小値と最大値を計算します。

計算は、設定された行モデルのファクトリー `facetedMinMaxValues` が担います。ファクトリーが登録されていなければ、結果は `undefined` です。

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

\[`number`, `number`\] \| `undefined`

## 例 {#example}

```ts
const range = column_getFacetedMinMaxValues(column, table)
```
