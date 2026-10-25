---
id: FeatureSlotPrereqs
title: FeatureSlotPrereqs
---

定義元: [types/TableFeatures.ts:94](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L94)

各行モデルと関数レジストリのスロットを、同じ features オブジェクトに一緒に登録しなければならない機能に対応付けます。

カスタム機能は、宣言のマージでこのインターフェースに自分のスロットの前提条件を追加できます。そうすると、`tableFeatures()` で同じ検証を受けられます。

## プロパティ {#properties}

### aggregationFns {#aggregationfns}

```ts
aggregationFns: "rowAggregationFeature";
```

定義元: [types/TableFeatures.ts:98](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L98)

名前付きの集計関数には、独立した集計機能が必要です。

***

### columnResizingFeature {#columnresizingfeature}

```ts
columnResizingFeature: "columnSizingFeature";
```

定義元: [types/TableFeatures.ts:102](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L102)

列幅の変更は、列幅の状態と API の上に成り立っています。

***

### expandedRowModel {#expandedrowmodel}

```ts
expandedRowModel: "rowExpandingFeature";
```

定義元: [types/TableFeatures.ts:106](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L106)

展開済み行モデルのファクトリーには、行の展開の API と状態が必要です。

***

### facetedMinMaxValues {#facetedminmaxvalues}

```ts
facetedMinMaxValues: "columnFacetingFeature";
```

定義元: [types/TableFeatures.ts:110](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L110)

ファセットの最小値・最大値のファクトリーには、列のファセットの API が必要です。

***

### facetedRowModel {#facetedrowmodel}

```ts
facetedRowModel: "columnFacetingFeature";
```

定義元: [types/TableFeatures.ts:114](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L114)

ファセット行モデルのファクトリーには、列のファセットの API が必要です。

***

### facetedUniqueValues {#faceteduniquevalues}

```ts
facetedUniqueValues: "columnFacetingFeature";
```

定義元: [types/TableFeatures.ts:118](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L118)

ファセットの一意な値のファクトリーには、列のファセットの API が必要です。

***

### filteredRowModel {#filteredrowmodel}

```ts
filteredRowModel: "columnFilteringFeature";
```

定義元: [types/TableFeatures.ts:122](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L122)

フィルター済み行モデルのファクトリーには、列フィルタリングの API と状態が必要です。

***

### filterFns {#filterfns}

```ts
filterFns: "columnFilteringFeature";
```

定義元: [types/TableFeatures.ts:126](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L126)

名前付きのフィルター関数は、列フィルタリングが有効なときにだけ意味を持ちます。

***

### filterMeta {#filtermeta}

```ts
filterMeta: "columnFilteringFeature";
```

定義元: [types/TableFeatures.ts:130](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L130)

フィルターのメタデータの型を読み書きするのは、フィルタリングの機能だけです。

***

### globalFilteringFeature {#globalfilteringfeature}

```ts
globalFilteringFeature: "columnFilteringFeature";
```

定義元: [types/TableFeatures.ts:134](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L134)

グローバルフィルタリングは、列フィルタリングの状態とフィルター関数の上に成り立っています。

***

### groupedRowModel {#groupedrowmodel}

```ts
groupedRowModel: "columnGroupingFeature";
```

定義元: [types/TableFeatures.ts:138](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L138)

グループ化済み行モデルのファクトリーには、列のグループ化の API と状態が必要です。

***

### paginatedRowModel {#paginatedrowmodel}

```ts
paginatedRowModel: "rowPaginationFeature";
```

定義元: [types/TableFeatures.ts:142](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L142)

ページ分割済み行モデルのファクトリーには、行のページネーションの API と状態が必要です。

***

### sortedRowModel {#sortedrowmodel}

```ts
sortedRowModel: "rowSortingFeature";
```

定義元: [types/TableFeatures.ts:146](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L146)

ソート済み行モデルのファクトリーには、行のソートの API と状態が必要です。

***

### sortFns {#sortfns}

```ts
sortFns: "rowSortingFeature";
```

定義元: [types/TableFeatures.ts:150](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L150)

名前付きのソート関数は、行のソートが有効なときにだけ意味を持ちます。
