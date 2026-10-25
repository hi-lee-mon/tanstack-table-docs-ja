---
id: RequiredKeys
title: RequiredKeys
---

```ts
type RequiredKeys<T, K> = Omit<T, K> & Required<Pick<T, K>>;
```

定義元: [types/type-utils.ts:19](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/type-utils.ts#L19)

## 型パラメーター {#type-parameters}

### T {#t}

`T`

### K {#k}

`K` *extends* keyof `T`
