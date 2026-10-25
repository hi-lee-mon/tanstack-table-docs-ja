---
id: table_getToggleAllRowsExpandedHandler
title: table_getToggleAllRowsExpandedHandler
---

```ts
function table_getToggleAllRowsExpandedHandler<TFeatures, TData>(table): (_e) => void;
```

定義元: [features/row-expanding/rowExpandingFeature.utils.ts:167](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.utils.ts#L167)

すべての行の展開を切り替えるイベントハンドラーを作成します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

(`_e`) => `void`

## 例 {#example}

```ts
const onClick = table_getToggleAllRowsExpandedHandler(table)
```
