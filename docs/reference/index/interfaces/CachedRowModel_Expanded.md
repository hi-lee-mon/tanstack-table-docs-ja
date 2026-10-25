---
id: CachedRowModel_Expanded
title: CachedRowModel_Expanded
---

定義元: [features/row-expanding/rowExpandingFeature.types.ts:142](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L142)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### expandedRowModel {#expandedrowmodel}

```ts
expandedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:146](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L146)

#### 戻り値 {#returns}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>
