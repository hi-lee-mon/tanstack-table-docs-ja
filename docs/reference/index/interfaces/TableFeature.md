---
id: TableFeature
title: TableFeature
---

定義元: [types/TableFeatures.ts:319](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L319)

テーブルの機能が提供する、ライフサイクルのフックと既定値です。

機能のオブジェクトは、テーブルの `features` オプションに登録します。
機能が提供できるのは、既定の状態とオプション、既定の列定義、テーブルの API、行・列・ヘッダー・セルで共有するプロトタイプの API、そしてテーブル・列・行・ヘッダー・ヘッダーグループ・セルのインスタンスごとのデータです。

## プロパティ {#properties}

### assignCellPrototype? {#assigncellprototype}

```ts
optional assignCellPrototype?: <TFeatures, TData>(prototype, table) => void;
```

定義元: [types/TableFeatures.ts:328](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L328)

テーブルで共有するセルのプロトタイプに、機能のメソッドを追加します。

これは、テーブルで最初にセルを作るときに遅延して実行されます。ここで割り当てたメソッドは、そのテーブルが作るすべてのセルのインスタンスで共有されます。
そのため、このフックは API やメモ化したメソッドのために使い、セルごとに変わるデータには使わないでください。

#### 型パラメーター {#type-parameters}

##### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

#### パラメーター {#parameters}

##### prototype {#prototype}

`Record`\<`string`, `any`\>

##### table {#table}

[`Table_Internal`](Table_Internal.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns}

`void`

***

### assignColumnPrototype? {#assigncolumnprototype}

```ts
optional assignColumnPrototype?: <TFeatures, TData>(prototype, table) => void;
```

定義元: [types/TableFeatures.ts:343](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L343)

テーブルで共有する列のプロトタイプに、機能のメソッドを追加します。

これは、テーブルで最初に列を作るときに遅延して実行されます。ここで割り当てたメソッドは、そのテーブルが作るすべての列のインスタンスで共有されます。
そのため、このフックは API やメモ化したメソッドのために使い、列ごとに変わるデータには使わないでください。

#### 型パラメーター {#type-parameters-1}

##### TFeatures {#tfeatures-1}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-1}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

#### パラメーター {#parameters-1}

##### prototype {#prototype-1}

`Record`\<`string`, `any`\>

##### table {#table-1}

[`Table_Internal`](Table_Internal.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns-1}

`void`

***

### assignHeaderPrototype? {#assignheaderprototype}

```ts
optional assignHeaderPrototype?: <TFeatures, TData>(prototype, table) => void;
```

定義元: [types/TableFeatures.ts:358](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L358)

テーブルで共有するヘッダーのプロトタイプに、機能のメソッドを追加します。

これは、テーブルで最初にヘッダーを作るときに遅延して実行されます。ここで割り当てたメソッドは、そのテーブルが作るすべてのヘッダーのインスタンスで共有されます。
そのため、このフックは API やメモ化したメソッドのために使い、ヘッダーごとに変わるデータには使わないでください。

#### 型パラメーター {#type-parameters-2}

##### TFeatures {#tfeatures-2}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-2}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

#### パラメーター {#parameters-2}

##### prototype {#prototype-2}

`Record`\<`string`, `any`\>

##### table {#table-2}

[`Table_Internal`](Table_Internal.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns-2}

`void`

***

### assignRowPrototype? {#assignrowprototype}

```ts
optional assignRowPrototype?: <TFeatures, TData>(prototype, table) => void;
```

定義元: [types/TableFeatures.ts:373](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L373)

テーブルで共有する行のプロトタイプに、機能のメソッドを追加します。

これは、テーブルで最初に行を作るときに遅延して実行されます。ここで割り当てたメソッドは、そのテーブルが作るすべての行のインスタンスで共有されます。
そのため、このフックは API やメモ化したメソッドのために使い、行ごとに変わるデータには使わないでください。

#### 型パラメーター {#type-parameters-3}

##### TFeatures {#tfeatures-3}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-3}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

#### パラメーター {#parameters-3}

##### prototype {#prototype-3}

`Record`\<`string`, `any`\>

##### table {#table-3}

[`Table_Internal`](Table_Internal.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns-3}

`void`

***

### constructTableAPIs? {#constructtableapis}

```ts
optional constructTableAPIs?: <TFeatures, TData>(table) => void;
```

定義元: [types/TableFeatures.ts:386](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L386)

機能の API をテーブルインスタンスに直接追加します。

テーブルは、行・列・ヘッダー・セルと違って1つしかないため、テーブルの API は共有のプロトタイプを通さず直接割り当てます。
このフックは、テーブルのメソッドを割り当てるためだけに使います。オプション、状態のアトム、ストアが作られ、すべての機能の `initTableInstanceData` フックが終わったあとに実行されます。

#### 型パラメーター {#type-parameters-4}

