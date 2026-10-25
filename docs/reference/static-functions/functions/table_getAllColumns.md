---
id: table_getAllColumns
title: table_getAllColumns
---

```ts
function table_getAllColumns<TFeatures, TData>(table): Column<TFeatures, TData, unknown>[];
```

定義元: [core/columns/coreColumnsFeature.utils.ts:151](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.utils.ts#L151)

`options.columns` を、テーブルの入れ子の列ツリーに正規化します。

各列定義は親と深さを付けて作られ、グループ列の子は再帰的に作られます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`Column`](../../index/type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

## 例 {#example}

```ts
const columns = table_getAllColumns(table)
```
