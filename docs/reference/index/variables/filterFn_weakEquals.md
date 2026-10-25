---
id: filterFn_weakEquals
title: filterFn_weakEquals
---

```ts
const filterFn_weakEquals: CreatedFilterFn<any, any>;
```

定義元: [features/column-filtering/filterFns.ts:89](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/filterFns.ts#L89)

列の値がフィルター値とゆるく等しい行を残します。

JavaScript の `==` で比較し、空のフィルター値は自動で取り除きます。文字列の入力を数値の行の値と照らし合わせたい場合に便利です。
