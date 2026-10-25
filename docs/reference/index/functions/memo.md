---
id: memo
title: memo
---

```ts
function memo<TDeps, TDepArgs, TResult>(__namedParameters): (depArgs?) => TResult;
```

定義元: [utils.ts:299](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L299)

テーブルの内部処理向けに、依存関係を追跡するメモ化関数を作成します。

メモは依存関係のタプルが変わったときだけ再計算され、デバッグ用の計測情報を出力できます。

## 型パラメーター {#type-parameters}

### TDeps {#tdeps}

`TDeps` *extends* readonly `any`[]

### TDepArgs {#tdepargs}

`TDepArgs`

### TResult {#tresult}

`TResult`

## パラメーター {#parameters}

### \_\_namedParameters {#namedparameters}

`MemoOptions`\<`TDeps`, `TDepArgs`, `TResult`\>

## 戻り値 {#returns}

(`depArgs?`) => `TResult`
