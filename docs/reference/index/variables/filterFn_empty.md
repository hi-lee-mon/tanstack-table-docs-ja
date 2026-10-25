---
id: filterFn_empty
title: filterFn_empty
---

```ts
const filterFn_empty: CreatedFilterFn<any, any>;
```

定義元: [features/column-filtering/filterFns.ts:190](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/filterFns.ts#L190)

列の値が空の行を残します。

値は、null や undefined のとき、または文字列にすると空白だけになるときに空とみなします。フィルター値はオン・オフのフラグとして働き、`false` と空の値は自動で取り除かれます。
