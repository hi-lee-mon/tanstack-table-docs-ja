---
id: legacyCreateColumnHelper
title: legacyCreateColumnHelper
---

```ts
function legacyCreateColumnHelper<TData>(): ColumnHelper<LegacyFeatures, TData>;
```

Defined in: [src/useLegacyTable.ts:360](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L360)

## Type Parameters {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## Returns {#returns}

`ColumnHelper`\<[`LegacyFeatures`](../interfaces/LegacyFeatures.md), `TData`\>

## Deprecated {#deprecated}

Use `createColumnHelper<TFeatures, TData>()` with useTable instead.

A column helper with LegacyFeatures pre-bound for use with useLegacyTable.
Only requires TData—no need to specify TFeatures.
