---
id: table_getGlobalFacetedRowModel
title: table_getGlobalFacetedRowModel
---

```ts
function table_getGlobalFacetedRowModel<TFeatures, TData>(table): RowModel<TFeatures, TData>;
```

定義元: [features/column-faceting/columnFacetingFeature.utils.ts:151](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.utils.ts#L151)

グローバルなファセット値を導き出すための行モデルを計算します。

グローバルの対象は、内部の列 ID `__global__` で要求します。ファセット行モデルのファクトリーが登録されていなければ、フィルタリング前の行モデルを返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`RowModel`](../../index/interfaces/RowModel.md)\<`TFeatures`, `TData`\>

## 例 {#example}

```ts
const rows = table_getGlobalFacetedRowModel(table)
```
