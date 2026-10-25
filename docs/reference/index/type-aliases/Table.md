---
id: Table
title: Table
---

```ts
type Table<TFeatures, TData> = Table_Core<TFeatures, TData> & ExtractFeatureMapTypes<TFeatures, Table_FeatureMap<TFeatures, TData>>;
```

定義元: [types/Table.ts:79](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/Table.ts#L79)

テーブルのコアの機能と、テーブルの `features` オプションで有効にした機能の両方を持つテーブルオブジェクトです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)
