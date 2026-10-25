---
id: table_toggleAllRowsSelected
title: table_toggleAllRowsSelected
---

```ts
function table_toggleAllRowsSelected<TFeatures, TData>(
   table,
   value?,
   opts?): void;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:104](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L104)

グループ化の前の、選択可能なすべての行を選択または選択解除します。

`value` を省略すると、`table_getIsAllRowsSelected(table)` の結果をもとに切り替えます。
選択するときは、祖先が `enableSubRowSelection` で子孫への連鎖を禁止しているサブ行を飛ばします。選択解除するときは、既存の選択のマップから該当する選択可能な ID を取り除きます。選択できない行は、`opts.deselectAll` が `true` でない限り選択が残ります。

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
table_toggleAllRowsSelected(table)
```
