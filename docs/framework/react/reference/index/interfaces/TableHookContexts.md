---
id: TableHookContexts
title: TableHookContexts
---

定義元: [src/createTableHookContexts.tsx:17](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHookContexts.tsx#L17)

[createTableHookContexts](../functions/createTableHookContexts.md) が返すオブジェクトです。スコープを限定した 3 つの React
コンテキストと、それぞれに対応するコンテキストのフックを持ちます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

## プロパティ {#properties}

### cellContext {#cellcontext}

```ts
cellContext: Context<Cell<any, any, any>>;
```

定義元: [src/createTableHookContexts.tsx:22](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHookContexts.tsx#L22)

***

### headerContext {#headercontext}

```ts
headerContext: Context<Header<any, any, any>>;
```

定義元: [src/createTableHookContexts.tsx:23](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHookContexts.tsx#L23)

***

### tableContext {#tablecontext}

```ts
tableContext: Context<ReactTable<any, any>>;
```

定義元: [src/createTableHookContexts.tsx:21](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHookContexts.tsx#L21)

***

### useCellContext {#usecellcontext}

```ts
useCellContext: <TValue>() => Cell<TFeatures, any, TValue>;
```

定義元: [src/createTableHookContexts.tsx:28](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHookContexts.tsx#L28)

#### 型パラメーター {#type-parameters-1}

##### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

#### 戻り値 {#returns}

`Cell`\<`TFeatures`, `any`, `TValue`\>

***

### useHeaderContext {#useheadercontext}

```ts
useHeaderContext: <TValue>() => Header<TFeatures, any, TValue>;
```

定義元: [src/createTableHookContexts.tsx:33](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHookContexts.tsx#L33)

#### 型パラメーター {#type-parameters-2}

##### TValue {#tvalue-1}

`TValue` *extends* `unknown` = `unknown`

#### 戻り値 {#returns-1}

`Header`\<`TFeatures`, `any`, `TValue`\>

***

### useTableContext {#usetablecontext}

```ts
useTableContext: <TTableData>() => ReactTable<TFeatures, TTableData>;
```

定義元: [src/createTableHookContexts.tsx:24](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHookContexts.tsx#L24)

#### 型パラメーター {#type-parameters-3}

##### TTableData {#ttabledata}

`TTableData` *extends* `RowData` = `TData`

#### 戻り値 {#returns-2}

[`ReactTable`](../type-aliases/ReactTable.md)\<`TFeatures`, `TTableData`\>
