---
id: UnionToIntersection
title: UnionToIntersection
---

```ts
type UnionToIntersection<T> = T extends any ? (x) => any : never extends (x) => any ? R : never;
```

定義元: [types/type-utils.ts:22](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/type-utils.ts#L22)

## 型パラメーター {#type-parameters}

### T {#t}

`T`
