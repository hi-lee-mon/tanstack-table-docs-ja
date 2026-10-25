---
id: makeObjectMap
title: makeObjectMap
---

```ts
function makeObjectMap<TValue>(): Record<string, TValue>;
```

定義元: [utils.ts:81](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L81)

文字列キーの辞書として引くためだけのオブジェクトを作成します。

null プロトタイプにしているので、`__proto__` や `hasOwnProperty` のような利用者が決める ID も、ただのデータのキーとして扱われます。

## 型パラメーター {#type-parameters}

### TValue {#tvalue}

`TValue` = `unknown`

## 戻り値 {#returns}

`Record`\<`string`, `TValue`\>
