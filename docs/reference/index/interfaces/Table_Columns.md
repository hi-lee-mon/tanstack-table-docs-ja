---
id: Table_Columns
title: Table_Columns
---

定義元: [core/columns/coreColumnsFeature.types.ts:76](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L76)

## 継承先 {#extended-by}

- [`Table_Core`](Table_Core.md)
- [`Table_Internal`](Table_Internal.md)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getAllColumns {#getallcolumns}

```ts
getAllColumns: () => Column<TFeatures, TData, unknown>[];
```

定義元: [core/columns/coreColumnsFeature.types.ts:91](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L91)

`options.columns` を、テーブルの入れ子の列の階層に正規化します。

#### 戻り値 {#returns}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getAllFlatColumns {#getallflatcolumns}

```ts
getAllFlatColumns: () => Column<TFeatures, TData, unknown>[];
```

定義元: [core/columns/coreColumnsFeature.types.ts:95](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L95)

入れ子の列の階層を平坦化します。親の列（グループ列）も含みます。

#### 戻り値 {#returns-1}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getAllFlatColumnsById {#getallflatcolumnsbyid}

```ts
getAllFlatColumnsById: () => Record<string, Column<TFeatures, TData, unknown>>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:83](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L83)

平坦化したすべての列を、ID で引けるマップにして返します。

#### 戻り値 {#returns-2}

`Record`\<`string`, [`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>\>

***

### getAllLeafColumns {#getallleafcolumns}

```ts
getAllLeafColumns: () => Column<TFeatures, TData, unknown>[];
```

定義元: [core/columns/coreColumnsFeature.types.ts:99](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L99)

すべての末端の列を集めます。親の列（グループ列）は含みません。

#### 戻り値 {#returns-3}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getAllLeafColumnsById {#getallleafcolumnsbyid}

```ts
getAllLeafColumnsById: () => Record<string, Column<TFeatures, TData, unknown>>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:103](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L103)

末端のノードにあたるすべての列を、ID で引けるマップにして返します。親の列は含みません。

#### 戻り値 {#returns-4}

`Record`\<`string`, [`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>\>

***

### getColumn {#getcolumn}

```ts
getColumn: (columnId) =>
  | Column<TFeatures, TData, unknown>
  | undefined;
```

定義元: [core/columns/coreColumnsFeature.types.ts:107](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L107)

ID を指定して列を1つ返します。

#### パラメーター {#parameters}

##### columnId {#columnid}

`string`

#### 戻り値 {#returns-5}

  \| [`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>
  \| `undefined`

***

### getDefaultColumnDef {#getdefaultcolumndef}

```ts
getDefaultColumnDef: () => Partial<ColumnDef<TFeatures, TData, unknown>>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:87](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L87)

組み込み、機能、利用者がそれぞれ定義した列の既定のオプションを解決します。

#### 戻り値 {#returns-6}

`Partial`\<[`ColumnDef`](../type-aliases/ColumnDef.md)\<`TFeatures`, `TData`, `unknown`\>\>
