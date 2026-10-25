---
id: Table_RowExpanding
title: Table_RowExpanding
---

定義元: [features/row-expanding/rowExpandingFeature.types.ts:72](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L72)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### \_expandRows {#_expandrows}

```ts
_expandRows: (rowModel) => RowModel<TFeatures, TData>;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:82](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L82)

**`Internal`**

展開されたサブ行を、親のすぐ下に並べます。行の表示順とページ分割済み行モデルは、これを通して行を展開します。

#### パラメーター {#parameters}

##### rowModel {#rowmodel}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

***

### autoResetExpanded {#autoresetexpanded}

```ts
autoResetExpanded: () => void;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:91](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L91)

テーブルのデータやグループ化が変わったあとに、展開状態をリセットします。

`autoResetAll`、`autoResetExpanded`、`manualExpanding` に従います。行モデルから呼ばれるので、自分で呼ぶ必要はほとんどありません。

#### 戻り値 {#returns-1}

`void`

***

### getCanSomeRowsExpand {#getcansomerowsexpand}

```ts
getCanSomeRowsExpand: () => boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:95](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L95)

展開できる行が少なくとも1つあるかどうかを判定します。

#### 戻り値 {#returns-2}

`boolean`

***

### getExpandedDepth {#getexpandeddepth}

```ts
getExpandedDepth: () => number;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:99](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L99)

展開された行 ID のうち、いちばん深い深さを計算します。

#### 戻り値 {#returns-3}

`number`

***

### getIsAllRowsExpanded {#getisallrowsexpanded}

```ts
getIsAllRowsExpanded: () => boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:103](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L103)

現在の行モデルのすべての行が展開されているかどうかを判定します。

#### 戻り値 {#returns-4}

`boolean`

***

### getIsSomeRowsExpanded {#getissomerowsexpanded}

```ts
getIsSomeRowsExpanded: () => boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:107](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L107)

現在展開されている行があるかどうかを判定します。

#### 戻り値 {#returns-5}

`boolean`

***

### getToggleAllRowsExpandedHandler {#gettoggleallrowsexpandedhandler}

```ts
getToggleAllRowsExpandedHandler: () => (event) => void;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:111](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L111)

すべての行の展開を切り替えるハンドラーを作成します。

#### 戻り値 {#returns-6}

(`event`) => `void`

***

### resetExpanded {#resetexpanded}

```ts
resetExpanded: (defaultState?) => void;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:117](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L117)

`expanded` を `initialState.expanded` に戻します。

`true` を渡すと、初期状態を無視して `{}` に戻します。

#### パラメーター {#parameters-1}

##### defaultState? {#defaultstate}

`boolean`

#### 戻り値 {#returns-7}

`void`

***

### setExpanded {#setexpanded}

```ts
setExpanded: (updater) => void;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:121](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L121)

`true`、行 ID のマップ、アップデーター関数のいずれかで、展開状態を更新します。

#### パラメーター {#parameters-2}

##### updater {#updater}

[`Updater`](../type-aliases/Updater.md)\<[`ExpandedState`](../type-aliases/ExpandedState.md)\>

#### 戻り値 {#returns-8}

`void`

***

### toggleAllRowsExpanded {#toggleallrowsexpanded}

```ts
toggleAllRowsExpanded: (expanded?) => void;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:125](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L125)

すべての行の展開状態を切り替えます。

#### パラメーター {#parameters-3}

##### expanded? {#expanded}

`boolean`

#### 戻り値 {#returns-9}

`void`
