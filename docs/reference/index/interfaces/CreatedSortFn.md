---
id: CreatedSortFn
title: CreatedSortFn
---

定義元: [features/row-sorting/rowSortingFeature.types.ts:81](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L81)

`constructSortFn` が返す形です。定義が付いた `SortFn` なので、これを別の `constructSortFn` の呼び出しにスプレッドして派生版を作れます。

呼び出しシグネチャはジェネリックです。そのため、作成したソート関数は、定義したときの機能の組み合わせに関係なく、どのテーブルの行にも使えます。

## 継承元 {#extends}

- [`SortFnDef`](SortFnDef.md)\<`TFeatures`, `TData`\>

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

```ts
CreatedSortFn<TRowFeatures, TRowData>(
   rowA,
   rowB,
   columnId): number;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:85](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L85)

`constructSortFn` が返す形です。定義が付いた `SortFn` なので、これを別の `constructSortFn` の呼び出しにスプレッドして派生版を作れます。

呼び出しシグネチャはジェネリックです。そのため、作成したソート関数は、定義したときの機能の組み合わせに関係なく、どのテーブルの行にも使えます。

## 型パラメーター {#type-parameters-1}

### TRowFeatures {#trowfeatures}

`TRowFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TRowData {#trowdata}

`TRowData` *extends* [`RowData`](../type-aliases/RowData.md)

## パラメーター {#parameters}

### rowA {#rowa}

[`Row`](../type-aliases/Row.md)\<`TRowFeatures`, `TRowData`\>

### rowB {#rowb}

[`Row`](../type-aliases/Row.md)\<`TRowFeatures`, `TRowData`\>

### columnId {#columnid}

`string`

## 戻り値 {#returns}

`number`

## プロパティ {#properties}

### resolveDataValue? {#resolvedatavalue}

```ts
optional resolveDataValue?: TransformDataValueFn;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:69](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L69)

#### 継承元のメンバー {#inherited-from}

[`SortFnDef`](SortFnDef.md).[`resolveDataValue`](SortFnDef.md#resolvedatavalue)

***

### sort {#sort}

```ts
sort: (dataValueA, dataValueB, rowA, rowB, columnId) => number;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:62](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L62)

#### パラメーター {#parameters-1}

##### dataValueA {#datavaluea}

`any`

##### dataValueB {#datavalueb}

`any`

##### rowA {#rowa-1}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

##### rowB {#rowb-1}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

##### columnId {#columnid-1}

`string`

#### 戻り値 {#returns-1}

`number`

#### 継承元のメンバー {#inherited-from-1}

[`SortFnDef`](SortFnDef.md).[`sort`](SortFnDef.md#sort)
