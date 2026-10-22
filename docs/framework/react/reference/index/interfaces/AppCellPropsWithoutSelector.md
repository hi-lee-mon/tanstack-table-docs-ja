---
id: AppCellPropsWithoutSelector
title: AppCellPropsWithoutSelector
---

Defined in: [src/createTableHook.tsx:398](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L398)

Props for AppCell component - without selector

## Type Parameters {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TValue {#tvalue}

`TValue` *extends* `CellData`

### TCellComponents {#tcellcomponents}

`TCellComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

## Properties {#properties}

### cell {#cell}

```ts
cell: Cell<TFeatures, TData, TValue>;
```

Defined in: [src/createTableHook.tsx:404](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L404)

***

### children {#children}

```ts
children: (cell) => ReactNode;
```

Defined in: [src/createTableHook.tsx:405](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L405)

#### Parameters {#parameters}

##### cell {#cell-1}

`Cell_Core`\<`TFeatures`, `TData`, `TValue`\> & `ExtractFeatureMapTypes`\<`TFeatures`, `Cell_FeatureMap`\> & `TCellComponents` & `object`

#### Returns {#returns}

`ReactNode`

***

### selector? {#selector}

```ts
optional selector?: undefined;
```

Defined in: [src/createTableHook.tsx:409](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L409)
