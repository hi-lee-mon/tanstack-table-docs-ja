---
id: HeaderContext
title: HeaderContext
---

定義元: [core/headers/coreHeadersFeature.types.ts:32](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L32)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](../type-aliases/CellData.md) = [`CellData`](../type-aliases/CellData.md)

## プロパティ {#properties}

### column {#column}

```ts
column: Column<TFeatures, TData, TValue>;
```

定義元: [core/headers/coreHeadersFeature.types.ts:40](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L40)

列のインスタンスです。

***

### header {#header}

```ts
header: Header<TFeatures, TData, TValue>;
```

定義元: [core/headers/coreHeadersFeature.types.ts:44](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L44)

ヘッダーのインスタンスです。

***

### table {#table}

```ts
table: Table<TFeatures, TData>;
```

定義元: [core/headers/coreHeadersFeature.types.ts:48](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L48)

テーブルインスタンスです。
