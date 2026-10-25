---
id: table_getStartTotalSize
title: table_getStartTotalSize
---

```ts
function table_getStartTotalSize<TFeatures, TData>(table): number;
```

定義元: [features/column-sizing/columnSizingFeature.utils.ts:415](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.utils.ts#L415)

論理的な先頭の領域に固定された、表示中の末端の列の幅を合計します。

先頭の固定領域が空なら `0` を返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`number`

## 例 {#example}

```ts
const width = table_getStartTotalSize(table)
```
