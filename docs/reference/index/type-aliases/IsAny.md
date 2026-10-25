---
id: IsAny
title: IsAny
---

```ts
type IsAny<T> = 0 extends 1 & T ? true : false;
```

定義元: [types/TableFeatures.ts:24](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L24)

型が `any` かどうかを判定します。

機能マップのヘルパーのいくつかは、`any` 用に別の分岐を必要とします。そうしないと、広いジェネリックな使い方でキーが1つもない型に絞り込まれてしまい、既知の機能の API がすべて公開されなくなるためです。

## 型パラメーター {#type-parameters}

### T {#t}

`T`
