---
id: column_getToggleSortingHandler
title: column_getToggleSortingHandler
---

```ts
function column_getToggleSortingHandler<TFeatures, TData, TValue>(column): (e) => void;
```

定義元: [features/row-sorting/rowSortingFeature.utils.ts:534](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.utils.ts#L534)

この列のソートを切り替える、ヘッダーのイベントハンドラーを作成します。

列がソートできない場合、ハンドラーはイベントを無視します。また、そのイベントを複数列ソートに加えるべきかどうかを `options.isMultiSortEvent` に問い合わせます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### column {#column}

[`Column_Internal`](../../index/interfaces/Column_Internal.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

(`e`) => `void`

## 例 {#example}

```ts
const onClick = column_getToggleSortingHandler(column)
```
