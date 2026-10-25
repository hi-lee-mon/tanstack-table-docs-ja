---
id: Table_ColumnVisibility
title: Table_ColumnVisibility
---

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:30](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L30)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getIsAllColumnsVisible {#getisallcolumnsvisible}

```ts
getIsAllColumnsVisible: () => boolean;
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:37](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L37)

すべての末端の列が現在表示されているかどうかを判定します。

#### 戻り値 {#returns}

`boolean`

***

### getIsSomeColumnsVisible {#getissomecolumnsvisible}

```ts
getIsSomeColumnsVisible: () => boolean;
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:41](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L41)

少なくとも1つの末端の列が現在表示されているかどうかを判定します。

#### 戻り値 {#returns-1}

`boolean`

***

### getToggleAllColumnsVisibilityHandler {#gettoggleallcolumnsvisibilityhandler}

```ts
getToggleAllColumnsVisibilityHandler: () => (event) => void;
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:45](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L45)

すべての列の表示・非表示を切り替える、チェックボックス用のハンドラーを作成します。

#### 戻り値 {#returns-2}

(`event`) => `void`

***

### getVisibleFlatColumns {#getvisibleflatcolumns}

```ts
getVisibleFlatColumns: () => Column<TFeatures, TData, unknown>[];
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:50](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L50)

表示中の列を、テーブルの平坦な順で並べます。表示中の子孫を持つ親の列も含みます。

#### 戻り値 {#returns-3}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getVisibleLeafColumns {#getvisibleleafcolumns}

```ts
getVisibleLeafColumns: () => Column<TFeatures, TData, unknown>[];
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:54](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L54)

表示中の末端の列を、行のセルとヘッダーで使う順で並べます。

#### 戻り値 {#returns-4}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### resetColumnVisibility {#resetcolumnvisibility}

```ts
resetColumnVisibility: (defaultState?) => void;
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:60](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L60)

`columnVisibility` を `initialState.columnVisibility` に戻します。

`true` を渡すと、初期状態を無視して `{}` に戻します。

#### パラメーター {#parameters}

##### defaultState? {#defaultstate}

`boolean`

#### 戻り値 {#returns-5}

`void`

***

### setColumnVisibility {#setcolumnvisibility}

```ts
setColumnVisibility: (updater) => void;
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:64](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L64)

次のマップかアップデーター関数で、列の表示の状態を更新します。

#### パラメーター {#parameters-1}

##### updater {#updater}

[`Updater`](../type-aliases/Updater.md)\<[`ColumnVisibilityState`](../type-aliases/ColumnVisibilityState.md)\>

#### 戻り値 {#returns-6}

`void`

***

### toggleAllColumnsVisible {#toggleallcolumnsvisible}

```ts
toggleAllColumnsVisible: (value?) => void;
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:68](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L68)

すべての列の表示を切り替えます。

#### パラメーター {#parameters-2}

##### value? {#value}

`boolean`

#### 戻り値 {#returns-7}

`void`
