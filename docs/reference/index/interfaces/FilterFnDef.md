---
id: FilterFnDef
title: FilterFnDef
---

定義元: [features/column-filtering/columnFilteringFeature.types.ts:102](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L102)

`constructFilterFn` が受け取る定義オブジェクトです。

`filter` は値レベルの比較関数です。行全体ではなく、行の（解決済みの）データ値と（解決済みの）フィルター値を受け取ります。そのため、正規化の処理は `resolveDataValue` / `resolveFilterValue` に分けておけます。

## 継承先 {#extended-by}

- [`CreatedFilterFn`](CreatedFilterFn.md)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### autoRemove? {#autoremove}

```ts
optional autoRemove?: (filterValue) => boolean;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:113](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L113)

#### パラメーター {#parameters}

##### filterValue {#filtervalue}

`any`

#### 戻り値 {#returns}

`boolean`

***

### filter {#filter}

```ts
filter: (dataValue, filterValue, row, columnId, addMeta?) => boolean;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:106](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L106)

#### パラメーター {#parameters-1}

##### dataValue {#datavalue}

`any`

##### filterValue {#filtervalue-1}

`any`

##### row {#row}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

##### columnId {#columnid}

`string`

##### addMeta? {#addmeta}

(`meta`) => `void`

#### 戻り値 {#returns-1}

`boolean`

***

### resolveDataValue? {#resolvedatavalue}

```ts
optional resolveDataValue?: TransformDataValueFn;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:115](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L115)

***

### resolveFilterValue? {#resolvefiltervalue}

```ts
optional resolveFilterValue?: (filterValue) => any;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:114](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L114)

#### パラメーター {#parameters-2}

##### filterValue {#filtervalue-2}

`any`

#### 戻り値 {#returns-2}

`any`
