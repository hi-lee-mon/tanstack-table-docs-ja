---
id: filterFn_equalsString
title: filterFn_equalsString
---

```ts
const filterFn_equalsString: CreatedFilterFn<any, any>;
```

定義元: [features/column-filtering/filterFns.ts:130](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/filterFns.ts#L130)

文字列にした列の値が、フィルターのテキストと等しい行を残します。

どちらの値も比較の前に小文字に変換され、空のフィルター値は自動で取り除かれます。
