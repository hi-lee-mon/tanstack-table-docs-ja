---
id: constructAggregationFn
title: constructAggregationFn
---

```ts
function constructAggregationFn<TFeatures, TData, TValue, TResult>(definition): AggregationFnDef<TFeatures, TData, TValue, TResult>;
```

定義元: [features/row-aggregation/aggregationFns.ts:10](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/aggregationFns.ts#L10)

列または集計関数のレジストリ向けに、型付きのコンテキストベースの集計定義を作成します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md) = `any`

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

### TValue {#tvalue}

`TValue` = `unknown`

### TResult {#tresult}

`TResult` = `unknown`

## パラメーター {#parameters}

### definition {#definition}

[`AggregationFnDef`](../interfaces/AggregationFnDef.md)\<`TFeatures`, `TData`, `TValue`, `TResult`\>

## 戻り値 {#returns}

[`AggregationFnDef`](../interfaces/AggregationFnDef.md)\<`TFeatures`, `TData`, `TValue`, `TResult`\>
