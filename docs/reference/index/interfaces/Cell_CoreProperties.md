---
id: Cell_CoreProperties
title: Cell_CoreProperties
---

定義元: [core/cells/coreCellsFeature.types.ts:21](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L21)

## 継承先 {#extended-by}

- [`Cell_Cell`](Cell_Cell.md)

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

定義元: [core/cells/coreCellsFeature.types.ts:29](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L29)

セルに対応する Column オブジェクトです。

***

### id {#id}

```ts
id: string;
```

定義元: [core/cells/coreCellsFeature.types.ts:33](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L33)

テーブル全体で一意なセルの ID です。

***

### row {#row}

```ts
row: Row<TFeatures, TData>;
```

定義元: [core/cells/coreCellsFeature.types.ts:37](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L37)

セルに対応する Row オブジェクトです。

***

### table {#table}

```ts
table: Table_Internal<TFeatures, TData>;
```

定義元: [core/cells/coreCellsFeature.types.ts:41](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L41)

親のテーブルインスタンスへの参照です。
