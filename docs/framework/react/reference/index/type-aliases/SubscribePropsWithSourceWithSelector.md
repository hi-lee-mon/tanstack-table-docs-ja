---
id: SubscribePropsWithSourceWithSelector
title: SubscribePropsWithSourceWithSelector
---

```ts
type SubscribePropsWithSourceWithSelector<TSourceValue, TSelected> = object;
```

Defined in: [src/Subscribe.ts:51](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L51)

Subscribe to a projected value from a source (atom or store). The selector
receives the source value; children receive the projected `TSelected`.

## Type Parameters {#type-parameters}

### TSourceValue {#tsourcevalue}

`TSourceValue`

### TSelected {#tselected}

`TSelected`

## Properties {#properties}

### children {#children}

```ts
children: ((state) => ReactNode) | ReactNode;
```

Defined in: [src/Subscribe.ts:54](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L54)

***

### selector {#selector}

```ts
selector: (state) => TSelected;
```

Defined in: [src/Subscribe.ts:53](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L53)

#### Parameters {#parameters}

##### state {#state}

`TSourceValue`

#### Returns {#returns}

`TSelected`

***

### source {#source}

```ts
source: SubscribeSource<TSourceValue>;
```

Defined in: [src/Subscribe.ts:52](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L52)
