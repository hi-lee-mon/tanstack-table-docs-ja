---
id: getDefaultSortingState
title: getDefaultSortingState
---

```ts
function getDefaultSortingState(): SortingState;
```

定義元: [features/row-sorting/rowSortingFeature.utils.ts:26](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.utils.ts#L26)

ソートの既定の状態を作ります。

機能の既定値は空の配列で、ソートされている列がない状態を表します。`defaultState` が `true` のとき、リセット API はこの値を使います。

## 戻り値 {#returns}

[`SortingState`](../../index/type-aliases/SortingState.md)

## 例 {#example}

```ts
const sorting = getDefaultSortingState()
```
