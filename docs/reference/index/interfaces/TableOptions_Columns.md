---
id: TableOptions_Columns
title: TableOptions_Columns
---

定義元: [core/columns/coreColumnsFeature.types.ts:61](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L61)

## 継承先 {#extended-by}

- [`TableOptions_Core`](TableOptions_Core.md)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](../type-aliases/CellData.md) = [`CellData`](../type-aliases/CellData.md)

## プロパティ {#properties}

### columns {#columns}

```ts
columns: readonly ColumnDef<TFeatures, TData, TValue>[];
```

定義元: [core/columns/coreColumnsFeature.types.ts:69](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L69)

テーブルで使う列定義の配列です。

***

### defaultColumn? {#defaultcolumn}

```ts
optional defaultColumn?: Partial<ColumnDef<TFeatures, TData, TValue>>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:73](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L73)

テーブルに渡すすべての列定義に適用する、列の既定のオプションです。
