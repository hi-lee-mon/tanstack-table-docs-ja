---
id: RowModelFactory
title: RowModelFactory
---

```ts
type RowModelFactory<TData> = (table) => () => RowModel<LegacyFeatures, TData>;
```

Defined in: [src/useLegacyTable.ts:177](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L177)

Row model factory function type from v8 API

## Type Parameters {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## Parameters {#parameters}

### table {#table}

`Table`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md), `TData`\>

## Returns {#returns}

() => `RowModel`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md), `TData`\>
