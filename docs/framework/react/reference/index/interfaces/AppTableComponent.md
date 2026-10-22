---
id: AppTableComponent
title: AppTableComponent
---

定義元: [src/createTableHook.tsx:524](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L524)

AppTable のコンポーネント型です。ルートのラッパーで、Subscribe は任意で使えます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

## 呼び出しシグネチャ {#call-signature}

```ts
AppTableComponent(props): ReactNode;
```

定義元: [src/createTableHook.tsx:525](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L525)

AppTable のコンポーネント型です。ルートのラッパーで、Subscribe は任意で使えます。

### パラメーター {#parameters}

#### props {#props}

[`AppTablePropsWithoutSelector`](AppTablePropsWithoutSelector.md)

### 戻り値 {#returns}

`ReactNode`

## 呼び出しシグネチャ {#call-signature-1}

```ts
AppTableComponent<TSelected>(props): ReactNode;
```

定義元: [src/createTableHook.tsx:526](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L526)

AppTable のコンポーネント型です。ルートのラッパーで、Subscribe は任意で使えます。

### 型パラメーター {#type-parameters-1}

#### TSelected {#tselected}

`TSelected`

### パラメーター {#parameters-1}

#### props {#props-1}

[`AppTablePropsWithSelector`](AppTablePropsWithSelector.md)\<`TFeatures`, `TSelected`\>

### 戻り値 {#returns-1}

`ReactNode`
