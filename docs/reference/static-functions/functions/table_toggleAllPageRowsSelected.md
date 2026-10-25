---
id: table_toggleAllPageRowsSelected
title: table_toggleAllPageRowsSelected
---

```ts
function table_toggleAllPageRowsSelected<TFeatures, TData>(
   table,
   value?,
   opts?): void;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:164](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L164)

現在のページにある選択可能な行を、すべて選択または選択解除します。

`value` を省略すると、`table_getIsAllPageRowsSelected(table)` の結果をもとに切り替えます。サブ行の選択が許可されていれば、子の行も含めます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### value? {#value}

`boolean`

### opts? {#opts}

#### deselectAll? {#deselectall}

`boolean`

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_toggleAllPageRowsSelected(table)
```
