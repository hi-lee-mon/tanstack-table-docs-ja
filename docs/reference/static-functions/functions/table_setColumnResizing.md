---
id: table_setColumnResizing
title: table_setColumnResizing
---

```ts
function table_setColumnResizing<TFeatures, TData>(table, updater): void;
```

定義元: [features/column-resizing/columnResizingFeature.utils.ts:345](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.utils.ts#L345)

一時的な列幅の変更のアップデーターを、テーブルのリサイズのハンドラーに通します。

この状態は進行中のドラッグ操作を追うもので、確定した幅は `columnSizing` にあります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### updater {#updater}

[`Updater`](../../index/type-aliases/Updater.md)\<[`columnResizingState`](../../index/interfaces/columnResizingState.md)\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setColumnResizing(table, (old) => ({ ...old, deltaOffset: 12 }))
```
