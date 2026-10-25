---
id: IdentifiedColumnDef
title: IdentifiedColumnDef
---

```ts
type IdentifiedColumnDef<TFeatures, TData, TValue> = ColumnDefBase<TFeatures, TData, TValue> & object;
```

定義元: [types/ColumnDef.ts:179](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L179)

## 型宣言 {#type-declaration}

### header? {#header}

```ts
optional header?: StringOrTemplateHeader<TFeatures, TData, TValue>;
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
