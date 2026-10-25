---
id: column_toggleVisibility
title: column_toggleVisibility
---

```ts
function column_toggleVisibility<TFeatures, TData, TValue>(column, visible?): void;
```

定義元: [features/column-visibility/columnVisibilityFeature.utils.ts:45](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.utils.ts#L45)

非表示が許可されている場合に、この列の表示の状態を更新します。

`visible` を渡すと、その値を保存します。省略すると、列の現在の表示の状態を反転させます。
表示の状態は末端の列 ID をキーにしているので、グループ列は非表示にできる末端の列を更新します。非表示にできない列は変わりません。

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

### visible? {#visible}

`boolean`

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
column_toggleVisibility(column)
```
