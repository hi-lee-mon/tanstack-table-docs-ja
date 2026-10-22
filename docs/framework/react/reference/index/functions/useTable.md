---
id: useTable
title: useTable
---

```ts
function useTable<TFeatures, TData, TSelected>(tableOptions, selector?): ReactTable<TFeatures, TData, TSelected>;
```

Defined in: [src/useTable.ts:149](https://github.com/TanStack/table/blob/main/packages/react-table/src/useTable.ts#L149)

Creates a React table instance backed by TanStack Store atoms.

The optional selector projects from `table.store`; the selected value is
exposed on `table.state` and compared shallowly for React re-renders. Omit
the selector to subscribe to every registered table state slice, or pass a
narrower selector and use `table.Subscribe` lower in the tree for targeted
subscriptions.

## Type Parameters {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TSelected {#tselected}

`TSelected` = `TableState`\<`TFeatures`\>

## Parameters {#parameters}

### tableOptions {#tableoptions}

`TableOptions`\<`TFeatures`, `TData`\>

### selector? {#selector}

(`state`) => `TSelected`

## Returns {#returns}

[`ReactTable`](../type-aliases/ReactTable.md)\<`TFeatures`, `TData`, `TSelected`\>

## Example {#example}

```tsx
const table = useTable(
  {
    features,
    columns,
    data,
  },
  (state) => ({ pagination: state.pagination }),
)

table.state.pagination
```
