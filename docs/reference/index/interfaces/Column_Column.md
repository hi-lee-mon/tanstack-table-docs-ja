---
id: Column_Column
title: Column_Column
---

定義元: [core/columns/coreColumnsFeature.types.ts:45](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L45)

## 継承元 {#extends}

- [`Column_CoreProperties`](Column_CoreProperties.md)\<`TFeatures`, `TData`, `TValue`\>

## 継承先 {#extended-by}

- [`Column_Core`](Column_Core.md)

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

#### 継承元のメンバー {#inherited-from}

[`Column_CoreProperties`](Column_CoreProperties.md).[`accessorFn`](Column_CoreProperties.md#accessorfn)

***

### columnDef {#columndef}

```ts
columnDef: ColumnDef<TFeatures, TData, TValue>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:19](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L19)

列を作るときに使われた元の列定義です。

#### 継承元のメンバー {#inherited-from-1}

[`Column_CoreProperties`](Column_CoreProperties.md).[`columnDef`](Column_CoreProperties.md#columndef)

***

### columns {#columns}

```ts
columns: Column<TFeatures, TData, TValue>[];
```

定義元: [core/columns/coreColumnsFeature.types.ts:23](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L23)

子の列です（グループ列の場合）。グループ列でなければ空の配列です。

#### 継承元のメンバー {#inherited-from-2}

[`Column_CoreProperties`](Column_CoreProperties.md).[`columns`](Column_CoreProperties.md#columns)

***

### depth {#depth}

```ts
depth: number;
```

定義元: [core/columns/coreColumnsFeature.types.ts:27](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L27)

ルートの列定義の配列から数えた、列の深さです（グループ化されている場合）。

#### 継承元のメンバー {#inherited-from-3}

[`Column_CoreProperties`](Column_CoreProperties.md).[`depth`](Column_CoreProperties.md#depth)

***

### getFlatColumns {#getflatcolumns}

```ts
getFlatColumns: () => Column<TFeatures, TData, TValue>[];
```

定義元: [core/columns/coreColumnsFeature.types.ts:53](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L53)

この列と、その子孫の列すべてを1つの配列に平坦化します。

#### 戻り値 {#returns}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>[]

***

### getLeafColumns {#getleafcolumns}

```ts
getLeafColumns: () => Column<TFeatures, TData, TValue>[];
```

定義元: [core/columns/coreColumnsFeature.types.ts:58](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L58)

この列の下にある末端の列を集めます。子を持たない場合は、この列自身を返します。

#### 戻り値 {#returns-1}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>[]

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

#### 継承元のメンバー {#inherited-from-4}

[`Column_CoreProperties`](Column_CoreProperties.md).[`id`](Column_CoreProperties.md#id)

***

### parent? {#parent}

```ts
optional parent?: Column<TFeatures, TData, TValue>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:38](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L38)

この列の親の列です。ルートの列なら undefined です。

#### 継承元のメンバー {#inherited-from-5}

[`Column_CoreProperties`](Column_CoreProperties.md).[`parent`](Column_CoreProperties.md#parent)

***

### table {#table}

```ts
table: Table_Internal<TFeatures, TData>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:42](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L42)

親のテーブルインスタンスへの参照です。

#### 継承元のメンバー {#inherited-from-6}

[`Column_CoreProperties`](Column_CoreProperties.md).[`table`](Column_CoreProperties.md#table)
