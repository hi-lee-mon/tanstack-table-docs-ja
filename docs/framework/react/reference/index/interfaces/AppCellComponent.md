---
id: AppCellComponent
title: AppCellComponent
---

定義元: [src/createTableHook.tsx:470](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L470)

AppCell のコンポーネント型です。セルをラップし、セルのコンテキストを提供します。Subscribe も任意で使えます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TCellComponents {#tcellcomponents}

`TCellComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

## 呼び出しシグネチャ {#call-signature}

```ts
AppCellComponent<TValue>(props): ReactNode;
```

定義元: [src/createTableHook.tsx:475](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L475)

AppCell のコンポーネント型です。セルをラップし、セルのコンテキストを提供します。Subscribe も任意で使えます。

### 型パラメーター {#type-parameters-1}

#### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

### パラメーター {#parameters}

#### props {#props}

[`AppCellPropsWithoutSelector`](AppCellPropsWithoutSelector.md)\<`TFeatures`, `TData`, `TValue`, `TCellComponents`\>

### 戻り値 {#returns}

`ReactNode`

## 呼び出しシグネチャ {#call-signature-1}

```ts
AppCellComponent<TValue, TSelected>(props): ReactNode;
```

定義元: [src/createTableHook.tsx:483](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L483)

AppCell のコンポーネント型です。セルをラップし、セルのコンテキストを提供します。Subscribe も任意で使えます。

### 型パラメーター {#type-parameters-2}

#### TValue {#tvalue-1}

`TValue` *extends* `unknown` = `unknown`

#### TSelected {#tselected}

`TSelected` = `unknown`

### パラメーター {#parameters-1}

#### props {#props-1}

[`AppCellPropsWithSelector`](AppCellPropsWithSelector.md)\<`TFeatures`, `TData`, `TValue`, `TCellComponents`, `TSelected`\>

### 戻り値 {#returns-1}

`ReactNode`
