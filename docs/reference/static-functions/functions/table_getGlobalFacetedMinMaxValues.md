---
id: table_getGlobalFacetedMinMaxValues
title: table_getGlobalFacetedMinMaxValues
---

```ts
function table_getGlobalFacetedMinMaxValues<TFeatures, TData>(table): [number, number] | undefined;
```

定義元: [features/column-faceting/columnFacetingFeature.utils.ts:125](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.utils.ts#L125)

グローバルフィルターについて、数値のファセットの最小値と最大値を計算します。

グローバルの対象は、内部の列 ID `__global__` で要求します。ファクトリーが登録されていなければ、結果は `undefined` です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

\[`number`, `number`\] \| `undefined`

## 例 {#example}

```ts
const range = table_getGlobalFacetedMinMaxValues(table)
```
