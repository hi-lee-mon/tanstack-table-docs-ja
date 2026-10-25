---
id: filterFn_endsWith
title: filterFn_endsWith
---

```ts
const filterFn_endsWith: CreatedFilterFn<any, any>;
```

定義元: [features/column-filtering/filterFns.ts:173](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/filterFns.ts#L173)

文字列にした列の値が、フィルターのテキストで終わる行を残します。

どちらの値も比較の前に小文字に変換され、空のフィルター値は自動で取り除かれます。
