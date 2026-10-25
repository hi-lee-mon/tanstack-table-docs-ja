---
id: table_getToggleAllColumnsVisibilityHandler
title: table_getToggleAllColumnsVisibilityHandler
---

```ts
function table_getToggleAllColumnsVisibilityHandler<TFeatures, TData>(table): (e) => void;
```

定義元: [features/column-visibility/columnVisibilityFeature.utils.ts:384](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.utils.ts#L384)

すべての列の表示・非表示を切り替える、チェックボックス用のハンドラーを作成します。

ハンドラーは `event.target.checked` を読むので、チェックされた状態が「すべての列を表示する」を意味する操作部品向けです。

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
const onChange = table_getToggleAllColumnsVisibilityHandler(table)
```
