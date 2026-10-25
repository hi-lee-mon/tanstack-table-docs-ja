---
id: Table_RowModels_Paginated
title: Table_RowModels_Paginated
---

定義元: [features/row-pagination/rowPaginationFeature.types.ts:134](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L134)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getPaginatedRowModel {#getpaginatedrowmodel}

```ts
getPaginatedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:141](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L141)

ページネーションで現在のページを切り出したあとの行モデルを返します。

#### 戻り値 {#returns}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

***

### getPrePaginatedRowModel {#getprepaginatedrowmodel}

```ts
getPrePaginatedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:145](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L145)

ページネーションの直前の行モデルを読み取ります。

#### 戻り値 {#returns-1}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>
