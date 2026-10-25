---
id: Column_ColumnFaceting
title: Column_ColumnFaceting
---

定義元: [features/column-faceting/columnFacetingFeature.types.ts:5](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L5)

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

定義元: [features/column-faceting/columnFacetingFeature.types.ts:12](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L12)

この列の、数値のファセットの最小値と最大値を計算します。

#### 戻り値 {#returns}

\[`number`, `number`\] \| `undefined`

***

### getFacetedRowModel {#getfacetedrowmodel}

```ts
getFacetedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:19](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L19)

この列のファセット値を導き出すための行モデルを計算します。

他の列のフィルターは適用し、この列自身のフィルターは除外します。

#### 戻り値 {#returns-1}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

***

### getFacetedUniqueValues {#getfaceteduniquevalues}

```ts
getFacetedUniqueValues: () => Map<any, number>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:23](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L23)

この列の、一意なファセット値とその出現回数を計算します。

#### 戻り値 {#returns-2}

`Map`\<`any`, `number`\>
