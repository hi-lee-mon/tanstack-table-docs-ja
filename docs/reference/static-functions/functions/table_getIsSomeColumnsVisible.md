---
id: table_getIsSomeColumnsVisible
title: table_getIsSomeColumnsVisible
---

```ts
function table_getIsSomeColumnsVisible<TFeatures, TData>(table): boolean;
```

定義元: [features/column-visibility/columnVisibilityFeature.utils.ts:362](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.utils.ts#L362)

少なくとも1つの末端の列が現在表示されているかどうかを判定します。

「すべての列を表示」のような3状態の操作部品に便利です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const someVisible = table_getIsSomeColumnsVisible(table)
```
