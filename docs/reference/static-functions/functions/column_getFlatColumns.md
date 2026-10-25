---
id: column_getFlatColumns
title: column_getFlatColumns
---

```ts
function column_getFlatColumns<TFeatures, TData, TValue>(column): Column<TFeatures, TData, TValue>[];
```

定義元: [core/columns/coreColumnsFeature.utils.ts:25](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.utils.ts#L25)

この列と、その子孫の列すべてを1つの配列に平坦化します。

グループ列は、その子の列より前に来ます。これは、テーブルを作るときに作られる正規化された列の階層と同じ順です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### column {#column}

[`Column`](../../index/type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

[`Column`](../../index/type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>[]

## 例 {#example}

```ts
const flatColumns = column_getFlatColumns(column)
```
