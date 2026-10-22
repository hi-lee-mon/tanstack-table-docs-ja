---
id: AppColumnHelper
title: AppColumnHelper
---

```ts
type AppColumnHelper<TFeatures, TData, TCellComponents, THeaderComponents> = object;
```

Defined in: [src/createTableHook.tsx:168](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L168)

Enhanced column helper with pre-bound components in cell/header/footer contexts.
This enables TypeScript to know about the registered components when defining columns.

## Type Parameters {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TCellComponents {#tcellcomponents}

`TCellComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

### THeaderComponents {#theadercomponents}

`THeaderComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

## Properties {#properties}

### accessor {#accessor}

```ts
accessor: <TAccessor, TValue>(accessor, column) => TAccessor extends AccessorFn<TData> ? AccessorFnColumnDef<TFeatures, TData, TValue> : AccessorKeyColumnDef<TFeatures, TData, TValue>;
```

Defined in: [src/createTableHook.tsx:178](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L178)

Creates a data column definition with an accessor key or function.
The cell, header, and footer contexts include pre-bound components.

#### Type Parameters {#type-parameters-1}

##### TAccessor {#taccessor}

`TAccessor` *extends* `AccessorFn`\<`TData`\> \| `DeepKeys`\<`TData`\>

##### TValue {#tvalue}

`TValue` *extends* `TAccessor` *extends* `AccessorFn`\<`TData`, infer TReturn\> ? `TReturn` : `TAccessor` *extends* `DeepKeys`\<`TData`\> ? `DeepValue`\<`TData`, `TAccessor`\> : `never`

#### Parameters {#parameters}

##### accessor {#accessor-1}

`TAccessor`

##### column {#column}

`TAccessor` *extends* `AccessorFn`\<`TData`\> ? [`AppColumnDefBase`](AppColumnDefBase.md)\<`TFeatures`, `TData`, `TValue`, `TCellComponents`, `THeaderComponents`\> & `object` : [`AppColumnDefBase`](AppColumnDefBase.md)\<`TFeatures`, `TData`, `TValue`, `TCellComponents`, `THeaderComponents`\>

#### Returns {#returns}

`TAccessor` *extends* `AccessorFn`\<`TData`\> ? `AccessorFnColumnDef`\<`TFeatures`, `TData`, `TValue`\> : `AccessorKeyColumnDef`\<`TFeatures`, `TData`, `TValue`\>

***

### columns {#columns}

```ts
columns: <TColumns>(columns) => ColumnDef<TFeatures, TData, any>[] & [...TColumns];
```

Defined in: [src/createTableHook.tsx:209](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L209)

Wraps an array of column definitions to preserve each column's individual TValue type.

#### Type Parameters {#type-parameters-2}

##### TColumns {#tcolumns}

`TColumns` *extends* `ReadonlyArray`\<`ColumnDef`\<`TFeatures`, `TData`, `any`\>\>

#### Parameters {#parameters-1}

##### columns {#columns-1}

\[`...TColumns`\]

#### Returns {#returns-1}

`ColumnDef`\<`TFeatures`, `TData`, `any`\>[] & \[`...TColumns`\]

***

### display {#display}

```ts
display: (column) => DisplayColumnDef<TFeatures, TData, unknown>;
```

Defined in: [src/createTableHook.tsx:217](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L217)

Creates a display column definition for non-data columns.
The cell, header, and footer contexts include pre-bound components.

#### Parameters {#parameters-2}

##### column {#column-1}

[`AppDisplayColumnDef`](AppDisplayColumnDef.md)\<`TFeatures`, `TData`, `TCellComponents`, `THeaderComponents`\>

#### Returns {#returns-2}

`DisplayColumnDef`\<`TFeatures`, `TData`, `unknown`\>

***

### group {#group}

```ts
group: (column) => GroupColumnDef<TFeatures, TData, unknown>;
```

Defined in: [src/createTableHook.tsx:230](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L230)

Creates a group column definition with nested child columns.
The cell, header, and footer contexts include pre-bound components.

#### Parameters {#parameters-3}

##### column {#column-2}

[`AppGroupColumnDef`](AppGroupColumnDef.md)\<`TFeatures`, `TData`, `TCellComponents`, `THeaderComponents`\>

#### Returns {#returns-3}

`GroupColumnDef`\<`TFeatures`, `TData`, `unknown`\>
