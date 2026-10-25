---
id: Table_Core
title: Table_Core
---

定義元: [types/Table.ts:42](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/Table.ts#L42)

列、ヘッダー、行、テーブルの API のような、テーブルのコアの機能だけを持つコアのテーブルオブジェクトです。
機能は含まれません。

## 継承元 {#extends}

- [`Table_Table`](Table_Table.md)\<`TFeatures`, `TData`\>.[`Table_Columns`](Table_Columns.md)\<`TFeatures`, `TData`\>.[`Table_Rows`](Table_Rows.md)\<`TFeatures`, `TData`\>.[`Table_RowModels`](../type-aliases/Table_RowModels.md)\<`TFeatures`, `TData`\>.[`Table_Headers`](Table_Headers.md)\<`TFeatures`, `TData`\>

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### \_cellInstanceInitFns {#_cellinstanceinitfns}

```ts
_cellInstanceInitFns: <TFeatures, TData, TValue>(cell) => void[];
```

定義元: [core/table/coreTablesFeature.types.ts:167](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L167)

`initCellInstanceData` 関数を定義している機能について、その関数のキャッシュです。

#### 型パラメーター {#type-parameters-1}

##### TFeatures {#tfeatures-1}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-1}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

##### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

#### パラメーター {#parameters}

##### cell {#cell}

[`Cell`](../type-aliases/Cell.md)\<`TFeatures`, `TData`, `TValue`\>

#### 戻り値 {#returns}

`void`

#### 継承元のメンバー {#inherited-from}

[`Table_Table`](Table_Table.md).[`_cellInstanceInitFns`](Table_Table.md#_cellinstanceinitfns)

***

### \_cellPrototype? {#_cellprototype}

```ts
optional _cellPrototype?: object;
```

定義元: [core/table/coreTablesFeature.types.ts:171](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L171)

Cell オブジェクトのプロトタイプのキャッシュです。このテーブルのすべてのセルで共有されます。

#### 継承元のメンバー {#inherited-from-1}

[`Table_Table`](Table_Table.md).[`_cellPrototype`](Table_Table.md#_cellprototype)

***

### \_columnInstanceInitFns {#_columninstanceinitfns}

```ts
_columnInstanceInitFns: <TFeatures, TData, TValue>(column) => void[];
```

定義元: [core/table/coreTablesFeature.types.ts:175](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L175)

`initColumnInstanceData` 関数を定義している機能について、その関数のキャッシュです。

#### 型パラメーター {#type-parameters-2}

##### TFeatures {#tfeatures-2}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-2}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

##### TValue {#tvalue-1}

`TValue` *extends* `unknown` = `unknown`

#### パラメーター {#parameters-1}

##### column {#column}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>

#### 戻り値 {#returns-1}

`void`

#### 継承元のメンバー {#inherited-from-2}

[`Table_Table`](Table_Table.md).[`_columnInstanceInitFns`](Table_Table.md#_columninstanceinitfns)

***

### \_columnPrototype? {#_columnprototype}

```ts
optional _columnPrototype?: object;
```

定義元: [core/table/coreTablesFeature.types.ts:181](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L181)

Column オブジェクトのプロトタイプのキャッシュです。このテーブルのすべての列で共有されます。

#### 継承元のメンバー {#inherited-from-3}

[`Table_Table`](Table_Table.md).[`_columnPrototype`](Table_Table.md#_columnprototype)

***

### \_features {#_features}

```ts
readonly _features: Partial<CoreFeatures> & TFeatures;
```

定義元: [core/table/coreTablesFeature.types.ts:185](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L185)

テーブルで有効になっている機能です。

#### 継承元のメンバー {#inherited-from-4}

[`Table_Table`](Table_Table.md).[`_features`](Table_Table.md#_features)

***

### \_headerGroupInstanceInitFns {#_headergroupinstanceinitfns}

```ts
_headerGroupInstanceInitFns: <TFeatures, TData>(headerGroup) => void[];
```

定義元: [core/table/coreTablesFeature.types.ts:189](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L189)

`initHeaderGroupInstanceData` 関数を定義している機能について、その関数のキャッシュです。

#### 型パラメーター {#type-parameters-3}

##### TFeatures {#tfeatures-3}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-3}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

#### パラメーター {#parameters-2}

##### headerGroup {#headergroup}

[`HeaderGroup`](HeaderGroup.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns-2}

`void`

#### 継承元のメンバー {#inherited-from-5}

[`Table_Table`](Table_Table.md).[`_headerGroupInstanceInitFns`](Table_Table.md#_headergroupinstanceinitfns)

***

### \_headerInstanceInitFns {#_headerinstanceinitfns}

```ts
_headerInstanceInitFns: <TFeatures, TData, TValue>(header) => void[];
```

定義元: [core/table/coreTablesFeature.types.ts:195](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L195)

`initHeaderInstanceData` 関数を定義している機能について、その関数のキャッシュです。

#### 型パラメーター {#type-parameters-4}

##### TFeatures {#tfeatures-4}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-4}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

##### TValue {#tvalue-2}

`TValue` *extends* `unknown` = `unknown`

#### パラメーター {#parameters-3}

##### header {#header}

[`Header`](../type-aliases/Header.md)\<`TFeatures`, `TData`, `TValue`\>

#### 戻り値 {#returns-3}

`void`

#### 継承元のメンバー {#inherited-from-6}

[`Table_Table`](Table_Table.md).[`_headerInstanceInitFns`](Table_Table.md#_headerinstanceinitfns)

***

### \_headerPrototype? {#_headerprototype}

```ts
optional _headerPrototype?: object;
```

定義元: [core/table/coreTablesFeature.types.ts:201](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L201)

Header オブジェクトのプロトタイプのキャッシュです。このテーブルのすべてのヘッダーで共有されます。

#### 継承元のメンバー {#inherited-from-7}

[`Table_Table`](Table_Table.md).[`_headerPrototype`](Table_Table.md#_headerprototype)

***

### \_reactivity {#_reactivity}

```ts
readonly _reactivity: TableReactivityBindings;
```

定義元: [core/table/coreTablesFeature.types.ts:163](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L163)

TanStack Store とやり取りするための、テーブルのリアクティビティのバインディングです。

#### 継承元のメンバー {#inherited-from-8}

[`Table_Table`](Table_Table.md).[`_reactivity`](Table_Table.md#_reactivity)

***

### \_rowInstanceInitFns {#_rowinstanceinitfns}

```ts
_rowInstanceInitFns: <TFeatures, TData>(row) => void[];
```

定義元: [core/table/coreTablesFeature.types.ts:217](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L217)

`initRowInstanceData` 関数を定義している機能について、その関数のキャッシュです。

#### 型パラメーター {#type-parameters-5}

##### TFeatures {#tfeatures-5}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-5}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

#### パラメーター {#parameters-4}

##### row {#row}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns-4}

`void`

#### 継承元のメンバー {#inherited-from-9}

[`Table_Table`](Table_Table.md).[`_rowInstanceInitFns`](Table_Table.md#_rowinstanceinitfns)

***

### \_rowModelFns {#_rowmodelfns}

```ts
readonly _rowModelFns: RowModelFns<TFeatures, TData>;
```

定義元: [core/table/coreTablesFeature.types.ts:205](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L205)

機能がデータを処理するために使う、行モデルの処理関数です。

#### 継承元のメンバー {#inherited-from-10}

[`Table_Table`](Table_Table.md).[`_rowModelFns`](Table_Table.md#_rowmodelfns)

***

### \_rowModels {#_rowmodels}

```ts
readonly _rowModels: CachedRowModels<TFeatures, TData>;
```

定義元: [core/table/coreTablesFeature.types.ts:209](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L209)

テーブルで有効になっている行モデルです。

#### 継承元のメンバー {#inherited-from-11}

[`Table_Table`](Table_Table.md).[`_rowModels`](Table_Table.md#_rowmodels)

***

### \_rowPrototype? {#_rowprototype}

```ts
optional _rowPrototype?: object;
```

定義元: [core/table/coreTablesFeature.types.ts:213](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L213)

Row オブジェクトのプロトタイプのキャッシュです。このテーブルのすべての行で共有されます。

#### 継承元のメンバー {#inherited-from-12}

[`Table_Table`](Table_Table.md).[`_rowPrototype`](Table_Table.md#_rowprototype)

***

### atoms {#atoms}

```ts
readonly atoms: Atoms<TFeatures>;
```

定義元: [core/table/coreTablesFeature.types.ts:223](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L223)

`TableState` の各スライスに対応する、読み取り専用の派生アトムです。それぞれ、対応する `baseAtom` と、スライスごとの外部のアトムまたは外部の状態の値（指定されていれば）から導き出されます（優先順位: 外部のアトム > 外部の状態 > 基底アトム）。

#### 継承元のメンバー {#inherited-from-13}

[`Table_Table`](Table_Table.md).[`atoms`](Table_Table.md#atoms)

***

### baseAtoms {#baseatoms}

```ts
readonly baseAtoms: BaseAtoms<TFeatures>;
```

定義元: [core/table/coreTablesFeature.types.ts:228](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L228)

`TableState` の各スライスに対応する、内部の書き込み可能なアトムです。これはライブラリで唯一の書き込み先で、機能による状態の変更はすべてここに届きます。

#### 継承元のメンバー {#inherited-from-14}

[`Table_Table`](Table_Table.md).[`baseAtoms`](Table_Table.md#baseatoms)

***

### getAllColumns {#getallcolumns}

```ts
getAllColumns: () => Column<TFeatures, TData, unknown>[];
```

定義元: [core/columns/coreColumnsFeature.types.ts:91](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L91)

`options.columns` を、テーブルの入れ子の列の階層に正規化します。

#### 戻り値 {#returns-5}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

#### 継承元のメンバー {#inherited-from-15}

[`Table_Columns`](Table_Columns.md).[`getAllColumns`](Table_Columns.md#getallcolumns)

***

### getAllFlatColumns {#getallflatcolumns}

```ts
getAllFlatColumns: () => Column<TFeatures, TData, unknown>[];
```

定義元: [core/columns/coreColumnsFeature.types.ts:95](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L95)

入れ子の列の階層を平坦化します。親の列（グループ列）も含みます。

#### 戻り値 {#returns-6}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

#### 継承元のメンバー {#inherited-from-16}

[`Table_Columns`](Table_Columns.md).[`getAllFlatColumns`](Table_Columns.md#getallflatcolumns)

***

### getAllFlatColumnsById {#getallflatcolumnsbyid}

```ts
getAllFlatColumnsById: () => Record<string, Column<TFeatures, TData, unknown>>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:83](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L83)

平坦化したすべての列を、ID で引けるマップにして返します。

#### 戻り値 {#returns-7}

`Record`\<`string`, [`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>\>

#### 継承元のメンバー {#inherited-from-17}

[`Table_Columns`](Table_Columns.md).[`getAllFlatColumnsById`](Table_Columns.md#getallflatcolumnsbyid)

***

### getAllLeafColumns {#getallleafcolumns}

```ts
getAllLeafColumns: () => Column<TFeatures, TData, unknown>[];
```

定義元: [core/columns/coreColumnsFeature.types.ts:99](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L99)

すべての末端の列を集めます。親の列（グループ列）は含みません。

#### 戻り値 {#returns-8}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

#### 継承元のメンバー {#inherited-from-18}

[`Table_Columns`](Table_Columns.md).[`getAllLeafColumns`](Table_Columns.md#getallleafcolumns)

***

### getAllLeafColumnsById {#getallleafcolumnsbyid}

```ts
getAllLeafColumnsById: () => Record<string, Column<TFeatures, TData, unknown>>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:103](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L103)

末端のノードにあたるすべての列を、ID で引けるマップにして返します。親の列は含みません。

#### 戻り値 {#returns-9}

`Record`\<`string`, [`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>\>

#### 継承元のメンバー {#inherited-from-19}

[`Table_Columns`](Table_Columns.md).[`getAllLeafColumnsById`](Table_Columns.md#getallleafcolumnsbyid)

***

### getColumn {#getcolumn}

```ts
getColumn: (columnId) =>
  | Column<TFeatures, TData, unknown>
  | undefined;
```

定義元: [core/columns/coreColumnsFeature.types.ts:107](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L107)

ID を指定して列を1つ返します。

#### パラメーター {#parameters-5}

##### columnId {#columnid}

`string`

#### 戻り値 {#returns-10}

  \| [`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>
  \| `undefined`

#### 継承元のメンバー {#inherited-from-20}

[`Table_Columns`](Table_Columns.md).[`getColumn`](Table_Columns.md#getcolumn)

***

### getCoreRowModel {#getcorerowmodel}

```ts
getCoreRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [core/row-models/coreRowModelsFeature.types.ts:34](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/row-models/coreRowModelsFeature.types.ts#L34)

何の処理も適用する前の、コア行モデルを返します。

#### 戻り値 {#returns-11}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-21}

```ts
Table_RowModels.getCoreRowModel
```

***

### getDefaultColumnDef {#getdefaultcolumndef}

```ts
getDefaultColumnDef: () => Partial<ColumnDef<TFeatures, TData, unknown>>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:87](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L87)

組み込み、機能、利用者がそれぞれ定義した列の既定のオプションを解決します。

#### 戻り値 {#returns-12}

`Partial`\<[`ColumnDef`](../type-aliases/ColumnDef.md)\<`TFeatures`, `TData`, `unknown`\>\>

#### 継承元のメンバー {#inherited-from-22}

[`Table_Columns`](Table_Columns.md).[`getDefaultColumnDef`](Table_Columns.md#getdefaultcolumndef)

***

### getExpandedRowModel {#getexpandedrowmodel}

```ts
getExpandedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:135](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L135)

展開された行を平坦化して表示に含めたあとの行モデルを返します。

#### 戻り値 {#returns-13}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-23}

```ts
Table_RowModels.getExpandedRowModel
```

***

### getFacetedMinMaxValues {#getfacetedminmaxvalues}

```ts
getFacetedMinMaxValues: () => [number, number] | undefined;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:35](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L35)

現在のファセットの対象について、数値のファセットの最小値と最大値を計算します。

`features` オプションに、行モデルのファクトリー `facetedMinMaxValues` が必要です。

#### 戻り値 {#returns-14}

\[`number`, `number`\] \| `undefined`

#### 継承元のメンバー {#inherited-from-24}

```ts
Table_RowModels.getFacetedMinMaxValues
```

***

### getFacetedRowModel {#getfacetedrowmodel}

```ts
getFacetedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:41](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L41)

ファセット値を導き出すための行モデルを計算します。

`features` オプションに、行モデルのファクトリー `facetedRowModel` が必要です。

#### 戻り値 {#returns-15}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-25}

```ts
Table_RowModels.getFacetedRowModel
```

***

### getFacetedUniqueValues {#getfaceteduniquevalues}

```ts
getFacetedUniqueValues: () => Map<any, number>;
```

定義元: [features/column-faceting/columnFacetingFeature.types.ts:47](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.types.ts#L47)

ファセットの一意な値とその出現回数を計算します。

`features` オプションに、行モデルのファクトリー `facetedUniqueValues` が必要です。

#### 戻り値 {#returns-16}

`Map`\<`any`, `number`\>

#### 継承元のメンバー {#inherited-from-26}

```ts
Table_RowModels.getFacetedUniqueValues
```

***

### getFilteredRowModel {#getfilteredrowmodel}

```ts
getFilteredRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:301](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L301)

列フィルターとグローバルフィルターを適用したあとの行モデルを返します。

#### 戻り値 {#returns-17}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-27}

```ts
Table_RowModels.getFilteredRowModel
```

***

### getFlatHeaders {#getflatheaders}

```ts
getFlatHeaders: () => Header<TFeatures, TData, unknown>[];
```

定義元: [core/headers/coreHeadersFeature.types.ts:25](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L25)

すべてのヘッダーグループにあるヘッダーを、すべて平坦化します。親のヘッダーとプレースホルダーのヘッダーも含みます。

#### 戻り値 {#returns-18}

[`Header`](../type-aliases/Header.md)\<`TFeatures`, `TData`, `unknown`\>[]

#### 継承元のメンバー {#inherited-from-28}

[`Table_Headers`](Table_Headers.md).[`getFlatHeaders`](Table_Headers.md#getflatheaders)

***

### getFooterGroups {#getfootergroups}

```ts
getFooterGroups: () => HeaderGroup<TFeatures, TData>[];
```

定義元: [core/headers/coreHeadersFeature.types.ts:20](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L20)

現在のヘッダーグループの順を逆にして、フッターグループを作ります。

#### 戻り値 {#returns-19}

[`HeaderGroup`](HeaderGroup.md)\<`TFeatures`, `TData`\>[]

#### 継承元のメンバー {#inherited-from-29}

[`Table_Headers`](Table_Headers.md).[`getFooterGroups`](Table_Headers.md#getfootergroups)

***

### getGroupedRowModel {#getgroupedrowmodel}

```ts
getGroupedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:150](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L150)

グループ化を適用したあとの行モデルを返します。

#### 戻り値 {#returns-20}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-30}

```ts
Table_RowModels.getGroupedRowModel
```

***

### getHeaderGroups {#getheadergroups}

```ts
getHeaderGroups: () => HeaderGroup<TFeatures, TData>[];
```

定義元: [core/headers/coreHeadersFeature.types.ts:16](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L16)

現在の列ツリー、表示の状態、固定の状態から、表示するヘッダーグループを作ります。

#### 戻り値 {#returns-21}

[`HeaderGroup`](HeaderGroup.md)\<`TFeatures`, `TData`\>[]

#### 継承元のメンバー {#inherited-from-31}

[`Table_Headers`](Table_Headers.md).[`getHeaderGroups`](Table_Headers.md#getheadergroups)

***

### getLeafHeaders {#getleafheaders}

```ts
getLeafHeaders: () => Header<TFeatures, TData, unknown>[];
```

定義元: [core/headers/coreHeadersFeature.types.ts:29](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.types.ts#L29)

末端のヘッダーだけを集めます。親のヘッダー（グループヘッダー）は含みません。

#### 戻り値 {#returns-22}

[`Header`](../type-aliases/Header.md)\<`TFeatures`, `TData`, `unknown`\>[]

#### 継承元のメンバー {#inherited-from-32}

[`Table_Headers`](Table_Headers.md).[`getLeafHeaders`](Table_Headers.md#getleafheaders)

***

### getMaxSubRowDepth {#getmaxsubrowdepth}

```ts
getMaxSubRowDepth: () => number;
```

定義元: [core/rows/coreRowsFeature.types.ts:138](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L138)

コア行モデルで、構造上いちばん深い行の深さを返します。
ルートの行は深さ `0`、直下のサブ行は深さ `1` で、以降も同様です。

#### 戻り値 {#returns-23}

`number`

#### 継承元のメンバー {#inherited-from-33}

[`Table_Rows`](Table_Rows.md).[`getMaxSubRowDepth`](Table_Rows.md#getmaxsubrowdepth)

***

### getPaginatedRowModel {#getpaginatedrowmodel}

```ts
getPaginatedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:141](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L141)

ページネーションで現在のページを切り出したあとの行モデルを返します。

#### 戻り値 {#returns-24}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-34}

```ts
Table_RowModels.getPaginatedRowModel
```

***

### getPreExpandedRowModel {#getpreexpandedrowmodel}

```ts
getPreExpandedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:139](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L139)

展開の直前の行モデルを読み取ります。

#### 戻り値 {#returns-25}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-35}

```ts
Table_RowModels.getPreExpandedRowModel
```

***

### getPreFilteredRowModel {#getprefilteredrowmodel}

```ts
getPreFilteredRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:305](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L305)

フィルタリングの直前の行モデルを読み取ります。

#### 戻り値 {#returns-26}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-36}

```ts
Table_RowModels.getPreFilteredRowModel
```

***

### getPreGroupedRowModel {#getpregroupedrowmodel}

```ts
getPreGroupedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:154](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L154)

グループ化の直前の行モデルを読み取ります。

#### 戻り値 {#returns-27}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-37}

```ts
Table_RowModels.getPreGroupedRowModel
```

***

### getPrePaginatedRowModel {#getprepaginatedrowmodel}

```ts
getPrePaginatedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:145](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L145)

ページネーションの直前の行モデルを読み取ります。

#### 戻り値 {#returns-28}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-38}

```ts
Table_RowModels.getPrePaginatedRowModel
```

***

### getPreSortedRowModel {#getpresortedrowmodel}

```ts
getPreSortedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:297](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L297)

ソートの直前の行モデルを読み取ります。

#### 戻り値 {#returns-29}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-39}

```ts
Table_RowModels.getPreSortedRowModel
```

***

### getRow {#getrow}

```ts
getRow: (id, searchAll?) => Row<TFeatures, TData>;
```

定義元: [core/rows/coreRowsFeature.types.ts:153](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L153)

指定した ID の行を返します。

#### パラメーター {#parameters-6}

##### id {#id}

`string`

##### searchAll? {#searchall}

`boolean`

#### 戻り値 {#returns-30}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-40}

[`Table_Rows`](Table_Rows.md).[`getRow`](Table_Rows.md#getrow)

***

### getRowId {#getrowid}

```ts
getRowId: (_, index, parent?) => string;
```

定義元: [core/rows/coreRowsFeature.types.ts:149](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L149)

指定した行の行 ID を返します。

#### パラメーター {#parameters-7}

##### \_ {#_}

`TData`

##### index {#index}

`number`

##### parent? {#parent}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns-31}

`string`

#### 継承元のメンバー {#inherited-from-41}

[`Table_Rows`](Table_Rows.md).[`getRowId`](Table_Rows.md#getrowid)

***

### getRowModel {#getrowmodel}

```ts
getRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [core/row-models/coreRowModelsFeature.types.ts:38](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/row-models/coreRowModelsFeature.types.ts#L38)

使っている他の機能の処理をすべて適用したあとの、最終的な行モデルを返します。描画にいちばんよく使う行モデルです。

#### 戻り値 {#returns-32}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-42}

```ts
Table_RowModels.getRowModel
```

***

### getRowsInDisplayOrder {#getrowsindisplayorder}

```ts
getRowsInDisplayOrder: () => Row<TFeatures, TData>[];
```

定義元: [core/rows/coreRowsFeature.types.ts:145](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L145)

現在の表示順で行を返し、各行に表示インデックスを割り当てます。展開された行がページネーションを素通りする場合は、展開された子孫もこの順に含まれます。
これは `row.getDisplayIndex()` が使う、メモ化された元データです。

#### 戻り値 {#returns-33}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>[]

#### 継承元のメンバー {#inherited-from-43}

[`Table_Rows`](Table_Rows.md).[`getRowsInDisplayOrder`](Table_Rows.md#getrowsindisplayorder)

***

### getSortedRowModel {#getsortedrowmodel}

```ts
getSortedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:301](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L301)

ソートを適用したあとの行モデルを返します。

#### 戻り値 {#returns-34}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-44}

```ts
Table_RowModels.getSortedRowModel
```

***

### initialState {#initialstate}

```ts
readonly initialState: ExtractFeatureMapTypes<TFeatures>;
```

定義元: [core/table/coreTablesFeature.types.ts:232](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L232)

テーブルの、解決済みの初期状態です。

#### 継承元のメンバー {#inherited-from-45}

[`Table_Table`](Table_Table.md).[`initialState`](Table_Table.md#initialstate)

***

### options {#options}

```ts
readonly options: TableOptions<TFeatures, TData>;
```

定義元: [core/table/coreTablesFeature.types.ts:236](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L236)

テーブルの現在のオプションへの、読み取り専用の参照です。

#### 継承元のメンバー {#inherited-from-46}

[`Table_Table`](Table_Table.md).[`options`](Table_Table.md#options)

***

### optionsStore? {#optionsstore}

```ts
readonly optional optionsStore?: Atom<TableOptions<TFeatures, TData>>;
```

定義元: [core/table/coreTablesFeature.types.ts:242](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L242)

テーブルのオプションの書き込み可能なアトムです。有効なコアのリアクティビティのバインディングで `createOptionsStore` が true の場合にだけ作られます。
これを使わないアダプターは、オプションをアトムで持たず、解決済みのただのデータとして持ちます。

#### 継承元のメンバー {#inherited-from-47}

[`Table_Table`](Table_Table.md).[`optionsStore`](Table_Table.md#optionsstore)

***

### reset {#reset}

```ts
reset: () => void;
```

定義元: [core/table/coreTablesFeature.types.ts:262](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L262)

テーブルの内部の基底アトムを `table.initialState` に戻します。

状態スライスを外部のアトムが持っている可能性がある場合や、その機能の空の状態（既定の状態）に戻す動作が必要な場合は、`resetPagination` のような機能ごとのリセット API を使ってください。
内部のアトムをリセットしたあと、変更可能で一時的なテーブルインスタンスのデータについて、機能のリセット用フックも呼び出します。

#### 戻り値 {#returns-35}

`void`

#### 継承元のメンバー {#inherited-from-48}

[`Table_Table`](Table_Table.md).[`reset`](Table_Table.md#reset)

***

### setOptions {#setoptions}

```ts
setOptions: (newOptions) => void;
```

定義元: [core/table/coreTablesFeature.types.ts:267](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L267)

現在の解決済みのオプションに値かアップデーターを適用し、それを `options.mergeOptions` でマージして、テーブルのオプションを更新します。

#### パラメーター {#parameters-8}

##### newOptions {#newoptions}

[`Updater`](../type-aliases/Updater.md)\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>\>

#### 戻り値 {#returns-36}

`void`

#### 継承元のメンバー {#inherited-from-49}

[`Table_Table`](Table_Table.md).[`setOptions`](Table_Table.md#setoptions)

***

### store {#store}

```ts
readonly store: ReadonlyStore<ExtractFeatureMapTypes<TFeatures, TableState_FeatureMap>>;
```

定義元: [core/table/coreTablesFeature.types.ts:247](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L247)

テーブルの状態の、読み取り専用の平坦なストアです。`table.atoms` だけから導き出され、外部の状態を直接読むことはありません。

#### 継承元のメンバー {#inherited-from-50}

[`Table_Table`](Table_Table.md).[`store`](Table_Table.md#store)
