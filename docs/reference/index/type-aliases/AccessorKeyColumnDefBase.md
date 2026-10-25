---
id: AccessorKeyColumnDefBase
title: AccessorKeyColumnDefBase
---

```ts
type AccessorKeyColumnDefBase<TFeatures, TData, TValue> = ColumnDefBase<TFeatures, TData, TValue> & object;
```

定義元: [types/ColumnDef.ts:224](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L224)

## 型宣言 {#type-declaration}

### accessorKey {#accessorkey}

```ts
accessorKey: string & object | keyof TData;
```

### id? {#id}

```ts
optional id?: string;
```

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](CellData.md) = [`CellData`](CellData.md)
