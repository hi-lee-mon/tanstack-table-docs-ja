---
id: AppHeaderComponent
title: AppHeaderComponent
---

定義元: [src/createTableHook.tsx:497](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L497)

AppHeader/AppFooter のコンポーネント型です。ヘッダーをラップし、ヘッダーのコンテキストを提供します。Subscribe は任意で使えます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### THeaderComponents {#theadercomponents}

`THeaderComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

## 呼び出しシグネチャ {#call-signature}

```ts
AppHeaderComponent<TValue>(props): ReactNode;
```

定義元: [src/createTableHook.tsx:502](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L502)

AppHeader/AppFooter のコンポーネント型です。ヘッダーをラップし、ヘッダーのコンテキストを提供します。Subscribe は任意で使えます。

### 型パラメーター {#type-parameters-1}

#### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

### パラメーター {#parameters}

#### props {#props}

[`AppHeaderPropsWithoutSelector`](AppHeaderPropsWithoutSelector.md)\<`TFeatures`, `TData`, `TValue`, `THeaderComponents`\>

### 戻り値 {#returns}

`ReactNode`

## 呼び出しシグネチャ {#call-signature-1}

```ts
AppHeaderComponent<TValue, TSelected>(props): ReactNode;
```

定義元: [src/createTableHook.tsx:510](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L510)

AppHeader/AppFooter のコンポーネント型です。ヘッダーをラップし、ヘッダーのコンテキストを提供します。Subscribe は任意で使えます。

### 型パラメーター {#type-parameters-2}

#### TValue {#tvalue-1}

`TValue` *extends* `unknown` = `unknown`

#### TSelected {#tselected}

`TSelected` = `unknown`

### パラメーター {#parameters-1}

#### props {#props-1}

[`AppHeaderPropsWithSelector`](AppHeaderPropsWithSelector.md)\<`TFeatures`, `TData`, `TValue`, `THeaderComponents`, `TSelected`\>

### 戻り値 {#returns-1}

`ReactNode`
