---
id: aggregationFns
title: aggregationFns
---

```ts
const aggregationFns: object;
```

定義元: [features/row-aggregation/aggregationFns.ts:387](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/aggregationFns.ts#L387)

組み込みのレジストリ全体です。ツリーシェイキングのためには、定義を個別に登録してください。

## 型宣言 {#type-declaration}

### ~~count~~ {#count}

```ts
count: AggregationFnDef<any, any, unknown, number> = aggregationFn_count;
```

### ~~extent~~ {#extent}

```ts
extent: AggregationFnDef<any, any, unknown, [RangeValue | undefined, RangeValue | undefined]> = aggregationFn_extent;
```

### ~~first~~ {#first}

```ts
first: AggregationFnDef<any, any, unknown, unknown> = aggregationFn_first;
```

### ~~last~~ {#last}

```ts
last: AggregationFnDef<any, any, unknown, unknown> = aggregationFn_last;
```

### ~~max~~ {#max}

```ts
max: AggregationFnDef<any, any, unknown, RangeValue | undefined> = aggregationFn_max;
```

### ~~mean~~ {#mean}

```ts
mean: AggregationFnDef<any, any, unknown, number | undefined> = aggregationFn_mean;
```

### ~~median~~ {#median}

```ts
median: AggregationFnDef<any, any, unknown, number | undefined> = aggregationFn_median;
```

### ~~min~~ {#min}

```ts
min: AggregationFnDef<any, any, unknown, RangeValue | undefined> = aggregationFn_min;
```

### ~~sum~~ {#sum}

```ts
sum: AggregationFnDef<any, any, unknown, number> = aggregationFn_sum;
```

### ~~unique~~ {#unique}

```ts
unique: AggregationFnDef<any, any, unknown, unknown[]> = aggregationFn_unique;
```

### ~~uniqueCount~~ {#uniquecount}

```ts
uniqueCount: AggregationFnDef<any, any, unknown, number> = aggregationFn_uniqueCount;
```

## 非推奨 {#deprecated}

バンドルを小さくするには、代わりに `aggregationFn_*` の定義を個別に import してください。このレジストリは互換性のために残されています。
