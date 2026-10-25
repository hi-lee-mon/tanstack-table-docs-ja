---
id: Header
title: Header
---

```ts
type Header<TFeatures, TData, TValue> = Header_Core<TFeatures, TData, TValue> & ExtractFeatureMapTypes<TFeatures, Header_FeatureMap>;
```

定義元: [types/Header.ts:18](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/Header.ts#L18)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](CellData.md) = [`CellData`](CellData.md)
