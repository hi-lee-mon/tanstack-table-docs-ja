---
id: column_clearSorting
title: column_clearSorting
---

```ts
function column_clearSorting<TFeatures, TData, TValue>(column): void;
```

定義元: [features/row-sorting/rowSortingFeature.utils.ts:512](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.utils.ts#L512)

この列をソートの状態から取り除きます。

他のソートされた列は、互いの順序も含めて保たれます。

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

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
column_clearSorting(column)
```
