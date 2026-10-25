---
id: row_getDisplayIndex
title: row_getDisplayIndex
---

```ts
function row_getDisplayIndex<TFeatures, TData>(row): number;
```

定義元: [core/rows/coreRowsFeature.utils.ts:14](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.utils.ts#L14)

現在のページネーション前の行モデルにおける、この行の0始まりの位置を返します。その行モデルに含まれない行は `-1` を返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`number`
