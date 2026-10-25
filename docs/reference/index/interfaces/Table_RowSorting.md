---
id: Table_RowSorting
title: Table_RowSorting
---

定義元: [features/row-sorting/rowSortingFeature.types.ts:266](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L266)

## 型パラメーター {#type-parameters}

### _TFeatures {#_tfeatures}

`_TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### _TData {#_tdata}

`_TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### autoResetSorting {#autoresetsorting}

```ts
autoResetSorting: () => void;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:277](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L277)

明示的に有効にした場合、テーブルのデータが変わったあとにソートをリセットします。

`autoResetAll` と `autoResetSorting` に従います。既定ではソートは保たれます。コア行モデルから呼ばれるので、自分で呼ぶ必要はほとんどありません。

#### 戻り値 {#returns}

`void`

***

### resetSorting {#resetsorting}

```ts
resetSorting: (defaultState?) => void;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:283](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L283)

`sorting` を `initialState.sorting` に戻します。

`true` を渡すと、初期状態を無視して `[]` に戻します。

#### パラメーター {#parameters}

##### defaultState? {#defaultstate}

`boolean`

#### 戻り値 {#returns-1}

`void`

***

### setSorting {#setsorting}

```ts
setSorting: (updater) => void;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:287](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L287)

次の順序付きの配列かアップデーター関数で、ソートの状態を更新します。

#### パラメーター {#parameters-1}

##### updater {#updater}

[`Updater`](../type-aliases/Updater.md)\<[`SortingState`](../type-aliases/SortingState.md)\>

#### 戻り値 {#returns-2}

`void`
