---
id: Table_ColumnPinning
title: Table_ColumnPinning
---

定義元: [features/column-pinning/columnPinningFeature.types.ts:98](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L98)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### \_orderByColumnPinning {#_orderbycolumnpinning}

```ts
_orderByColumnPinning: <TItem>(items, getColumnId, getItemsByColumnId?) => TItem[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:114](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L114)

**`Internal`**

表示中の末端の列や行の表示中のセルのように、それぞれが末端の列に属する要素を並べます。並び順は、先頭に固定された要素（固定した順）、固定されていない要素（渡された順）、末尾に固定された要素（固定した順）です。
コアのヘッダー、行の表示中のセル、セル選択は、これを通して並べられます。

`getItemsByColumnId` は、同じ要素の既存の検索用マップを返してもかまいません。これが読まれるのは、何かが固定されているときだけです。

#### 型パラメーター {#type-parameters-1}

##### TItem {#titem}

`TItem`

#### パラメーター {#parameters}

##### items {#items}

`TItem`[]

##### getColumnId {#getcolumnid}

(`item`) => `string`

##### getItemsByColumnId? {#getitemsbycolumnid}

() => `Record`\<`string`, `TItem` \| `undefined`\>

#### 戻り値 {#returns}

`TItem`[]

***

### getCenterFlatHeaders {#getcenterflatheaders}

```ts
getCenterFlatHeaders: () => Header<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:123](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L123)

固定されていない列について、中央領域の平坦なヘッダーを作ります。親のヘッダーも含みます。

#### 戻り値 {#returns-1}

[`Header`](../type-aliases/Header.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getCenterFooterGroups {#getcenterfootergroups}

```ts
getCenterFooterGroups: () => HeaderGroup<TFeatures, TData>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:127](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L127)

固定されていない列の中央領域について、フッターグループを作ります。

#### 戻り値 {#returns-2}

[`HeaderGroup`](HeaderGroup.md)\<`TFeatures`, `TData`\>[]

***

### getCenterHeaderGroups {#getcenterheadergroups}

```ts
getCenterHeaderGroups: () => HeaderGroup<TFeatures, TData>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:131](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L131)

固定されていない列の中央領域について、ヘッダーグループを作ります。

#### 戻り値 {#returns-3}

[`HeaderGroup`](HeaderGroup.md)\<`TFeatures`, `TData`\>[]

***

### getCenterLeafColumns {#getcenterleafcolumns}

```ts
getCenterLeafColumns: () => Column<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:135](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L135)

先頭にも末尾にも固定されていない末端の列を取得します。

#### 戻り値 {#returns-4}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getCenterLeafHeaders {#getcenterleafheaders}

```ts
getCenterLeafHeaders: () => Header<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:139](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L139)

固定されていない列について、中央領域の末端のヘッダーを作ります。

#### 戻り値 {#returns-5}

