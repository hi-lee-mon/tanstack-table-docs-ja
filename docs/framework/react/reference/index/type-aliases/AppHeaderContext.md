---
id: AppHeaderContext
title: AppHeaderContext
---

```ts
type AppHeaderContext<TFeatures, TData, TValue, THeaderComponents> = object;
```

Defined in: [src/createTableHook.tsx:67](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L67)

Enhanced HeaderContext with pre-bound header components.
The `header` property includes the registered headerComponents.

## Type Parameters {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TValue {#tvalue}

`TValue` *extends* `CellData`

### THeaderComponents {#theadercomponents}

`THeaderComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

## Properties {#properties}

### column {#column}

```ts
column: Column<TFeatures, TData, TValue>;
```

Defined in: [src/createTableHook.tsx:73](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L73)

***

### header {#header}

```ts
header: Header<TFeatures, TData, TValue> & THeaderComponents & object;
```

Defined in: [src/createTableHook.tsx:74](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L74)

#### Type Declaration {#type-declaration}

##### FlexRender {#flexrender}

```ts
FlexRender: () => ReactNode;
```

###### Returns {#returns}

`ReactNode`

***

### table {#table}

```ts
table: Table<TFeatures, TData>;
```

Defined in: [src/createTableHook.tsx:76](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L76)
