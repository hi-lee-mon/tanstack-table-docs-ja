---
id: getDefaultRowPinningState
title: getDefaultRowPinningState
---

```ts
function getDefaultRowPinningState(): RowPinningState;
```

定義元: [features/row-pinning/rowPinningFeature.utils.ts:25](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.utils.ts#L25)

行の固定の既定の状態を作ります。

どちらの固定領域も空から始まります。`defaultState` が `true` のとき、リセット API はこの値を使います。

## 戻り値 {#returns}

[`RowPinningState`](../../index/interfaces/RowPinningState.md)

## 例 {#example}

```ts
const pinning = getDefaultRowPinningState()
```
