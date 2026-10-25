---
id: Column_RowSorting
title: Column_RowSorting
---

定義元: [features/row-sorting/rowSortingFeature.types.ts:160](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L160)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### clearSorting {#clearsorting}

```ts
clearSorting: () => void;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:167](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L167)

この列をテーブルのソートの状態から取り除きます。

#### 戻り値 {#returns}

`void`

***

### getAutoSortDir {#getautosortdir}

```ts
getAutoSortDir: () => SortDirection;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:171](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L171)

列の値から自動で推論したソートの向きを返します。

#### 戻り値 {#returns-1}

[`SortDirection`](../type-aliases/SortDirection.md)

***

### getAutoSortFn {#getautosortfn}

```ts
getAutoSortFn: () => SortFn<TFeatures, TData>;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:175](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L175)

列の値から自動で推論したソート関数を返します。

#### 戻り値 {#returns-2}

[`SortFn`](SortFn.md)\<`TFeatures`, `TData`\>

***

### getCanMultiSort {#getcanmultisort}

```ts
getCanMultiSort: () => boolean;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:179](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L179)

この列を複数列ソートできるかどうかを返します。

#### 戻り値 {#returns-3}

`boolean`

***

### getCanSort {#getcansort}

```ts
getCanSort: () => boolean;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:183](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L183)

この列をソートできるかどうかを返します。

#### 戻り値 {#returns-4}

`boolean`

***

### getFirstSortDir {#getfirstsortdir}

```ts
getFirstSortDir: () => SortDirection;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:187](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L187)

この列をソートするときに最初に使う向きを返します。

#### 戻り値 {#returns-5}

[`SortDirection`](../type-aliases/SortDirection.md)

***

### getIsSorted {#getissorted}

```ts
getIsSorted: () => false | SortDirection;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:191](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L191)

この列の現在のソートの向きを読み取ります。ソートされていなければ `false` です。

#### 戻り値 {#returns-6}

`false` \| [`SortDirection`](../type-aliases/SortDirection.md)

***

### getNextSortingOrder {#getnextsortingorder}

```ts
getNextSortingOrder: (multi?) => false | SortDirection;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:197](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L197)

次のソート順を返します。`multi` を渡すと、複数列ソートの切り替えでの順を返します。このとき、切り替えの流れでソートを外せるかどうかは `enableMultiRemove` で決まります。

#### パラメーター {#parameters}

##### multi? {#multi}

`boolean`

#### 戻り値 {#returns-7}

`false` \| [`SortDirection`](../type-aliases/SortDirection.md)

***

### getSortFn {#getsortfn}

```ts
getSortFn: () => SortFn<TFeatures, TData>;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:205](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L205)

この列で使う、解決済みのソート関数を返します。

#### 戻り値 {#returns-8}

[`SortFn`](SortFn.md)\<`TFeatures`, `TData`\>

***

### getSortIndex {#getsortindex}

```ts
getSortIndex: () => number;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:201](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L201)

順序付きのソートの状態の中で、この列の位置を探します。

#### 戻り値 {#returns-9}

`number`

***

### getToggleSortingHandler {#gettogglesortinghandler}

```ts
getToggleSortingHandler: () => ((event) => void) | undefined;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:209](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L209)

この列のソートの状態を切り替える、ヘッダーや操作部品向けのハンドラーを作成します。

#### 戻り値 {#returns-10}

((`event`) => `void`) \| `undefined`

***

### toggleSorting {#togglesorting}

```ts
toggleSorting: (desc?, isMulti?) => void;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:213](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L213)

この列のソートの状態を切り替えます。`desc` を渡すと、ソートの向きをその値に固定します。`isMulti` を渡すと、この列を複数列ソートに追加します（すでにソートされていれば切り替えます）。

#### パラメーター {#parameters-1}

##### desc? {#desc}

`boolean`

##### isMulti? {#ismulti}

`boolean`

#### 戻り値 {#returns-11}

`void`
