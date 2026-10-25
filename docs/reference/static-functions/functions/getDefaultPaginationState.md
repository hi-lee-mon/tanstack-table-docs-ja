---
id: getDefaultPaginationState
title: getDefaultPaginationState
---

```ts
function getDefaultPaginationState(): PaginationState;
```

定義元: [features/row-pagination/rowPaginationFeature.utils.ts:21](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.utils.ts#L21)

ページネーションの機能で使う、ページネーションの既定の状態を作ります。

機能の既定値は、最初のページから始まり、ページサイズは 10 です。`defaultState` が `true` のとき、リセット API はこの値を使います。

## 戻り値 {#returns}

[`PaginationState`](../../index/interfaces/PaginationState.md)

## 例 {#example}

```ts
const pagination = getDefaultPaginationState()
```
