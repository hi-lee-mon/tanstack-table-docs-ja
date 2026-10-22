---
id: AppHeaderPropsWithSelector
title: AppHeaderPropsWithSelector
---

定義元: [src/createTableHook.tsx:451](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L451)

AppHeader/AppFooter コンポーネントの props（セレクターあり）です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TValue {#tvalue}

`TValue` *extends* `CellData`

### THeaderComponents {#theadercomponents}

`THeaderComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

### TSelected {#tselected}

`TSelected`

## プロパティ {#properties}

### children {#children}

```ts
children: (header, state) => ReactNode;
```

定義元: [src/createTableHook.tsx:459](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L459)

#### パラメーター {#parameters}

##### header {#header}

`Header_Core`\<`TFeatures`, `TData`, `TValue`\> & `ExtractFeatureMapTypes`\<`TFeatures`, `Header_FeatureMap`\> & `THeaderComponents` & `object`

##### state {#state}

`TSelected`

#### 戻り値 {#returns}

`ReactNode`

***

### header {#header-1}

```ts
header: Header<TFeatures, TData, TValue>;
```

定義元: [src/createTableHook.tsx:458](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L458)

***

### selector {#selector}

```ts
selector: (state) => TSelected;
```

定義元: [src/createTableHook.tsx:464](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L464)

#### パラメーター {#parameters-1}

##### state {#state-1}

`TableState`\<`TFeatures`\>

#### 戻り値 {#returns-1}

`TSelected`
