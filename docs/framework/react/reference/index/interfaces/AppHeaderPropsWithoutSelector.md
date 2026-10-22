---
id: AppHeaderPropsWithoutSelector
title: AppHeaderPropsWithoutSelector
---

Defined in: [src/createTableHook.tsx:434](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L434)

Props for AppHeader/AppFooter component - without selector

## Type Parameters {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TValue {#tvalue}

`TValue` *extends* `CellData`

### THeaderComponents {#theadercomponents}

`THeaderComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

## Properties {#properties}

### children {#children}

```ts
children: (header) => ReactNode;
```

Defined in: [src/createTableHook.tsx:441](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L441)

#### Parameters {#parameters}

##### header {#header}

`Header_Core`\<`TFeatures`, `TData`, `TValue`\> & `ExtractFeatureMapTypes`\<`TFeatures`, `Header_FeatureMap`\> & `THeaderComponents` & `object`

#### Returns {#returns}

`ReactNode`

***

### header {#header-1}

```ts
header: Header<TFeatures, TData, TValue>;
```

Defined in: [src/createTableHook.tsx:440](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L440)

***

### selector? {#selector}

```ts
optional selector?: undefined;
```

Defined in: [src/createTableHook.tsx:445](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L445)
