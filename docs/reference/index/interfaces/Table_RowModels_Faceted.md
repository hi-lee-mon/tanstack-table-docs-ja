---
id: Table_RowModels_Faceted
title: Table_RowModels_Faceted
---

定義元: [features/column-faceting/columnFacetingFeature.types.ts:26](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L26)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getFacetedMinMaxValues {#getfacetedminmaxvalues}

```ts
getFacetedMinMaxValues: () => [number, number] | undefined;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:35](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L35)

現在のファセットの対象について、数値のファセットの最小値と最大値を計算します。

`features` オプションに、行モデルのファクトリー `facetedMinMaxValues` が必要です。

#### 戻り値 {#returns}

\[`number`, `number`\] \| `undefined`

***

### getFacetedRowModel {#getfacetedrowmodel}

```ts
getFacetedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:41](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L41)

ファセット値を導き出すための行モデルを計算します。

`features` オプションに、行モデルのファクトリー `facetedRowModel` が必要です。

#### 戻り値 {#returns-1}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

***

### getFacetedUniqueValues {#getfaceteduniquevalues}

```ts
getFacetedUniqueValues: () => Map<any, number>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:47](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L47)

ファセットの一意な値とその出現回数を計算します。

`features` オプションに、行モデルのファクトリー `facetedUniqueValues` が必要です。

#### 戻り値 {#returns-2}

`Map`\<`any`, `number`\>
