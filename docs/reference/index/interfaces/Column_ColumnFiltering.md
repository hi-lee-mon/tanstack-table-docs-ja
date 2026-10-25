---
id: Column_ColumnFiltering
title: Column_ColumnFiltering
---

定義元: [features/column-filtering/columnFilteringFeature.types.ts:194](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L194)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getAutoFilterFn {#getautofilterfn}

```ts
getAutoFilterFn: () => FilterFn<TFeatures, TData>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:201](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L201)

列で最初に見つかった値をもとに、自動で決めたフィルター関数を返します。

#### 戻り値 {#returns}

[`FilterFn`](FilterFn.md)\<`TFeatures`, `TData`\>

***

### getCanFilter {#getcanfilter}

```ts
getCanFilter: () => boolean;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:205](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L205)

このアクセサー列で、列フィルタリングが現在できるかどうかを判定します。

#### 戻り値 {#returns-1}

`boolean`

***

### getFilterFn {#getfilterfn}

```ts
getFilterFn: () => FilterFn<TFeatures, TData>;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:209](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L209)

指定した columnId のフィルター関数を返します（設定によって、利用者が定義したものか自動で決まったもののどちらかです）。

#### 戻り値 {#returns-2}

[`FilterFn`](FilterFn.md)\<`TFeatures`, `TData`\>

***

### getFilterIndex {#getfilterindex}

```ts
getFilterIndex: () => number;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:213](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L213)

テーブルの `state.columnFilters` 配列における、この列のフィルターのインデックスを返します（`-1` もありえます）。

#### 戻り値 {#returns-3}

`number`

***

### getFilterValue {#getfiltervalue}

```ts
getFilterValue: () => unknown;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:217](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L217)

`state.columnFilters` から、この列の現在の値を読み取ります。

#### 戻り値 {#returns-4}

`unknown`

***

### getIsFiltered {#getisfiltered}

```ts
getIsFiltered: () => boolean;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:221](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L221)

この列が `state.columnFilters` に有効なエントリーを持つかどうかを判定します。

#### 戻り値 {#returns-5}

`boolean`

***

### setFilterValue {#setfiltervalue}

```ts
setFilterValue: (updater) => void;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:228](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L228)

この列のフィルター値を追加、更新、または削除します。

アップデーター関数は前のフィルター値を受け取ります。フィルター関数の `autoRemove` の条件を満たす値は、フィルターの状態から削除されます。

#### パラメーター {#parameters}

##### updater {#updater}

`any`

#### 戻り値 {#returns-6}

`void`
