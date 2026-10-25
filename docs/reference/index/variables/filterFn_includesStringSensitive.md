---
id: filterFn_includesStringSensitive
title: filterFn_includesStringSensitive
---

```ts
const filterFn_includesStringSensitive: CreatedFilterFn<any, any>;
```

定義元: [features/column-filtering/filterFns.ts:101](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/filterFns.ts#L101)

文字列にした列の値が、フィルターのテキストを含む行を残します。

大文字と小文字を区別して比較し、空のフィルター値は自動で取り除きます。
