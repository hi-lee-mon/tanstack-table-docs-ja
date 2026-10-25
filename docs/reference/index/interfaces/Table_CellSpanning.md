---
id: Table_CellSpanning
title: Table_CellSpanning
---

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:166](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L166)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getCellSpanIndex {#getcellspanindex}

```ts
getCellSpanIndex: () => CellSpanIndex<TFeatures, TData>;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:173](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L173)

現在描画されている行についての、メモ化された結合インデックスです。

#### 戻り値 {#returns}

[`CellSpanIndex`](CellSpanIndex.md)\<`TFeatures`, `TData`\>
