---
id: GroupColumnDef
title: GroupColumnDef
---

```ts
type GroupColumnDef<TFeatures, TData, TValue> = GroupColumnDefBase<TFeatures, TData, TValue> & ColumnIdentifiers<TFeatures, TData, TValue>;
```

定義元: [types/ColumnDef.ts:202](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L202)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](CellData.md) = [`CellData`](CellData.md)
