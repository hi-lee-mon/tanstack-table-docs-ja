---
id: LegacyRowModelOptions
title: LegacyRowModelOptions
---

定義元: [src/useLegacyTable.ts:208](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L208)

v8 スタイルのレガシーな行モデルのオプションです。

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## プロパティ {#properties}

### ~~aggregationFns?~~ {#aggregationfns}

```ts
optional aggregationFns?: AggregationFns;
```

定義元: [src/useLegacyTable.ts:268](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L268)

テーブルに適用する追加の集計関数です。

#### 非推奨 {#deprecated}

代わりに、`rowAggregationFeature` と `aggregationFns` スロットを使ってください。`columnGroupingFeature` と `groupedRowModel` は、行をグループ化する場合にだけ追加します。

***

### ~~filterFns?~~ {#filterfns}

```ts
optional filterFns?: FilterFns;
```

定義元: [src/useLegacyTable.ts:258](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L258)

テーブルに適用する追加のフィルター関数です。

#### 非推奨 {#deprecated-1}

代わりに、`features` オプションの `filteredRowModel`/`filterFns` スロットと `createFilteredRowModel()` を使ってください。

***

### ~~getCoreRowModel?~~ {#getcorerowmodel}

```ts
optional getCoreRowModel?: RowModelFactory<TData>;
```

定義元: [src/useLegacyTable.ts:213](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L213)

テーブルのコア行モデルを返します。

#### 非推奨 {#deprecated-2}

このオプションは v9 では不要です。コア行モデルは常に自動で作成されます。

***

### ~~getExpandedRowModel?~~ {#getexpandedrowmodel}

```ts
optional getExpandedRowModel?: RowModelFactory<TData>;
```

定義元: [src/useLegacyTable.ts:233](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L233)

テーブルの展開済み行モデルを返します。

#### 非推奨 {#deprecated-3}

代わりに、`features` オプションの `expandedRowModel` スロットと `createExpandedRowModel()` を使ってください。

***

### ~~getFacetedMinMaxValues?~~ {#getfacetedminmaxvalues}

```ts
optional getFacetedMinMaxValues?: FacetedMinMaxValuesFactory<TData>;
```

定義元: [src/useLegacyTable.ts:248](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L248)

列のファセットの最小値と最大値を返します。

#### 非推奨 {#deprecated-4}

代わりに、`features` オプションの `facetedMinMaxValues` スロットと `createFacetedMinMaxValues()` を使ってください。

***

### ~~getFacetedRowModel?~~ {#getfacetedrowmodel}

```ts
optional getFacetedRowModel?: FacetedRowModelFactory<TData>;
```

定義元: [src/useLegacyTable.ts:243](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L243)

列のファセット行モデルを返します。

#### 非推奨 {#deprecated-5}

代わりに、`features` オプションの `facetedRowModel` スロットと `createFacetedRowModel()` を使ってください。

***

### ~~getFacetedUniqueValues?~~ {#getfaceteduniquevalues}

```ts
optional getFacetedUniqueValues?: FacetedUniqueValuesFactory<TData>;
```

定義元: [src/useLegacyTable.ts:253](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L253)

列のファセットの一意な値を返します。

#### 非推奨 {#deprecated-6}

代わりに、`features` オプションの `facetedUniqueValues` スロットと `createFacetedUniqueValues()` を使ってください。

***

### ~~getFilteredRowModel?~~ {#getfilteredrowmodel}

```ts
optional getFilteredRowModel?: RowModelFactory<TData>;
```

定義元: [src/useLegacyTable.ts:218](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L218)

テーブルのフィルター済み行モデルを返します。

#### 非推奨 {#deprecated-7}

代わりに、`features` オプションの `filteredRowModel`/`filterFns` スロットと `createFilteredRowModel()` を使ってください。

***

### ~~getGroupedRowModel?~~ {#getgroupedrowmodel}

```ts
optional getGroupedRowModel?: RowModelFactory<TData>;
```

定義元: [src/useLegacyTable.ts:238](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L238)

テーブルのグループ化済み行モデルを返します。

#### 非推奨 {#deprecated-8}

代わりに、`columnGroupingFeature` と `groupedRowModel` スロット、`createGroupedRowModel()` を使ってください。グループ化した行で値を集計する場合は、`rowAggregationFeature` を別途追加します。

***

### ~~getPaginationRowModel?~~ {#getpaginationrowmodel}

```ts
optional getPaginationRowModel?: RowModelFactory<TData>;
```

定義元: [src/useLegacyTable.ts:228](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L228)

テーブルのページ分割済み行モデルを返します。

#### 非推奨 {#deprecated-9}

代わりに、`features` オプションの `paginatedRowModel` スロットと `createPaginatedRowModel()` を使ってください。

***

### ~~getSortedRowModel?~~ {#getsortedrowmodel}

```ts
optional getSortedRowModel?: RowModelFactory<TData>;
```

定義元: [src/useLegacyTable.ts:223](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L223)

テーブルのソート済み行モデルを返します。

#### 非推奨 {#deprecated-10}

代わりに、`features` オプションの `sortedRowModel`/`sortFns` スロットと `createSortedRowModel()` を使ってください。

***

### ~~sortFns?~~ {#sortfns}

```ts
optional sortFns?: SortFns;
```

定義元: [src/useLegacyTable.ts:263](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L263)

テーブルに適用する追加のソート関数です。

#### 非推奨 {#deprecated-11}

代わりに、`features` オプションの `sortedRowModel`/`sortFns` スロットと `createSortedRowModel()` を使ってください。
