---
id: column_toggleSorting
title: column_toggleSorting
---

```ts
function column_toggleSorting<TFeatures, TData, TValue>(
   column,
   desc?,
   multi?): void;
```

定義元: [features/row-sorting/rowSortingFeature.utils.ts:254](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.utils.ts#L254)

この列について、次のソートの状態を適用します。

切り替えによって、この列のソートのエントリーが追加、置き換え、反転、削除のいずれかになります。複数列ソートは、`enableMultiSort`、`enableMultiRemove`、`maxMultiSortColCount`、引数の `multi` に従います。

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

### desc? {#desc}

`boolean`

### multi? {#multi}

`boolean`

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
column_toggleSorting(column, undefined, true)
```
