---
id: column_getAutoSortFn
title: column_getAutoSortFn
---

```ts
function column_getAutoSortFn<TFeatures, TData, TValue>(column): SortFn<TFeatures, TData>;
```

定義元: [features/row-sorting/rowSortingFeature.utils.ts:110](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.utils.ts#L110)

フィルタリング後の行から抜き出した値をもとに、組み込みのソート関数を選びます。

日付のような値には `datetime`、テキストと数値が混ざった文字列には `alphanumeric`、ふつうの文字列には `text` を使い、不明な値には `basic` を使います。

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

[`SortFn`](../../index/interfaces/SortFn.md)\<`TFeatures`, `TData`\>

## 例 {#example}

```ts
const sortFn = column_getAutoSortFn(column)
```
