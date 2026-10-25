---
id: CachedRowModel_Paginated
title: CachedRowModel_Paginated
---

定義元: [features/row-pagination/rowPaginationFeature.types.ts:148](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L148)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### paginatedRowModel {#paginatedrowmodel}

```ts
paginatedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:152](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L152)

#### 戻り値 {#returns}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>
