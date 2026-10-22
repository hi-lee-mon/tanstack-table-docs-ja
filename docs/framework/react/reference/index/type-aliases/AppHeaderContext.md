---
id: AppHeaderContext
title: AppHeaderContext
---

```ts
type AppHeaderContext<TFeatures, TData, TValue, THeaderComponents> = object;
```

定義元: [src/createTableHook.tsx:67](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L67)

ヘッダーコンポーネントがあらかじめ結び付けられた、拡張版の HeaderContext です。
`header` プロパティには、登録した headerComponents が含まれます。

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

### column {#column}

```ts
column: Column<TFeatures, TData, TValue>;
```

定義元: [src/createTableHook.tsx:73](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L73)

***

### header {#header}

```ts
header: Header<TFeatures, TData, TValue> & THeaderComponents & object;
```

定義元: [src/createTableHook.tsx:74](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L74)

#### 型宣言 {#type-declaration}

##### FlexRender {#flexrender}

```ts
FlexRender: () => ReactNode;
```

###### 戻り値 {#returns}

`ReactNode`

***

### table {#table}

```ts
table: Table<TFeatures, TData>;
```

定義元: [src/createTableHook.tsx:76](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L76)
