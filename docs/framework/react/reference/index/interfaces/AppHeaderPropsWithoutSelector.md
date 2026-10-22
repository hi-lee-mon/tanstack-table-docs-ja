---
id: AppHeaderPropsWithoutSelector
title: AppHeaderPropsWithoutSelector
---

定義元: [src/createTableHook.tsx:434](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L434)

AppHeader/AppFooter コンポーネントの props です（selector なし）。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TValue {#tvalue}

`TValue` *extends* `CellData`

### THeaderComponents {#theadercomponents}

`THeaderComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

## プロパティ {#properties}

### children {#children}

```ts
children: (header) => ReactNode;
```

定義元: [src/createTableHook.tsx:441](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L441)

#### パラメーター {#parameters}

##### header {#header}

`Header_Core`\<`TFeatures`, `TData`, `TValue`\> & `ExtractFeatureMapTypes`\<`TFeatures`, `Header_FeatureMap`\> & `THeaderComponents` & `object`

#### 戻り値 {#returns}

`ReactNode`

***

### header {#header-1}

```ts
header: Header<TFeatures, TData, TValue>;
```

定義元: [src/createTableHook.tsx:440](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L440)

***

### selector? {#selector}

```ts
optional selector?: undefined;
```

定義元: [src/createTableHook.tsx:445](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L445)
