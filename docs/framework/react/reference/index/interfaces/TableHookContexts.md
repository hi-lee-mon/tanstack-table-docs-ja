---
id: TableHookContexts
title: TableHookContexts
---

Defined in: [src/createTableHookContexts.tsx:17](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHookContexts.tsx#L17)

The object returned by [createTableHookContexts](../functions/createTableHookContexts.md): three scoped React
contexts plus matching context hooks.

## Type Parameters {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

## Properties {#properties}

### cellContext {#cellcontext}

```ts
cellContext: Context<Cell<any, any, any>>;
```

Defined in: [src/createTableHookContexts.tsx:22](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHookContexts.tsx#L22)

***

### headerContext {#headercontext}

```ts
headerContext: Context<Header<any, any, any>>;
```

Defined in: [src/createTableHookContexts.tsx:23](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHookContexts.tsx#L23)

***

### tableContext {#tablecontext}

```ts
tableContext: Context<ReactTable<any, any>>;
```

Defined in: [src/createTableHookContexts.tsx:21](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHookContexts.tsx#L21)

***

### useCellContext {#usecellcontext}

```ts
useCellContext: <TValue>() => Cell<TFeatures, any, TValue>;
```

Defined in: [src/createTableHookContexts.tsx:28](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHookContexts.tsx#L28)

#### Type Parameters {#type-parameters-1}

##### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

#### Returns {#returns}

`Cell`\<`TFeatures`, `any`, `TValue`\>

***

### useHeaderContext {#useheadercontext}

```ts
useHeaderContext: <TValue>() => Header<TFeatures, any, TValue>;
```

Defined in: [src/createTableHookContexts.tsx:33](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHookContexts.tsx#L33)

#### Type Parameters {#type-parameters-2}

##### TValue {#tvalue-1}

`TValue` *extends* `unknown` = `unknown`

#### Returns {#returns-1}

`Header`\<`TFeatures`, `any`, `TValue`\>

***

### useTableContext {#usetablecontext}

```ts
useTableContext: <TTableData>() => ReactTable<TFeatures, TTableData>;
```

Defined in: [src/createTableHookContexts.tsx:24](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHookContexts.tsx#L24)

#### Type Parameters {#type-parameters-3}

##### TTableData {#ttabledata}

`TTableData` *extends* `RowData` = `TData`

#### Returns {#returns-2}

[`ReactTable`](../type-aliases/ReactTable.md)\<`TFeatures`, `TTableData`\>
