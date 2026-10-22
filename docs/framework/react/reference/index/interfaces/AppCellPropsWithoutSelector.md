---
id: AppCellPropsWithoutSelector
title: AppCellPropsWithoutSelector
---

定義元: [src/createTableHook.tsx:398](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L398)

AppCell コンポーネントの props です（selector なし）。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TValue {#tvalue}

`TValue` *extends* `CellData`

### TCellComponents {#tcellcomponents}

`TCellComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

## プロパティ {#properties}

### cell {#cell}

```ts
cell: Cell<TFeatures, TData, TValue>;
```

定義元: [src/createTableHook.tsx:404](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L404)

***

### children {#children}

```ts
children: (cell) => ReactNode;
```

定義元: [src/createTableHook.tsx:405](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L405)

#### パラメーター {#parameters}

##### cell {#cell-1}

`Cell_Core`\<`TFeatures`, `TData`, `TValue`\> & `ExtractFeatureMapTypes`\<`TFeatures`, `Cell_FeatureMap`\> & `TCellComponents` & `object`

#### 戻り値 {#returns}

`ReactNode`

***

### selector? {#selector}

```ts
optional selector?: undefined;
```

定義元: [src/createTableHook.tsx:409](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L409)
