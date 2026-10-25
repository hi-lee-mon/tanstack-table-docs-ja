---
id: AccessorFnColumnDefBase
title: AccessorFnColumnDefBase
---

```ts
type AccessorFnColumnDefBase<TFeatures, TData, TValue> = ColumnDefBase<TFeatures, TData, TValue> & object;
```

定義元: [types/ColumnDef.ts:209](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L209)

## 型宣言 {#type-declaration}

### accessorFn {#accessorfn}

```ts
accessorFn: AccessorFn<TData, TValue>;
```

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](CellData.md) = [`CellData`](CellData.md)
