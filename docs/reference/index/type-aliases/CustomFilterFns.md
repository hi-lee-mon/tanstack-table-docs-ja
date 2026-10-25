---
id: CustomFilterFns
title: CustomFilterFns
---

```ts
type CustomFilterFns<TFeatures, TData> = Record<string, FilterFn<TFeatures, TData>>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:150](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L150)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)
