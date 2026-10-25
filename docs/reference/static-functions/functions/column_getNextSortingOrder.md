---
id: column_getNextSortingOrder
title: column_getNextSortingOrder
---

```ts
function column_getNextSortingOrder<TFeatures, TData, TValue>(column, multi?): false | "asc" | "desc";
```

定義元: [features/row-sorting/rowSortingFeature.utils.ts:391](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.utils.ts#L391)

この列の切り替えの流れで、次のソート順を求めます。

流れは最初のソートの向きから始まり、`asc` と `desc` を行き来します。ソートを外すことが有効なら `false` を返すこともあります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### column {#column}

[`Column_Internal`](../../index/interfaces/Column_Internal.md)\<`TFeatures`, `TData`, `TValue`\>

### multi? {#multi}

`boolean`

## 戻り値 {#returns}

`false` \| `"asc"` \| `"desc"`

## 例 {#example}

```ts
const nextOrder = column_getNextSortingOrder(column)
```
