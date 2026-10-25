---
id: RowSpanContext
title: RowSpanContext
---

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:51](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L51)

候補の行ごとに `spanRows` の述語関数へ渡されるコンテキストです。

結合には起点があります。`anchorRow` は結合した内容を描画するセルを持つ行で、結合に含まれる後続の行はどれもこの行と比べられます。こうすることで、結合は構造上つねに推移的になります。
1行ずつ順に比べたい述語関数のために、`previousRow` も渡されます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](../type-aliases/CellData.md) = [`CellData`](../type-aliases/CellData.md)

## プロパティ {#properties}

### anchorRow {#anchorrow}

```ts
anchorRow: Row<TFeatures, TData>;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:56](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L56)

***

### anchorValue {#anchorvalue}

```ts
anchorValue: TValue;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:57](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L57)

***

### column {#column}

```ts
column: Column<TFeatures, TData, TValue>;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:58](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L58)

***

### previousRow {#previousrow}

```ts
previousRow: Row<TFeatures, TData>;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:59](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L59)

***

### row {#row}

```ts
row: Row<TFeatures, TData>;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:60](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L60)

***

### table {#table}

```ts
table: Table<TFeatures, TData>;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:61](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L61)

***

### value {#value}

```ts
value: TValue;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:62](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L62)
