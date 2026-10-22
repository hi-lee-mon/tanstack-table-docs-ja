---
id: AppCellComponent
title: AppCellComponent
---

Defined in: [src/createTableHook.tsx:470](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L470)

Component type for AppCell - wraps a cell and provides cell context with optional Subscribe

## Type Parameters {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TCellComponents {#tcellcomponents}

`TCellComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

## Call Signature {#call-signature}

```ts
AppCellComponent<TValue>(props): ReactNode;
```

Defined in: [src/createTableHook.tsx:475](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L475)

Component type for AppCell - wraps a cell and provides cell context with optional Subscribe

### Type Parameters {#type-parameters-1}

#### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

### Parameters {#parameters}

#### props {#props}

[`AppCellPropsWithoutSelector`](AppCellPropsWithoutSelector.md)\<`TFeatures`, `TData`, `TValue`, `TCellComponents`\>

### Returns {#returns}

`ReactNode`

## Call Signature {#call-signature-1}

```ts
AppCellComponent<TValue, TSelected>(props): ReactNode;
```

Defined in: [src/createTableHook.tsx:483](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L483)

Component type for AppCell - wraps a cell and provides cell context with optional Subscribe

### Type Parameters {#type-parameters-2}

#### TValue {#tvalue-1}

`TValue` *extends* `unknown` = `unknown`

#### TSelected {#tselected}

`TSelected` = `unknown`

### Parameters {#parameters-1}

#### props {#props-1}

[`AppCellPropsWithSelector`](AppCellPropsWithSelector.md)\<`TFeatures`, `TData`, `TValue`, `TCellComponents`, `TSelected`\>

### Returns {#returns-1}

`ReactNode`
