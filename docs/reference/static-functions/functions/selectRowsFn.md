---
id: selectRowsFn
title: selectRowsFn
---

```ts
function selectRowsFn<TFeatures, TData>(rowModel, table): RowModel<TFeatures, TData>;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:965](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L965)

現在の行選択の状態で選択されている行を含む、行モデルを作ります。

結果は渡された行モデルから導き出すので、選択された ID のうち、その行モデルにないものは行として作られません。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### rowModel {#rowmodel}

[`RowModel`](../../index/interfaces/RowModel.md)\<`TFeatures`, `TData`\>

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`RowModel`](../../index/interfaces/RowModel.md)\<`TFeatures`, `TData`\>

## 例 {#example}

```ts
const selectedRows = selectRowsFn(rowModel)
```
