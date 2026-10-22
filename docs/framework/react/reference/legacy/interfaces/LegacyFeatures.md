---
id: LegacyFeatures
title: LegacyFeatures
---

定義元: [src/useLegacyTable.ts:168](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L168)

`useLegacyTable` が登録する機能のセットです。

標準機能に、組み込みのフィルター・ソート・集計のレジストリを加えたものです。
これにより、列定義で `'mean'` や `'includesString'` のような
v8 の文字列の識別子を指定できます。

## 継承元 {#extends}

- `StockFeatures`

## プロパティ {#properties}

### aggregationFns {#aggregationfns}

```ts
aggregationFns: object;
```

定義元: [src/useLegacyTable.ts:169](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L169)

#### range {#range}

```ts
range: AggregationFnDef<TableFeatures, RowData, unknown, number>;
```

***

### filterFns {#filterfns}

```ts
filterFns: object;
```

定義元: [src/useLegacyTable.ts:170](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L170)

#### startsWithLetter {#startswithletter}

```ts
startsWithLetter: FilterFn<TableFeatures, RowData>;
```

***

### sortFns {#sortfns}

```ts
sortFns: object;
```

定義元: [src/useLegacyTable.ts:171](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L171)

#### byNameLength {#bynamelength}

```ts
byNameLength: SortFn<TableFeatures, RowData>;
```
