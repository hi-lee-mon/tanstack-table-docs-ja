---
id: table_getIsAllRowsSelected
title: table_getIsAllRowsSelected
---

```ts
function table_getIsAllRowsSelected<TFeatures, TData>(table): boolean;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:358](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L358)

フィルタリング後の選択可能な行が、すべて選択されているかどうかを判定します。

フィルタリング後の行がない場合や、選択の状態が空の場合は false です。祖先が `enableSubRowSelection` で子孫への連鎖を禁止しているサブ行は無視します。これは `table_toggleAllRowsSelected` が選択する行と同じです。

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
const allSelected = table_getIsAllRowsSelected(table)
```
