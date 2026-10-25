---
id: Table_RowModels_Filtered
title: Table_RowModels_Filtered
---

定義元: [features/column-filtering/columnFilteringFeature.types.ts:294](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L294)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getFilteredRowModel {#getfilteredrowmodel}

```ts
getFilteredRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:301](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L301)

列フィルターとグローバルフィルターを適用したあとの行モデルを返します。

#### 戻り値 {#returns}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

***

### getPreFilteredRowModel {#getprefilteredrowmodel}

```ts
getPreFilteredRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:305](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L305)

フィルタリングの直前の行モデルを読み取ります。

#### 戻り値 {#returns-1}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>
