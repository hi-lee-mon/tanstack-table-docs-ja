---
id: Table_RowModels_Grouped
title: Table_RowModels_Grouped
---

定義元: [features/column-grouping/columnGroupingFeature.types.ts:143](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L143)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getGroupedRowModel {#getgroupedrowmodel}

```ts
getGroupedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:150](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L150)

グループ化を適用したあとの行モデルを返します。

#### 戻り値 {#returns}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

***

### getPreGroupedRowModel {#getpregroupedrowmodel}

```ts
getPreGroupedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:154](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L154)

グループ化の直前の行モデルを読み取ります。

#### 戻り値 {#returns-1}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>
