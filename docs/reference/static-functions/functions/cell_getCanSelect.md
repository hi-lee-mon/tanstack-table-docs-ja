---
id: cell_getCanSelect
title: cell_getCanSelect
---

```ts
function cell_getCanSelect<TFeatures, TData, TValue>(cell): boolean;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:483](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L483)

このセルが現在選択できるかどうかを判定します。

列定義で `enableCellSelection: false` にして対象から外した場合は、テーブルのオプションより優先されます。他の列ごとの有効化フラグと同じ決まり方です。

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
const canSelect = cell_getCanSelect(cell)
```
