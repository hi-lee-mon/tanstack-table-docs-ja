---
id: AppTablePropsWithSelector
title: AppTablePropsWithSelector
---

定義元: [src/createTableHook.tsx:387](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L387)

AppTable コンポーネントの props（セレクターあり）

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TSelected {#tselected}

`TSelected`

## プロパティ {#properties}

### children {#children}

```ts
children: (state) => ReactNode;
```

定義元: [src/createTableHook.tsx:391](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L391)

#### パラメーター {#parameters}

##### state {#state}

`TSelected`

#### 戻り値 {#returns}

`ReactNode`

***

### selector {#selector}

```ts
selector: (state) => TSelected;
```

定義元: [src/createTableHook.tsx:392](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L392)

#### パラメーター {#parameters-1}

##### state {#state-1}

`TableState`\<`TFeatures`\>

#### 戻り値 {#returns-1}

`TSelected`
