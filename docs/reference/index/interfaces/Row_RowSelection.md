---
id: Row_RowSelection
title: Row_RowSelection
---

定義元: [features/row-selection/rowSelectionFeature.types.ts:89](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L89)

## プロパティ {#properties}

### getCanMultiSelect {#getcanmultiselect}

```ts
getCanMultiSelect: () => boolean;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:93](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L93)

この行を他の行と一緒に選択できるかどうかを判定します。

#### 戻り値 {#returns}

`boolean`

***

### getCanSelect {#getcanselect}

```ts
getCanSelect: () => boolean;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:97](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L97)

この行が現在選択できるかどうかを判定します。

#### 戻り値 {#returns-1}

`boolean`

***

### getCanSelectSubRows {#getcanselectsubrows}

```ts
getCanSelectSubRows: () => boolean;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:101](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L101)

この行を選択したときに、そのサブ行も選択するかどうかを判定します。

#### 戻り値 {#returns-2}

`boolean`

***

### getIsAllSubRowsSelected {#getisallsubrowsselected}

```ts
getIsAllSubRowsSelected: () => boolean;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:105](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L105)

選択可能な子孫がすべて選択されているかどうかを判定します。

#### 戻り値 {#returns-3}

`boolean`

***

### getIsSelected {#getisselected}

```ts
getIsSelected: () => boolean;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:109](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L109)

この行 ID が選択されているかどうかを判定します。

#### 戻り値 {#returns-4}

`boolean`

***

### getIsSomeSelected {#getissomeselected}

```ts
getIsSomeSelected: () => boolean;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:113](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L113)

選択可能な子孫の一部が選択されているかどうかを判定します。

#### 戻り値 {#returns-5}

`boolean`

***

### getToggleSelectedHandler {#gettoggleselectedhandler}

```ts
getToggleSelectedHandler: (opts?) => (event) => void;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:120](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L120)

この行の選択状態を切り替える、チェックボックス用のハンドラーを作成します。
Shift キーでの範囲選択で修飾キーを検出できるよう、元のチェックボックスのクリックイベントか、`nativeEvent` にそのクリックを持つフレームワークのイベントを渡してください。

#### パラメーター {#parameters}

##### opts? {#opts}

[`ToggleSelectedOptions`](ToggleSelectedOptions.md)

#### 戻り値 {#returns-6}

(`event`) => `void`

***

### toggleSelected {#toggleselected}

```ts
toggleSelected: (value?, opts?) => void;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:126](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L126)

行を選択または選択解除します。

#### パラメーター {#parameters-1}

##### value? {#value}

`boolean`

##### opts? {#opts-1}

[`ToggleSelectedOptions`](ToggleSelectedOptions.md)

#### 戻り値 {#returns-7}

`void`
