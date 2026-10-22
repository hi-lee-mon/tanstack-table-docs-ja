---
id: AppHeaderPropsWithSelector
title: AppHeaderPropsWithSelector
---

Defined in: [src/createTableHook.tsx:451](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L451)

Props for AppHeader/AppFooter component - with selector

## Type Parameters {#type-parameters}

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

## Properties {#properties}

### children {#children}

```ts
children: (header, state) => ReactNode;
```

Defined in: [src/createTableHook.tsx:459](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L459)

#### Parameters {#parameters}

##### header {#header}

`Header_Core`\<`TFeatures`, `TData`, `TValue`\> & `ExtractFeatureMapTypes`\<`TFeatures`, `Header_FeatureMap`\> & `THeaderComponents` & `object`

##### state {#state}

`TSelected`

#### Returns {#returns}

`ReactNode`

***

### header {#header-1}

```ts
header: Header<TFeatures, TData, TValue>;
```

Defined in: [src/createTableHook.tsx:458](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L458)

***

### selector {#selector}

```ts
selector: (state) => TSelected;
```

Defined in: [src/createTableHook.tsx:464](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L464)

#### Parameters {#parameters-1}

##### state {#state-1}

`TableState`\<`TFeatures`\>

#### Returns {#returns-1}

`TSelected`
