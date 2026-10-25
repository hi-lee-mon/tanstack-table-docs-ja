---
id: getFunctionNameInfo
title: getFunctionNameInfo
---

```ts
function getFunctionNameInfo(staticFnName, splitBy?): object;
```

定義元: [utils.ts:524](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L524)

関数名が `parentName_fnKey` の形式であるとみなし、`fnKey` と、`parentName.fnKey` 形式の `fnName` を返します。

最初の区切り文字でだけ分割します。そのため、`table__expandRows` のような内部 API 名の `fnKey` は `_expandRows` になります。

## パラメーター {#parameters}

### staticFnName {#staticfnname}

`string`

### splitBy? {#splitby}

`"."` \| `"_"`

## 戻り値 {#returns}

`object`

### fnKey {#fnkey}

```ts
fnKey: string;
```

### fnName {#fnname}

```ts
fnName: string;
```

### parentName {#parentname}

```ts
parentName: string;
```
