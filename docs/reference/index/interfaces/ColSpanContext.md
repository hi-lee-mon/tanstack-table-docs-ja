---
id: ColSpanContext
title: ColSpanContext
---

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:68](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L68)

描画される行ごとに、`spanColumns` のリゾルバーへ渡されるコンテキストです。

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

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:73](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L73)

***

### row {#row}

```ts
row: Row<TFeatures, TData>;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:74](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L74)

***

### table {#table}

```ts
table: Table<TFeatures, TData>;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:75](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L75)
