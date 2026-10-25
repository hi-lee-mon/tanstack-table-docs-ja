---
id: Table_RowModels
title: Table_RowModels
---

```ts
type Table_RowModels<TFeatures, TData> = Table_RowModels_Core<TFeatures, TData> & Table_RowModels_Faceted<TFeatures, TData> & Table_RowModels_Filtered<TFeatures, TData> & Table_RowModels_Grouped<TFeatures, TData> & Table_RowModels_Expanded<TFeatures, TData> & Table_RowModels_Paginated<TFeatures, TData> & Table_RowModels_Sorted<TFeatures, TData>;
```

定義元: [core/row-models/coreRowModelsFeature.types.ts:41](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/row-models/coreRowModelsFeature.types.ts#L41)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)
