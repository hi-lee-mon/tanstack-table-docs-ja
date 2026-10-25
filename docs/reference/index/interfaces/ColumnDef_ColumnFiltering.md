---
id: ColumnDef_ColumnFiltering
title: ColumnDef_ColumnFiltering
---

定義元: [features/column-filtering/columnFilteringFeature.types.ts:177](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L177)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### enableColumnFilter? {#enablecolumnfilter}

```ts
optional enableColumnFilter?: boolean;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:187](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L187)

この列を、列ごとのフィルタリングの対象にします。

既定値は `true` です。テーブル側の `enableColumnFilters` と `enableFilters` でもフィルタリングが許可されている必要があります。

***

### filterFn? {#filterfn}

```ts
optional filterFn?: FilterFnOption<TFeatures, TData>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:191](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L191)

この列で使うフィルター関数です。組み込みのフィルター関数の名前か、カスタムのフィルター関数を指定できます。
