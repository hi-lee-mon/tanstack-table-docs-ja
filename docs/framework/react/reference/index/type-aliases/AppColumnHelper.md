---
id: AppColumnHelper
title: AppColumnHelper
---

```ts
type AppColumnHelper<TFeatures, TData, TCellComponents, THeaderComponents> = object;
```

定義元: [src/createTableHook.tsx:168](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L168)

セル・ヘッダー・フッターのコンテキストにコンポーネントをあらかじめ結び付けた、拡張版の列ヘルパーです。
これにより、列を定義するときに、登録済みのコンポーネントを TypeScript が認識できます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TCellComponents {#tcellcomponents}

`TCellComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

### THeaderComponents {#theadercomponents}

`THeaderComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

## プロパティ {#properties}

### accessor {#accessor}

```ts
accessor: <TAccessor, TValue>(accessor, column) => TAccessor extends AccessorFn<TData> ? AccessorFnColumnDef<TFeatures, TData, TValue> : AccessorKeyColumnDef<TFeatures, TData, TValue>;
```

定義元: [src/createTableHook.tsx:178](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L178)

アクセサーのキーまたは関数を使って、データ列の列定義を作成します。
セル・ヘッダー・フッターのコンテキストには、あらかじめ結び付けたコンポーネントが含まれます。

#### 型パラメーター {#type-parameters-1}

##### TAccessor {#taccessor}

`TAccessor` *extends* `AccessorFn`\<`TData`\> \| `DeepKeys`\<`TData`\>

##### TValue {#tvalue}

`TValue` *extends* `TAccessor` *extends* `AccessorFn`\<`TData`, infer TReturn\> ? `TReturn` : `TAccessor` *extends* `DeepKeys`\<`TData`\> ? `DeepValue`\<`TData`, `TAccessor`\> : `never`

#### パラメーター {#parameters}

##### accessor {#accessor-1}

`TAccessor`

##### column {#column}

`TAccessor` *extends* `AccessorFn`\<`TData`\> ? [`AppColumnDefBase`](AppColumnDefBase.md)\<`TFeatures`, `TData`, `TValue`, `TCellComponents`, `THeaderComponents`\> & `object` : [`AppColumnDefBase`](AppColumnDefBase.md)\<`TFeatures`, `TData`, `TValue`, `TCellComponents`, `THeaderComponents`\>

#### 戻り値 {#returns}

`TAccessor` *extends* `AccessorFn`\<`TData`\> ? `AccessorFnColumnDef`\<`TFeatures`, `TData`, `TValue`\> : `AccessorKeyColumnDef`\<`TFeatures`, `TData`, `TValue`\>

***

### columns {#columns}

```ts
columns: <TColumns>(columns) => ColumnDef<TFeatures, TData, any>[] & [...TColumns];
```

定義元: [src/createTableHook.tsx:209](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L209)

列定義の配列をラップして、各列がそれぞれ持つ TValue 型を保ちます。

#### 型パラメーター {#type-parameters-2}

##### TColumns {#tcolumns}

`TColumns` *extends* `ReadonlyArray`\<`ColumnDef`\<`TFeatures`, `TData`, `any`\>\>

#### パラメーター {#parameters-1}

##### columns {#columns-1}

\[`...TColumns`\]

#### 戻り値 {#returns-1}

`ColumnDef`\<`TFeatures`, `TData`, `any`\>[] & \[`...TColumns`\]

***

### display {#display}

```ts
display: (column) => DisplayColumnDef<TFeatures, TData, unknown>;
```

定義元: [src/createTableHook.tsx:217](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L217)

データを持たない列のための、表示用の列定義を作成します。
セル・ヘッダー・フッターのコンテキストには、あらかじめ結び付けたコンポーネントが含まれます。

#### パラメーター {#parameters-2}

##### column {#column-1}

[`AppDisplayColumnDef`](AppDisplayColumnDef.md)\<`TFeatures`, `TData`, `TCellComponents`, `THeaderComponents`\>

#### 戻り値 {#returns-2}

`DisplayColumnDef`\<`TFeatures`, `TData`, `unknown`\>

***

### group {#group}

```ts
group: (column) => GroupColumnDef<TFeatures, TData, unknown>;
```

定義元: [src/createTableHook.tsx:230](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L230)

子の列を入れ子にした、グループ列の列定義を作成します。
セル・ヘッダー・フッターのコンテキストには、あらかじめ結び付けたコンポーネントが含まれます。

#### パラメーター {#parameters-3}

##### column {#column-2}

[`AppGroupColumnDef`](AppGroupColumnDef.md)\<`TFeatures`, `TData`, `TCellComponents`, `THeaderComponents`\>

#### 戻り値 {#returns-3}

`GroupColumnDef`\<`TFeatures`, `TData`, `unknown`\>
