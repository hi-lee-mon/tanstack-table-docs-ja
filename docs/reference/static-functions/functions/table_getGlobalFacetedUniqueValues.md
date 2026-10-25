---
id: table_getGlobalFacetedUniqueValues
title: table_getGlobalFacetedUniqueValues
---

```ts
function table_getGlobalFacetedUniqueValues<TFeatures, TData>(table): Map<any, number>;
```

定義元: [features/column-faceting/columnFacetingFeature.utils.ts:176](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.utils.ts#L176)

グローバルフィルターについて、一意な値とその出現回数を計算します。

グローバルの対象は、内部の列 ID `__global__` で要求します。ファクトリーが登録されていなければ、空の `Map` を返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`Map`\<`any`, `number`\>

## 例 {#example}

```ts
const values = table_getGlobalFacetedUniqueValues(table)
```
