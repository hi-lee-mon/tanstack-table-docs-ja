---
id: CreateTableHookResult
title: CreateTableHookResult
---

定義元: [src/createTableHook.tsx:298](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L298)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TTableComponents {#ttablecomponents}

`TTableComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

### TCellComponents {#tcellcomponents}

`TCellComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

### THeaderComponents {#theadercomponents}

`THeaderComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

## プロパティ {#properties}

### appFeatures {#appfeatures}

```ts
appFeatures: TFeatures;
```

定義元: [src/createTableHook.tsx:305](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L305)

`createTableHook` に渡された features オブジェクトです。

***

### createAppColumnHelper {#createappcolumnhelper}

```ts
createAppColumnHelper: <TData>() => AppColumnHelper<TFeatures, TData, TCellComponents, THeaderComponents>;
```

定義元: [src/createTableHook.tsx:310](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L310)

`TFeatures` と登録済みのコンポーネントがあらかじめ結び付けられた列ヘルパーです。そのため、cell・header・footer のレンダー props から、結び付けられたコンポーネントを使えます。

#### 型パラメーター {#type-parameters-1}

##### TData {#tdata}

`TData` *extends* `RowData`

#### 戻り値 {#returns}

[`AppColumnHelper`](../type-aliases/AppColumnHelper.md)\<`TFeatures`, `TData`, `TCellComponents`, `THeaderComponents`\>

***

### useAppTable {#useapptable}

```ts
useAppTable: <TData, TSelected>(tableOptions, selector?) => AppReactTable<TFeatures, TData, TSelected, TTableComponents, TCellComponents, THeaderComponents>;
```

定義元: [src/createTableHook.tsx:320](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L320)

`App*` ラッパーコンポーネントと、登録済みの `tableComponents` が付いたテーブルを作ります。`TData` は `data` オプションから推論されます。

#### 型パラメーター {#type-parameters-2}

##### TData {#tdata-1}

`TData` *extends* `RowData`

##### TSelected {#tselected}

`TSelected` = `TableState`\<`TFeatures`\>

#### パラメーター {#parameters}

##### tableOptions {#tableoptions}

`Omit`\<`TableOptions`\<`TFeatures`, `TData`\>, `"features"`\>

##### selector? {#selector}

(`state`) => `TSelected`

#### 戻り値 {#returns-1}

[`AppReactTable`](../type-aliases/AppReactTable.md)\<`TFeatures`, `TData`, `TSelected`, `TTableComponents`, `TCellComponents`, `THeaderComponents`\>

***

### useCellContext {#usecellcontext}

```ts
useCellContext: <TValue>() => Cell_Core<TFeatures, any, TValue> & ExtractFeatureMapTypes<TFeatures, Cell_FeatureMap> & TCellComponents & object;
```

定義元: [src/createTableHook.tsx:357](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L357)

最も近い `<table.AppCell>` が提供するセルを読み取ります。このセルは、登録した `cellComponents` と、コンテキストに結び付いた `FlexRender` で拡張されています。

#### 型パラメーター {#type-parameters-3}

##### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

#### 戻り値 {#returns-2}

`Cell_Core`\<`TFeatures`, `any`, `TValue`\> & `ExtractFeatureMapTypes`\<`TFeatures`, `Cell_FeatureMap`\> & `TCellComponents` & `object`

***

### useHeaderContext {#useheadercontext}

```ts
useHeaderContext: <TValue>() => Header_Core<TFeatures, any, TValue> & ExtractFeatureMapTypes<TFeatures, Header_FeatureMap> & THeaderComponents & object;
```

定義元: [src/createTableHook.tsx:368](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L368)

最も近い `<table.AppHeader>` または `<table.AppFooter>` が提供するヘッダーを読み取ります。このヘッダーは、登録した `headerComponents` と、コンテキストに結び付いた `FlexRender` で拡張されています。

#### 型パラメーター {#type-parameters-4}

##### TValue {#tvalue-1}

`TValue` *extends* `unknown` = `unknown`

#### 戻り値 {#returns-3}

`Header_Core`\<`TFeatures`, `any`, `TValue`\> & `ExtractFeatureMapTypes`\<`TFeatures`, `Header_FeatureMap`\> & `THeaderComponents` & `object`

***

### useTableContext {#usetablecontext}

```ts
useTableContext: <TData, TSelected>() => AppReactTable<TFeatures, TData, TSelected, TTableComponents, TCellComponents, THeaderComponents>;
```

定義元: [src/createTableHook.tsx:342](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L342)

最も近い `<table.AppTable>` が提供するテーブルを読み取ります。これは `useAppTable` が返すのと同じ拡張済みのインスタンスなので、`App*` コンポーネントと登録した `tableComponents` を使えます。

`useAppTable` に渡したセレクターに合わせて `TSelected` を指定すると、`table.state` の型が選択した部分（スライス）になります。この型は自動では推論できません（React のコンテキストはプロバイダーのジェネリクスを引き継がないため）。そのため、デフォルトはテーブルの状態全体になります。セレクターなしで `useAppTable` を使うよくあるケースでは、これで正しい型になります。

#### 型パラメーター {#type-parameters-5}

##### TData {#tdata-2}

`TData` *extends* `RowData` = `RowData`

##### TSelected {#tselected-1}

`TSelected` = `TableState`\<`TFeatures`\>

#### 戻り値 {#returns-4}

[`AppReactTable`](../type-aliases/AppReactTable.md)\<`TFeatures`, `TData`, `TSelected`, `TTableComponents`, `TCellComponents`, `THeaderComponents`\>
