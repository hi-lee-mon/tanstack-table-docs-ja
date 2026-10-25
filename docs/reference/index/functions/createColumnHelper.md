---
id: createColumnHelper
title: createColumnHelper
---

```ts
function createColumnHelper<TFeatures, TData>(): ColumnHelper<TFeatures, TData>;
```

定義元: [helpers/columnHelper.ts:99](https://github.com/TanStack/table/blob/main/packages/table-core/src/helpers/columnHelper.ts#L99)

値の型推論を強めた列定義を書くためのヘルパー関数を作成します。

`accessor` はアクセサーのキーまたはアクセサー関数から `TValue` を推論し、`display` はデータを持たない列を、`group` は親の列を作成します。`columns` は配列に対してタプル単位の値の型を保ちます。
実行時には、これらのヘルパーは列定義のオブジェクトを返すだけです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## 戻り値 {#returns}

[`ColumnHelper`](../interfaces/ColumnHelper.md)\<`TFeatures`, `TData`\>

## 例 {#example}

```tsx
const helper = createColumnHelper<typeof features, Person>() // features is the result of `tableFeatures({})` helper
const columns = [
 helper.display({ id: 'actions', header: 'Actions' }),
 helper.accessor('firstName', {}),
 helper.accessor((row) => row.lastName, { id: 'lastName' }),
]
```
