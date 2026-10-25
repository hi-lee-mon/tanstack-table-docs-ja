---
id: Table_RowModels_Sorted
title: Table_RowModels_Sorted
---

定義元: [features/row-sorting/rowSortingFeature.types.ts:290](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L290)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getPreSortedRowModel {#getpresortedrowmodel}

```ts
getPreSortedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:297](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L297)

ソートの直前の行モデルを読み取ります。

#### 戻り値 {#returns}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

***

### getSortedRowModel {#getsortedrowmodel}

```ts
getSortedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:301](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L301)

ソートを適用したあとの行モデルを返します。

#### 戻り値 {#returns-1}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>
