---
id: table_getRowId
title: table_getRowId
---

```ts
function table_getRowId<TFeatures, TData>(
   originalRow,
   table,
   index,
   parent?): string;
```

定義元: [core/rows/coreRowsFeature.utils.ts:295](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.utils.ts#L295)

行の、変わらない ID を求めます。

`options.getRowId` を渡した場合は、そちらが優先されます。そうでなければ、ルートの行はインデックスを使い、子の行は親の ID に自分のインデックスを付け足します（`0.2` など）。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### originalRow {#originalrow}

`TData`

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### index {#index}

`number`

### parent? {#parent}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`string`

## 例 {#example}

```ts
const id = table_getRowId(originalRow, table, index, parentRow)
```
