---
id: table_getCellSelectionMergeBounds
title: table_getCellSelectionMergeBounds
---

```ts
function table_getCellSelectionMergeBounds<TFeatures, TData>(table): CellSelectionBounds[];
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:231](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L231)

描画中の行に含まれる結合セルの長方形を、選択自身のインデックスの座標に変換します。

結合インデックスはページ分割後の描画順で行の位置を決め、選択はページ分割前の表示順で行の位置を決めます。そのため、各結合は `row.getDisplayIndex()` を通して変換されます。
行が連続した表示範囲に対応しない結合は、念のため読み飛ばします。その場合は、形を壊さずに、結合していないセルと同じように振る舞います。

`cellSpanningFeature` が登録されていなければ空の配列を返します。これにより、選択の処理はどの経路でも、結合を考えない場合とまったく同じになります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`CellSelectionBounds`](../../index/interfaces/CellSelectionBounds.md)[]

## 例 {#example}

```ts
const merges = table_getCellSelectionMergeBounds(table)
```
