---
id: AppCellContext
title: AppCellContext
---

```ts
type AppCellContext<TFeatures, TData, TValue, TCellComponents> = object;
```

Defined in: [src/createTableHook.tsx:48](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L48)

Enhanced CellContext with pre-bound cell components.
The `cell` property includes the registered cellComponents.

## Type Parameters {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TValue {#tvalue}

`TValue` *extends* `CellData`

### TCellComponents {#tcellcomponents}

`TCellComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

## Properties {#properties}

### cell {#cell}

```ts
cell: Cell<TFeatures, TData, TValue> & TCellComponents & object;
```

Defined in: [src/createTableHook.tsx:54](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L54)

#### Type Declaration {#type-declaration}

##### FlexRender {#flexrender}

```ts
FlexRender: () => ReactNode;
```

###### Returns {#returns}

`ReactNode`

***

### column {#column}

```ts
column: Column<TFeatures, TData, TValue>;
```

Defined in: [src/createTableHook.tsx:56](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L56)

***

### getValue {#getvalue}

```ts
getValue: CellContext<TFeatures, TData, TValue>["getValue"];
```

Defined in: [src/createTableHook.tsx:57](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L57)

***

### renderValue {#rendervalue}

```ts
renderValue: CellContext<TFeatures, TData, TValue>["renderValue"];
```

Defined in: [src/createTableHook.tsx:58](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L58)

***

### row {#row}

```ts
row: Row<TFeatures, TData>;
```

Defined in: [src/createTableHook.tsx:59](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L59)

***

### table {#table}

```ts
table: Table<TFeatures, TData>;
```

Defined in: [src/createTableHook.tsx:60](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L60)
