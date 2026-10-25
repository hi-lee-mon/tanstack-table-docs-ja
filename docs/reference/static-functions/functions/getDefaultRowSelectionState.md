---
id: getDefaultRowSelectionState
title: getDefaultRowSelectionState
---

```ts
function getDefaultRowSelectionState(): RowSelectionState;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:31](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L31)

行選択の既定の状態を作ります。

機能の既定値は空のマップで、選択されている行がない状態を表します。`defaultState` が `true` のとき、リセット API はこの値を使います。

## 戻り値 {#returns}

[`RowSelectionState`](../../index/type-aliases/RowSelectionState.md)

## 例 {#example}

```ts
const selection = getDefaultRowSelectionState()
```
