---
id: filterFn_inDateRange
title: filterFn_inDateRange
---

```ts
const filterFn_inDateRange: CreatedFilterFn<any, any>;
```

定義元: [features/column-filtering/filterFns.ts:336](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/filterFns.ts#L336)

日付の値が、両端を含む `[min, max]` の日付の範囲内にある行を残します。

行の値と範囲の端には、`Date` オブジェクト、タイムスタンプ、日付として解釈できる文字列を使えます。空や無効な端は制限なしとして扱い、逆順の端は入れ替えます。有効な日付を持たない行は一致しません。
