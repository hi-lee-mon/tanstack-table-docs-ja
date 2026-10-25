---
id: row_getIsSomeSelected
title: row_getIsSomeSelected
---

```ts
function row_getIsSomeSelected<TFeatures, TData>(row): boolean;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:589](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L589)

選択可能な子孫が、すべてではなく一部だけ選択されているかどうかを判定します。

親の行で、中間状態（indeterminate）の選択の UI を表示するために使えます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const partial = row_getIsSomeSelected(row)
```
