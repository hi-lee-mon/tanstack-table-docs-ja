---
id: column_getCanSpan
title: column_getCanSpan
---

```ts
function column_getCanSpan<TFeatures, TData, TValue>(column): boolean;
```

定義元: [features/cell-spanning/cellSpanningFeature.utils.ts:126](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.utils.ts#L126)

この列がセル結合の対象かどうかを判定します。

列定義で `enableCellSpanning: false` にして対象から外した場合は、テーブルのオプションより優先されます。他の列ごとの有効化フラグと同じ決まり方です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### column {#column}

[`Column`](../../index/type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const canSpan = column_getCanSpan(column)
```
