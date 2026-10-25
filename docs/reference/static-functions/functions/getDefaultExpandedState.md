---
id: getDefaultExpandedState
title: getDefaultExpandedState
---

```ts
function getDefaultExpandedState(): ExpandedState;
```

定義元: [features/row-expanding/rowExpandingFeature.utils.ts:22](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.utils.ts#L22)

展開の既定の状態を作ります。

機能の既定値は空のマップで、展開されている行がない状態を表します。`defaultState` が `true` のとき、リセット API はこの値を使います。

## 戻り値 {#returns}

[`ExpandedState`](../../index/type-aliases/ExpandedState.md)

## 例 {#example}

```ts
const expanded = getDefaultExpandedState()
```
