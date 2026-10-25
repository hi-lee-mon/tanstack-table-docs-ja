---
id: callMemoOrStaticFn
title: callMemoOrStaticFn
---

```ts
function callMemoOrStaticFn<TObject, TArgs, TReturn>(
   obj,
   fnKey,
   staticFn, ...
   args): TReturn;
```

定義元: [utils.ts:630](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L630)

オブジェクトにメモ化された関数があれば、ビルダーパターンでそれを実行します。なければ、渡された静的メソッドを使います。

## 型パラメーター {#type-parameters}

### TObject {#tobject}

`TObject` *extends* `Record`\<`string`, `any`\>

### TArgs {#targs}

`TArgs` *extends* `any`[]

### TReturn {#treturn}

`TReturn`

## パラメーター {#parameters}

### obj {#obj}

`TObject`

### fnKey {#fnkey}

`string`

### staticFn {#staticfn}

(`obj`, ...`args`) => `TReturn`

### args {#args}

...`TArgs`

## 戻り値 {#returns}

`TReturn`
