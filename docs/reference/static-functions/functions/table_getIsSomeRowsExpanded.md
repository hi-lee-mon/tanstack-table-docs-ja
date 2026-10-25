---
id: table_getIsSomeRowsExpanded
title: table_getIsSomeRowsExpanded
---

```ts
function table_getIsSomeRowsExpanded<TFeatures, TData>(table): boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.utils.ts:186](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.utils.ts#L186)

展開されている行があるかどうかを判定します。

「すべて展開」を表す特別な値 `true` も、展開されている行があるとみなします。

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
const someExpanded = table_getIsSomeRowsExpanded(table)
```
