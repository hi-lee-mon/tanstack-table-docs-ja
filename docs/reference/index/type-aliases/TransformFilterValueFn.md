---
id: TransformFilterValueFn
title: TransformFilterValueFn
---

```ts
type TransformFilterValueFn<TFeatures, TData, TValue> = (value, column?) => TValue;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:138](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L138)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](CellData.md) = [`CellData`](CellData.md)

## パラメーター {#parameters}

### value {#value}

`any`

### column? {#column}

[`Column`](Column.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

`TValue`
