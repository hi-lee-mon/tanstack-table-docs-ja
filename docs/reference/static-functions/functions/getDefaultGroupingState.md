---
id: getDefaultGroupingState
title: getDefaultGroupingState
---

```ts
function getDefaultGroupingState(): GroupingState;
```

定義元: [features/column-grouping/columnGroupingFeature.utils.ts:24](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.utils.ts#L24)

グループ化の既定の状態を作ります。

機能の既定値は空の配列で、グループ化されている列がない状態を表します。`defaultState` が `true` のとき、リセット API はこの値を使います。

## 戻り値 {#returns}

[`GroupingState`](../../index/type-aliases/GroupingState.md)

## 例 {#example}

```ts
const grouping = getDefaultGroupingState()
```
