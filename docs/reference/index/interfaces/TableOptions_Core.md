---
id: TableOptions_Core
title: TableOptions_Core
---

定義元: [types/TableOptions.ts:33](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableOptions.ts#L33)

省略可能な機能のオプションが加わる前の、テーブルで常に使えるコアのオプションです。

## 継承元 {#extends}

- [`TableOptions_Table`](TableOptions_Table.md)\<`TFeatures`, `TData`\>.[`TableOptions_Cell`](TableOptions_Cell.md).[`TableOptions_Columns`](TableOptions_Columns.md)\<`TFeatures`, `TData`\>.[`TableOptions_Rows`](TableOptions_Rows.md)\<`TFeatures`, `TData`\>

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### atoms? {#atoms}

```ts
readonly optional atoms?: Partial<{ [K in string | number | symbol]: Atom<ExtractFeatureMapTypes<TFeatures, TableState_FeatureMap>[K]> }>;
```

定義元: [core/table/coreTablesFeature.types.ts:109](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L109)

状態スライスごとに、外部の書き込み可能なアトムを渡せます（省略可能）。
あるスライスにアトムを渡すと、そのスライスでは `options.state[key]` と内部の基底アトムよりも優先されます。
機能の状態を更新する API は対応するアトムのアップデーターを通して書き込むので、アプリで管理するテーブルの状態スライスには、v9 では外部のアトムで持つ形がおすすめです。

#### 継承元のメンバー {#inherited-from}

[`TableOptions_Table`](TableOptions_Table.md).[`atoms`](TableOptions_Table.md#atoms)

***

### autoResetAll? {#autoresetall}

```ts
readonly optional autoResetAll?: boolean;
```

定義元: [core/table/coreTablesFeature.types.ts:113](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L113)

このオプションを指定すると、機能ごとの `autoReset...` オプションをすべて上書きします。

#### 継承元のメンバー {#inherited-from-1}

[`TableOptions_Table`](TableOptions_Table.md).[`autoResetAll`](TableOptions_Table.md#autoresetall)

***

### columns {#columns}

```ts
columns: readonly ColumnDef<TFeatures, TData, unknown>[];
```

定義元: [core/columns/coreColumnsFeature.types.ts:69](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L69)

テーブルで使う列定義の配列です。

#### 継承元のメンバー {#inherited-from-2}

[`TableOptions_Columns`](TableOptions_Columns.md).[`columns`](TableOptions_Columns.md#columns)

***

### data {#data}

```ts
readonly data: readonly TData[];
```

定義元: [core/table/coreTablesFeature.types.ts:117](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L117)

テーブルに表示するデータです。`data` オプションの参照が変わると、テーブルはデータを処理し直します。

#### 継承元のメンバー {#inherited-from-3}

[`TableOptions_Table`](TableOptions_Table.md).[`data`](TableOptions_Table.md#data)

***

### defaultColumn? {#defaultcolumn}

```ts
optional defaultColumn?: Partial<ColumnDef<TFeatures, TData, unknown>>;
```

定義元: [core/columns/coreColumnsFeature.types.ts:73](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/columns/coreColumnsFeature.types.ts#L73)

テーブルに渡すすべての列定義に適用する、列の既定のオプションです。

#### 継承元のメンバー {#inherited-from-4}

[`TableOptions_Columns`](TableOptions_Columns.md).[`defaultColumn`](TableOptions_Columns.md#defaultcolumn)

***

### features {#features}

```ts
readonly features: TFeatures & ValidateFeatureSlots<TFeatures>;
```

定義元: [core/table/coreTablesFeature.types.ts:101](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L101)

このテーブルインスタンスに登録された機能モジュールです。

機能の登録によって、どの状態スライス、オプション、プロトタイプの API が使えるかが決まります。
このオブジェクトには、テーブルの行モデルのファクトリー（`sortedRowModel`、`filteredRowModel` など）、行モデル関数のレジストリ（`sortFns`、`filterFns`、`aggregationFns`）、型専用の meta のスロット（`tableMeta`、`columnMeta`）も入ります。

#### 継承元のメンバー {#inherited-from-5}

[`TableOptions_Table`](TableOptions_Table.md).[`features`](TableOptions_Table.md#features)

***

### getRowId? {#getrowid}

```ts
optional getRowId?: (originalRow, index, parent?) => string;
```

定義元: [core/rows/coreRowsFeature.types.ts:115](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L115)

各行の一意な ID を導き出すための関数です（省略可能）。指定しない場合は行のインデックスが使われます（入れ子の行は、祖先のインデックスを `.` でつないだもの、たとえば `index.index.index` になります）。
サーバーサイドの処理から来た個々の行を識別する必要がある場合は、この関数で、通信やあいまいさに左右されない意味のある ID（userId、taskId、データベースの ID フィールドなど）を返すことをおすすめします。

#### パラメーター {#parameters}

##### originalRow {#originalrow}

`TData`

##### index {#index}

`number`

##### parent? {#parent}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns}

`string`

#### 例 {#example}

```ts
getRowId: row => row.userId
```

#### 継承元のメンバー {#inherited-from-6}

[`TableOptions_Rows`](TableOptions_Rows.md).[`getRowId`](TableOptions_Rows.md#getrowid)

***

### getSubRows? {#getsubrows}

```ts
optional getSubRows?: (originalRow, index) => readonly TData[] | undefined;
```

定義元: [core/rows/coreRowsFeature.types.ts:124](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L124)

各行のサブ行を取り出すための関数です（省略可能）。入れ子の行を使う場合は、この関数で行からサブ行のオブジェクト（または undefined）を返す必要があります。

#### パラメーター {#parameters-1}

##### originalRow {#originalrow-1}

`TData`

##### index {#index-1}

`number`

#### 戻り値 {#returns-1}

readonly `TData`[] \| `undefined`

#### 例 {#example-1}

```ts
getSubRows: row => row.subRows
```

#### 継承元のメンバー {#inherited-from-7}

[`TableOptions_Rows`](TableOptions_Rows.md).[`getSubRows`](TableOptions_Rows.md#getsubrows)

***

### initialState? {#initialstate}

```ts
readonly optional initialState?: Partial<ExtractFeatureMapTypes<TFeatures, TableState_FeatureMap>>;
```

定義元: [core/table/coreTablesFeature.types.ts:131](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L131)

登録されたテーブルの状態スライスの初期値を渡せます（省略可能）。
機能のリセット API は既定でこの値を使います。多くのリセット API は `true` を受け付け、その場合は代わりに機能の空の状態（既定の状態）に戻します。
あとでこのオブジェクトを変えてもテーブルの状態はリセットされないので、参照を安定させておく必要はありません。

#### 継承元のメンバー {#inherited-from-8}

[`TableOptions_Table`](TableOptions_Table.md).[`initialState`](TableOptions_Table.md#initialstate)

***

### key? {#key}

```ts
readonly optional key?: string;
```

定義元: [core/table/coreTablesFeature.types.ts:124](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L124)

このテーブルインスタンスを識別するためのキーです（省略可能）。

TanStack Table Devtools がテーブルを登録・選択するために使います。テーブルを Devtools に渡さないなら不要です。

#### 継承元のメンバー {#inherited-from-9}

[`TableOptions_Table`](TableOptions_Table.md).[`key`](TableOptions_Table.md#key)

***

### mergeOptions? {#mergeoptions}

```ts
readonly optional mergeOptions?: (defaultOptions, options) => TableOptions<TFeatures, TData>;
```

定義元: [core/table/coreTablesFeature.types.ts:135](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L135)

テーブルのオプションのマージ方法を、必要に応じて自分で実装するためのオプションです。

#### パラメーター {#parameters-2}

##### defaultOptions {#defaultoptions}

[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>

##### options {#options}

`Partial`\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>\>

#### 戻り値 {#returns-2}

[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>

#### 継承元のメンバー {#inherited-from-10}

[`TableOptions_Table`](TableOptions_Table.md).[`mergeOptions`](TableOptions_Table.md#mergeoptions)

***

### meta? {#meta}

```ts
readonly optional meta?: ExtractTableMeta<TFeatures, TData>;
```

定義元: [core/table/coreTablesFeature.types.ts:145](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L145)

`options.meta` には任意のオブジェクトを渡せます。渡したオブジェクトには、`table` が使えるところならどこからでも `table.options.meta` でアクセスできます。

型は、`features` オプションの型専用スロット `tableMeta` でテーブルごとに宣言するか、`TableMeta` への宣言のマージでグローバルに宣言してください。

#### 継承元のメンバー {#inherited-from-11}

[`TableOptions_Table`](TableOptions_Table.md).[`meta`](TableOptions_Table.md#meta)

***

### renderFallbackValue? {#renderfallbackvalue}

```ts
optional renderFallbackValue?: any;
```

定義元: [core/cells/coreCellsFeature.types.ts:67](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.types.ts#L67)

目的の値がデータに見つからないときに使う値です。

#### 継承元のメンバー {#inherited-from-12}

[`TableOptions_Cell`](TableOptions_Cell.md).[`renderFallbackValue`](TableOptions_Cell.md#renderfallbackvalue)

***

### state? {#state}

```ts
readonly optional state?: Partial<ExtractFeatureMapTypes<TFeatures, TableState_FeatureMap>>;
```

定義元: [core/table/coreTablesFeature.types.ts:153](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L153)

状態スライスごとに、外部で管理する値を渡せます（省略可能）。

各スライスは、対応する `on[State]Change` コールバックと組み合わせてください。そうすれば、テーブルの状態の更新をテーブルの外に保存できます。同じスライスにこのオプションと外部のアトムの両方を渡した場合は、外部のアトムが優先されます。

#### 継承元のメンバー {#inherited-from-13}

[`TableOptions_Table`](TableOptions_Table.md).[`state`](TableOptions_Table.md#state)
