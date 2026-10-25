---
id: column_getFirstSortDir
title: column_getFirstSortDir
---

```ts
function column_getFirstSortDir<TFeatures, TData, TValue>(column): "asc" | "desc";
```

定義元: [features/row-sorting/rowSortingFeature.utils.ts:368](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.utils.ts#L368)

この列のソートを始めるときに最初に使う向きを決めます。

列の `sortDescFirst`、テーブルの `sortDescFirst`、抜き出した値から推論した自動の向きの順に優先されます。

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

`"asc"` \| `"desc"`

## 例 {#example}

```ts
const firstDirection = column_getFirstSortDir(column)
```
