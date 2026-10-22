---
id: LegacyReactTable
title: LegacyReactTable
---

```ts
type LegacyReactTable<TData> = ReactTable<LegacyFeatures, TData, TableState<LegacyFeatures>> & object;
```

Defined in: [src/useLegacyTable.ts:290](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L290)

Legacy table instance type that includes the v8-style `getState()` method.

## Type Declaration {#type-declaration}

### ~~getState~~ {#getstate}

```ts
getState: () => TableState<LegacyFeatures>;
```

Returns the current table state.

#### Returns {#returns}

`TableState`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md)\>

#### Deprecated {#deprecated}

In v9, access state directly via `table.state` or use `table.state` for the full state.

### ~~setState~~ {#setstate}

```ts
setState: (state) => void;
```

Sets the current table state.

#### Parameters {#parameters}

##### state {#state}

`TableState`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md)\>

#### Returns {#returns-1}

`void`

#### Deprecated {#deprecated-1}

In v9, access state directly via `table.baseAtoms`

## Type Parameters {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## Deprecated {#deprecated-2}

Use `useTable` with explicit state selection instead.
