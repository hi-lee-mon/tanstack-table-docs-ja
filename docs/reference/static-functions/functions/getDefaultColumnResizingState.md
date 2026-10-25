---
id: getDefaultColumnResizingState
title: getDefaultColumnResizingState
---

```ts
function getDefaultColumnResizingState(): columnResizingState;
```

定義元: [features/column-resizing/columnResizingFeature.utils.ts:26](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.utils.ts#L26)

一時的な列幅の変更の、既定の状態を作ります。

機能の既定値は、ドラッグ操作をしていない状態を表します。`defaultState` が `true` のとき、リセット API はこの値を使います。

## 戻り値 {#returns}

[`columnResizingState`](../../index/interfaces/columnResizingState.md)

## 例 {#example}

```ts
const resizeInfo = getDefaultColumnResizingState()
```
