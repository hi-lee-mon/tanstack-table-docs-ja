---
id: tableMemo
title: tableMemo
---

```ts
function tableMemo<TFeatures, TDeps, TDepArgs, TResult>(__namedParameters): (depArgs?) => TResult;
```

定義元: [utils.ts:387](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L387)

テーブル向けのメモ化関数を作成します。

`memo` をテーブルのデバッグオプションと機能のメタデータで包みます。これにより、行モデルや派生 API が同じ形式の診断情報を共有できます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TDeps {#tdeps}

`TDeps` *extends* readonly `any`[]

### TDepArgs {#tdepargs}

`TDepArgs`

### TResult {#tresult}

`TResult`

## パラメーター {#parameters}

### \_\_namedParameters {#namedparameters}

`TableMemoOptions`\<`TFeatures`, `TDeps`, `TDepArgs`, `TResult`\>

## 戻り値 {#returns}

(`depArgs?`) => `TResult`
