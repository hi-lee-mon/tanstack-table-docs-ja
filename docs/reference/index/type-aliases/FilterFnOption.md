---
id: FilterFnOption
title: FilterFnOption
---

```ts
type FilterFnOption<TFeatures, TData> =
  | "auto"
  | ExtractFilterFnKeys<TFeatures>
| FilterFn<TFeatures, TData>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:172](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L172)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)
