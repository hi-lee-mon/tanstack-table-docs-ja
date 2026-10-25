---
id: AccessorColumnDef
title: AccessorColumnDef
---

```ts
type AccessorColumnDef<TFeatures, TData, TValue> =
  | AccessorKeyColumnDef<TFeatures, TData, TValue>
| AccessorFnColumnDef<TFeatures, TData, TValue>;
```

定義元: [types/ColumnDef.ts:240](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L240)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](CellData.md) = [`CellData`](CellData.md)
