---
id: header_getContext
title: header_getContext
---

```ts
function header_getContext<TFeatures, TData, TValue>(header): object;
```

定義元: [core/headers/coreHeadersFeature.utils.ts:57](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.utils.ts#L57)

列の `header` または `footer` テンプレートに渡す描画コンテキストを作ります。

コンテキストには、ヘッダー、その列、それを持つテーブルインスタンスが入ります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue`

## パラメーター {#parameters}

### header {#header}

[`Header`](../../index/type-aliases/Header.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

`object`

### column {#column}

```ts
column: Column<TFeatures, TData, TValue> = header.column;
```

### header {#header-1}

```ts
header: Header<TFeatures, TData, TValue>;
```

### table {#table}

```ts
table: Table_Internal<TFeatures, TData> = header.column.table;
```

## 例 {#example}

```ts
const context = header_getContext(header)
```
