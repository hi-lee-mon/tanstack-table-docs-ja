---
id: Row_CoreProperties
title: Row_CoreProperties
---

定義元: [core/rows/coreRowsFeature.types.ts:8](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L8)

## 継承先 {#extended-by}

- [`Row_Row`](Row_Row.md)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### \_cellsCache? {#_cellscache}

```ts
optional _cellsCache?: WeakMap<Column<TFeatures, TData, unknown>, Cell<TFeatures, TData, unknown>>;
```

定義元: [core/rows/coreRowsFeature.types.ts:12](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L12)

***

### \_displayIndexCache {#_displayindexcache}

```ts
_displayIndexCache: number;
```

定義元: [core/rows/coreRowsFeature.types.ts:25](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L25)

**`Internal`**

現在の表示順を求める間に使う内部のキャッシュです。

この値は、表示順が再計算されるまで古いままのことがあります。代わりに `row.getDisplayIndex()` を使ってください。こちらは、キャッシュされた位置を更新・検証してから返します。

***

### \_uniqueValuesCache {#_uniquevaluescache}

```ts
_uniqueValuesCache: Record<string, unknown>;
```

定義元: [core/rows/coreRowsFeature.types.ts:26](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L26)

***

### \_valuesCache {#_valuescache}

```ts
_valuesCache: Record<string, unknown>;
```

定義元: [core/rows/coreRowsFeature.types.ts:27](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L27)

***

### depth {#depth}

```ts
depth: number;
```

定義元: [core/rows/coreRowsFeature.types.ts:31](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L31)

ルートの行の配列から数えた、行の深さです（入れ子やグループ化されている場合）。

***

### id {#id}

```ts
id: string;
```

定義元: [core/rows/coreRowsFeature.types.ts:35](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L35)

`options.getRowId` オプションで決まる、行の一意な識別子です。既定では行のインデックス（サブ行なら親の中での相対的なインデックス）です。

***

### index {#index}

```ts
index: number;
```

定義元: [core/rows/coreRowsFeature.types.ts:39](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L39)

親の配列（またはルートのデータ配列）の中での行のインデックスです。

***

### original {#original}

```ts
original: TData;
```

定義元: [core/rows/coreRowsFeature.types.ts:43](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L43)

テーブルに渡された元の行オブジェクトです。グループ行の場合は、グループ内の最初の元の行オブジェクトになります。

***

### originalSubRows? {#originalsubrows}

```ts
optional originalSubRows?: readonly TData[];
```

定義元: [core/rows/coreRowsFeature.types.ts:47](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L47)

`options.getSubRows` オプションが返した、元のサブ行の配列です。

***

### parentId? {#parentid}

```ts
optional parentId?: string;
```

定義元: [core/rows/coreRowsFeature.types.ts:51](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L51)

入れ子になっている場合、この行の親の行 ID です。

***

### subRows {#subrows}

```ts
subRows: Row<TFeatures, TData>[];
```

定義元: [core/rows/coreRowsFeature.types.ts:55](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L55)

`options.getSubRows` オプションが返した値から作られた、この行のサブ行の配列です。

***

### table {#table}

```ts
table: Table_Internal<TFeatures, TData>;
```

定義元: [core/rows/coreRowsFeature.types.ts:59](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L59)

親のテーブルインスタンスへの参照です。
