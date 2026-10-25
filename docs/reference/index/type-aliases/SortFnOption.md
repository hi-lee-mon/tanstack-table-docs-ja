---
id: SortFnOption
title: SortFnOption
---

```ts
type SortFnOption<TFeatures, TData> =
  | "auto"
  | ExtractSortFnKeys<TFeatures>
| SortFn<TFeatures, TData>;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:113](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L113)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)
