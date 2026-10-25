---
id: table_getRowsInDisplayOrder
title: table_getRowsInDisplayOrder
---

```ts
function table_getRowsInDisplayOrder<TFeatures, TData>(table): Row<TFeatures, TData>[];
```

定義元: [core/rows/coreRowsFeature.utils.ts:32](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.utils.ts#L32)

0始まりの表示インデックスを割り当てたうえで、現在の表示順で行を返します。

展開された行がページネーションを素通りする場合は、ページネーション前の行モデルに含まれていなくても、展開された子孫が返す順に挿入されます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>[]
