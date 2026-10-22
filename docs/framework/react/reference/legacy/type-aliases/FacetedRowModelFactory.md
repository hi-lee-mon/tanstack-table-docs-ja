---
id: FacetedRowModelFactory
title: FacetedRowModelFactory
---

```ts
type FacetedRowModelFactory<TData> = (table, columnId) => () => RowModel<LegacyFeatures, TData>;
```

Defined in: [src/useLegacyTable.ts:184](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L184)

Faceted row model factory function type from v8 API

## Type Parameters {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## Parameters {#parameters}

### table {#table}

`Table`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md), `TData`\>

### columnId {#columnid}

`string`

## Returns {#returns}

() => `RowModel`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md), `TData`\>
