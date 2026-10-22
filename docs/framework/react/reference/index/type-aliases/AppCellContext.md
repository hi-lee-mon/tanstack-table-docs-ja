---
id: AppCellContext
title: AppCellContext
---

```ts
type AppCellContext<TFeatures, TData, TValue, TCellComponents> = object;
```

定義元: [src/createTableHook.tsx:48](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L48)

セルコンポーネントをあらかじめバインドした、拡張版の CellContext です。
`cell` プロパティには、登録した cellComponents が含まれます。

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
cell: Cell<TFeatures, TData, TValue> & TCellComponents & object;
```

定義元: [src/createTableHook.tsx:54](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L54)

#### 型宣言 {#type-declaration}

##### FlexRender {#flexrender}

```ts
FlexRender: () => ReactNode;
```

###### 戻り値 {#returns}

`ReactNode`

***

### column {#column}

```ts
column: Column<TFeatures, TData, TValue>;
```

定義元: [src/createTableHook.tsx:56](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L56)

***

### getValue {#getvalue}

```ts
getValue: CellContext<TFeatures, TData, TValue>["getValue"];
```

定義元: [src/createTableHook.tsx:57](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L57)

***

### renderValue {#rendervalue}

```ts
renderValue: CellContext<TFeatures, TData, TValue>["renderValue"];
```

定義元: [src/createTableHook.tsx:58](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L58)

***

### row {#row}

```ts
row: Row<TFeatures, TData>;
```

定義元: [src/createTableHook.tsx:59](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L59)

***

### table {#table}

```ts
table: Table<TFeatures, TData>;
```

定義元: [src/createTableHook.tsx:60](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L60)
