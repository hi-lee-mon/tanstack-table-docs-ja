---
id: Table_RowPinning
title: Table_RowPinning
---

定義元: [features/row-pinning/rowPinningFeature.types.ts:65](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L65)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getBottomRows {#getbottomrows}

```ts
getBottomRows: () => Row<TFeatures, TData>[];
```

定義元: [features/row-pinning/rowPinningFeature.types.ts:72](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L72)

下部の領域に固定された行を取得します。

#### 戻り値 {#returns}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>[]

***

### getCenterRows {#getcenterrows}

```ts
getCenterRows: () => Row<TFeatures, TData>[];
```

定義元: [features/row-pinning/rowPinningFeature.types.ts:76](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L76)

上部にも下部にも固定されていない行を取得します。

#### 戻り値 {#returns-1}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>[]

***

### getIsSomeRowsPinned {#getissomerowspinned}

```ts
getIsSomeRowsPinned: (position?) => boolean;
```

定義元: [features/row-pinning/rowPinningFeature.types.ts:80](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L80)

固定されている行があるかどうかを判定します。1つの領域だけに絞ることもできます。

#### パラメーター {#parameters}

##### position? {#position}

[`RowPinningPosition`](../type-aliases/RowPinningPosition.md)

#### 戻り値 {#returns-2}

`boolean`

***

### getTopRows {#gettoprows}

```ts
getTopRows: () => Row<TFeatures, TData>[];
```

定義元: [features/row-pinning/rowPinningFeature.types.ts:84](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L84)

上部の領域に固定された行を取得します。

#### 戻り値 {#returns-3}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>[]

***

### resetRowPinning {#resetrowpinning}

```ts
resetRowPinning: (defaultState?) => void;
```

定義元: [features/row-pinning/rowPinningFeature.types.ts:90](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L90)

`rowPinning` を `initialState.rowPinning` に戻します。

`true` を渡すと、初期状態を無視して、上部と下部が空の配列の状態に戻します。

#### パラメーター {#parameters-1}

##### defaultState? {#defaultstate}

`boolean`

#### 戻り値 {#returns-4}

`void`

***

### setRowPinning {#setrowpinning}

```ts
setRowPinning: (updater) => void;
```

定義元: [features/row-pinning/rowPinningFeature.types.ts:94](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L94)

次の状態かアップデーター関数で、行の固定の状態を更新します。

#### パラメーター {#parameters-2}

##### updater {#updater}

[`Updater`](../type-aliases/Updater.md)\<[`RowPinningState`](RowPinningState.md)\>

#### 戻り値 {#returns-5}

`void`
