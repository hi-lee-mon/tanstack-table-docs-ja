---
id: NoInfer
title: NoInfer
---

```ts
type NoInfer<T> = [T][T extends any ? 0 : never];
```

定義元: [types/type-utils.ts:87](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/type-utils.ts#L87)

## 型パラメーター {#type-parameters}

### T {#t}

`T`
