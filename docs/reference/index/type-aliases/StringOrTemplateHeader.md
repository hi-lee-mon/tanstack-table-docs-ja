---
id: StringOrTemplateHeader
title: StringOrTemplateHeader
---

```ts
type StringOrTemplateHeader<TFeatures, TData, TValue> =
  | string
| ColumnDefTemplate<HeaderContext<TFeatures, TData, TValue>>;
```

定義元: [types/ColumnDef.ts:67](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L67)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](CellData.md) = [`CellData`](CellData.md)
