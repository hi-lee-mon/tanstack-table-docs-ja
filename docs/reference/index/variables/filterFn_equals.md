---
id: filterFn_equals
title: filterFn_equals
---

```ts
const filterFn_equals: CreatedFilterFn<any, any>;
```

定義元: [features/column-filtering/filterFns.ts:78](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/filterFns.ts#L78)

列の値がフィルター値と厳密に等しい行を残します。

JavaScript の `===` で比較し、空のフィルター値は自動で取り除きます。
