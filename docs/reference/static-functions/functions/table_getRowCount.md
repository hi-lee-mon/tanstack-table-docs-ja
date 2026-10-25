---
id: table_getRowCount
title: table_getRowCount
---

```ts
function table_getRowCount<TFeatures, TData>(table): number;
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:432](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L432)

ページネーションの計算に使う総行数を求めます。

手動のページネーションでは `options.rowCount` が優先されます。そうでなければ、ページ分割前の行モデルから数えるので、ページを切り出す前のフィルタリング、グループ化、ソート、展開が反映されます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`number`

## 例 {#example}

```ts
const rows = table_getRowCount(table)
```
