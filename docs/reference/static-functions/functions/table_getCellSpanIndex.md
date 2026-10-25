---
id: table_getCellSpanIndex
title: table_getCellSpanIndex
---

```ts
function table_getCellSpanIndex<TFeatures, TData>(table): CellSpanIndex<TFeatures, TData>;
```

定義元: [features/cell-spanning/cellSpanningFeature.utils.ts:152](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.utils.ts#L152)

現在描画されている行について、テーブルのセル結合インデックスを作ります。

結合は常に最終的な行モデルから一から導き出されるので、ソート、フィルタリング、ページネーション、展開、行の固定で変わるのは隣り合う関係だけで、インデックスはそれに従います。保存するものも、設定するものもありません。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`CellSpanIndex`](../../index/interfaces/CellSpanIndex.md)\<`TFeatures`, `TData`\>

## 例 {#example}

```ts
const spanIndex = table_getCellSpanIndex(table)
```
