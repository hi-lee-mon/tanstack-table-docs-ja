---
id: buildHeaderGroups
title: buildHeaderGroups
---

```ts
function buildHeaderGroups<TFeatures, TData, TValue>(
   allColumns,
   columnsToGroup,
   table,
   headerFamily?): HeaderGroup<TFeatures, TData>[];
```

定義元: [core/headers/buildHeaderGroups.ts:227](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/buildHeaderGroups.ts#L227)

テーブルの入れ子になったヘッダーグループの構造を組み立てます。

結果には、表示中の末端の列、固定された列グループ、多段ヘッダーの描画に必要なプレースホルダーのヘッダーが反映されます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### allColumns {#allcolumns}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>[]

### columnsToGroup {#columnstogroup}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>[]

### table {#table}

[`Table_Internal`](../interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### headerFamily? {#headerfamily}

`"start"` \| `"end"` \| `"center"`

## 戻り値 {#returns}

[`HeaderGroup`](../interfaces/HeaderGroup.md)\<`TFeatures`, `TData`\>[]
