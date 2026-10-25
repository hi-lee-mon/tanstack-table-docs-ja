---
id: Table_ColumnOrdering
title: Table_ColumnOrdering
---

定義元: [features/column-ordering/columnOrderingFeature.types.ts:66](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L66)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getColumnIndexes {#getcolumnindexes}

```ts
getColumnIndexes: () => ColumnIndexes;
```

定義元: [features/column-ordering/columnOrderingFeature.types.ts:76](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L76)

表示中の固定領域ごとに、列 ID からインデックスへのレコードを作ります。

これは `column.getIndex` が読む、メモ化された元データです。ほとんどのアプリでは直接呼ぶ必要はありません。

#### 戻り値 {#returns}

[`ColumnIndexes`](ColumnIndexes.md)

***

### getOrderColumnsFn {#getordercolumnsfn}

```ts
getOrderColumnsFn: () => (columns) => Column<TFeatures, TData, unknown>[];
```

定義元: [features/column-ordering/columnOrderingFeature.types.ts:83](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L83)

グループ化された列を `groupedColumnMode` の設定どおりに移動したうえで、末端の列を `columnOrder` の順に並べる関数を返します。

末端の列の並び順がこれを読みます。ほとんどのアプリでは直接呼ぶ必要はありません。

#### 戻り値 {#returns-1}

(`columns`) => [`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### resetColumnOrder {#resetcolumnorder}

```ts
resetColumnOrder: (defaultState?) => void;
```

定義元: [features/column-ordering/columnOrderingFeature.types.ts:91](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L91)

`columnOrder` を `initialState.columnOrder` に戻します。

`true` を渡すと、初期状態を無視して `[]` に戻します。

#### パラメーター {#parameters}

##### defaultState? {#defaultstate}

`boolean`

#### 戻り値 {#returns-2}

`void`

***

### setColumnOrder {#setcolumnorder}

```ts
setColumnOrder: (updater) => void;
```

定義元: [features/column-ordering/columnOrderingFeature.types.ts:95](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L95)

次の順序付きの ID 配列かアップデーター関数で、列の並び順の状態を更新します。

#### パラメーター {#parameters-1}

##### updater {#updater}

[`Updater`](../type-aliases/Updater.md)\<[`ColumnOrderState`](../type-aliases/ColumnOrderState.md)\>

#### 戻り値 {#returns-3}

`void`
