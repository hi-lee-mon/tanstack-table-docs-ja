---
id: Row_Core
title: Row_Core
---

定義元: [types/Row.ts:13](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/Row.ts#L13)

## 継承元 {#extends}

- [`Row_Row`](Row_Row.md)\<`TFeatures`, `TData`\>

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

#### 継承元のメンバー {#inherited-from}

[`Row_Row`](Row_Row.md).[`_cellsCache`](Row_Row.md#_cellscache)

***

### \_displayIndexCache {#_displayindexcache}

```ts
_displayIndexCache: number;
```

定義元: [core/rows/coreRowsFeature.types.ts:25](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L25)

**`Internal`**

現在の表示順を求める間に使う内部のキャッシュです。

この値は、表示順が再計算されるまで古いままのことがあります。代わりに `row.getDisplayIndex()` を使ってください。こちらは、キャッシュされた位置を更新・検証してから返します。

#### 継承元のメンバー {#inherited-from-1}

[`Row_Row`](Row_Row.md).[`_displayIndexCache`](Row_Row.md#_displayindexcache)

***

### \_uniqueValuesCache {#_uniquevaluescache}

```ts
_uniqueValuesCache: Record<string, unknown>;
```

定義元: [core/rows/coreRowsFeature.types.ts:26](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L26)

#### 継承元のメンバー {#inherited-from-2}

[`Row_Row`](Row_Row.md).[`_uniqueValuesCache`](Row_Row.md#_uniquevaluescache)

***

### \_valuesCache {#_valuescache}

```ts
_valuesCache: Record<string, unknown>;
```

定義元: [core/rows/coreRowsFeature.types.ts:27](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L27)

#### 継承元のメンバー {#inherited-from-3}

[`Row_Row`](Row_Row.md).[`_valuesCache`](Row_Row.md#_valuescache)

***

### depth {#depth}

```ts
depth: number;
```

定義元: [core/rows/coreRowsFeature.types.ts:31](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L31)

ルートの行の配列から数えた、行の深さです（入れ子やグループ化されている場合）。

#### 継承元のメンバー {#inherited-from-4}

[`Row_Row`](Row_Row.md).[`depth`](Row_Row.md#depth)

***

### getAllCells {#getallcells}

```ts
getAllCells: () => Cell<TFeatures, TData, unknown>[];
```

定義元: [core/rows/coreRowsFeature.types.ts:80](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L80)

末端の列ごとにセルを1つずつ作ります。非表示の列のセルも作ります。

#### 戻り値 {#returns}

[`Cell`](../type-aliases/Cell.md)\<`TFeatures`, `TData`, `unknown`\>[]

#### 継承元のメンバー {#inherited-from-5}

[`Row_Row`](Row_Row.md).[`getAllCells`](Row_Row.md#getallcells)

***

### getAllCellsByColumnId {#getallcellsbycolumnid}

```ts
getAllCellsByColumnId: () => Record<string, Cell<TFeatures, TData, unknown>>;
```

定義元: [core/rows/coreRowsFeature.types.ts:76](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L76)

この行のセルを、末端の列 ID をキーにして引けるようにします。

#### 戻り値 {#returns-1}

`Record`\<`string`, [`Cell`](../type-aliases/Cell.md)\<`TFeatures`, `TData`, `unknown`\>\>

#### 継承元のメンバー {#inherited-from-6}

[`Row_Row`](Row_Row.md).[`getAllCellsByColumnId`](Row_Row.md#getallcellsbycolumnid)

***

### getDisplayIndex {#getdisplayindex}

```ts
getDisplayIndex: () => number;
```

定義元: [core/rows/coreRowsFeature.types.ts:72](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L72)

ページネーション前の現在の表示順における行の0始まりのインデックスを返します。行がその行モデルに含まれなければ `-1` を返します。
行番号を表示する列には、`row.index` や内部の `_displayIndexCache` フィールドではなく、これを使ってください。

#### 戻り値 {#returns-2}

`number`

#### 継承元のメンバー {#inherited-from-7}

[`Row_Row`](Row_Row.md).[`getDisplayIndex`](Row_Row.md#getdisplayindex)

***

### getLeafRows {#getleafrows}

```ts
getLeafRows: () => Row<TFeatures, TData>[];
```

定義元: [core/rows/coreRowsFeature.types.ts:84](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L84)

この行の末端の行を返します。親の行は含みません。

#### 戻り値 {#returns-3}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>[]

#### 継承元のメンバー {#inherited-from-8}

[`Row_Row`](Row_Row.md).[`getLeafRows`](Row_Row.md#getleafrows)

***

### getParentRow {#getparentrow}

```ts
getParentRow: () => Row<TFeatures, TData> | undefined;
```

定義元: [core/rows/coreRowsFeature.types.ts:88](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L88)

この行の親の行があれば返します。

#### 戻り値 {#returns-4}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\> \| `undefined`

#### 継承元のメンバー {#inherited-from-9}

[`Row_Row`](Row_Row.md).[`getParentRow`](Row_Row.md#getparentrow)

***

### getParentRows {#getparentrows}

```ts
getParentRows: () => Row<TFeatures, TData>[];
```

定義元: [core/rows/coreRowsFeature.types.ts:92](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L92)

この行の親の行を、ルートの行までさかのぼってすべて返します。

#### 戻り値 {#returns-5}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>[]

#### 継承元のメンバー {#inherited-from-10}

[`Row_Row`](Row_Row.md).[`getParentRows`](Row_Row.md#getparentrows)

***

### getUniqueValues {#getuniquevalues}

```ts
getUniqueValues: <TValue>(columnId) => TValue[];
```

定義元: [core/rows/coreRowsFeature.types.ts:96](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L96)

列について、この行がファセットやグループ化に提供する値を読み取ります。

#### 型パラメーター {#type-parameters-1}

##### TValue {#tvalue}

`TValue`

#### パラメーター {#parameters}

##### columnId {#columnid}

`string`

#### 戻り値 {#returns-6}

`TValue`[]

#### 継承元のメンバー {#inherited-from-11}

[`Row_Row`](Row_Row.md).[`getUniqueValues`](Row_Row.md#getuniquevalues)

***

### getValue {#getvalue}

```ts
getValue: <TValue>(columnId) => TValue;
```

定義元: [core/rows/coreRowsFeature.types.ts:100](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L100)

列 ID について、この行のアクセサーの値を読み取り、結果をキャッシュします。

#### 型パラメーター {#type-parameters-2}

##### TValue {#tvalue-1}

`TValue`

#### パラメーター {#parameters-1}

##### columnId {#columnid-1}

`string`

#### 戻り値 {#returns-7}

`TValue`

#### 継承元のメンバー {#inherited-from-12}

[`Row_Row`](Row_Row.md).[`getValue`](Row_Row.md#getvalue)

***

### id {#id}

```ts
id: string;
```

定義元: [core/rows/coreRowsFeature.types.ts:35](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L35)

`options.getRowId` オプションで決まる、行の一意な識別子です。既定では行のインデックス（サブ行なら親の中での相対的なインデックス）です。

#### 継承元のメンバー {#inherited-from-13}

[`Row_Row`](Row_Row.md).[`id`](Row_Row.md#id)

***

### index {#index}

```ts
index: number;
```

定義元: [core/rows/coreRowsFeature.types.ts:39](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L39)

親の配列（またはルートのデータ配列）の中での行のインデックスです。

#### 継承元のメンバー {#inherited-from-14}

[`Row_Row`](Row_Row.md).[`index`](Row_Row.md#index)

***

### original {#original}

```ts
original: TData;
```

定義元: [core/rows/coreRowsFeature.types.ts:43](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L43)

テーブルに渡された元の行オブジェクトです。グループ行の場合は、グループ内の最初の元の行オブジェクトになります。

#### 継承元のメンバー {#inherited-from-15}

[`Row_Row`](Row_Row.md).[`original`](Row_Row.md#original)

***

### originalSubRows? {#originalsubrows}

```ts
optional originalSubRows?: readonly TData[];
```

定義元: [core/rows/coreRowsFeature.types.ts:47](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L47)

`options.getSubRows` オプションが返した、元のサブ行の配列です。

#### 継承元のメンバー {#inherited-from-16}

[`Row_Row`](Row_Row.md).[`originalSubRows`](Row_Row.md#originalsubrows)

***

### parentId? {#parentid}

```ts
optional parentId?: string;
```

定義元: [core/rows/coreRowsFeature.types.ts:51](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L51)

入れ子になっている場合、この行の親の行 ID です。

#### 継承元のメンバー {#inherited-from-17}

[`Row_Row`](Row_Row.md).[`parentId`](Row_Row.md#parentid)

***

### renderValue {#rendervalue}

```ts
renderValue: <TValue>(columnId) => TValue;
```

定義元: [core/rows/coreRowsFeature.types.ts:104](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L104)

`getValue` と同じように、指定した columnId でのこの行の値を描画しますが、値が見つからない場合は `renderFallbackValue` を返します。

#### 型パラメーター {#type-parameters-3}

##### TValue {#tvalue-2}

`TValue`

#### パラメーター {#parameters-2}

##### columnId {#columnid-2}

`string`

#### 戻り値 {#returns-8}

`TValue`

#### 継承元のメンバー {#inherited-from-18}

[`Row_Row`](Row_Row.md).[`renderValue`](Row_Row.md#rendervalue)

***

### subRows {#subrows}

```ts
subRows: Row<TFeatures, TData>[];
```

定義元: [core/rows/coreRowsFeature.types.ts:55](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L55)

`options.getSubRows` オプションが返した値から作られた、この行のサブ行の配列です。

#### 継承元のメンバー {#inherited-from-19}

[`Row_Row`](Row_Row.md).[`subRows`](Row_Row.md#subrows)

***

### table {#table}

```ts
table: Table_Internal<TFeatures, TData>;
```

定義元: [core/rows/coreRowsFeature.types.ts:59](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L59)

親のテーブルインスタンスへの参照です。

#### 継承元のメンバー {#inherited-from-20}

[`Row_Row`](Row_Row.md).[`table`](Row_Row.md#table)
