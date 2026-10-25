---
id: filterFn_between
title: filterFn_between
---

```ts
const filterFn_between: CreatedFilterFn<any, any>;
```

定義元: [features/column-filtering/filterFns.ts:261](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/filterFns.ts#L261)

値が、両端を含まない最小値・最大値の組の間にある行を残します。

範囲の端が空の場合は、その側に制限がないものとして扱います。
