---
id: column_toggleGrouping
title: column_toggleGrouping
---

```ts
function column_toggleGrouping<TFeatures, TData, TValue>(column): void;
```

定義元: [features/column-grouping/columnGroupingFeature.utils.ts:39](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.utils.ts#L39)

この列 ID をグループ化の状態に追加、または状態から削除します。

既存のグループ化された列は順序を保ちます。すでに `state.grouping` にある列は削除され、なければ末尾に追加されます。

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
column_toggleGrouping(column)
```
