---
id: column_getToggleGroupingHandler
title: column_getToggleGroupingHandler
---

```ts
function column_getToggleGroupingHandler<TFeatures, TData, TValue>(column): () => void;
```

定義元: [features/column-grouping/columnGroupingFeature.utils.ts:124](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.utils.ts#L124)

この列のグループ化を切り替える、ヘッダーや操作部品向けのハンドラーを作成します。

`column_getCanGroup(column)` が false の場合、ハンドラーは何もしません。

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

() => `void`

## 例 {#example}

```ts
const onClick = column_getToggleGroupingHandler(column)
```
