---
id: filterFn_inNumberRange
title: filterFn_inNumberRange
---

```ts
const filterFn_inNumberRange: CreatedFilterFn<any, any>;
```

定義元: [features/column-filtering/filterFns.ts:290](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/filterFns.ts#L290)

数値の値が、両端を含む `[min, max]` の範囲内にある行を残します。

フィルター値は正規化され、空の端は制限なしとして扱い、逆順の端は入れ替えます。範囲内に入るのは本当の数値だけで、数値でない行の値（`null`、`undefined`、文字列、真偽値）は一致しません。
