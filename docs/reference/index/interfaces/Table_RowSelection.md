---
id: Table_RowSelection
title: Table_RowSelection
---

定義元: [features/row-selection/rowSelectionFeature.types.ts:129](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L129)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### \_lastSelectedRowId {#_lastselectedrowid}

```ts
_lastSelectedRowId: string | null;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:138](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L138)

**`Internal`**

行選択のハンドラーで直近に操作された行です。

***

### getFilteredSelectedRowModel {#getfilteredselectedrowmodel}

```ts
getFilteredSelectedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:142](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L142)

フィルタリング後の行から、選択された行の行モデルを作ります。

#### 戻り値 {#returns}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

***

### getGroupedSelectedRowModel {#getgroupedselectedrowmodel}

```ts
getGroupedSelectedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:146](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L146)

グループ化後の行から、選択された行の行モデルを作ります。

#### 戻り値 {#returns-1}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

***

### getIsAllPageRowsSelected {#getisallpagerowsselected}

```ts
getIsAllPageRowsSelected: () => boolean;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:155](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L155)

現在のページにある選択可能な行が、すべて選択されているかどうかを判定します。
祖先がサブ行の選択を禁止しているサブ行は無視します。

#### 戻り値 {#returns-2}

`boolean`

***

### getIsAllRowsSelected {#getisallrowsselected}

```ts
getIsAllRowsSelected: () => boolean;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:160](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L160)

フィルタリング後の選択可能な行が、すべて選択されているかどうかを判定します。
祖先がサブ行の選択を禁止しているサブ行は無視します。

#### 戻り値 {#returns-3}

`boolean`

***

### getIsSomePageRowsSelected {#getissomepagerowsselected}

```ts
getIsSomePageRowsSelected: () => boolean;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:164](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L164)

現在のページにある選択可能な行が、少なくとも1つ選択されているかどうかを判定します。

#### 戻り値 {#returns-4}

`boolean`

***

### getIsSomeRowsSelected {#getissomerowsselected}

```ts
getIsSomeRowsSelected: () => boolean;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:168](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L168)

選択されている行 ID が少なくとも1つあるかどうかを判定します。

#### 戻り値 {#returns-5}

`boolean`

***

### getPreSelectedRowModel {#getpreselectedrowmodel}

```ts
getPreSelectedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:172](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L172)

行選択を適用する前の、すべての行のコア行モデルを返します。

#### 戻り値 {#returns-6}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

***

### getSelectedRowIds {#getselectedrowids}

```ts
getSelectedRowIds: () => string[];
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:150](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L150)

選択されているすべての行の ID を返します。

#### 戻り値 {#returns-7}

`string`[]

***

### getSelectedRowModel {#getselectedrowmodel}

```ts
getSelectedRowModel: () => RowModel<TFeatures, TData>;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:176](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L176)

コア行モデルから、選択された行の行モデルを作ります。

#### 戻り値 {#returns-8}

[`RowModel`](RowModel.md)\<`TFeatures`, `TData`\>

***

### getToggleAllPageRowsSelectedHandler {#gettoggleallpagerowsselectedhandler}

```ts
getToggleAllPageRowsSelectedHandler: () => (event) => void;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:180](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L180)

現在のページのすべての行を切り替える、チェックボックス用のハンドラーを作成します。

#### 戻り値 {#returns-9}

(`event`) => `void`

***

### getToggleAllRowsSelectedHandler {#gettoggleallrowsselectedhandler}

```ts
getToggleAllRowsSelectedHandler: () => (event) => void;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:184](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L184)

選択可能なすべての行を切り替える、チェックボックス用のハンドラーを作成します。

#### 戻り値 {#returns-10}

(`event`) => `void`

***

### resetRowSelection {#resetrowselection}

```ts
resetRowSelection: (defaultState?) => void;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:190](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L190)

`rowSelection` を `initialState.rowSelection` に戻します。

`true` を渡すと、初期状態を無視して `{}` に戻します。

#### パラメーター {#parameters}

##### defaultState? {#defaultstate}

`boolean`

#### 戻り値 {#returns-11}

`void`

***

### setRowSelection {#setrowselection}

```ts
setRowSelection: (updater) => void;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:194](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L194)

次のマップかアップデーター関数で、行選択の状態を更新します。

#### パラメーター {#parameters-1}

##### updater {#updater}

[`Updater`](../type-aliases/Updater.md)\<[`RowSelectionState`](../type-aliases/RowSelectionState.md)\>

#### 戻り値 {#returns-12}

`void`

***

### toggleAllPageRowsSelected {#toggleallpagerowsselected}

```ts
toggleAllPageRowsSelected: (value?, opts?) => void;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:198](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L198)

現在のページのすべての行を選択または選択解除します。

#### パラメーター {#parameters-2}

##### value? {#value}

`boolean`

##### opts? {#opts}

###### deselectAll? {#deselectall}

`boolean`

#### 戻り値 {#returns-13}

`void`

***

### toggleAllRowsSelected {#toggleallrowsselected}

```ts
toggleAllRowsSelected: (value?, opts?) => void;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:208](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L208)

テーブルのすべての行を選択または選択解除します。

選択解除しても、選択できない行は選択のマップに残ります。`opts.deselectAll` が `true` の場合は残りません。

#### パラメーター {#parameters-3}

##### value? {#value-1}

`boolean`

##### opts? {#opts-1}

###### deselectAll? {#deselectall-1}

`boolean`

#### 戻り値 {#returns-14}

`void`
