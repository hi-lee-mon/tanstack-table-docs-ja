---
id: cell_getIsPlaceholder
title: cell_getIsPlaceholder
---

```ts
function cell_getIsPlaceholder<TFeatures, TData, TValue>(cell): boolean;
```

定義元: [features/column-grouping/columnGroupingFeature.utils.ts:265](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.utils.ts#L265)

このセルがグループ化によって隠されたプレースホルダーかどうかを判定します。

プレースホルダーのセルは、グループ化された列のうち、その行のアクティブなグループ化の列以外に属するセルです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### cell {#cell}

[`Cell`](../../index/type-aliases/Cell.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const isPlaceholder = cell_getIsPlaceholder(cell)
```
