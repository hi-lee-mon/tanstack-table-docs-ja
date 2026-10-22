---
id: SubscribePropsWithSourceIdentity
title: SubscribePropsWithSourceIdentity
---

```ts
type SubscribePropsWithSourceIdentity<TSourceValue> = object;
```

定義元: [src/Subscribe.ts:41](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L41)

ソース（`table.atoms.rowSelection` や `table.optionsStore` など）の値全体を購読します。`selector` を省略すると、値をそのまま返す恒等セレクターを指定したのと同じになり、children は `TSourceValue` を受け取ります。

## 型パラメーター {#type-parameters}

### TSourceValue {#tsourcevalue}

`TSourceValue`

## プロパティ {#properties}

### children {#children}

```ts
children: ((state) => ReactNode) | ReactNode;
```

定義元: [src/Subscribe.ts:44](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L44)

***

### selector? {#selector}

```ts
optional selector?: undefined;
```

定義元: [src/Subscribe.ts:43](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L43)

***

### source {#source}

```ts
source: SubscribeSource<TSourceValue>;
```

定義元: [src/Subscribe.ts:42](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L42)
