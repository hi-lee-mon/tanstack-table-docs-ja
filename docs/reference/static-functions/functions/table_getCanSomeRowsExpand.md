---
id: table_getCanSomeRowsExpand
title: table_getCanSomeRowsExpand
---

```ts
function table_getCanSomeRowsExpand<TFeatures, TData>(table): boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.utils.ts:150](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.utils.ts#L150)

ページネーション前の行のうち、展開できる行が少なくとも1つあるかどうかを判定します。

ページネーションはあえて無視しています。現在のページにない展開可能な行も、操作部品に反映できるようにするためです。

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
const canExpand = table_getCanSomeRowsExpand(table)
```
