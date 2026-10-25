---
id: filterFn_greaterThan
title: filterFn_greaterThan
---

```ts
const filterFn_greaterThan: CreatedFilterFn<any, any>;
```

定義元: [features/column-filtering/filterFns.ts:215](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/filterFns.ts#L215)

値がフィルター値より大きい行を残します。

両方の値を数値に変換できる場合は数値として比べます。そうでなければ、正規化した文字列どうしで比べます。
