---
id: AppCellPropsWithSelector
title: AppCellPropsWithSelector
---

Defined in: [src/createTableHook.tsx:415](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L415)

Props for AppCell component - with selector

## Type Parameters {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TValue {#tvalue}

`TValue` *extends* `CellData`

### TCellComponents {#tcellcomponents}

`TCellComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

### TSelected {#tselected}

`TSelected`

## Properties {#properties}

### cell {#cell}

```ts
cell: Cell<TFeatures, TData, TValue>;
```

Defined in: [src/createTableHook.tsx:422](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L422)

***

### children {#children}

```ts
children: (cell, state) => ReactNode;
```

Defined in: [src/createTableHook.tsx:423](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L423)

#### Parameters {#parameters}

##### cell {#cell-1}

`Cell_Core`\<`TFeatures`, `TData`, `TValue`\> & `ExtractFeatureMapTypes`\<`TFeatures`, `Cell_FeatureMap`\> & `TCellComponents` & `object`

##### state {#state}

`TSelected`

#### Returns {#returns}

`ReactNode`

***

### selector {#selector}

```ts
selector: (state) => TSelected;
```

Defined in: [src/createTableHook.tsx:428](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L428)

#### Parameters {#parameters-1}

##### state {#state-1}

`TableState`\<`TFeatures`\>

#### Returns {#returns-1}

`TSelected`
