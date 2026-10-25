---
id: FilterFn
title: FilterFn
---

定義元: [features/column-filtering/columnFilteringFeature.types.ts:60](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L60)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

```ts
FilterFn(
   row,
   columnId,
   filterValue,
   addMeta?): boolean;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:64](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L64)

## パラメーター {#parameters}

### row {#row}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

### columnId {#columnid}

`string`

### filterValue {#filtervalue}

`any`

### addMeta? {#addmeta}

(`meta`) => `void`

## 戻り値 {#returns}

`boolean`

## プロパティ {#properties}

### autoRemove? {#autoremove}

```ts
optional autoRemove?: ColumnFilterAutoRemoveTestFn<TFeatures, TData, unknown>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:79](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L79)

フィルター値がこの判定に通らないとき（テキストフィルターでの空文字列など）、`state.columnFilters` からフィルターを取り除きます。

指定した場合は、この判定が優先されます。この判定で残すとした値は、既定の判定なら取り除かれる空文字列であっても、フィルターの状態に残ります。ただし、フィルター値が `undefined` の場合は、常にフィルターが解除されます。

***

### resolveDataValue? {#resolvedatavalue}

```ts
optional resolveDataValue?: TransformDataValueFn;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:92](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L92)

フィルター値と比べる前に、各行の値を正規化します。`constructFilterFn` で作ったフィルター関数（組み込みのフィルター関数をすべて含みます）でだけ使われます。

***

### resolveFilterValue? {#resolvefiltervalue}

```ts
optional resolveFilterValue?: TransformFilterValueFn<TFeatures, TData, unknown>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:86](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L86)

フィルタリングを実行する前に、フィルター値を正規化します。

テーブルはこれをフィルターごとに1回だけ（行ごとではなく）適用し、解決した値を `filterValue` としてフィルター関数に渡します。
