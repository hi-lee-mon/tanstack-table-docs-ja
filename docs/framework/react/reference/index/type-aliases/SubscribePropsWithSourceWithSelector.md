---
id: SubscribePropsWithSourceWithSelector
title: SubscribePropsWithSourceWithSelector
---

```ts
type SubscribePropsWithSourceWithSelector<TSourceValue, TSelected> = object;
```

定義元: [src/Subscribe.ts:51](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L51)

ソース（アトムまたはストア）から射影した値を購読します。selector はソースの値を受け取り、
children は射影された `TSelected` を受け取ります。

## 型パラメーター {#type-parameters}

### TSourceValue {#tsourcevalue}

`TSourceValue`

### TSelected {#tselected}

`TSelected`

## プロパティ {#properties}

### children {#children}

```ts
children: ((state) => ReactNode) | ReactNode;
```

定義元: [src/Subscribe.ts:54](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L54)

***

### selector {#selector}

```ts
selector: (state) => TSelected;
```

定義元: [src/Subscribe.ts:53](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L53)

#### パラメーター {#parameters}

##### state {#state}

`TSourceValue`

#### 戻り値 {#returns}

`TSelected`

***

### source {#source}

```ts
source: SubscribeSource<TSourceValue>;
```

定義元: [src/Subscribe.ts:52](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L52)
