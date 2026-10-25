---
id: Prettify
title: Prettify
---

```ts
type Prettify<T> = { [K in keyof T]: T[K] } & unknown;
```

定義元: [types/type-utils.ts:91](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/type-utils.ts#L91)

## 型パラメーター {#type-parameters}

### T {#t}

`T`
