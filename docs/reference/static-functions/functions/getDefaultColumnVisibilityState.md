---
id: getDefaultColumnVisibilityState
title: getDefaultColumnVisibilityState
---

```ts
function getDefaultColumnVisibilityState(): ColumnVisibilityState;
```

定義元: [features/column-visibility/columnVisibilityFeature.utils.ts:28](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.utils.ts#L28)

列の表示の、既定の状態を作ります。

機能の既定値は空のオブジェクトで、含まれない列 ID は表示されているものとして扱います。`defaultState` が `true` のとき、リセット API はこの値を使います。

## 戻り値 {#returns}

[`ColumnVisibilityState`](../../index/type-aliases/ColumnVisibilityState.md)

## 例 {#example}

```ts
const visibility = getDefaultColumnVisibilityState()
```
