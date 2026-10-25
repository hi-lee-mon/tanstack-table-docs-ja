---
id: table_getPreSelectedRowModel
title: table_getPreSelectedRowModel
---

```ts
function table_getPreSelectedRowModel<TFeatures, TData>(table): RowModel<TFeatures, TData>;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:220](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L220)

行選択を選択された行に反映する前の行モデルを読み取ります。

選択は行の基本のパイプラインを変えないので、これはコア行モデルを返します。

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
const rowsBeforeSelection = table_getPreSelectedRowModel(table)
```
