---
id: SortFn
title: SortFn
---

定義元: [features/row-sorting/rowSortingFeature.types.ts:34](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L34)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

```ts
SortFn(
   rowA,
   rowB,
   columnId): number;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:38](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L38)

## パラメーター {#parameters}

### rowA {#rowa}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

### rowB {#rowb}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

### columnId {#columnid}

`string`

## 戻り値 {#returns}

`number`

## プロパティ {#properties}

### resolveDataValue? {#resolvedatavalue}

```ts
optional resolveDataValue?: TransformDataValueFn;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:48](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L48)

2つの値を比べる前に、各行の値を正規化します。`constructSortFn` で作ったソート関数（組み込みのソート関数をすべて含みます）でだけ使われます。
