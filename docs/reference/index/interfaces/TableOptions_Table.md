---
id: TableOptions_Table
title: TableOptions_Table
---

定義元: [core/table/coreTablesFeature.types.ts:88](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L88)

## 継承先 {#extended-by}

- [`TableOptions_Core`](TableOptions_Core.md)

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

***

### autoResetAll? {#autoresetall}

```ts
readonly optional autoResetAll?: boolean;
```

定義元: [core/table/coreTablesFeature.types.ts:113](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L113)

このオプションを指定すると、機能ごとの `autoReset...` オプションをすべて上書きします。

***

### data {#data}

```ts
readonly data: readonly TData[];
```

定義元: [core/table/coreTablesFeature.types.ts:117](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L117)

テーブルに表示するデータです。`data` オプションの参照が変わると、テーブルはデータを処理し直します。

***

### features {#features}

```ts
readonly features: TFeatures & ValidateFeatureSlots<TFeatures>;
```

定義元: [core/table/coreTablesFeature.types.ts:101](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L101)

このテーブルインスタンスに登録された機能モジュールです。

機能の登録によって、どの状態スライス、オプション、プロトタイプの API が使えるかが決まります。
このオブジェクトには、テーブルの行モデルのファクトリー（`sortedRowModel`、`filteredRowModel` など）、行モデル関数のレジストリ（`sortFns`、`filterFns`、`aggregationFns`）、型専用の meta のスロット（`tableMeta`、`columnMeta`）も入ります。

***

### initialState? {#initialstate}

```ts
readonly optional initialState?: Partial<ExtractFeatureMapTypes<TFeatures, TableState_FeatureMap>>;
```

定義元: [core/table/coreTablesFeature.types.ts:131](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L131)

登録されたテーブルの状態スライスの初期値を渡せます（省略可能）。
機能のリセット API は既定でこの値を使います。多くのリセット API は `true` を受け付け、その場合は代わりに機能の空の状態（既定の状態）に戻します。
あとでこのオブジェクトを変えてもテーブルの状態はリセットされないので、参照を安定させておく必要はありません。

***

### key? {#key}

```ts
readonly optional key?: string;
```

定義元: [core/table/coreTablesFeature.types.ts:124](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L124)

このテーブルインスタンスを識別するためのキーです（省略可能）。

TanStack Table Devtools がテーブルを登録・選択するために使います。テーブルを Devtools に渡さないなら不要です。

***

### mergeOptions? {#mergeoptions}

```ts
readonly optional mergeOptions?: (defaultOptions, options) => TableOptions<TFeatures, TData>;
```

定義元: [core/table/coreTablesFeature.types.ts:135](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L135)

テーブルのオプションのマージ方法を、必要に応じて自分で実装するためのオプションです。

#### パラメーター {#parameters}

##### defaultOptions {#defaultoptions}

[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>

##### options {#options}

`Partial`\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>\>

#### 戻り値 {#returns}

[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>

***

### meta? {#meta}

```ts
readonly optional meta?: ExtractTableMeta<TFeatures, TData>;
```

定義元: [core/table/coreTablesFeature.types.ts:145](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L145)

`options.meta` には任意のオブジェクトを渡せます。渡したオブジェクトには、`table` が使えるところならどこからでも `table.options.meta` でアクセスできます。

型は、`features` オプションの型専用スロット `tableMeta` でテーブルごとに宣言するか、`TableMeta` への宣言のマージでグローバルに宣言してください。

***

### state? {#state}

```ts
readonly optional state?: Partial<ExtractFeatureMapTypes<TFeatures, TableState_FeatureMap>>;
```

定義元: [core/table/coreTablesFeature.types.ts:153](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L153)

状態スライスごとに、外部で管理する値を渡せます（省略可能）。

各スライスは、対応する `on[State]Change` コールバックと組み合わせてください。そうすれば、テーブルの状態の更新をテーブルの外に保存できます。同じスライスにこのオプションと外部のアトムの両方を渡した場合は、外部のアトムが優先されます。