##### TFeatures {#tfeatures-4}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-4}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

#### パラメーター {#parameters-4}

##### table {#table-4}

[`Table_Internal`](Table_Internal.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns-4}

`void`

***

### getDefaultColumnDef? {#getdefaultcolumndef}

```ts
optional getDefaultColumnDef?: <TFeatures, TData, TValue>() => ColumnDefBase_All<TFeatures, TData, TValue>;
```

定義元: [types/TableFeatures.ts:396](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L396)

この機能が提供する、列定義の既定のオプションを返します。

これらの既定値は、`options.defaultColumn` と、利用者が渡した各列定義が解決される前に、テーブルの既定の列定義にマージされます。そのため、利用者はここで渡された値を上書きできます。

#### 型パラメーター {#type-parameters-5}

##### TFeatures {#tfeatures-5}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-5}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

##### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

#### 戻り値 {#returns-5}

[`ColumnDefBase_All`](../type-aliases/ColumnDefBase_All.md)\<`TFeatures`, `TData`, `TValue`\>

***

### getDefaultTableOptions? {#getdefaulttableoptions}

```ts
optional getDefaultTableOptions?: <TFeatures, TData>(table) => Partial<TableOptions_All<TFeatures, TData>>;
```

定義元: [types/TableFeatures.ts:409](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L409)

この機能が提供する、テーブルの既定のオプションを返します。

これは、テーブルのオプションを解決している間に実行されます。機能を有効にするフラグや、状態を更新する既定のコールバックのような、オプションの既定値に使ってください。
利用者が渡したテーブルのオプションは、ここで返した値より優先されます。

#### 型パラメーター {#type-parameters-6}

##### TFeatures {#tfeatures-6}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-6}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

#### パラメーター {#parameters-5}

##### table {#table-5}

[`Table_Internal`](Table_Internal.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns-6}

`Partial`\<[`TableOptions_All`](../type-aliases/TableOptions_All.md)\<`TFeatures`, `TData`\>\>

***

### getInitialState? {#getinitialstate}

```ts
optional getInitialState?: (initialState) => TableState_All;
```

定義元: [types/TableFeatures.ts:423](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L423)

この機能の、テーブルの初期状態を返します。

受け取る `initialState` には、先に処理された機能と、利用者が渡した初期状態から積み上げた状態が入っています。
この機能の完全な状態オブジェクトを返してください。利用者が渡した値で機能の既定値を上書きできるよう、`initialState` は保ったままにしてください。

#### パラメーター {#parameters-6}

##### initialState {#initialstate}

`Partial`\<[`TableState_All`](TableState_All.md)\>

#### 戻り値 {#returns-7}

[`TableState_All`](TableState_All.md)

***

### initCellInstanceData? {#initcellinstancedata}

```ts
optional initCellInstanceData?: <TFeatures, TData, TValue>(cell) => void;
```

定義元: [types/TableFeatures.ts:452](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L452)

各セルにインスタンスごとのデータを初期化します。

これは、`id`、`column`、`row` のようなセルのコアのフィールドが割り当てられたあとに、作られたすべてのセルについて実行されます。
セルは行と列の組ごとに最初にアクセスされたときに遅延して作られ、キャッシュされるので、これはセルのインスタンスごとに1回実行されます。
セルごとに変わるデータ、キャッシュ、注釈に使ってください。共有するメソッドは、代わりに `assignCellPrototype` で割り当ててください。

#### 型パラメーター {#type-parameters-7}

##### TFeatures {#tfeatures-7}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-7}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

##### TValue {#tvalue-1}

`TValue` *extends* `unknown` = `unknown`

#### パラメーター {#parameters-7}

##### cell {#cell}

[`Cell`](../type-aliases/Cell.md)\<`TFeatures`, `TData`, `TValue`\>

#### 戻り値 {#returns-8}

`void`

***

### initColumnInstanceData? {#initcolumninstancedata}

```ts
optional initColumnInstanceData?: <TFeatures, TData, TValue>(column) => void;
```

定義元: [types/TableFeatures.ts:467](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L467)

各列にインスタンスごとのデータを初期化します。

これは、`id`、`depth`、`parent`、`columnDef`、`columns` のような列のコアのフィールドが割り当てられたあとに、作られたすべての列について実行されます。
列ごとに変わるデータ、キャッシュ、注釈に使ってください。共有するメソッドは、代わりに `assignColumnPrototype` で割り当ててください。

#### 型パラメーター {#type-parameters-8}

##### TFeatures {#tfeatures-8}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-8}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

##### TValue {#tvalue-2}

`TValue` *extends* `unknown` = `unknown`

#### パラメーター {#parameters-8}

##### column {#column}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `TValue`\>

#### 戻り値 {#returns-9}

`void`

***

### initHeaderGroupInstanceData? {#initheadergroupinstancedata}

