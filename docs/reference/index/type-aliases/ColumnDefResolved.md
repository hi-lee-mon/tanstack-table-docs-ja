---
id: ColumnDefResolved
title: ColumnDefResolved
---

```ts
type ColumnDefResolved<TFeatures, TData, TValue> = Partial<UnionToIntersection<ColumnDef<TFeatures, TData, TValue>>> & object;
```

定義元: [types/ColumnDef.ts:257](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L257)

## 型宣言 {#type-declaration}

### accessorKey? {#accessorkey}

```ts
optional accessorKey?: string & object | keyof TData;
```

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](CellData.md) = [`CellData`](CellData.md)
