---
id: Table_ColumnSizing
title: Table_ColumnSizing
---

定義元: [features/column-sizing/columnSizingFeature.types.ts:62](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L62)

## プロパティ {#properties}

### getCenterTotalSize {#getcentertotalsize}

```ts
getCenterTotalSize: () => number;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:66](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L66)

中央領域にある表示中の末端の列の、現在の幅を合計します。

#### 戻り値 {#returns}

`number`

***

### getColumnOffsets {#getcolumnoffsets}

```ts
getColumnOffsets: () => ColumnOffsetsByPosition;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:73](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L73)

メモ化された列のオフセットのマップ（列 ID をキーにした、先頭からと後ろからのオフセット）を、固定領域ごとと、表示中の末端の列全体について返します。

`column.getStart()` と `column.getAfter()` が O(1) で引けるのは、これのおかげです。

#### 戻り値 {#returns-1}

[`ColumnOffsetsByPosition`](ColumnOffsetsByPosition.md)

***

### getEndTotalSize {#getendtotalsize}

```ts
getEndTotalSize: () => number;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:81](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L81)

論理的な末尾に固定された、表示中の末端の列の現在の幅を合計します。

#### 戻り値 {#returns-2}

`number`

***

### getStartTotalSize {#getstarttotalsize}

```ts
getStartTotalSize: () => number;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:77](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L77)

論理的な先頭に固定された、表示中の末端の列の現在の幅を合計します。

#### 戻り値 {#returns-3}

`number`

***

### getTotalSize {#gettotalsize}

```ts
getTotalSize: () => number;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:85](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L85)

表示中のすべての末端の列の、現在の幅を合計します。

#### 戻り値 {#returns-4}

`number`

***

### resetColumnSizing {#resetcolumnsizing}

```ts
resetColumnSizing: (defaultState?) => void;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:90](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L90)

列幅を `initialState.columnSizing` に戻します。`true` を渡すと、機能の既定値 `{}` に戻します。

#### パラメーター {#parameters}

##### defaultState? {#defaultstate}

`boolean`

#### 戻り値 {#returns-5}

`void`

***

### setColumnSizing {#setcolumnsizing}

```ts
setColumnSizing: (updater) => void;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:94](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L94)

次のマップかアップデーター関数で、確定した列幅の状態を更新します。

#### パラメーター {#parameters-1}

##### updater {#updater}

[`Updater`](../type-aliases/Updater.md)\<[`ColumnSizingState`](../type-aliases/ColumnSizingState.md)\>

#### 戻り値 {#returns-6}

`void`
