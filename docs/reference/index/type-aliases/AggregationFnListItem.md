---
id: AggregationFnListItem
title: AggregationFnListItem
---

```ts
type AggregationFnListItem<TFeatures, TData, TValue> =
  | "auto"
  | ExtractAggregationFnKeys<TFeatures>
| AggregationFnDescriptor<TFeatures, TData, TValue, any>;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:127](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L127)

複数の結果を返す集計オプションの、名前付き、または明示的にキーを付けたエントリーの1つです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` = `unknown`
