---
id: column_getAutoFilterFn
title: column_getAutoFilterFn
---

```ts
function column_getAutoFilterFn<TFeatures, TData, TValue>(column):
  | FilterFn<TFeatures, TData>
  | undefined;
```

定義元: [features/column-filtering/columnFilteringFeature.utils.ts:47](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.utils.ts#L47)

列の最初のコア行の値から、組み込みのフィルター関数を選びます。

文字列には `includesString`、数値には `inNumberRange`、真偽値とオブジェクトには `equals`、日付には `inDateRange`、配列には `arrIncludes` を使い、不明な値には `weakEquals` を使います。

選んだフィルター関数は、テーブルの `filterFns` レジストリから探します。そこに登録されていなければ、別のフィルター関数で代用せず `undefined` を返し、開発環境では警告を出します。

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

  \| [`FilterFn`](../../index/interfaces/FilterFn.md)\<`TFeatures`, `TData`\>
  \| `undefined`

## 例 {#example}

```ts
const filterFn = column_getAutoFilterFn(column)
```
