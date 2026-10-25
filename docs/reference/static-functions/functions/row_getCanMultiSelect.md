---
id: row_getCanMultiSelect
title: row_getCanMultiSelect
---

```ts
function row_getCanMultiSelect<TFeatures, TData>(row): boolean;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:670](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L670)

この行を他の行と一緒に選択できるかどうかを判定します。

`options.enableMultiRowSelection` には、真偽値か行の述語関数を指定できます。既定値は `true` です。

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
const canMultiSelect = row_getCanMultiSelect(row)
```
