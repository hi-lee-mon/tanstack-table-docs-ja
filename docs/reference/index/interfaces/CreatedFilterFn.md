---
id: CreatedFilterFn
title: CreatedFilterFn
---

定義元: [features/column-filtering/columnFilteringFeature.types.ts:126](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L126)

`constructFilterFn` が返す形です。定義が付いた `FilterFn` なので、これを別の `constructFilterFn` の呼び出しにスプレッドして派生版を作れます。

呼び出しシグネチャはジェネリックです。そのため、作成したフィルター関数は、定義したときの機能の組み合わせに関係なく、どのテーブルの行にも使えます。

## 継承元 {#extends}

- [`FilterFnDef`](FilterFnDef.md)\<`TFeatures`, `TData`\>

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

```ts
CreatedFilterFn<TRowFeatures, TRowData>(
   row,
   columnId,
   filterValue,
   addMeta?): boolean;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:130](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L130)

`constructFilterFn` が返す形です。定義が付いた `FilterFn` なので、これを別の `constructFilterFn` の呼び出しにスプレッドして派生版を作れます。

呼び出しシグネチャはジェネリックです。そのため、作成したフィルター関数は、定義したときの機能の組み合わせに関係なく、どのテーブルの行にも使えます。

## 型パラメーター {#type-parameters-1}

### TRowFeatures {#trowfeatures}

`TRowFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TRowData {#trowdata}

`TRowData` *extends* [`RowData`](../type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../type-aliases/Row.md)\<`TRowFeatures`, `TRowData`\>

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
optional autoRemove?: (filterValue) => boolean;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:113](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L113)

#### パラメーター {#parameters-1}

##### filterValue {#filtervalue-1}

`any`

#### 戻り値 {#returns-1}

`boolean`

#### 継承元のメンバー {#inherited-from}

[`FilterFnDef`](FilterFnDef.md).[`autoRemove`](FilterFnDef.md#autoremove)

***

### filter {#filter}

```ts
filter: (dataValue, filterValue, row, columnId, addMeta?) => boolean;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:106](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L106)

#### パラメーター {#parameters-2}

##### dataValue {#datavalue}

`any`

##### filterValue {#filtervalue-2}

`any`

##### row {#row-1}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

##### columnId {#columnid-1}

`string`

##### addMeta? {#addmeta-1}

(`meta`) => `void`

#### 戻り値 {#returns-2}

`boolean`

#### 継承元のメンバー {#inherited-from-1}

[`FilterFnDef`](FilterFnDef.md).[`filter`](FilterFnDef.md#filter)

***

### resolveDataValue? {#resolvedatavalue}

```ts
optional resolveDataValue?: TransformDataValueFn;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:115](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L115)

#### 継承元のメンバー {#inherited-from-2}

[`FilterFnDef`](FilterFnDef.md).[`resolveDataValue`](FilterFnDef.md#resolvedatavalue)

***

### resolveFilterValue? {#resolvefiltervalue}

```ts
optional resolveFilterValue?: (filterValue) => any;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:114](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L114)

#### パラメーター {#parameters-3}

##### filterValue {#filtervalue-3}

`any`

#### 戻り値 {#returns-3}

`any`

#### 継承元のメンバー {#inherited-from-3}

[`FilterFnDef`](FilterFnDef.md).[`resolveFilterValue`](FilterFnDef.md#resolvefiltervalue)
