---
id: reSplitAlphaNumeric
title: reSplitAlphaNumeric
---

```ts
const reSplitAlphaNumeric: RegExp;
```

定義元: [features/row-sorting/sortFns.ts:12](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/sortFns.ts#L12)

テキストと数値が混ざった部分を分割するための正規表現です。

英数字のソート関数は、この分割結果を使って、`item2` が `item10` より前に来るような自然な並びで文字列をソートします。
