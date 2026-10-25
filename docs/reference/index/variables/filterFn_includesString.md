---
id: filterFn_includesString
title: filterFn_includesString
---

```ts
const filterFn_includesString: CreatedFilterFn<any, any>;
```

定義元: [features/column-filtering/filterFns.ts:116](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/filterFns.ts#L116)

文字列にした列の値が、フィルターのテキストを含む行を残します。

どちらの値も比較の前に小文字に変換され、空のフィルター値は自動で取り除かれます。
