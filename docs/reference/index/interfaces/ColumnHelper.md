---
id: ColumnHelper
title: ColumnHelper
---

定義元: [helpers/columnHelper.ts:13](https://github.com/TanStack/table/blob/main/packages/table-core/src/helpers/columnHelper.ts#L13)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### accessor {#accessor}

```ts
accessor: <TAccessor, TValue>(accessor, column) => TAccessor extends AccessorFn<TData> ? AccessorFnColumnDef<TFeatures, TData, TValue> : AccessorKeyColumnDef<TFeatures, TData, TValue>;
```

定義元: [helpers/columnHelper.ts:25](https://github.com/TanStack/table/blob/main/packages/table-core/src/helpers/columnHelper.ts#L25)

セルの値を取り出すアクセサーのキーまたは関数を持つ、データ列の定義を作成します。

#### 型パラメーター {#type-parameters-1}

##### TAccessor {#taccessor}

`TAccessor` *extends* `string` \| [`AccessorFn`](../type-aliases/AccessorFn.md)\<`TData`\>

##### TValue {#tvalue}

`TValue` *extends* `unknown`

#### パラメーター {#parameters}

##### accessor {#accessor-1}

`TAccessor`

##### column {#column}

`TAccessor` *extends* [`AccessorFn`](../type-aliases/AccessorFn.md)\<`TData`\> ? [`DisplayColumnDef`](../type-aliases/DisplayColumnDef.md)\<`TFeatures`, `TData`, `TValue`\> : [`IdentifiedColumnDef`](../type-aliases/IdentifiedColumnDef.md)\<`TFeatures`, `TData`, `TValue`\>

#### 戻り値 {#returns}

`TAccessor` *extends* [`AccessorFn`](../type-aliases/AccessorFn.md)\<`TData`\> ? [`AccessorFnColumnDef`](../type-aliases/AccessorFnColumnDef.md)\<`TFeatures`, `TData`, `TValue`\> : [`AccessorKeyColumnDef`](../type-aliases/AccessorKeyColumnDef.md)\<`TFeatures`, `TData`, `TValue`\>

#### 例 {#example}

```ts
helper.accessor('firstName', { cell: (info) => info.getValue() })
helper.accessor((row) => row.lastName, { id: 'lastName' })
```

***

### columns {#columns}

```ts
columns: <TColumns>(columns) => ColumnDef<TFeatures, TData, any>[] & [...TColumns[]];
```

定義元: [helpers/columnHelper.ts:48](https://github.com/TanStack/table/blob/main/packages/table-core/src/helpers/columnHelper.ts#L48)

列定義の配列を包み、各列の TValue の型を個別に保ちます。
可変長タプル型を使い、制約を確かめる前に要素の型を推論することで、型が広がるのを防ぎます。

#### 型パラメーター {#type-parameters-2}

##### TColumns {#tcolumns}

`TColumns` *extends* readonly [`ColumnDef`](../type-aliases/ColumnDef.md)\<`TFeatures`, `TData`, `any`\>[]

#### パラメーター {#parameters-1}

##### columns {#columns-1}

\[`...TColumns[]`\]

#### 戻り値 {#returns-1}

[`ColumnDef`](../type-aliases/ColumnDef.md)\<`TFeatures`, `TData`, `any`\>[] & \[`...TColumns[]`\]

#### 例 {#example-1}

```ts
helper.columns([helper.accessor('firstName', {}), helper.accessor('age', {})])
```

***

### display {#display}

```ts
display: (column) => DisplayColumnDef<TFeatures, TData, unknown>;
```

定義元: [helpers/columnHelper.ts:58](https://github.com/TanStack/table/blob/main/packages/table-core/src/helpers/columnHelper.ts#L58)

操作ボタンや行選択のような、データを持たない表示用の列の定義を作成します。

#### パラメーター {#parameters-2}

##### column {#column-1}

[`DisplayColumnDef`](../type-aliases/DisplayColumnDef.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns-2}

[`DisplayColumnDef`](../type-aliases/DisplayColumnDef.md)\<`TFeatures`, `TData`, `unknown`\>

#### 例 {#example-2}

```ts
helper.display({ id: 'actions', header: 'Actions', cell: () => <button>Edit</button> })
```

***

### group {#group}

```ts
group: (column) => GroupColumnDef<TFeatures, TData, unknown>;
```

定義元: [helpers/columnHelper.ts:75](https://github.com/TanStack/table/blob/main/packages/table-core/src/helpers/columnHelper.ts#L75)

入れ子の子の列を持つ、グループ列の定義を作成します。

#### パラメーター {#parameters-3}

##### column {#column-2}

[`GroupColumnDef`](../type-aliases/GroupColumnDef.md)\<`TFeatures`, `TData`, `unknown`\>

#### 戻り値 {#returns-3}

[`GroupColumnDef`](../type-aliases/GroupColumnDef.md)\<`TFeatures`, `TData`, `unknown`\>

#### 例 {#example-3}

```ts
helper.group({
  id: 'name',
  header: 'Name',
  columns: helper.columns([
    helper.accessor('firstName', {}),
    helper.accessor('lastName', { id: 'lastName' }),
  ]),
})
```
