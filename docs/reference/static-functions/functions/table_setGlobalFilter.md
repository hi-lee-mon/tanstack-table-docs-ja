---
id: table_setGlobalFilter
title: table_setGlobalFilter
---

```ts
function table_setGlobalFilter<TFeatures, TData>(table, updater): void;
```

定義元: [features/global-filtering/globalFilteringFeature.utils.ts:99](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/global-filtering/globalFilteringFeature.utils.ts#L99)

グローバルフィルターのアップデーターを、テーブルのグローバルフィルターのハンドラーに通します。

アップデーターには、次の値か、前の値を受け取る関数を指定できます。インスタンスの `table.setGlobalFilter` と同じ動作です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### updater {#updater}

`any`

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setGlobalFilter(table, 'search text')
```
