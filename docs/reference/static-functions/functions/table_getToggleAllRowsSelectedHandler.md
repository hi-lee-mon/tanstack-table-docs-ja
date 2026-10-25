---
id: table_getToggleAllRowsSelectedHandler
title: table_getToggleAllRowsSelectedHandler
---

```ts
function table_getToggleAllRowsSelectedHandler<TFeatures, TData>(table): (e) => void;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:480](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L480)

すべての行を選択または選択解除する、チェックボックス用のハンドラーを作成します。

ハンドラーは `event.target.checked` を読むので、チェックされた状態が「すべての行を選択する」を意味する操作部品向けです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

(`e`) => `void`

## 例 {#example}

```ts
const onChange = table_getToggleAllRowsSelectedHandler(table)
```
