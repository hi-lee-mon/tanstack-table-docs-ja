---
id: Subscribe
title: Subscribe
---

## Call Signature {#call-signature}

```ts
function Subscribe<TSourceValue>(props): ReactNode | Promise<ReactNode>;
```

Defined in: [src/Subscribe.ts:122](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L122)

A React component that allows you to subscribe to the table state.

This is useful for opting into state re-renders for specific parts of the table state.

For `table.Subscribe` from `useTable`, prefer that API — it uses overloads so JSX
contextual typing works. This standalone component uses a union `props` type.

### Type Parameters {#type-parameters}

#### TSourceValue {#tsourcevalue}

`TSourceValue`

### Parameters {#parameters}

#### props {#props}

[`SubscribePropsWithSourceIdentity`](../type-aliases/SubscribePropsWithSourceIdentity.md)\<`TSourceValue`\>

### Returns {#returns}

`ReactNode` \| `Promise`\<`ReactNode`\>

### Examples {#examples}

```tsx
// As a standalone component — full store
<Subscribe source={table.store} selector={(state) => ({ rowSelection: state.rowSelection })}>
  {({ rowSelection }) => (
    <div>Selected rows: {Object.keys(rowSelection).length}</div>
  )}
</Subscribe>
```

```tsx
// Entire source (atom or store) — no selector
<Subscribe source={table.atoms.rowSelection}>
  {(rowSelection) => <div>...</div>}
</Subscribe>
```

```tsx
// Project source value (e.g. one row’s selection)
<Subscribe
  source={table.atoms.rowSelection}
  selector={(rowSelection) => rowSelection?.[row.id]}
>
  {(selected) => <tr data-selected={!!selected}>...</tr>}
</Subscribe>
```

```tsx
// As table.Subscribe (table instance method)
<table.Subscribe selector={(state) => ({ rowSelection: state.rowSelection })}>
  {({ rowSelection }) => (
    <div>Selected rows: {Object.keys(rowSelection).length}</div>
  )}
</table.Subscribe>
```

## Call Signature {#call-signature-1}

```ts
function Subscribe<TSourceValue, TSelected>(props): ReactNode | Promise<ReactNode>;
```

Defined in: [src/Subscribe.ts:125](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L125)

A React component that allows you to subscribe to the table state.

This is useful for opting into state re-renders for specific parts of the table state.

For `table.Subscribe` from `useTable`, prefer that API — it uses overloads so JSX
contextual typing works. This standalone component uses a union `props` type.

### Type Parameters {#type-parameters-1}

#### TSourceValue {#tsourcevalue-1}

`TSourceValue`

#### TSelected {#tselected}

`TSelected`

### Parameters {#parameters-1}

#### props {#props-1}

[`SubscribePropsWithSourceWithSelector`](../type-aliases/SubscribePropsWithSourceWithSelector.md)\<`TSourceValue`, `TSelected`\>

### Returns {#returns-1}

`ReactNode` \| `Promise`\<`ReactNode`\>

### Examples {#examples-1}

```tsx
// As a standalone component — full store
<Subscribe source={table.store} selector={(state) => ({ rowSelection: state.rowSelection })}>
  {({ rowSelection }) => (
    <div>Selected rows: {Object.keys(rowSelection).length}</div>
  )}
</Subscribe>
```

```tsx
// Entire source (atom or store) — no selector
<Subscribe source={table.atoms.rowSelection}>
  {(rowSelection) => <div>...</div>}
</Subscribe>
```

```tsx
// Project source value (e.g. one row’s selection)
<Subscribe
  source={table.atoms.rowSelection}
  selector={(rowSelection) => rowSelection?.[row.id]}
>
  {(selected) => <tr data-selected={!!selected}>...</tr>}
</Subscribe>
```

```tsx
// As table.Subscribe (table instance method)
<table.Subscribe selector={(state) => ({ rowSelection: state.rowSelection })}>
  {({ rowSelection }) => (
    <div>Selected rows: {Object.keys(rowSelection).length}</div>
  )}
</table.Subscribe>
```

## Call Signature {#call-signature-2}

```ts
function Subscribe<TFeatures, TSelected>(props): ReactNode | Promise<ReactNode>;
```

Defined in: [src/Subscribe.ts:128](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L128)

A React component that allows you to subscribe to the table state.

This is useful for opting into state re-renders for specific parts of the table state.

For `table.Subscribe` from `useTable`, prefer that API — it uses overloads so JSX
contextual typing works. This standalone component uses a union `props` type.

### Type Parameters {#type-parameters-2}

#### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

#### TSelected {#tselected-1}

`TSelected`

### Parameters {#parameters-2}

#### props {#props-2}

[`SubscribePropsWithStore`](../type-aliases/SubscribePropsWithStore.md)\<`TFeatures`, `TSelected`\>

### Returns {#returns-2}

`ReactNode` \| `Promise`\<`ReactNode`\>

### Examples {#examples-2}

```tsx
// As a standalone component — full store
<Subscribe source={table.store} selector={(state) => ({ rowSelection: state.rowSelection })}>
  {({ rowSelection }) => (
    <div>Selected rows: {Object.keys(rowSelection).length}</div>
  )}
</Subscribe>
```

```tsx
// Entire source (atom or store) — no selector
<Subscribe source={table.atoms.rowSelection}>
  {(rowSelection) => <div>...</div>}
</Subscribe>
```

```tsx
// Project source value (e.g. one row’s selection)
<Subscribe
  source={table.atoms.rowSelection}
  selector={(rowSelection) => rowSelection?.[row.id]}
>
  {(selected) => <tr data-selected={!!selected}>...</tr>}
</Subscribe>
```

```tsx
// As table.Subscribe (table instance method)
<table.Subscribe selector={(state) => ({ rowSelection: state.rowSelection })}>
  {({ rowSelection }) => (
    <div>Selected rows: {Object.keys(rowSelection).length}</div>
  )}
</table.Subscribe>
```
