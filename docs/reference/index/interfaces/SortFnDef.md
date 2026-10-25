---
id: SortFnDef
title: SortFnDef
---

定義元: [features/row-sorting/rowSortingFeature.types.ts:58](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L58)

`constructSortFn` が受け取る定義オブジェクトです。

`sort` は値レベルの比較関数です。行全体ではなく、2つの行の（解決済みの）データ値を受け取ります。そのため、正規化の処理は `resolveDataValue` に分けておけます。

## 継承先 {#extended-by}

- [`CreatedSortFn`](CreatedSortFn.md)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### resolveDataValue? {#resolvedatavalue}

```ts
optional resolveDataValue?: TransformDataValueFn;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:69](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L69)

***

### sort {#sort}

```ts
sort: (dataValueA, dataValueB, rowA, rowB, columnId) => number;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:62](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L62)

#### パラメーター {#parameters}

##### dataValueA {#datavaluea}

`any`

##### dataValueB {#datavalueb}

`any`

##### rowA {#rowa}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

##### rowB {#rowb}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

##### columnId {#columnid}

`string`

#### 戻り値 {#returns}

`number`
