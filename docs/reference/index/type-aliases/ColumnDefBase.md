---
id: ColumnDefBase
title: ColumnDefBase
---

```ts
type ColumnDefBase<TFeatures, TData, TValue> = ColumnDefBase_Core<TFeatures, TData, TValue> & ExtractFeatureMapTypes<TFeatures, ColumnDef_FeatureMap<TFeatures, TData, TValue>>;
```

定義元: [types/ColumnDef.ts:150](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L150)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](CellData.md) = [`CellData`](CellData.md)
