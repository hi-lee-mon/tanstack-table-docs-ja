---
id: table_setColumnFilters
title: table_setColumnFilters
---

```ts
function table_setColumnFilters<TFeatures, TData>(table, updater): void;
```

定義元: [features/column-filtering/columnFilteringFeature.utils.ts:283](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.utils.ts#L283)

列フィルターのアップデーターを、テーブルのフィルターの変更ハンドラーに通します。

解決したフィルターは、通知する前に片付けられます。既知の列のフィルターは、フィルター関数がその値を自動で取り除くべきと判断した場合に取り除かれます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### updater {#updater}

[`Updater`](../../index/type-aliases/Updater.md)\<[`ColumnFiltersState`](../../index/type-aliases/ColumnFiltersState.md)\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setColumnFilters(table, (old) => old.filter((filter) => filter.id !== 'age'))
```
