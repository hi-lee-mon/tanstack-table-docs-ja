---
id: AppGroupColumnDef
title: AppGroupColumnDef
---

```ts
type AppGroupColumnDef<TFeatures, TData, TCellComponents, THeaderComponents> = Omit<GroupColumnDef<TFeatures, TData, unknown>, "cell" | "header" | "footer" | "columns"> & object;
```

定義元: [src/createTableHook.tsx:139](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L139)

コンポーネントをあらかじめ結び付けた、拡張版のグループ列定義です。

## 型宣言 {#type-declaration}

### cell? {#cell}

```ts
optional cell?: AppColumnDefTemplate<AppCellContext<TFeatures, TData, unknown, TCellComponents>>;
```

### columns? {#columns}

```ts
optional columns?: ReadonlyArray<ColumnDef<TFeatures, TData, unknown>>;
```

### footer? {#footer}

```ts
optional footer?: AppColumnDefTemplate<AppHeaderContext<TFeatures, TData, unknown, THeaderComponents>>;
```

### header? {#header}

```ts
optional header?: AppColumnDefTemplate<AppHeaderContext<TFeatures, TData, unknown, THeaderComponents>>;
```

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TCellComponents {#tcellcomponents}

`TCellComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

### THeaderComponents {#theadercomponents}

`THeaderComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>
