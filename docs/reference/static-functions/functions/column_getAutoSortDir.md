---
id: column_getAutoSortDir
title: column_getAutoSortDir
---

```ts
function column_getAutoSortDir<TFeatures, TData, TValue>(column): "asc" | "desc";
```

定義元: [features/row-sorting/rowSortingFeature.utils.ts:183](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.utils.ts#L183)

フィルタリング後の行から抜き出した値をもとに、既定の最初のソートの向きを選びます。

抜き出した行の中で、最初の null でも undefined でもない値で決まります。文字列の列は、アルファベット順が自然になるよう昇順から始まります。それ以外の型の値（または null や undefined でない値が見つからない列）は降順から始まります。
先頭の null や undefined の値を飛ばして抜き出すので、ソートやデータの差し替えで空の値が最初の行に来ても、切り替えの流れは変わりません。

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
const direction = column_getAutoSortDir(column)
```
