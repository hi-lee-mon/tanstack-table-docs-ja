---
id: FacetedUniqueValuesFactory
title: FacetedUniqueValuesFactory
---

```ts
type FacetedUniqueValuesFactory<TData> = (table, columnId) => () => Map<any, number>;
```

Defined in: [src/useLegacyTable.ts:200](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L200)

Faceted unique values factory function type from v8 API

## Type Parameters {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## Parameters {#parameters}

### table {#table}

`Table`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md), `TData`\>

### columnId {#columnid}

`string`

## Returns {#returns}

() => `Map`\<`any`, `number`\>
