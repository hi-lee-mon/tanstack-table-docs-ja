---
id: TableOptions_ColumnFiltering
title: TableOptions_ColumnFiltering
---

定義元: [features/column-filtering/columnFilteringFeature.types.ts:245](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L245)

## 型パラメーター {#type-parameters}

### _TFeatures {#_tfeatures}

`_TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### _TData {#_tdata}

`_TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### enableColumnFilters? {#enablecolumnfilters}

```ts
optional enableColumnFilters?: boolean;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:252](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L252)

列ごとのフィルタリングを、それを許可しているすべての列で有効にします。

***

### enableFilters? {#enablefilters}

```ts
optional enableFilters?: boolean;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:258](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L258)

テーブルのすべてのフィルタリング機能を有効にします。

`false` にすると、列フィルタリングとグローバルフィルタリングの両方が無効になります。

***

### filterFromLeafRows? {#filterfromleafrows}

```ts
optional filterFromLeafRows?: boolean;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:262](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L262)

既定では、フィルタリングは親の行から下に向かって行われます（そのため、親の行がフィルターで除かれると、その子もすべて除かれます）。
このオプションを `true` にすると、フィルタリングは末端の行から上に向かって行われます（つまり、子や孫の行が1つでも残れば、その親の行も残ります）。

***

### manualFiltering? {#manualfiltering}

```ts
optional manualFiltering?: boolean;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:266](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L266)

データのフィルタリングに `getFilteredRowModel` を使わないようにします。テーブルで、クライアントサイドとサーバーサイドのフィルタリングの両方を動的に切り替えたい場合に便利です。

***

### maxLeafRowFilterDepth? {#maxleafrowfilterdepth}

```ts
optional maxLeafRowFilterDepth?: number;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:272](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L272)

既定では、ルート階層の親の行か、親の行の子である末端の行かに関係なく、すべての行（最大の深さ 100）がフィルタリングされます。
このオプションを `0` にすると、フィルタリングはルート階層の親の行にだけ適用され、サブ行はすべてフィルタリングされずに残ります。同じように、`1` にすると1階層下の子の行まで適用され、以降も同様です。

適用されたフィルターに関係なく、行の子の階層全体を表示したい場合に便利です。

***

### onColumnFiltersChange? {#oncolumnfilterschange}

```ts
optional onColumnFiltersChange?: OnChangeFn<ColumnFiltersState>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:278](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L278)

列フィルターの状態が変わったときに、アップデーターを渡して呼び出されます。外部の状態を使う場合は `state.columnFilters` と組み合わせてください。外部のアトムなら、このコールバックなしでスライスを持てます。
