---
id: table_getIsAllPageRowsSelected
title: table_getIsAllPageRowsSelected
---

```ts
function table_getIsAllPageRowsSelected<TFeatures, TData>(table): boolean;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:398](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L398)

現在のページにある選択可能な行が、すべて選択されているかどうかを判定します。

この計算では、選択できない行と、祖先が `enableSubRowSelection` で子孫への連鎖を禁止しているサブ行を無視します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const allPageRowsSelected = table_getIsAllPageRowsSelected(table)
```
