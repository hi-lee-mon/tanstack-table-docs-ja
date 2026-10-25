---
id: Table_RowModels_Expanded
title: Table_RowModels_Expanded
---

定義元: [features/row-expanding/rowExpandingFeature.types.ts:128](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L128)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getExpandedRowModel {#getexpandedrowmodel}

```ts
getExpandedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:135](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L135)

展開された行を平坦化して表示に含めたあとの行モデルを返します。

#### 戻り値 {#returns}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

***

### getPreExpandedRowModel {#getpreexpandedrowmodel}

```ts
getPreExpandedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:139](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L139)

展開の直前の行モデルを読み取ります。

#### 戻り値 {#returns-1}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>
