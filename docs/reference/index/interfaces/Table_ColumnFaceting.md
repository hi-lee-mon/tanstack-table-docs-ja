---
id: Table_ColumnFaceting
title: Table_ColumnFaceting
---

定義元: [features/column-faceting/columnFacetingFeature.types.ts:62](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L62)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getGlobalFacetedMinMaxValues {#getglobalfacetedminmaxvalues}

```ts
getGlobalFacetedMinMaxValues: () => [number, number] | undefined;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:69](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L69)

グローバルフィルターの最小値と最大値を返します。

#### 戻り値 {#returns}

\[`number`, `number`\] \| `undefined`

***

### getGlobalFacetedRowModel {#getglobalfacetedrowmodel}

```ts
getGlobalFacetedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:73](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L73)

グローバルなファセット値を導き出すための行モデルを計算します。

#### 戻り値 {#returns-1}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

***

### getGlobalFacetedUniqueValues {#getglobalfaceteduniquevalues}

```ts
getGlobalFacetedUniqueValues: () => Map<any, number>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:77](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L77)

グローバルフィルターの、ファセットの一意な値を返します。

#### 戻り値 {#returns-2}

`Map`\<`any`, `number`\>
