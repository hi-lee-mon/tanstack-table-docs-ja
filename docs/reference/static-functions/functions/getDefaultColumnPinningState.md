---
id: getDefaultColumnPinningState
title: getDefaultColumnPinningState
---

```ts
function getDefaultColumnPinningState(): ColumnPinningState;
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:35](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L35)

列の固定の既定の状態を作ります。

どちらの固定領域も空から始まります。`defaultState` が `true` のとき、リセット API はこの値を使います。

## 戻り値 {#returns}

[`ColumnPinningState`](../../index/interfaces/ColumnPinningState.md)

## 例 {#example}

```ts
const pinning = getDefaultColumnPinningState()
```
