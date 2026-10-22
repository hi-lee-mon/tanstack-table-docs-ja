---
id: ReactTable
title: ReactTable
---

```ts
type ReactTable<TFeatures, TData, TSelected> = Omit<Table<TFeatures, TData>, "store"> & object;
```

Defined in: [src/useTable.ts:29](https://github.com/TanStack/table/blob/main/packages/react-table/src/useTable.ts#L29)

## Type Declaration {#type-declaration}

### FlexRender {#flexrender}

```ts
FlexRender: <TValue>(props) => ReactNode;
```

A React component that renders headers, cells, or footers with custom markup.
Use this utility component instead of manually calling flexRender.

#### Type Parameters {#type-parameters}

##### TValue {#tvalue}

`TValue` *extends* `CellData` = `CellData`

#### Parameters {#parameters}

##### props {#props}

[`FlexRenderProps`](FlexRenderProps.md)\<`TFeatures`, `TData`, `TValue`\>

#### Returns {#returns}

`ReactNode`

#### Example {#example}

```tsx
<table.FlexRender cell={cell} />
<table.FlexRender header={header} />
<table.FlexRender footer={footer} />
```

This replaces calling `flexRender` directly like this:
```tsx
flexRender(cell.column.columnDef.cell, cell.getContext())
flexRender(header.column.columnDef.header, header.getContext())
flexRender(footer.column.columnDef.footer, footer.getContext())
```

### state {#state}

```ts
readonly state: Readonly<TSelected>;
```

The selected state of the table. This state may not match the structure of
the full table state because it is selected by the selector function that
you pass as the 2nd argument to `useTable`.

#### Example {#example-1}

```ts
const table = useTable(options, (state) => ({ globalFilter: state.globalFilter })) // only globalFilter is part of the selected state

console.log(table.state.globalFilter)
```

### ~~store~~ {#store}

```ts
readonly store: Table<TFeatures, TData>["store"];
```

#### Deprecated {#deprecated}

Prefer `table.state` for render reads,
`table.atoms.<slice>.get()` for slice snapshots, or
`table.Subscribe` / `useSelector(table.store, selector)` for explicit
subscriptions. `table.store.state` is a current-value snapshot and is easy
to misuse in render code.

### Subscribe {#subscribe}

```ts
Subscribe: {
<TSourceValue>  (props): ReactNode | Promise<ReactNode>;
<TSourceValue, TSubSelected>  (props): ReactNode | Promise<ReactNode>;
<TSubSelected>  (props): ReactNode | Promise<ReactNode>;
};
```

Overloads (not a single union) so `selector` callbacks get correct contextual
types in JSX; a union of two `selector` signatures degrades to implicit `any`.

Source **without** `selector` is a separate overload so children receive `TSourceValue`
(identity projection). If `selector` were optional on one overload, `TSubSelected`
would default to `unknown` instead of inferring from the source.

The **source** overloads are listed first so `TSourceValue` is inferred from `source`.

#### Call Signature {#call-signature}

```ts
<TSourceValue>(props): ReactNode | Promise<ReactNode>;
```

##### Type Parameters {#type-parameters-1}

###### TSourceValue {#tsourcevalue}

`TSourceValue`

##### Parameters {#parameters-1}

###### props {#props-1}

###### children {#children}

((`state`) => `ReactNode`) \| `ReactNode`

###### selector? {#selector}

`undefined`

###### source {#source}

[`SubscribeSource`](SubscribeSource.md)\<`TSourceValue`\>

##### Returns {#returns-1}

`ReactNode` \| `Promise`\<`ReactNode`\>

#### Call Signature {#call-signature-1}

```ts
<TSourceValue, TSubSelected>(props): ReactNode | Promise<ReactNode>;
```

##### Type Parameters {#type-parameters-2}

###### TSourceValue {#tsourcevalue-1}

`TSourceValue`

###### TSubSelected {#tsubselected}

`TSubSelected`

##### Parameters {#parameters-2}

###### props {#props-2}

###### children {#children-1}

((`state`) => `ReactNode`) \| `ReactNode`

###### selector {#selector-1}

(`state`) => `TSubSelected`

###### source {#source-1}

[`SubscribeSource`](SubscribeSource.md)\<`TSourceValue`\>

##### Returns {#returns-2}

`ReactNode` \| `Promise`\<`ReactNode`\>

#### Call Signature {#call-signature-2}

```ts
<TSubSelected>(props): ReactNode | Promise<ReactNode>;
```

##### Type Parameters {#type-parameters-3}

###### TSubSelected {#tsubselected-1}

`TSubSelected`

##### Parameters {#parameters-3}

###### props {#props-3}

`Omit`\<[`SubscribePropsWithStore`](SubscribePropsWithStore.md)\<`TFeatures`, `TSubSelected`\>, `"source"`\>

##### Returns {#returns-3}

`ReactNode` \| `Promise`\<`ReactNode`\>

## Type Parameters {#type-parameters-4}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TSelected {#tselected}

`TSelected` = `TableState`\<`TFeatures`\>
