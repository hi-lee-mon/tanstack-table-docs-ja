---
id: AppDisplayColumnDef
title: AppDisplayColumnDef
---

```ts
type AppDisplayColumnDef<TFeatures, TData, TCellComponents, THeaderComponents> = Omit<DisplayColumnDef<TFeatures, TData, unknown>, "cell" | "header" | "footer"> & object;
```

定義元: [src/createTableHook.tsx:116](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L116)

コンポーネントがあらかじめ結び付けられた、拡張版の表示用列定義です。

## 型宣言 {#type-declaration}

### cell? {#cell}

```ts
optional cell?: AppColumnDefTemplate<AppCellContext<TFeatures, TData, unknown, TCellComponents>>;
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
