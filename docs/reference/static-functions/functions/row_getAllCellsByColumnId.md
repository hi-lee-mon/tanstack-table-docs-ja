---
id: row_getAllCellsByColumnId
title: row_getAllCellsByColumnId
---

```ts
function row_getAllCellsByColumnId<TFeatures, TData>(row): Record<string, Cell<TFeatures, TData, unknown>>;
```

定義元: [core/rows/coreRowsFeature.utils.ts:271](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.utils.ts#L271)

この行のセルを、列 ID をキーにして引けるマップにします。

これは `row.getAllCellsByColumnId()` の裏にある静的な実装です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`Record`\<`string`, [`Cell`](../../index/type-aliases/Cell.md)\<`TFeatures`, `TData`, `unknown`\>\>

## 例 {#example}

```ts
const cellsById = row_getAllCellsByColumnId(row)
```
