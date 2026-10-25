---
id: Table_ColumnResizing
title: Table_ColumnResizing
---

定義元: [features/column-resizing/columnResizingFeature.types.ts:48](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.types.ts#L48)

## プロパティ {#properties}

### resetHeaderSizeInfo {#resetheadersizeinfo}

```ts
resetHeaderSizeInfo: (defaultState?) => void;
```

定義元: [features/column-resizing/columnResizingFeature.types.ts:54](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.types.ts#L54)

`columnResizing` を `initialState.columnResizing` に戻します。

`true` を渡すと、初期状態を無視して、ドラッグしていない既定の状態に戻します。

#### パラメーター {#parameters}

##### defaultState? {#defaultstate}

`boolean`

#### 戻り値 {#returns}

`void`

***

### setColumnResizing {#setcolumnresizing}

```ts
setColumnResizing: (updater) => void;
```

定義元: [features/column-resizing/columnResizingFeature.types.ts:58](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.types.ts#L58)

次の状態かアップデーター関数で、一時的なリサイズ操作の状態を更新します。

#### パラメーター {#parameters-1}

##### updater {#updater}

[`Updater`](../type-aliases/Updater.md)\<[`columnResizingState`](columnResizingState.md)\>

#### 戻り値 {#returns-1}

`void`
