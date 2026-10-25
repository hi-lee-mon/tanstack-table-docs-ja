---
id: ColumnDef
title: ColumnDef
---

```ts
type ColumnDef<TFeatures, TData, TValue> =
  | DisplayColumnDef<TFeatures, TData, TValue>
  | GroupColumnDef<TFeatures, TData, TValue>
| AccessorColumnDef<TFeatures, TData, TValue>;
```

定義元: [types/ColumnDef.ts:248](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L248)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](CellData.md) = [`CellData`](CellData.md)