[`Header`](../type-aliases/Header.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getCenterVisibleLeafColumns {#getcentervisibleleafcolumns}

```ts
getCenterVisibleLeafColumns: () => Column<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:143](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L143)

固定されていない中央領域にある、表示中の末端の列を並べます。

#### 戻り値 {#returns-6}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getEndFlatHeaders {#getendflatheaders}

```ts
getEndFlatHeaders: () => Header<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:177](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L177)

固定された列について、論理的な末尾領域の平坦なヘッダーを作ります。親のヘッダーも含みます。

#### 戻り値 {#returns-7}

[`Header`](../type-aliases/Header.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getEndFooterGroups {#getendfootergroups}

```ts
getEndFooterGroups: () => HeaderGroup<TFeatures, TData>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:181](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L181)

論理的な末尾に固定された列について、フッターグループを作ります。

#### 戻り値 {#returns-8}

[`HeaderGroup`](HeaderGroup.md)\<`TFeatures`, `TData`\>[]

***

### getEndHeaderGroups {#getendheadergroups}

```ts
getEndHeaderGroups: () => HeaderGroup<TFeatures, TData>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:185](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L185)

論理的な末尾に固定された列について、ヘッダーグループを作ります。

#### 戻り値 {#returns-9}

[`HeaderGroup`](HeaderGroup.md)\<`TFeatures`, `TData`\>[]

***

### getEndLeafColumns {#getendleafcolumns}

```ts
getEndLeafColumns: () => Column<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:189](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L189)

論理的な末尾領域に固定された末端の列を、固定の状態の順に取得します。

#### 戻り値 {#returns-10}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getEndLeafHeaders {#getendleafheaders}

```ts
getEndLeafHeaders: () => Header<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:193](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L193)

論理的な末尾に固定された列について、末端のヘッダーを作ります。

#### 戻り値 {#returns-11}

[`Header`](../type-aliases/Header.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getEndVisibleLeafColumns {#getendvisibleleafcolumns}

```ts
getEndVisibleLeafColumns: () => Column<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:197](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L197)

論理的な末尾の固定領域にある、表示中の末端の列を並べます。

#### 戻り値 {#returns-12}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getIsSomeColumnsPinned {#getissomecolumnspinned}

```ts
getIsSomeColumnsPinned: (position?) => boolean;
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:147](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L147)

固定されている列があるかどうかを判定します。片側だけに絞ることもできます。

#### パラメーター {#parameters-1}

##### position? {#position}

[`ColumnPinningPosition`](../type-aliases/ColumnPinningPosition.md)

#### 戻り値 {#returns-13}

`boolean`

***

### getPinnedLeafColumns {#getpinnedleafcolumns}

```ts
getPinnedLeafColumns: (position) => Column<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:211](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L211)

指定した固定領域の、固定された末端の列を返します。

#### パラメーター {#parameters-2}

##### position {#position-1}

  \| [`ColumnPinningPosition`](../type-aliases/ColumnPinningPosition.md)
  \| `"center"`

#### 戻り値 {#returns-14}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getPinnedVisibleLeafColumns {#getpinnedvisibleleafcolumns}

```ts
getPinnedVisibleLeafColumns: (position) => Column<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:217](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L217)

指定した固定領域の、表示中の末端の列を並べます。

#### パラメーター {#parameters-3}

##### position {#position-2}

  \| [`ColumnPinningPosition`](../type-aliases/ColumnPinningPosition.md)
  \| `"center"`

#### 戻り値 {#returns-15}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getStartFlatHeaders {#getstartflatheaders}

```ts
getStartFlatHeaders: () => Header<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:152](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L152)

固定された列について、論理的な先頭領域の平坦なヘッダーを作ります。親のヘッダーも含みます。

#### 戻り値 {#returns-16}

[`Header`](../type-aliases/Header.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getStartFooterGroups {#getstartfootergroups}

```ts
getStartFooterGroups: () => HeaderGroup<TFeatures, TData>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:156](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L156)

論理的な先頭に固定された列について、フッターグループを作ります。

#### 戻り値 {#returns-17}

[`HeaderGroup`](HeaderGroup.md)\<`TFeatures`, `TData`\>[]

***

### getStartHeaderGroups {#getstartheadergroups}

```ts
getStartHeaderGroups: () => HeaderGroup<TFeatures, TData>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:160](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L160)

論理的な先頭に固定された列について、ヘッダーグループを作ります。

#### 戻り値 {#returns-18}

[`HeaderGroup`](HeaderGroup.md)\<`TFeatures`, `TData`\>[]

***

### getStartLeafColumns {#getstartleafcolumns}

```ts
getStartLeafColumns: () => Column<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:164](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L164)

論理的な先頭領域に固定された末端の列を、固定の状態の順に取得します。

#### 戻り値 {#returns-19}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getStartLeafHeaders {#getstartleafheaders}

```ts
getStartLeafHeaders: () => Header<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:168](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L168)

論理的な先頭に固定された列について、末端のヘッダーを作ります。

#### 戻り値 {#returns-20}

[`Header`](../type-aliases/Header.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getStartVisibleLeafColumns {#getstartvisibleleafcolumns}

```ts
getStartVisibleLeafColumns: () => Column<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:172](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L172)

論理的な先頭の固定領域にある、表示中の末端の列を並べます。

#### 戻り値 {#returns-21}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### resetColumnPinning {#resetcolumnpinning}

```ts
resetColumnPinning: (defaultState?) => void;
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:203](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L203)

`columnPinning` を `initialState.columnPinning` に戻します。

`true` を渡すと、初期状態を無視して、先頭と末尾が空の配列の状態に戻します。

#### パラメーター {#parameters-4}

##### defaultState? {#defaultstate}

`boolean`

#### 戻り値 {#returns-22}

`void`

***

### setColumnPinning {#setcolumnpinning}

```ts
setColumnPinning: (updater) => void;
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:207](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L207)

次の状態かアップデーター関数で、列の固定の状態を更新します。

#### パラメーター {#parameters-5}

##### updater {#updater}

[`Updater`](../type-aliases/Updater.md)\<[`ColumnPinningState`](ColumnPinningState.md)\>

#### 戻り値 {#returns-23}

`void`
