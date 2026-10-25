---
id: AccessorFnColumnDef
title: AccessorFnColumnDef
---

```ts
type AccessorFnColumnDef<TFeatures, TData, TValue> = AccessorFnColumnDefBase<TFeatures, TData, TValue> & ColumnIdentifiers<TFeatures, TData, TValue>;
```

定義元: [types/ColumnDef.ts:217](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L217)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](CellData.md) = [`CellData`](CellData.md)
