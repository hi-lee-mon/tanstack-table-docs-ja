---
id: Row
title: Row
---

```ts
type Row<TFeatures, TData> = Row_Core<TFeatures, TData> & ExtractFeatureMapTypes<TFeatures, Row_FeatureMap<TFeatures, TData>>;
```

定義元: [types/Row.ts:32](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/Row.ts#L32)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)
