---
id: CellContext
title: CellContext
---

定義元: [core/cells/coreCellsFeature.types.ts:8](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L8)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](../type-aliases/CellData.md) = [`CellData`](../type-aliases/CellData.md)

## プロパティ {#properties}

### cell {#cell}

```ts
cell: Cell<TFeatures, TData, TValue>;
```

定義元: [core/cells/coreCellsFeature.types.ts:13](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L13)

***

### column {#column}

```ts
column: Column<TFeatures, TData, TValue>;
```

定義元: [core/cells/coreCellsFeature.types.ts:14](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L14)

***

### getValue {#getvalue}

```ts
getValue: Getter<TValue>;
```

定義元: [core/cells/coreCellsFeature.types.ts:15](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L15)

***

### renderValue {#rendervalue}

```ts
renderValue: Getter<TValue | null>;
```

定義元: [core/cells/coreCellsFeature.types.ts:16](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L16)

***

### row {#row}

```ts
row: Row<TFeatures, TData>;
```

定義元: [core/cells/coreCellsFeature.types.ts:17](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L17)

***

### table {#table}

```ts
table: Table<TFeatures, TData>;
```

定義元: [core/cells/coreCellsFeature.types.ts:18](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L18)
