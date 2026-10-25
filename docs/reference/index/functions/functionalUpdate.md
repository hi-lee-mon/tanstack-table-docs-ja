---
id: functionalUpdate
title: functionalUpdate
---

```ts
function functionalUpdate<T>(updater, input): T;
```

定義元: [utils.ts:11](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L11)

TanStack のアップデーターを値に適用します。

アップデーターが関数なら前の値を渡して呼び出し、そうでなければアップデーターの値をそのまま返します。

## 型パラメーター {#type-parameters}

### T {#t}

`T`

## パラメーター {#parameters}

### updater {#updater}

[`Updater`](../type-aliases/Updater.md)\<`T`\>

### input {#input}

`T`

## 戻り値 {#returns}

`T`
