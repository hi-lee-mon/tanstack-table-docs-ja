---
id: getDefaultColumnOrderState
title: getDefaultColumnOrderState
---

```ts
function getDefaultColumnOrderState(): ColumnOrderState;
```

定義元: [features/column-ordering/columnOrderingFeature.utils.ts:30](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.utils.ts#L30)

列の並び順の既定の状態を作ります。

機能の既定値は空の配列で、末端の列が定義どおりの順を保つことを表します。`defaultState` が `true` のとき、リセット API はこの値を使います。

## 戻り値 {#returns}

[`ColumnOrderState`](../../index/type-aliases/ColumnOrderState.md)

## 例 {#example}

```ts
const order = getDefaultColumnOrderState()
```
