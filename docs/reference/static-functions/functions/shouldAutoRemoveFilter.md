---
id: shouldAutoRemoveFilter
title: shouldAutoRemoveFilter
---

```ts
function shouldAutoRemoveFilter<TFeatures, TData, TValue>(
   filterFn?,
   value?,
   column?): boolean;
```

定義元: [features/column-filtering/columnFilteringFeature.utils.ts:348](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.utils.ts#L348)

フィルター値をフィルターの状態から取り除くべきかどうかを返します。

`undefined` は常に取り除かれます。これは、`setFilterValue(undefined)` や関数のアップデーターで使う、すべてに共通の「このフィルターを解除する」という目印です。
それ以外の値では、フィルター関数の `autoRemove` フックがあればそれが優先されます。そのため、カスタムのフィルター関数は、既定の判定なら捨てられる値（空文字列など）を残せます。`autoRemove` フックがなければ、空文字列は取り除かれます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### filterFn? {#filterfn}

[`FilterFn`](../../index/interfaces/FilterFn.md)\<`TFeatures`, `TData`\>

### value? {#value}

`any`

### column? {#column}

[`Column_Internal`](../../index/interfaces/Column_Internal.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const removeFilter = shouldAutoRemoveFilter(filterFn, value, column)
```
