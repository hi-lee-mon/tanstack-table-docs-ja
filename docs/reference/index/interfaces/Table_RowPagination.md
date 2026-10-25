---
id: Table_RowPagination
title: Table_RowPagination
---

定義元: [features/row-pagination/rowPaginationFeature.types.ts:47](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L47)

## 型パラメーター {#type-parameters}

### _TFeatures {#_tfeatures}

`_TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### _TData {#_tdata}

`_TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### autoResetPageIndex {#autoresetpageindex}

```ts
autoResetPageIndex: () => void;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:58](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L58)

新しいデータ、フィルタリング、ソート、グループ化のような、ページの内容を変える変更があったあとに、ページ番号を `0` に戻します。

`autoResetAll`、`autoResetPageIndex`、`manualPagination` に従います。行モデルから呼ばれるので、自分で呼ぶ必要はほとんどありません。

#### 戻り値 {#returns}

`void`

***

### firstPage {#firstpage}

```ts
firstPage: () => void;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:97](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L97)

ページ番号を `0` にします。

#### 戻り値 {#returns-1}

`void`

***

### getCanLastPage {#getcanlastpage}

```ts
getCanLastPage: () => boolean;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:66](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L66)

現在のページより後ろに、わかっている有限の最後のページがあるかどうかを判定します。

#### 戻り値 {#returns-2}

`boolean`

***

### getCanNextPage {#getcannextpage}

```ts
getCanNextPage: () => boolean;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:62](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L62)

現在のページ番号を先に進められるかどうかを判定します。

#### 戻り値 {#returns-3}

`boolean`

***

### getCanPreviousPage {#getcanpreviouspage}

```ts
getCanPreviousPage: () => boolean;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:70](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L70)

現在のページ番号を前に戻せるかどうかを判定します。

#### 戻り値 {#returns-4}

`boolean`

***

### getPageCount {#getpagecount}

```ts
getPageCount: () => number;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:75](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L75)

`options.pageCount`、または行数とページサイズから、現在のページ数を求めます。

#### 戻り値 {#returns-5}

`number`

***

### getPageOptions {#getpageoptions}

```ts
getPageOptions: () => number[];
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:85](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L85)

現在のページ数について、0始まりのページ番号の配列を作ります。

#### 戻り値 {#returns-6}

`number`[]

***

### getRowCount {#getrowcount}

```ts
getRowCount: () => number;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:81](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L81)

ページネーションの計算に使う行数を求めます。

`options.rowCount` が優先されます。指定がなければ、ページ分割前の行モデルの行を数えます。

#### 戻り値 {#returns-7}

`number`

***

### lastPage {#lastpage}

```ts
lastPage: () => void;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:102](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L102)

ページ番号を、わかっている最後のページにします。ページ数が不明、0、有限でない場合は何もしません。

#### 戻り値 {#returns-8}

`void`

***

### nextPage {#nextpage}

```ts
nextPage: () => void;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:89](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L89)

可能なら、ページ番号を1つ増やします。

#### 戻り値 {#returns-9}

`void`

***

### previousPage {#previouspage}

```ts
previousPage: () => void;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:93](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L93)

可能なら、ページ番号を1つ減らします。

#### 戻り値 {#returns-10}

`void`

***

### resetPageIndex {#resetpageindex}

```ts
resetPageIndex: (defaultState?) => void;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:107](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L107)

`pagination.pageIndex` を初期状態に戻します。`defaultState` が `true` の場合は `0` に戻します。

#### パラメーター {#parameters}

##### defaultState? {#defaultstate}

`boolean`

#### 戻り値 {#returns-11}

`void`

***

### resetPageSize {#resetpagesize}

```ts
resetPageSize: (defaultState?) => void;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:112](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L112)

`pagination.pageSize` を初期状態に戻します。`defaultState` が `true` の場合は `10` に戻します。

#### パラメーター {#parameters-1}

##### defaultState? {#defaultstate-1}

`boolean`

#### 戻り値 {#returns-12}

`void`

***

### resetPagination {#resetpagination}

```ts
resetPagination: (defaultState?) => void;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:119](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L119)

`pagination` を `initialState.pagination` に戻します。

`true` を渡すと、初期状態を無視して `{ pageIndex: 0, pageSize: 10 }` に戻します。

#### パラメーター {#parameters-2}

##### defaultState? {#defaultstate-2}

`boolean`

#### 戻り値 {#returns-13}

`void`

***

### setPageIndex {#setpageindex}

```ts
setPageIndex: (updater) => void;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:123](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L123)

値かアップデーターで `pagination.pageIndex` を更新します。

#### パラメーター {#parameters-3}

##### updater {#updater}

[`Updater`](../type-aliases/Updater.md)\<`number`\>

#### 戻り値 {#returns-14}

`void`

***

### setPageSize {#setpagesize}

```ts
setPageSize: (updater) => void;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:127](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L127)

値かアップデーターで `pagination.pageSize` を更新します。

#### パラメーター {#parameters-4}

##### updater {#updater-1}

[`Updater`](../type-aliases/Updater.md)\<`number`\>

#### 戻り値 {#returns-15}

`void`

***

### setPagination {#setpagination}

```ts
setPagination: (updater) => void;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:131](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L131)

次の状態かアップデーター関数で、ページネーションの状態を更新します。

#### パラメーター {#parameters-5}

##### updater {#updater-2}

[`Updater`](../type-aliases/Updater.md)\<[`PaginationState`](PaginationState.md)\>

#### 戻り値 {#returns-16}

`void`
