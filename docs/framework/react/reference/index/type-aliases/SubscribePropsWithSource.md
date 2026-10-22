---
id: SubscribePropsWithSource
title: SubscribePropsWithSource
---

```ts
type SubscribePropsWithSource<TSourceValue, TSelected> =
  | SubscribePropsWithSourceIdentity<TSourceValue>
| SubscribePropsWithSourceWithSelector<TSourceValue, TSelected>;
```

定義元: [src/Subscribe.ts:62](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L62)

単一の source（アトムまたはストア）を購読します（そのまま受け取るか、射影して受け取るか）。`selector` を省略する場合に
型推論を分かりやすくするには、[SubscribePropsWithSourceIdentity](SubscribePropsWithSourceIdentity.md) か [SubscribePropsWithSourceWithSelector](SubscribePropsWithSourceWithSelector.md)
を使ってください。

## 型パラメーター {#type-parameters}

### TSourceValue {#tsourcevalue}

`TSourceValue`

### TSelected {#tselected}

`TSelected` = `TSourceValue`
