---
id: AppHeaderComponent
title: AppHeaderComponent
---

Defined in: [src/createTableHook.tsx:497](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L497)

Component type for AppHeader/AppFooter - wraps a header and provides header context with optional Subscribe

## Type Parameters {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### THeaderComponents {#theadercomponents}

`THeaderComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

## Call Signature {#call-signature}

```ts
AppHeaderComponent<TValue>(props): ReactNode;
```

Defined in: [src/createTableHook.tsx:502](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L502)

Component type for AppHeader/AppFooter - wraps a header and provides header context with optional Subscribe

### Type Parameters {#type-parameters-1}

#### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

### Parameters {#parameters}

#### props {#props}

[`AppHeaderPropsWithoutSelector`](AppHeaderPropsWithoutSelector.md)\<`TFeatures`, `TData`, `TValue`, `THeaderComponents`\>

### Returns {#returns}

`ReactNode`

## Call Signature {#call-signature-1}

```ts
AppHeaderComponent<TValue, TSelected>(props): ReactNode;
```

Defined in: [src/createTableHook.tsx:510](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L510)

Component type for AppHeader/AppFooter - wraps a header and provides header context with optional Subscribe

### Type Parameters {#type-parameters-2}

#### TValue {#tvalue-1}

`TValue` *extends* `unknown` = `unknown`

#### TSelected {#tselected}

`TSelected` = `unknown`

### Parameters {#parameters-1}

#### props {#props-1}

[`AppHeaderPropsWithSelector`](AppHeaderPropsWithSelector.md)\<`TFeatures`, `TData`, `TValue`, `THeaderComponents`, `TSelected`\>

### Returns {#returns-1}

`ReactNode`
