---
id: CreateTableHookResult
title: CreateTableHookResult
---

Defined in: [src/createTableHook.tsx:298](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L298)

## Type Parameters {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TTableComponents {#ttablecomponents}

`TTableComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

### TCellComponents {#tcellcomponents}

`TCellComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

### THeaderComponents {#theadercomponents}

`THeaderComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

## Properties {#properties}

### appFeatures {#appfeatures}

```ts
appFeatures: TFeatures;
```

Defined in: [src/createTableHook.tsx:305](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L305)

The features object that was passed to `createTableHook`.

***

### createAppColumnHelper {#createappcolumnhelper}

```ts
createAppColumnHelper: <TData>() => AppColumnHelper<TFeatures, TData, TCellComponents, THeaderComponents>;
```

Defined in: [src/createTableHook.tsx:310](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L310)

A column helper pre-bound to `TFeatures` and the registered components, so
the cell/header/footer render props expose the bound components.

#### Type Parameters {#type-parameters-1}

##### TData {#tdata}

`TData` *extends* `RowData`

#### Returns {#returns}

[`AppColumnHelper`](../type-aliases/AppColumnHelper.md)\<`TFeatures`, `TData`, `TCellComponents`, `THeaderComponents`\>

***

### useAppTable {#useapptable}

```ts
useAppTable: <TData, TSelected>(tableOptions, selector?) => AppReactTable<TFeatures, TData, TSelected, TTableComponents, TCellComponents, THeaderComponents>;
```

Defined in: [src/createTableHook.tsx:320](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L320)

Creates a table with the `App*` wrapper components and registered
`tableComponents` attached. `TData` is inferred from the `data` option.

#### Type Parameters {#type-parameters-2}

##### TData {#tdata-1}

`TData` *extends* `RowData`

##### TSelected {#tselected}

`TSelected` = `TableState`\<`TFeatures`\>

#### Parameters {#parameters}

##### tableOptions {#tableoptions}

`Omit`\<`TableOptions`\<`TFeatures`, `TData`\>, `"features"`\>

##### selector? {#selector}

(`state`) => `TSelected`

#### Returns {#returns-1}

[`AppReactTable`](../type-aliases/AppReactTable.md)\<`TFeatures`, `TData`, `TSelected`, `TTableComponents`, `TCellComponents`, `THeaderComponents`\>

***

### useCellContext {#usecellcontext}

```ts
useCellContext: <TValue>() => Cell_Core<TFeatures, any, TValue> & ExtractFeatureMapTypes<TFeatures, Cell_FeatureMap> & TCellComponents & object;
```

Defined in: [src/createTableHook.tsx:357](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L357)

Reads the cell provided by the nearest `<table.AppCell>`, extended with your
`cellComponents` and a context-bound `FlexRender`.

#### Type Parameters {#type-parameters-3}

##### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

#### Returns {#returns-2}

`Cell_Core`\<`TFeatures`, `any`, `TValue`\> & `ExtractFeatureMapTypes`\<`TFeatures`, `Cell_FeatureMap`\> & `TCellComponents` & `object`

***

### useHeaderContext {#useheadercontext}

```ts
useHeaderContext: <TValue>() => Header_Core<TFeatures, any, TValue> & ExtractFeatureMapTypes<TFeatures, Header_FeatureMap> & THeaderComponents & object;
```

Defined in: [src/createTableHook.tsx:368](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L368)

Reads the header provided by the nearest `<table.AppHeader>` /
`<table.AppFooter>`, extended with your `headerComponents` and a
context-bound `FlexRender`.

#### Type Parameters {#type-parameters-4}

##### TValue {#tvalue-1}

`TValue` *extends* `unknown` = `unknown`

#### Returns {#returns-3}

`Header_Core`\<`TFeatures`, `any`, `TValue`\> & `ExtractFeatureMapTypes`\<`TFeatures`, `Header_FeatureMap`\> & `THeaderComponents` & `object`

***

### useTableContext {#usetablecontext}

```ts
useTableContext: <TData, TSelected>() => AppReactTable<TFeatures, TData, TSelected, TTableComponents, TCellComponents, THeaderComponents>;
```

Defined in: [src/createTableHook.tsx:342](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L342)

Reads the table provided by the nearest `<table.AppTable>`. This is the same
extended instance `useAppTable` returns, so the `App*` components and your
`tableComponents` are available on it.

Pass `TSelected` to match the selector you gave `useAppTable`, so
`table.state` is typed as the selected slice. It cannot be inferred
automatically (React context does not carry the provider's generics), so it
defaults to the full table state, which is correct for the common case of
`useAppTable` without a selector.

#### Type Parameters {#type-parameters-5}

##### TData {#tdata-2}

`TData` *extends* `RowData` = `RowData`

##### TSelected {#tselected-1}

`TSelected` = `TableState`\<`TFeatures`\>

#### Returns {#returns-4}

[`AppReactTable`](../type-aliases/AppReactTable.md)\<`TFeatures`, `TData`, `TSelected`, `TTableComponents`, `TCellComponents`, `THeaderComponents`\>
