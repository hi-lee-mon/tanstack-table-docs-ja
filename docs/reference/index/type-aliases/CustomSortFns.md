---
id: CustomSortFns
title: CustomSortFns
---

```ts
type CustomSortFns<TFeatures, TData> = Record<string, SortFn<TFeatures, TData>>;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:92](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L92)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)
