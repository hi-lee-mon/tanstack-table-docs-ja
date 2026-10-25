---
id: table_getIsAllRowsExpanded
title: table_getIsAllRowsExpanded
---

```ts
function table_getIsAllRowsExpanded<TFeatures, TData>(table): boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.utils.ts:207](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.utils.ts#L207)

現在の行モデルの展開できる行が、すべて展開されているかどうかを判定します。

「すべて展開」を表す特別な値 `true` なら、すぐに true を返します。展開状態が空なら false を返します。
展開できない行は無視するので、「すべて展開」を行 ID のマップに展開したもの（展開できる行の ID だけを含みます）でも、すべての行が展開されているとみなします。

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
const allExpanded = table_getIsAllRowsExpanded(table)
```
