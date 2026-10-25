---
id: Cell
title: Cell
---

```ts
type Cell<TFeatures, TData, TValue> = Cell_Core<TFeatures, TData, TValue> & ExtractFeatureMapTypes<TFeatures, Cell_FeatureMap>;
```

定義元: [types/Cell.ts:22](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/Cell.ts#L22)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](CellData.md) = [`CellData`](CellData.md)
