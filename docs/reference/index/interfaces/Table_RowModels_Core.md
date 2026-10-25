---
id: Table_RowModels_Core
title: Table_RowModels_Core
---

定義元: [core/row-models/coreRowModelsFeature.types.ts:27](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/row-models/coreRowModelsFeature.types.ts#L27)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getCoreRowModel {#getcorerowmodel}

```ts
getCoreRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [core/row-models/coreRowModelsFeature.types.ts:34](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/row-models/coreRowModelsFeature.types.ts#L34)

何の処理も適用する前の、コア行モデルを返します。

#### 戻り値 {#returns}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

***

### getRowModel {#getrowmodel}

```ts
getRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [core/row-models/coreRowModelsFeature.types.ts:38](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/row-models/coreRowModelsFeature.types.ts#L38)

使っている他の機能の処理をすべて適用したあとの、最終的な行モデルを返します。描画にいちばんよく使う行モデルです。

#### 戻り値 {#returns-1}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>
