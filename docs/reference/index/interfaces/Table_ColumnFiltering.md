---
id: Table_ColumnFiltering
title: Table_ColumnFiltering
---

定義元: [features/column-filtering/columnFilteringFeature.types.ts:281](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L281)

## プロパティ {#properties}

### resetColumnFilters {#resetcolumnfilters}

```ts
resetColumnFilters: (defaultState?) => void;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:287](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L287)

`columnFilters` を `initialState.columnFilters` に戻します。

`true` を渡すと、初期状態を無視して `[]` に戻します。

#### パラメーター {#parameters}

##### defaultState? {#defaultstate}

`boolean`

#### 戻り値 {#returns}

`void`

***

### setColumnFilters {#setcolumnfilters}

```ts
setColumnFilters: (updater) => void;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:291](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L291)

次の配列かアップデーター関数で、列フィルターの状態を更新します。

#### パラメーター {#parameters-1}

##### updater {#updater}

[`Updater`](../type-aliases/Updater.md)\<[`ColumnFiltersState`](../type-aliases/ColumnFiltersState.md)\>

#### 戻り値 {#returns-1}

`void`
