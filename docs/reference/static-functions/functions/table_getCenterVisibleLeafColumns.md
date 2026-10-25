---
id: table_getCenterVisibleLeafColumns
title: table_getCenterVisibleLeafColumns
---

```ts
function table_getCenterVisibleLeafColumns<TFeatures, TData>(table): Column<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:842](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L842)

固定されていない表示中の末端の列を求めます。

これは、固定された列をスクロールする中央の領域と分けて描画するレイアウトで使う、中央の区分です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`Column`](../../index/type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

## 例 {#example}

```ts
const columns = table_getCenterVisibleLeafColumns(table)
```
