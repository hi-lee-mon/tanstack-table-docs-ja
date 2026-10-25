---
id: Column_CoreProperties
title: Column_CoreProperties
---

定義元: [core/columns/coreColumnsFeature.types.ts:7](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L7)

## 継承先 {#extended-by}

- [`Column_Column`](Column_Column.md)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](../type-aliases/CellData.md) = [`CellData`](../type-aliases/CellData.md)

## プロパティ {#properties}

### accessorFn? {#accessorfn}

```ts
optional accessorFn?: AccessorFn<TData, TValue>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:15](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L15)

各行からこの列の値を取り出すときに使う、解決済みのアクセサー関数です。列定義に有効なアクセサーのキーまたは関数がある場合にだけ定義されます。

***

### columnDef {#columndef}

```ts
columnDef: ColumnDef<TFeatures, TData, TValue>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:19](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L19)

列を作るときに使われた元の列定義です。

***

### columns {#columns}

```ts
columns: Column<TFeatures, TData, TValue>[];
```

定義元: [core/columns/coreColumnsFeature.types.ts:23](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L23)

子の列です（グループ列の場合）。グループ列でなければ空の配列です。

***

### depth {#depth}

```ts
depth: number;
```

定義元: [core/columns/coreColumnsFeature.types.ts:27](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L27)

ルートの列定義の配列から数えた、列の深さです（グループ化されている場合）。

***

### id {#id}

```ts
id: string;
```

定義元: [core/columns/coreColumnsFeature.types.ts:34](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L34)

列の一意な識別子です。次の優先順で決まります:
   - 列定義で手動で指定した `id` プロパティ
   - 列定義のアクセサーのキー
   - 列定義のヘッダー文字列

***

### parent? {#parent}

```ts
optional parent?: Column<TFeatures, TData, TValue>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:38](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L38)

この列の親の列です。ルートの列なら undefined です。

***

### table {#table}

```ts
table: Table_Internal<TFeatures, TData>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:42](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L42)

親のテーブルインスタンスへの参照です。
