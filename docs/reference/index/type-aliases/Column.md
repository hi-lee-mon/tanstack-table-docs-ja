---
id: Column
title: Column
---

```ts
type Column<TFeatures, TData, TValue> = Column_Core<TFeatures, TData, TValue> & ExtractFeatureMapTypes<TFeatures, Column_FeatureMap<TFeatures, TData>>;
```

定義元: [types/Column.ts:41](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/Column.ts#L41)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` = `unknown`
