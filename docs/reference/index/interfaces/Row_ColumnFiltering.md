---
id: Row_ColumnFiltering
title: Row_ColumnFiltering
---

定義元: [features/column-filtering/columnFilteringFeature.types.ts:231](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L231)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### _TData {#_tdata}

`_TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### columnFilters {#columnfilters}

```ts
columnFilters: Record<string, boolean>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:238](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L238)

行の列フィルターのマップです。このオブジェクトは、行が各フィルターに通ったかどうかを列 ID ごとに記録します。

***

### columnFiltersMeta {#columnfiltersmeta}

```ts
columnFiltersMeta: Record<string, ExtractFilterMeta<TFeatures>>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:242](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L242)

行の列フィルターのメタデータのマップです。このオブジェクトは、フィルタリングの処理中に任意で渡された、行のフィルターのメタデータを記録します。
