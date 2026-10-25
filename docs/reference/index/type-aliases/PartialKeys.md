---
id: PartialKeys
title: PartialKeys
---

```ts
type PartialKeys<T, K> = Omit<T, K> & Partial<Pick<T, K>>;
```

定義元: [types/type-utils.ts:17](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/type-utils.ts#L17)

## 型パラメーター {#type-parameters}

### T {#t}

`T`

### K {#k}

`K` *extends* keyof `T`
