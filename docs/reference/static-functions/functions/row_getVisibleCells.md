---
id: row_getVisibleCells
title: row_getVisibleCells
---

```ts
function row_getVisibleCells<TFeatures, TData>(row): Cell<TFeatures, TData, unknown>[];
```

定義元: [features/column-visibility/columnVisibilityFeature.utils.ts:160](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.utils.ts#L160)

この行のセルのうち、列が表示されているものを集めます。

列の固定が有効な場合、結果は先頭に固定されたセル、中央のセル、末尾に固定されたセルの順に並びます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`Cell`](../../index/type-aliases/Cell.md)\<`TFeatures`, `TData`, `unknown`\>[]

## 例 {#example}

```ts
const visibleCells = row_getVisibleCells(row)
```
