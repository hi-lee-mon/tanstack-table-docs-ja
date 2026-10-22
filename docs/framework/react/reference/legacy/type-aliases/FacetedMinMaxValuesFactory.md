---
id: FacetedMinMaxValuesFactory
title: FacetedMinMaxValuesFactory
---

```ts
type FacetedMinMaxValuesFactory<TData> = (table, columnId) => () => undefined | [number, number];
```

Defined in: [src/useLegacyTable.ts:192](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L192)

Faceted min/max values factory function type from v8 API

## Type Parameters {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## Parameters {#parameters}

### table {#table}

`Table`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md), `TData`\>

### columnId {#columnid}

`string`

## Returns {#returns}

() => `undefined` \| \[`number`, `number`\]
