---
id: AppTablePropsWithSelector
title: AppTablePropsWithSelector
---

Defined in: [src/createTableHook.tsx:387](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L387)

Props for AppTable component - with selector

## Type Parameters {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TSelected {#tselected}

`TSelected`

## Properties {#properties}

### children {#children}

```ts
children: (state) => ReactNode;
```

Defined in: [src/createTableHook.tsx:391](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L391)

#### Parameters {#parameters}

##### state {#state}

`TSelected`

#### Returns {#returns}

`ReactNode`

***

### selector {#selector}

```ts
selector: (state) => TSelected;
```

Defined in: [src/createTableHook.tsx:392](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L392)

#### Parameters {#parameters-1}

##### state {#state-1}

`TableState`\<`TFeatures`\>

#### Returns {#returns-1}

`TSelected`
