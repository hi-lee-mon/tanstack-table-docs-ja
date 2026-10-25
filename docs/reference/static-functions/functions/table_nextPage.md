---
id: table_nextPage
title: table_nextPage
---

```ts
function table_nextPage<TFeatures, TData>(table): void;
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:340](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L340)

テーブルを次のページに移動します。

ページネーションの状態の持ち主とアップデーターの意味を一貫させるため、`table_setPageIndex` に処理を任せます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_nextPage(table)
```
