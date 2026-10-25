---
id: AccessorKeyColumnDef
title: AccessorKeyColumnDef
---

```ts
type AccessorKeyColumnDef<TFeatures, TData, TValue> = AccessorKeyColumnDefBase<TFeatures, TData, TValue> & Partial<ColumnIdentifiers<TFeatures, TData, TValue>>;
```

定義元: [types/ColumnDef.ts:233](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L233)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](CellData.md) = [`CellData`](CellData.md)
