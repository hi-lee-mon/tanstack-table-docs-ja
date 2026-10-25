---
id: skipFirstRun
title: skipFirstRun
---

```ts
function skipFirstRun(fn): () => void;
```

定義元: [utils.ts:350](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L350)

コールバックを包み、最初の呼び出しだけを読み飛ばすようにします。

行モデルの `onAfterUpdate` フックは、入力が変わったときに自動リセットを予約します。
行モデルの最初の計算は変更ではないので、そこで状態のリセットを起こしてはいけません。起こすと、マウント時に行モデルを読んだだけで初期状態や制御された状態が消えてしまいます。

## パラメーター {#parameters}

### fn {#fn}

() => `void`

## 戻り値 {#returns}

() => `void`
