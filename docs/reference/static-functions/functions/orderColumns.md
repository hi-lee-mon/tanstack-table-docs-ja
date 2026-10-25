---
id: orderColumns
title: orderColumns
---

```ts
function orderColumns<TFeatures, TData>(table, leafColumns): Column_Internal<TFeatures, TData, unknown>[];
```

定義元: [features/column-ordering/columnOrderingFeature.utils.ts:259](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.utils.ts#L259)

並び順が決まった末端の列のリストに、グループ化された列の配置の決まりを適用します。

`groupedColumnMode: 'remove'` は、グループ化された列をリストから取り除きます。
`groupedColumnMode: 'reorder'` は、グループ化された列をグループ化の状態の順で先頭に移します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### leafColumns {#leafcolumns}

[`Column_Internal`](../../index/interfaces/Column_Internal.md)\<`TFeatures`, `TData`, `unknown`\>[]

## 戻り値 {#returns}

[`Column_Internal`](../../index/interfaces/Column_Internal.md)\<`TFeatures`, `TData`, `unknown`\>[]

## 例 {#example}

```ts
const orderedColumns = orderColumns(table, leafColumns)
```
