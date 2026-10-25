---
id: NonFeatureKeys
title: NonFeatureKeys
---

```ts
type NonFeatureKeys =
  | "aggregationFns"
  | "columnMeta"
  | "coreRowModel"
  | "expandedRowModel"
  | "facetedMinMaxValues"
  | "facetedRowModel"
  | "facetedUniqueValues"
  | "filterFns"
  | "filterMeta"
  | "filteredRowModel"
  | "groupedRowModel"
  | "paginatedRowModel"
  | "sortFns"
  | "sortedRowModel"
  | "tableMeta";
```

定義元: [types/TableFeatures.ts:70](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L70)

`features` オプションのキーのうち、テーブルの機能そのものではないものです。

これらのスロットは、テーブルごとの型（`tableMeta`、`columnMeta`）、行モデルのファクトリー、行モデル関数のレジストリを持ちます。
実行時にはテーブルに登録される `_features` から取り除かれ、生成される `debug*` キーのような、機能から導き出すオプションからも除外されます。
