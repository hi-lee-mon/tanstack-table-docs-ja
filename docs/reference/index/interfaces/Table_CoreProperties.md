---
id: Table_CoreProperties
title: Table_CoreProperties
---

定義元: [core/table/coreTablesFeature.types.ts:156](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L156)

## 継承先 {#extended-by}

- [`Table_Table`](Table_Table.md)

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

***

### \_cellPrototype? {#_cellprototype}

```ts
optional _cellPrototype?: object;
```

定義元: [core/table/coreTablesFeature.types.ts:171](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L171)

Cell オブジェクトのプロトタイプのキャッシュです。このテーブルのすべてのセルで共有されます。

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

***

### \_columnPrototype? {#_columnprototype}

```ts
optional _columnPrototype?: object;
```

定義元: [core/table/coreTablesFeature.types.ts:181](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L181)

Column オブジェクトのプロトタイプのキャッシュです。このテーブルのすべての列で共有されます。

***

### \_features {#_features}

```ts
readonly _features: Partial<CoreFeatures> & TFeatures;
```

定義元: [core/table/coreTablesFeature.types.ts:185](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L185)

テーブルで有効になっている機能です。

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

***

### \_headerPrototype? {#_headerprototype}

```ts
optional _headerPrototype?: object;
```

定義元: [core/table/coreTablesFeature.types.ts:201](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L201)

Header オブジェクトのプロトタイプのキャッシュです。このテーブルのすべてのヘッダーで共有されます。

***

### \_reactivity {#_reactivity}

```ts
readonly _reactivity: TableReactivityBindings;
```

定義元: [core/table/coreTablesFeature.types.ts:163](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L163)

TanStack Store とやり取りするための、テーブルのリアクティビティのバインディングです。

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

***

### \_rowModelFns {#_rowmodelfns}

```ts
readonly _rowModelFns: RowModelFns<TFeatures, TData>;
```

定義元: [core/table/coreTablesFeature.types.ts:205](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L205)

機能がデータを処理するために使う、行モデルの処理関数です。

***

### \_rowModels {#_rowmodels}

```ts
readonly _rowModels: CachedRowModels<TFeatures, TData>;
```

定義元: [core/table/coreTablesFeature.types.ts:209](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L209)

テーブルで有効になっている行モデルです。

***

### \_rowPrototype? {#_rowprototype}

```ts
optional _rowPrototype?: object;
```

定義元: [core/table/coreTablesFeature.types.ts:213](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L213)

Row オブジェクトのプロトタイプのキャッシュです。このテーブルのすべての行で共有されます。

***

### atoms {#atoms}

```ts
readonly atoms: Atoms<TFeatures>;
```

定義元: [core/table/coreTablesFeature.types.ts:223](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L223)

`TableState` の各スライスに対応する、読み取り専用の派生アトムです。それぞれ、対応する `baseAtom` と、スライスごとの外部のアトムまたは外部の状態の値（指定されていれば）から導き出されます（優先順位: 外部のアトム > 外部の状態 > 基底アトム）。

***

### baseAtoms {#baseatoms}

```ts
readonly baseAtoms: BaseAtoms<TFeatures>;
```

定義元: [core/table/coreTablesFeature.types.ts:228](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L228)

`TableState` の各スライスに対応する、内部の書き込み可能なアトムです。これはライブラリで唯一の書き込み先で、機能による状態の変更はすべてここに届きます。

***

### initialState {#initialstate}

```ts
readonly initialState: ExtractFeatureMapTypes<TFeatures>;
```

定義元: [core/table/coreTablesFeature.types.ts:232](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L232)

テーブルの、解決済みの初期状態です。

***

### options {#options}

```ts
readonly options: TableOptions<TFeatures, TData>;
```

定義元: [core/table/coreTablesFeature.types.ts:236](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L236)

テーブルの現在のオプションへの、読み取り専用の参照です。

***

### optionsStore? {#optionsstore}

```ts
readonly optional optionsStore?: Atom<TableOptions<TFeatures, TData>>;
```

定義元: [core/table/coreTablesFeature.types.ts:242](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L242)

テーブルのオプションの書き込み可能なアトムです。有効なコアのリアクティビティのバインディングで `createOptionsStore` が true の場合にだけ作られます。
これを使わないアダプターは、オプションをアトムで持たず、解決済みのただのデータとして持ちます。

***

### store {#store}

```ts
readonly store: ReadonlyStore<ExtractFeatureMapTypes<TFeatures, TableState_FeatureMap>>;
```

定義元: [core/table/coreTablesFeature.types.ts:247](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L247)

テーブルの状態の、読み取り専用の平坦なストアです。`table.atoms` だけから導き出され、外部の状態を直接読むことはありません。
