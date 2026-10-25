---
id: getDefaultColumnSizingState
title: getDefaultColumnSizingState
---

```ts
function getDefaultColumnSizingState(): ColumnSizingState;
```

定義元: [features/column-sizing/columnSizingFeature.utils.ts:31](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.utils.ts#L31)

確定した列幅の、既定の状態を作ります。

機能の既定値は空のマップです。そのため、列の幅は列定義の幅か、組み込みの幅の既定値になります。

## 戻り値 {#returns}

[`ColumnSizingState`](../../index/type-aliases/ColumnSizingState.md)

## 例 {#example}

```ts
const sizing = getDefaultColumnSizingState()
```
