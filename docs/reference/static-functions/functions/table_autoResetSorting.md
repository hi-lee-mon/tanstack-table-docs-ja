---
id: table_autoResetSorting
title: table_autoResetSorting
---

```ts
function table_autoResetSorting<TFeatures, TData>(table): void;
```

定義元: [features/row-sorting/rowSortingFeature.utils.ts:83](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.utils.ts#L83)

明示的に有効にした場合、テーブルのデータが変わったあとにソートをリセットします。

他の自動リセットの動作と違い、ソートは既定で保たれます。`autoResetAll` を明示的に指定した場合は、`autoResetSorting` より優先されます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_autoResetSorting(table)
```
