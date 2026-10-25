---
id: table_getSelectedCellRangesData
title: table_getSelectedCellRangesData
---

```ts
function table_getSelectedCellRangesData<TFeatures, TData>(table): unknown[][][];
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:1206](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L1206)

最終的な選択の各領域の値を、行優先のグリッドとして返します。

これはクリップボードへの書き出しの素材です。テキストに変換する処理は利用者側に任せています。区切り文字、null の表し方、区切り文字を含む値を引用符で囲むかどうかは、どれもアプリケーションが決めることだからです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`unknown`[][][]

## 例 {#example}

```ts
const [firstRange] = table_getSelectedCellRangesData(table)
```
