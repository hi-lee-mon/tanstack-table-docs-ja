---
id: Column_Core
title: Column_Core
---

定義元: [types/Column.ts:18](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/Column.ts#L18)

## 継承元 {#extends}

- [`Column_Column`](Column_Column.md)\<`TFeatures`, `TData`, `TValue`\>

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` = `unknown`

## プロパティ {#properties}

### accessorFn? {#accessorfn}

```ts
optional accessorFn?: AccessorFn<TData, TValue>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:15](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L15)

各行からこの列の値を取り出すときに使う、解決済みのアクセサー関数です。列定義に有効なアクセサーのキーまたは関数がある場合にだけ定義されます。

#### 継承元のメンバー {#inherited-from}

[`Column_Column`](Column_Column.md).[`accessorFn`](Column_Column.md#accessorfn)

***

### columnDef {#columndef}

```ts
columnDef: ColumnDef<TFeatures, TData, TValue>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:19](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L19)

列を作るときに使われた元の列定義です。

#### 継承元のメンバー {#inherited-from-1}

[`Column_Column`](Column_Column.md).[`columnDef`](Column_Column.md#columndef)

***

### columns {#columns}

```ts
columns: Column<TFeatures, TData, TValue>[];
```

定義元: [core/columns/coreColumnsFeature.types.ts:23](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L23)

子の列です（グループ列の場合）。グループ列でなければ空の配列です。

#### 継承元のメンバー {#inherited-from-2}

[`Column_Column`](Column_Column.md).[`columns`](Column_Column.md#columns)

***

### depth {#depth}

```ts
depth: number;
```

定義元: [core/columns/coreColumnsFeature.types.ts:27](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L27)

ルートの列定義の配列から数えた、列の深さです（グループ化されている場合）。

#### 継承元のメンバー {#inherited-from-3}

[`Column_Column`](Column_Column.md).[`depth`](Column_Column.md#depth)

***

### getFlatColumns {#getflatcolumns}

```ts
getFlatColumns: () => Column<TFeatures, TData, TValue>[];
```

定義元: [core/columns/coreColumnsFeature.types.ts:53](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L53)

この列と、その子孫の列すべてを1つの配列に平坦化します。

#### 戻り値 {#returns}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>[]

#### 継承元のメンバー {#inherited-from-4}

[`Column_Column`](Column_Column.md).[`getFlatColumns`](Column_Column.md#getflatcolumns)

***

### getLeafColumns {#getleafcolumns}

```ts
getLeafColumns: () => Column<TFeatures, TData, TValue>[];
```

定義元: [core/columns/coreColumnsFeature.types.ts:58](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L58)

この列の下にある末端の列を集めます。子を持たない場合は、この列自身を返します。

#### 戻り値 {#returns-1}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>[]

#### 継承元のメンバー {#inherited-from-5}

[`Column_Column`](Column_Column.md).[`getLeafColumns`](Column_Column.md#getleafcolumns)

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

#### 継承元のメンバー {#inherited-from-6}

[`Column_Column`](Column_Column.md).[`id`](Column_Column.md#id)

***

### parent? {#parent}

```ts
optional parent?: Column<TFeatures, TData, TValue>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:38](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L38)

この列の親の列です。ルートの列なら undefined です。

#### 継承元のメンバー {#inherited-from-7}

[`Column_Column`](Column_Column.md).[`parent`](Column_Column.md#parent)

***

### table {#table}

```ts
table: Table_Internal<TFeatures, TData>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:42](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L42)

親のテーブルインスタンスへの参照です。

#### 継承元のメンバー {#inherited-from-8}

[`Column_Column`](Column_Column.md).[`table`](Column_Column.md#table)
