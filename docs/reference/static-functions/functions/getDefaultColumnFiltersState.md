---
id: getDefaultColumnFiltersState
title: getDefaultColumnFiltersState
---

```ts
function getDefaultColumnFiltersState(): ColumnFiltersState;
```

定義元: [features/column-filtering/columnFilteringFeature.utils.ts:27](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.utils.ts#L27)

列フィルターの既定の状態を作ります。

機能の既定値は空の配列で、有効な列フィルターがない状態を表します。`defaultState` が `true` のとき、リセット API はこの値を使います。

## 戻り値 {#returns}

[`ColumnFiltersState`](../../index/type-aliases/ColumnFiltersState.md)

## 例 {#example}

```ts
const filters = getDefaultColumnFiltersState()
```
