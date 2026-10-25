---
id: CachedRowModels
title: CachedRowModels
---

```ts
type CachedRowModels<TFeatures, TData> = Partial<CachedRowModel_Core<TFeatures, TData>> & ExtractFeatureMapTypes<TFeatures, CachedRowModels_FeatureMap<TFeatures, TData>>;
```

定義元: [types/RowModel.ts:23](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/RowModel.ts#L23)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)
