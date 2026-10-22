---
id: AppCellPropsWithSelector
title: AppCellPropsWithSelector
---

定義元: [src/createTableHook.tsx:415](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L415)

AppCell コンポーネントの props（セレクターを指定する場合）

## 型パラメーター {#type-parameters}

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

## プロパティ {#properties}

### cell {#cell}

```ts
cell: Cell<TFeatures, TData, TValue>;
```

定義元: [src/createTableHook.tsx:422](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L422)

***

### children {#children}

```ts
children: (cell, state) => ReactNode;
```

定義元: [src/createTableHook.tsx:423](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L423)

#### パラメーター {#parameters}

##### cell {#cell-1}

`Cell_Core`\<`TFeatures`, `TData`, `TValue`\> & `ExtractFeatureMapTypes`\<`TFeatures`, `Cell_FeatureMap`\> & `TCellComponents` & `object`

##### state {#state}

`TSelected`

#### 戻り値 {#returns}

`ReactNode`

***

### selector {#selector}

```ts
selector: (state) => TSelected;
```

定義元: [src/createTableHook.tsx:428](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L428)

#### パラメーター {#parameters-1}

##### state {#state-1}

`TableState`\<`TFeatures`\>

#### 戻り値 {#returns-1}

`TSelected`
