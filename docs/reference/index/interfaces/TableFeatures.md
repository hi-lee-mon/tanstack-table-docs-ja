---
id: TableFeatures
title: TableFeatures
---

定義元: [types/TableFeatures.ts:184](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L184)

テーブルの機能のレジストリ全体です。

この型は、コア機能、標準機能、宣言のマージで追加したカスタムプラグイン、行モデルのファクトリーのスロット、関数レジストリ、型専用の meta のスロットをまとめたものです。
`tableFeatures()` に渡す具体的な `features` オブジェクトによって、テーブル・行・列・セル・ヘッダー・オプション・状態の型にどの機能の API が含まれるかが決まります。

## 継承元 {#extends}

- `Partial`\<[`CoreFeatures`](CoreFeatures.md)\>.`Partial`\<[`StockFeatures`](StockFeatures.md)\>.`Partial`\<[`Plugins`](Plugins.md)\>

## プロパティ {#properties}

### aggregationFns? {#aggregationfns}

```ts
optional aggregationFns?: Record<string, AggregationFnDef<any, any, any, any>>;
```

定義元: [types/TableFeatures.ts:196](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L196)

このテーブルで名前を使って指定できる、集計関数のレジストリです。

ここに登録したキーが、列定義の `aggregationFn` に指定できる文字列になり、型も完全に推論されます。
使う組み込みの集計関数は個別に import し、慣例の名前で登録してください: `aggregationFns: { sum: aggregationFn_sum, myCustomAggregationFn }`。
エクスポートされている `aggregationFns` レジストリをスプレッドしても動きますが、組み込みの集計関数がすべてバンドルに含まれます。

***

### cellSelectionFeature? {#cellselectionfeature}

```ts
optional cellSelectionFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:20](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L20)

#### 継承元のメンバー {#inherited-from}

[`StockFeatures`](StockFeatures.md).[`cellSelectionFeature`](StockFeatures.md#cellselectionfeature)

***

### cellSpanningFeature? {#cellspanningfeature}

```ts
optional cellSpanningFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:21](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L21)

#### 継承元のメンバー {#inherited-from-1}

[`StockFeatures`](StockFeatures.md).[`cellSpanningFeature`](StockFeatures.md#cellspanningfeature)

***

### columnFacetingFeature? {#columnfacetingfeature}

```ts
optional columnFacetingFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:22](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L22)

#### 継承元のメンバー {#inherited-from-2}

[`StockFeatures`](StockFeatures.md).[`columnFacetingFeature`](StockFeatures.md#columnfacetingfeature)

***

### columnFilteringFeature? {#columnfilteringfeature}

```ts
optional columnFilteringFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:23](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L23)

#### 継承元のメンバー {#inherited-from-3}

[`StockFeatures`](StockFeatures.md).[`columnFilteringFeature`](StockFeatures.md#columnfilteringfeature)

***

### columnGroupingFeature? {#columngroupingfeature}

```ts
optional columnGroupingFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:24](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L24)

#### 継承元のメンバー {#inherited-from-4}

[`StockFeatures`](StockFeatures.md).[`columnGroupingFeature`](StockFeatures.md#columngroupingfeature)

***

### columnMeta? {#columnmeta}

```ts
optional columnMeta?: object;
```

定義元: [types/TableFeatures.ts:207](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L207)

このテーブルのすべての列の `columnDef.meta` の型を宣言するための、型専用のスロットです。

実体のない値を渡してください: `columnMeta: {} as MyColumnMeta`。値そのものは実行時に無視され、テーブルに登録された機能から取り除かれます。使われるのは型だけで、`TFeatures` が渡る先々で推論されます。

省略した場合は、グローバルに宣言のマージをした `ColumnMeta` インターフェースが使われます。

***

### columnOrderingFeature? {#columnorderingfeature}

```ts
optional columnOrderingFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:25](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L25)

#### 継承元のメンバー {#inherited-from-5}

[`StockFeatures`](StockFeatures.md).[`columnOrderingFeature`](StockFeatures.md#columnorderingfeature)

***

### columnPinningFeature? {#columnpinningfeature}

```ts
optional columnPinningFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:26](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L26)

#### 継承元のメンバー {#inherited-from-6}

[`StockFeatures`](StockFeatures.md).[`columnPinningFeature`](StockFeatures.md#columnpinningfeature)

***

### columnResizingFeature? {#columnresizingfeature}

```ts
optional columnResizingFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:27](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L27)

#### 継承元のメンバー {#inherited-from-7}

