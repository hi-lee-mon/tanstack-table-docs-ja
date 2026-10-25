---
id: row_getVisibleCellsByColumnId
title: row_getVisibleCellsByColumnId
---

```ts
function row_getVisibleCellsByColumnId<TFeatures, TData>(row): Record<string, Cell<TFeatures, TData, unknown>>;
```

定義元: [features/column-visibility/columnVisibilityFeature.utils.ts:196](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.utils.ts#L196)

この行の表示中のセルを、列 ID をキーにして引けるマップにします。

非表示の列はマップに含まれません。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`Record`\<`string`, [`Cell`](../../index/type-aliases/Cell.md)\<`TFeatures`, `TData`, `unknown`\>\>

## 例 {#example}

```ts
const visibleCellsById = row_getVisibleCellsByColumnId(row)
```
