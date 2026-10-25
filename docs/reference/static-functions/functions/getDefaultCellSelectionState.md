---
id: getDefaultCellSelectionState
title: getDefaultCellSelectionState
---

```ts
function getDefaultCellSelectionState(): CellSelectionState;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:45](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L45)

セル選択の既定の状態を作ります。

機能の既定値は空の選択です。`defaultState` が `true` のとき、リセット API はこの値を使います。

## 戻り値 {#returns}

[`CellSelectionState`](../../index/type-aliases/CellSelectionState.md)

## 例 {#example}

```ts
const selection = getDefaultCellSelectionState()
```
