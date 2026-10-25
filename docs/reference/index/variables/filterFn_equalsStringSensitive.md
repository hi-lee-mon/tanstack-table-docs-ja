---
id: filterFn_equalsStringSensitive
title: filterFn_equalsStringSensitive
---

```ts
const filterFn_equalsStringSensitive: CreatedFilterFn<any, any>;
```

定義元: [features/column-filtering/filterFns.ts:143](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/filterFns.ts#L143)

文字列にした列の値が、フィルターのテキストと完全に一致する行を残します。

大文字と小文字を区別して比較し、空のフィルター値は自動で取り除きます。
