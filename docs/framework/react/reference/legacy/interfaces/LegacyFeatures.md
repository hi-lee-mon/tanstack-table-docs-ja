---
id: LegacyFeatures
title: LegacyFeatures
---

Defined in: [src/useLegacyTable.ts:168](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L168)

Feature set registered by `useLegacyTable`.

Extends the stock features with the built-in filter, sort, and aggregation
registries so column definitions accept the v8 string identifiers such as
`'mean'` and `'includesString'`.

## Extends {#extends}

- `StockFeatures`

## Properties {#properties}

### aggregationFns {#aggregationfns}

```ts
aggregationFns: object;
```

Defined in: [src/useLegacyTable.ts:169](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L169)

#### range {#range}

```ts
range: AggregationFnDef<TableFeatures, RowData, unknown, number>;
```

***

### filterFns {#filterfns}

```ts
filterFns: object;
```

Defined in: [src/useLegacyTable.ts:170](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L170)

#### startsWithLetter {#startswithletter}

```ts
startsWithLetter: FilterFn<TableFeatures, RowData>;
```

***

### sortFns {#sortfns}

```ts
sortFns: object;
```

Defined in: [src/useLegacyTable.ts:171](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L171)

#### byNameLength {#bynamelength}

```ts
byNameLength: SortFn<TableFeatures, RowData>;
```
