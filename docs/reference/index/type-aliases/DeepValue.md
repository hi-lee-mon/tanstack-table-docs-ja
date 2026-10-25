---
id: DeepValue
title: DeepValue
---

```ts
type DeepValue<T, TProp> = T extends null | undefined ? undefined : T extends Record<string | number, any> ? TProp extends `${infer TBranch}.${infer TDeepProp}` ? DeepValue<T[TBranch], TDeepProp> : T[TProp & keyof T] : never;
```

定義元: [types/type-utils.ts:79](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/type-utils.ts#L79)

## 型パラメーター {#type-parameters}

### T {#t}

`T`

### TProp {#tprop}

`TProp`
