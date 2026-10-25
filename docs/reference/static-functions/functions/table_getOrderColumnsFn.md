---
id: table_getOrderColumnsFn
title: table_getOrderColumnsFn
---

```ts
function table_getOrderColumnsFn<TFeatures, TData>(table): (columns) => Column_Internal<TFeatures, TData, unknown>[];
```

定義元: [features/column-ordering/columnOrderingFeature.utils.ts:200](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.utils.ts#L200)

末端の列を並べるための、並び順の関数を作ります。

返される関数は `state.columnOrder` を適用し、指定されていない列は元の順を保ちます。そのあと、グループ化の決まりに処理を任せます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

(`columns`) => [`Column_Internal`](../../index/interfaces/Column_Internal.md)\<`TFeatures`, `TData`, `unknown`\>[]

## 例 {#example}

```ts
const orderColumnsForTable = table_getOrderColumnsFn(table)
```
