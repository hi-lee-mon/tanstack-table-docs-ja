---
id: table_getGlobalAutoFilterFn
title: table_getGlobalAutoFilterFn
---

```ts
function table_getGlobalAutoFilterFn(): CreatedFilterFn<any, any>;
```

定義元: [features/global-filtering/globalFilteringFeature.utils.ts:45](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/global-filtering/globalFilteringFeature.utils.ts#L45)

組み込みの、自動で決まるグローバルフィルターの関数を返します。

グローバルフィルタリングの既定は `includesString` です。これにより、グローバルフィルタリングできる列を対象に、検索ボックスのような照合ができます。

## 戻り値 {#returns}

[`CreatedFilterFn`](../../index/interfaces/CreatedFilterFn.md)\<`any`, `any`\>

## 例 {#example}

```ts
const filterFn = table_getGlobalAutoFilterFn()
```