```ts
optional initHeaderGroupInstanceData?: <TFeatures, TData>(headerGroup) => void;
```

定義元: [types/TableFeatures.ts:483](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L483)

各ヘッダーグループにインスタンスごとのデータを初期化します。

これは、`depth`、`id`、中身がそろった `headers` 配列が割り当てられたあとに、作られたすべてのヘッダーグループについて実行されます。
ヘッダーグループには共有のプロトタイプがないので、インスタンスごとに拡張できるのはここだけです。
ヘッダーグループは再計算のたびに（列の表示、並び順、固定が変わったときなど）作り直されるので、これも作り直すたびに再実行されます。

#### 型パラメーター {#type-parameters-9}

##### TFeatures {#tfeatures-9}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-9}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

#### パラメーター {#parameters-9}

##### headerGroup {#headergroup}

[`HeaderGroup`](HeaderGroup.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns-10}

`void`

***

### initHeaderInstanceData? {#initheaderinstancedata}

```ts
optional initHeaderInstanceData?: <TFeatures, TData, TValue>(header) => void;
```

定義元: [types/TableFeatures.ts:500](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L500)

各ヘッダーにインスタンスごとのデータを初期化します。

これは、`id`、`column`、`depth`、`index`、`isPlaceholder` のようなヘッダーのコアのフィールドが割り当てられたあと、`subHeaders` が埋められて `headerGroup` が結び付けられる前に、作られたすべてのヘッダーについて実行されます。
ヘッダーはヘッダーグループを作り直すたびに作り直されるので、これも作り直すたびに再実行されます。
ヘッダーごとに変わるデータ、キャッシュ、注釈に使ってください。共有するメソッドは、代わりに `assignHeaderPrototype` で割り当ててください。

#### 型パラメーター {#type-parameters-10}

##### TFeatures {#tfeatures-10}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-10}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

##### TValue {#tvalue-3}

`TValue` *extends* `unknown` = `unknown`

#### パラメーター {#parameters-10}

##### header {#header}

[`Header`](../type-aliases/Header.md)\<`TFeatures`, `TData`, `TValue`\>

#### 戻り値 {#returns-11}

`void`

***

### initRowInstanceData? {#initrowinstancedata}

```ts
optional initRowInstanceData?: <TFeatures, TData>(row) => void;
```

定義元: [types/TableFeatures.ts:515](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L515)

各行にインスタンスごとのデータを初期化します。

これは、`id`、`index`、`depth`、`original`、`parentId`、`subRows` のような行のコアのフィールドが割り当てられたあとに、作られたすべての行について実行されます。
行ごとに変わるデータ、キャッシュ、注釈に使ってください。共有するメソッドは、代わりに `assignRowPrototype` で割り当ててください。

#### 型パラメーター {#type-parameters-11}

##### TFeatures {#tfeatures-11}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-11}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

#### パラメーター {#parameters-11}

##### row {#row}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns-12}

`void`

***

### initTableInstanceData? {#inittableinstancedata}

```ts
optional initTableInstanceData?: <TFeatures, TData>(table) => void;
```

定義元: [types/TableFeatures.ts:437](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L437)

この機能が持つ、変更可能でリアクティブでないデータを、テーブルインスタンスに初期化します。

これは、オプション、状態のアトム、ストアが使えるようになったあと、テーブルを作る間に1回だけ実行されます。
機能は登録順に1回で処理され、各機能のインスタンスデータは、その機能の `constructTableAPIs` フックの直前に初期化されます。そのため、このフックでは先に登録された機能のデータと API を当てにできます。
テーブルのメソッドの割り当てには、`constructTableAPIs` だけを使ってください。テーブルをリセットしてもこのフックは再実行されません。一時的なインスタンスデータを消すには、代わりに `resetTableInstanceData` を使ってください。

#### 型パラメーター {#type-parameters-12}

##### TFeatures {#tfeatures-12}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-12}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

#### パラメーター {#parameters-12}

##### table {#table-6}

[`Table_Internal`](Table_Internal.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns-13}

`void`

***

### resetTableInstanceData? {#resettableinstancedata}

```ts
optional resetTableInstanceData?: <TFeatures, TData>(table) => void;
```

定義元: [types/TableFeatures.ts:528](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L528)

この機能が持つ、変更可能でリアクティブでないテーブルインスタンスのデータをリセットします。

これは、`table.reset()` によって内部で持つ状態のアトムが `table.initialState` に戻されたあとに実行されます。
一時的な機能のデータのためのもので、テーブルの状態スライスや外部で制御された状態のためのものではありません。

#### 型パラメーター {#type-parameters-13}

##### TFeatures {#tfeatures-13}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

##### TData {#tdata-13}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

#### パラメーター {#parameters-13}

##### table {#table-7}

[`Table_Internal`](Table_Internal.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns-14}

`void`
