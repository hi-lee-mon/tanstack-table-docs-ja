---
id: AppColumnDefBase
title: AppColumnDefBase
---

```ts
type AppColumnDefBase<TFeatures, TData, TValue, TCellComponents, THeaderComponents> = Omit<IdentifiedColumnDef<TFeatures, TData, TValue>, "cell" | "header" | "footer"> & object;
```

定義元: [src/createTableHook.tsx:92](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L92)

cell / header / footer の各コンテキストにコンポーネントをあらかじめバインドした、拡張版の列定義のベース型です。

## 型宣言 {#type-declaration}

### cell? {#cell}

```ts
optional cell?: AppColumnDefTemplate<AppCellContext<TFeatures, TData, TValue, TCellComponents>>;
```

### footer? {#footer}

```ts
optional footer?: AppColumnDefTemplate<AppHeaderContext<TFeatures, TData, TValue, THeaderComponents>>;
```

### header? {#header}

```ts
optional header?: AppColumnDefTemplate<AppHeaderContext<TFeatures, TData, TValue, THeaderComponents>>;
```

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TValue {#tvalue}

`TValue` *extends* `CellData`

### TCellComponents {#tcellcomponents}

`TCellComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

### THeaderComponents {#theadercomponents}

`THeaderComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>
