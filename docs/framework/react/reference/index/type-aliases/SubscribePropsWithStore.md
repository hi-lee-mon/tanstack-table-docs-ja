---
id: SubscribePropsWithStore
title: SubscribePropsWithStore
---

```ts
type SubscribePropsWithStore<TFeatures, TSelected> = object;
```

定義元: [src/Subscribe.ts:20](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L20)

`table.store`（テーブルの状態全体）を購読します。セレクターは TableState 全体を受け取ります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TSelected {#tselected}

`TSelected`

## プロパティ {#properties}

### children {#children}

```ts
children: ((state) => ReactNode) | ReactNode;
```

定義元: [src/Subscribe.ts:33](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L33)

***

### selector {#selector}

```ts
selector: (state) => TSelected;
```

定義元: [src/Subscribe.ts:32](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L32)

テーブルの状態全体から値を選び出します。選んだ値が変わると（浅い比較で判定）再レンダーします。

明示的に値を選び出さないまま、うっかりストア全体を購読してしまうことがないように、ストアモードでは必須です。

#### パラメーター {#parameters}

##### state {#state}

`TableState`\<`TFeatures`\>

#### 戻り値 {#returns}

`TSelected`

***

### source {#source}

```ts
source: SubscribeSource<TableState<TFeatures>>;
```

定義元: [src/Subscribe.ts:24](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L24)
