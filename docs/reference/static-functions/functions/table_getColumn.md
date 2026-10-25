---
id: table_getColumn
title: table_getColumn
---

```ts
function table_getColumn<TFeatures, TData>(table, columnId):
  | Column<TFeatures, TData, unknown>
  | undefined;
```

定義元: [core/columns/coreColumnsFeature.utils.ts:266](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.utils.ts#L266)

平坦化した列のマップから、ID で列を探します。

グループ列と末端の列のどちらも返りえます。開発環境では、ID が見つからないと警告を出し、古くなった列の参照に気づけるようにします。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### columnId {#columnid}

`string`

## 戻り値 {#returns}

  \| [`Column`](../../index/type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>
  \| `undefined`

## 例 {#example}

```ts
const column = table_getColumn(table, 'firstName')
```
