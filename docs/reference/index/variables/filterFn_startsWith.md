---
id: filterFn_startsWith
title: filterFn_startsWith
---

```ts
const filterFn_startsWith: CreatedFilterFn<any, any>;
```

定義元: [features/column-filtering/filterFns.ts:158](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/filterFns.ts#L158)

文字列にした列の値が、フィルターのテキストで始まる行を残します。

どちらの値も比較の前に小文字に変換され、空のフィルター値は自動で取り除かれます。
