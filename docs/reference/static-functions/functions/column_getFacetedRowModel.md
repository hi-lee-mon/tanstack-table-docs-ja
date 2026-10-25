---
id: column_getFacetedRowModel
title: column_getFacetedRowModel
---

```ts
function column_getFacetedRowModel<TFeatures, TData, TValue>(column, table): RowModel<TFeatures, TData>;
```

定義元: [features/column-faceting/columnFacetingFeature.utils.ts:52](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.utils.ts#L52)

1つの列のファセット値を導き出すための行モデルを計算します。

ファセット行モデルは、ふつう、この列自身のフィルターを除いた、他のすべての有効なフィルターを適用します。ファクトリーが登録されていなければ、フィルタリング前の行モデルを返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### column {#column}

  \| [`Column_Internal`](../../index/interfaces/Column_Internal.md)\<`TFeatures`, `TData`, `TValue`\>
  \| `undefined`

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`RowModel`](../../index/interfaces/RowModel.md)\<`TFeatures`, `TData`\>

## 例 {#example}

```ts
const rows = column_getFacetedRowModel(column, table)
```
