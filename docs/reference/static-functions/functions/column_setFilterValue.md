---
id: column_setFilterValue
title: column_setFilterValue
---

```ts
function column_setFilterValue<TFeatures, TData, TValue>(column, value): void;
```

定義元: [features/column-filtering/columnFilteringFeature.utils.ts:234](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.utils.ts#L234)

この列のフィルター値を追加、更新、または削除します。

受け取る値はアップデーターでもかまいません。解決したあと、`autoRemove` の条件によって、フィルターを保存するか取り除くかが決まります。

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

### value {#value}

`any`

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
column_setFilterValue(column, (old) => String(old ?? '').trim())
```