[`StockFeatures`](StockFeatures.md).[`columnResizingFeature`](StockFeatures.md#columnresizingfeature)

***

### columnSizingFeature? {#columnsizingfeature}

```ts
optional columnSizingFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:28](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L28)

#### 継承元のメンバー {#inherited-from-8}

[`StockFeatures`](StockFeatures.md).[`columnSizingFeature`](StockFeatures.md#columnsizingfeature)

***

### columnVisibilityFeature? {#columnvisibilityfeature}

```ts
optional columnVisibilityFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:29](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L29)

#### 継承元のメンバー {#inherited-from-9}

[`StockFeatures`](StockFeatures.md).[`columnVisibilityFeature`](StockFeatures.md#columnvisibilityfeature)

***

### coreCellsFeature? {#corecellsfeature}

```ts
optional coreCellsFeature?: TableFeature;
```

定義元: [core/coreFeatures.ts:11](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/coreFeatures.ts#L11)

#### 継承元のメンバー {#inherited-from-10}

[`CoreFeatures`](CoreFeatures.md).[`coreCellsFeature`](CoreFeatures.md#corecellsfeature)

***

### coreColumnsFeature? {#corecolumnsfeature}

```ts
optional coreColumnsFeature?: TableFeature;
```

定義元: [core/coreFeatures.ts:12](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/coreFeatures.ts#L12)

#### 継承元のメンバー {#inherited-from-11}

[`CoreFeatures`](CoreFeatures.md).[`coreColumnsFeature`](CoreFeatures.md#corecolumnsfeature)

***

### coreHeadersFeature? {#coreheadersfeature}

```ts
optional coreHeadersFeature?: TableFeature;
```

定義元: [core/coreFeatures.ts:13](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/coreFeatures.ts#L13)

#### 継承元のメンバー {#inherited-from-12}

[`CoreFeatures`](CoreFeatures.md).[`coreHeadersFeature`](CoreFeatures.md#coreheadersfeature)

***

### coreReactivityFeature? {#corereactivityfeature}

```ts
optional coreReactivityFeature?: TableReactivityBindings;
```

定義元: [core/coreFeatures.ts:10](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/coreFeatures.ts#L10)

#### 継承元のメンバー {#inherited-from-13}

[`CoreFeatures`](CoreFeatures.md).[`coreReactivityFeature`](CoreFeatures.md#corereactivityfeature)

***

### coreRowModel? {#corerowmodel}

```ts
optional coreRowModel?: (table) => () => RowModel<any, any>;
```

定義元: [types/TableFeatures.ts:212](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L212)

テーブルのコア（加工前の）行モデルのファクトリーです。省略した場合は、組み込みの `createCoreRowModel()` が使われます。

#### パラメーター {#parameters}

##### table {#table}

`any`

#### 戻り値 {#returns}

() => [`RowModel`](RowModel.md)\<`any`, `any`\>

***

### coreRowModelsFeature? {#corerowmodelsfeature}

```ts
optional coreRowModelsFeature?: TableFeature;
```

定義元: [core/coreFeatures.ts:14](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/coreFeatures.ts#L14)

#### 継承元のメンバー {#inherited-from-14}

[`CoreFeatures`](CoreFeatures.md).[`coreRowModelsFeature`](CoreFeatures.md#corerowmodelsfeature)

***

### coreRowsFeature? {#corerowsfeature}

```ts
optional coreRowsFeature?: TableFeature;
```

定義元: [core/coreFeatures.ts:15](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/coreFeatures.ts#L15)

#### 継承元のメンバー {#inherited-from-15}

[`CoreFeatures`](CoreFeatures.md).[`coreRowsFeature`](CoreFeatures.md#corerowsfeature)

***

### coreTablesFeature? {#coretablesfeature}

```ts
optional coreTablesFeature?: TableFeature;
```

定義元: [core/coreFeatures.ts:16](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/coreFeatures.ts#L16)

#### 継承元のメンバー {#inherited-from-16}

[`CoreFeatures`](CoreFeatures.md).[`coreTablesFeature`](CoreFeatures.md#coretablesfeature)

***

### expandedRowModel? {#expandedrowmodel}

```ts
optional expandedRowModel?: (table) => () => RowModel<any, any>;
```

定義元: [types/TableFeatures.ts:218](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L218)

クライアントサイドの展開済み行モデルのファクトリーです。エクスポートされている `createExpandedRowModel()` を渡すか、自分で実装してください。サーバーサイドで展開する場合は不要です。

#### パラメーター {#parameters-1}

##### table {#table-1}

`any`

#### 戻り値 {#returns-1}

() => [`RowModel`](RowModel.md)\<`any`, `any`\>

***

### facetedMinMaxValues? {#facetedminmaxvalues}

```ts
optional facetedMinMaxValues?: (table, columnId) => () => [number, number] | undefined;
```

定義元: [types/TableFeatures.ts:224](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L224)

列ごとのファセットの最小値・最大値のファクトリーです。エクスポートされている `createFacetedMinMaxValues()` を渡すか、自分で実装してください。サーバーサイドでファセットを計算する場合は不要です。

#### パラメーター {#parameters-2}

##### table {#table-2}

`any`

##### columnId {#columnid}

`string`

#### 戻り値 {#returns-2}

() => \[`number`, `number`\] \| `undefined`

***

### facetedRowModel? {#facetedrowmodel}

```ts
optional facetedRowModel?: (table, columnId) => () => RowModel<any, any>;
```

定義元: [types/TableFeatures.ts:233](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L233)

列ごとのファセット行モデルのファクトリーです。エクスポートされている `createFacetedRowModel()` を渡すか、自分で実装してください。サーバーサイドでファセットを計算する場合は不要です。

#### パラメーター {#parameters-3}

##### table {#table-3}

`any`

##### columnId {#columnid-1}

`string`

#### 戻り値 {#returns-3}

() => [`RowModel`](RowModel.md)\<`any`, `any`\>

***

### facetedUniqueValues? {#faceteduniquevalues}

```ts
optional facetedUniqueValues?: (table, columnId) => () => Map<any, number>;
```

定義元: [types/TableFeatures.ts:239](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L239)

列ごとのファセットの一意な値のファクトリーです。エクスポートされている `createFacetedUniqueValues()` を渡すか、自分で実装してください。サーバーサイドでファセットを計算する場合は不要です。

#### パラメーター {#parameters-4}

##### table {#table-4}

`any`

##### columnId {#columnid-2}

`string`

#### 戻り値 {#returns-4}

() => `Map`\<`any`, `number`\>

***

### filteredRowModel? {#filteredrowmodel}

```ts
optional filteredRowModel?: (table) => () => RowModel<any, any>;
```

定義元: [types/TableFeatures.ts:245](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L245)

クライアントサイドのフィルター済み行モデルのファクトリーです。エクスポートされている `createFilteredRowModel()` を渡すか、自分で実装してください。サーバーサイドでフィルタリングする場合は不要です。

#### パラメーター {#parameters-5}

##### table {#table-5}

`any`

#### 戻り値 {#returns-5}

() => [`RowModel`](RowModel.md)\<`any`, `any`\>

***

### filterFns? {#filterfns}

```ts
optional filterFns?: Record<string, FilterFn<any, any>>;
```

定義元: [types/TableFeatures.ts:257](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L257)

このテーブルで名前を使って指定できる、フィルター関数のレジストリです。

ここに登録したキーが、列定義の `filterFn` と `globalFilterFn` オプションに指定できる文字列になり、型も完全に推論されます。
使う組み込みのフィルター関数は個別に import し、慣例の名前で登録してください:
`filterFns: { includesString: filterFn_includesString, myCustomFilterFn }`。
エクスポートされている `filterFns` レジストリをスプレッドしても動きますが、組み込みのフィルター関数がすべてバンドルに含まれます。

***

### filterMeta? {#filtermeta}

```ts
optional filterMeta?: object;
```

定義元: [types/TableFeatures.ts:269](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L269)

フィルターのメタデータの型を宣言するための、型専用のスロットです。このメタデータは、フィルター関数が `addMeta` で行に付け、`row.columnFiltersMeta` から読み戻すものです。

実体のない値を渡してください: `filterMeta: {} as MyFilterMeta`（または `metaHelper<MyFilterMeta>()`）。値そのものは実行時に無視され、テーブルに登録された機能から取り除かれます。使われるのは型だけです。

省略した場合は、グローバルに宣言のマージをした `FilterMeta` インターフェースが使われます。

***

### globalFilteringFeature? {#globalfilteringfeature}

```ts
optional globalFilteringFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:30](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L30)

#### 継承元のメンバー {#inherited-from-17}

[`StockFeatures`](StockFeatures.md).[`globalFilteringFeature`](StockFeatures.md#globalfilteringfeature)

***

### groupedRowModel? {#groupedrowmodel}

```ts
optional groupedRowModel?: (table) => () => RowModel<any, any>;
```

定義元: [types/TableFeatures.ts:275](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L275)

クライアントサイドのグループ化済み行モデルのファクトリーです。エクスポートされている `createGroupedRowModel()` を渡すか、自分で実装してください。サーバーサイドでグループ化する場合は不要です。

#### パラメーター {#parameters-6}

##### table {#table-6}

`any`

#### 戻り値 {#returns-6}

() => [`RowModel`](RowModel.md)\<`any`, `any`\>

***

### paginatedRowModel? {#paginatedrowmodel}

```ts
optional paginatedRowModel?: (table) => () => RowModel<any, any>;
```

定義元: [types/TableFeatures.ts:281](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L281)

クライアントサイドのページ分割済み行モデルのファクトリーです。エクスポートされている `createPaginatedRowModel()` を渡すか、自分で実装してください。サーバーサイドでページネーションする場合は不要です。

#### パラメーター {#parameters-7}

##### table {#table-7}

`any`

#### 戻り値 {#returns-7}

() => [`RowModel`](RowModel.md)\<`any`, `any`\>

***

### rowAggregationFeature? {#rowaggregationfeature}

```ts
optional rowAggregationFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:31](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L31)

#### 継承元のメンバー {#inherited-from-18}

[`StockFeatures`](StockFeatures.md).[`rowAggregationFeature`](StockFeatures.md#rowaggregationfeature)

***

### rowExpandingFeature? {#rowexpandingfeature}

```ts
optional rowExpandingFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:32](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L32)

#### 継承元のメンバー {#inherited-from-19}

[`StockFeatures`](StockFeatures.md).[`rowExpandingFeature`](StockFeatures.md#rowexpandingfeature)

***

### rowPaginationFeature? {#rowpaginationfeature}

```ts
optional rowPaginationFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:33](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L33)

#### 継承元のメンバー {#inherited-from-20}

[`StockFeatures`](StockFeatures.md).[`rowPaginationFeature`](StockFeatures.md#rowpaginationfeature)

***

### rowPinningFeature? {#rowpinningfeature}

```ts
optional rowPinningFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:34](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L34)

#### 継承元のメンバー {#inherited-from-21}

[`StockFeatures`](StockFeatures.md).[`rowPinningFeature`](StockFeatures.md#rowpinningfeature)

***

### rowSelectionFeature? {#rowselectionfeature}

```ts
optional rowSelectionFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:35](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L35)

#### 継承元のメンバー {#inherited-from-22}

[`StockFeatures`](StockFeatures.md).[`rowSelectionFeature`](StockFeatures.md#rowselectionfeature)

***

### rowSortingFeature? {#rowsortingfeature}

```ts
optional rowSortingFeature?: TableFeature;
```

定義元: [features/stockFeatures.ts:36](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/stockFeatures.ts#L36)

#### 継承元のメンバー {#inherited-from-23}

[`StockFeatures`](StockFeatures.md).[`rowSortingFeature`](StockFeatures.md#rowsortingfeature)

***

### sortedRowModel? {#sortedrowmodel}

```ts
optional sortedRowModel?: (table) => () => RowModel<any, any>;
```

定義元: [types/TableFeatures.ts:287](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L287)

クライアントサイドのソート済み行モデルのファクトリーです。エクスポートされている `createSortedRowModel()` を渡すか、自分で実装してください。サーバーサイドでソートする場合は不要です。

#### パラメーター {#parameters-8}

##### table {#table-8}

`any`

#### 戻り値 {#returns-8}

() => [`RowModel`](RowModel.md)\<`any`, `any`\>

***

### sortFns? {#sortfns}

```ts
optional sortFns?: Record<string, SortFn<any, any>>;
```

定義元: [types/TableFeatures.ts:298](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L298)

このテーブルで名前を使って指定できる、ソート関数のレジストリです。

ここに登録したキーが、列定義の `sortFn` に指定できる文字列になり、型も完全に推論されます。
使う組み込みのソート関数は個別に import し、慣例の名前で登録してください: `sortFns: { alphanumeric: sortFn_alphanumeric, myCustomSortFn }`。
エクスポートされている `sortFns` レジストリをスプレッドしても動きますが、組み込みのソート関数がすべてバンドルに含まれます。

***

### tableMeta? {#tablemeta}

```ts
optional tableMeta?: object;
```

定義元: [types/TableFeatures.ts:308](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L308)

このテーブルの `options.meta` の型を宣言するための、型専用のスロットです。

実体のない値を渡してください: `tableMeta: {} as MyTableMeta`。値そのものは実行時に無視され、テーブルに登録された機能から取り除かれます。使われるのは型だけで、`TFeatures` が渡る先々で推論されます。

省略した場合は、グローバルに宣言のマージをした `TableMeta` インターフェースが使われます。

***

### workerRowModelsFeature? {#workerrowmodelsfeature}

```ts
optional workerRowModelsFeature?: TableFeature;
```

定義元: [worker/createTableWorker.ts:24](https://github.com/TanStack/table/blob/main/packages/table-core/src/worker/createTableWorker.ts#L24)

#### 継承元のメンバー {#inherited-from-24}

[`Plugins`](Plugins.md).[`workerRowModelsFeature`](Plugins.md#workerrowmodelsfeature)
