---
id: column_getToggleVisibilityHandler
title: column_getToggleVisibilityHandler
---

```ts
function column_getToggleVisibilityHandler<TFeatures, TData, TValue>(column): (e) => void;
```

定義元: [features/column-visibility/columnVisibilityFeature.utils.ts:136](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.utils.ts#L136)

この列の表示の状態を書き込む、チェックボックス用のハンドラーを作成します。

ハンドラーは `event.target.checked` を読むので、チェックされた状態が「表示する」を意味する、表示切り替えの操作部品向けです。

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
const onChange = column_getToggleVisibilityHandler(column)
```
