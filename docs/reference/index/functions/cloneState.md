---
id: cloneState
title: cloneState
---

```ts
function cloneState<T>(value): T;
```

定義元: [utils.ts:22](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L22)

プレーンでないオブジェクトはそのまま残し、テーブルの状態の値を複製します。

プレーンなオブジェクトと配列は再帰的にコピーされるため、状態の更新で既存の参照を書き換えずに済みます。

## 型パラメーター {#type-parameters}

### T {#t}

`T`

## パラメーター {#parameters}

### value {#value}

`T`

## 戻り値 {#returns}

`T`
