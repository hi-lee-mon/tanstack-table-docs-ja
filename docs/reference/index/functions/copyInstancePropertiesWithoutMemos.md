---
id: copyInstancePropertiesWithoutMemos
title: copyInstancePropertiesWithoutMemos
---

```ts
function copyInstancePropertiesWithoutMemos<TTarget, TSource>(target, source): TTarget & TSource;
```

定義元: [utils.ts:58](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L58)

プロトタイプインスタンスの自身のプロパティをコピーします。遅延作成されるメモのクロージャーと行ごとのセルのキャッシュは引き継ぎません。どちらもコピー元のインスタンスに結び付いているためです（キャッシュされたセルはコピー元の行を参照しています）。

## 型パラメーター {#type-parameters}

### TTarget {#ttarget}

`TTarget` *extends* `Record`\<`string`, `any`\>

### TSource {#tsource}

`TSource` *extends* `Record`\<`string`, `any`\>

## パラメーター {#parameters}

### target {#target}

`TTarget`

### source {#source}

`TSource`

## 戻り値 {#returns}

`TTarget` & `TSource`
