---
id: row_getCanSelectSubRows
title: row_getCanSelectSubRows
---

```ts
function row_getCanSelectSubRows<TFeatures, TData>(row): boolean;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:647](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L647)

この行を選択したときに、そのサブ行も選択するかどうかを判定します。

`options.enableSubRowSelection` には、真偽値か行の述語関数を指定できます。既定値は `true` です。

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
const canSelectChildren = row_getCanSelectSubRows(row)
```
