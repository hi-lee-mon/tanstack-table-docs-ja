---
id: tableOptions
title: tableOptions
---

`tableOptions` の実行時の実装です。

このヘルパーは受け取ったオブジェクトをそのまま返します。価値はすべてオーバーロード側にあり、コンパイル時にテーブルのオプションの型推論を保ちます。

## 呼び出しシグネチャ {#call-signature}

```ts
function tableOptions<TFeatures, TData>(options): Omit<TableOptions<TFeatures, TData>, "columns" | "features"> & object;
```

定義元: [helpers/tableOptions.ts:11](https://github.com/TanStack/table/blob/main/packages/table-core/src/helpers/tableOptions.ts#L11)

再利用するオプションが `columns` を省略していても、テーブルのオプションの型推論を保ちます。

あとからフレームワークのアダプターやテーブルのファクトリーで列を受け取る、共有のオプションを組み立てるときに便利です。

### 型パラメーター {#type-parameters}

#### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

#### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

### パラメーター {#parameters}

#### options {#options}

`Omit`\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>, `"columns"`\> & `object`

### 戻り値 {#returns}

`Omit`\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>, `"columns"` \| `"features"`\> & `object`

## 呼び出しシグネチャ {#call-signature-1}

```ts
function tableOptions<TFeatures, TData>(options): Omit<TableOptions<TFeatures, TData>, "data" | "features"> & object;
```

定義元: [helpers/tableOptions.ts:25](https://github.com/TanStack/table/blob/main/packages/table-core/src/helpers/tableOptions.ts#L25)

再利用するオプションが `data` を省略していても、テーブルのオプションの型推論を保ちます。

### 型パラメーター {#type-parameters-1}

#### TFeatures {#tfeatures-1}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

#### TData {#tdata-1}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

### パラメーター {#parameters-1}

#### options {#options-1}

`Omit`\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>, `"data"`\> & `object`

### 戻り値 {#returns-1}

`Omit`\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>, `"data"` \| `"features"`\> & `object`

## 呼び出しシグネチャ {#call-signature-2}

```ts
function tableOptions<TFeatures, TData>(options): Omit<TableOptions<TFeatures, TData>, "data" | "columns" | "features"> & object;
```

定義元: [helpers/tableOptions.ts:40](https://github.com/TanStack/table/blob/main/packages/table-core/src/helpers/tableOptions.ts#L40)

再利用するオプションが `data` と `columns` の両方を省略していても、テーブルのオプションの型推論を保ちます。

### 型パラメーター {#type-parameters-2}

#### TFeatures {#tfeatures-2}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

#### TData {#tdata-2}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

### パラメーター {#parameters-2}

#### options {#options-2}

`Omit`\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>, `"data"` \| `"columns"`\> & `object`

### 戻り値 {#returns-2}

`Omit`\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>, `"data"` \| `"columns"` \| `"features"`\> & `object`

## 呼び出しシグネチャ {#call-signature-3}

```ts
function tableOptions<TFeatures, TData>(options): TableOptions<TFeatures, TData>;
```

定義元: [helpers/tableOptions.ts:54](https://github.com/TanStack/table/blob/main/packages/table-core/src/helpers/tableOptions.ts#L54)

すべて指定されたテーブルのオプションのオブジェクトについて、型推論を保ちます。

### 型パラメーター {#type-parameters-3}

#### TFeatures {#tfeatures-3}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

#### TData {#tdata-3}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

### パラメーター {#parameters-3}

#### options {#options-3}

[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>

### 戻り値 {#returns-3}

[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>

## 呼び出しシグネチャ {#call-signature-4}

```ts
function tableOptions<TFeatures, TData>(options): Omit<TableOptions<TFeatures, TData>, "features">;
```

定義元: [helpers/tableOptions.ts:62](https://github.com/TanStack/table/blob/main/packages/table-core/src/helpers/tableOptions.ts#L62)

ラッパーが `features` を渡す場合にも型推論を保ちます。

### 型パラメーター {#type-parameters-4}

#### TFeatures {#tfeatures-4}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

#### TData {#tdata-4}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

### パラメーター {#parameters-4}

#### options {#options-4}

`Omit`\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>, `"features"`\>

### 戻り値 {#returns-4}

`Omit`\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>, `"features"`\>

## 呼び出しシグネチャ {#call-signature-5}

```ts
function tableOptions<TFeatures, TData>(options): Omit<TableOptions<TFeatures, TData>, "data" | "features">;
```

定義元: [helpers/tableOptions.ts:72](https://github.com/TanStack/table/blob/main/packages/table-core/src/helpers/tableOptions.ts#L72)

ラッパーが `data` と `features` の両方を渡す場合にも型推論を保ちます。

### 型パラメーター {#type-parameters-5}

#### TFeatures {#tfeatures-5}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

#### TData {#tdata-5}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

### パラメーター {#parameters-5}

#### options {#options-5}

`Omit`\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>, `"data"` \| `"features"`\>

### 戻り値 {#returns-5}

`Omit`\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>, `"data"` \| `"features"`\>

## 呼び出しシグネチャ {#call-signature-6}

```ts
function tableOptions<TFeatures, TData>(options): Omit<TableOptions<TFeatures, TData>, "columns" | "features">;
```

定義元: [helpers/tableOptions.ts:82](https://github.com/TanStack/table/blob/main/packages/table-core/src/helpers/tableOptions.ts#L82)

ラッパーが `columns` と `features` の両方を渡す場合にも型推論を保ちます。

### 型パラメーター {#type-parameters-6}

#### TFeatures {#tfeatures-6}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

#### TData {#tdata-6}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

### パラメーター {#parameters-6}

#### options {#options-6}

`Omit`\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>, `"columns"` \| `"features"`\>

### 戻り値 {#returns-6}

`Omit`\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>, `"columns"` \| `"features"`\>

## 呼び出しシグネチャ {#call-signature-7}

```ts
function tableOptions<TFeatures, TData>(options): Omit<TableOptions<TFeatures, TData>, "data" | "columns" | "features">;
```

定義元: [helpers/tableOptions.ts:93](https://github.com/TanStack/table/blob/main/packages/table-core/src/helpers/tableOptions.ts#L93)

ラッパーが `data`、`columns`、`features` を渡す場合にも型推論を保ちます。

### 型パラメーター {#type-parameters-7}

#### TFeatures {#tfeatures-7}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

#### TData {#tdata-7}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

### パラメーター {#parameters-7}

#### options {#options-7}

`Omit`\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>, `"data"` \| `"columns"` \| `"features"`\>

### 戻り値 {#returns-7}

`Omit`\<[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>, `"data"` \| `"columns"` \| `"features"`\>
