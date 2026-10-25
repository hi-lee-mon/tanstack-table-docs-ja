---
id: Table_CellSelection
title: Table_CellSelection
---

定義元: [features/cell-selection/cellSelectionFeature.types.ts:207](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L207)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### \_isSelectingCells {#_isselectingcells}

```ts
_isSelectingCells: boolean;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:220](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L220)

**`Internal`**

ドラッグでの選択が現在進行中かどうかです。

状態ではなく、リアクティブでないインスタンスのデータです。読むのはマウスのハンドラーだけで、ここから描画されるものはありません。スライスに入れないことで、ドラッグの途中で保存された選択を復元しても、ドラッグ中のまま固まることがありません。

***

### autoResetCellSelection {#autoresetcellselection}

```ts
autoResetCellSelection: () => void;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:227](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L227)

`data` が変わったあとに、セル選択のリセットを予約します。

`autoResetAll` と `autoResetCellSelection` に従います。コア行モデルから呼ばれるので、自分で呼ぶ必要はほとんどありません。

#### 戻り値 {#returns}

`void`

***

### extendCellSelection {#extendcellselection}

```ts
extendCellSelection: (direction) => void;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:231](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L231)

アンカーを固定したまま、アクティブな範囲を指定した方向に1つ広げます。

#### パラメーター {#parameters}

##### direction {#direction}

[`CellSelectionDirection`](../type-aliases/CellSelectionDirection.md)

#### 戻り値 {#returns-1}

`void`

***

### getCellSelectionBounds {#getcellselectionbounds}

```ts
getCellSelectionBounds: () => CellSelectionBounds[];
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:239](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L239)

すべての包含と除外の操作を適用したあとの最終的な選択を、互いに重ならない、両端を含む表示順インデックスの長方形として返します。

これは、セルごとの読み取りがすべて通る、メモ化されたキャッシュです。角が解決できなくなった範囲は除外されます。

#### 戻り値 {#returns-2}

[`CellSelectionBounds`](CellSelectionBounds.md)[]

***

### getCellSelectionColumnIds {#getcellselectioncolumnids}

```ts
getCellSelectionColumnIds: () => string[];
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:252](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L252)

選択範囲と交わるすべての列の ID を返します。

#### 戻り値 {#returns-3}

`string`[]

***

### getCellSelectionColumnIndexes {#getcellselectioncolumnindexes}

```ts
getCellSelectionColumnIndexes: () => Record<string, number>;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:261](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L261)

**`Internal`**

現在の列の並び順について、列 ID から表示インデックスへのマップを返します。

`columnOrderingFeature` がなくても検索結果がメモ化されたままになるよう、登録されています。その静的関数 `getColumnIndexes` は呼ぶたびに作り直すためです。

#### 戻り値 {#returns-4}

`Record`\<`string`, `number`\>

***

### getCellSelectionMergeBounds {#getcellselectionmergebounds}

```ts
getCellSelectionMergeBounds: () => CellSelectionBounds[];
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:248](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L248)

描画中の行に含まれる結合セルの長方形を、選択と同じ表示順インデックスの座標で返します。`cellSpanningFeature` が登録されていなければ空の配列を返します。

選択の長方形はこれらを完全に含むように広げられます。そのため、結合セルは常に、全体が選択されているか、全体が選択されていないかのどちらかになります。

#### 戻り値 {#returns-5}

[`CellSelectionBounds`](CellSelectionBounds.md)[]

***

### getCellSelectionRowIds {#getcellselectionrowids}

```ts
getCellSelectionRowIds: () => string[];
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:265](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L265)

選択範囲と交わるすべての行の ID を返します。

#### 戻り値 {#returns-6}

`string`[]

***

### getFocusedCell {#getfocusedcell}

```ts
getFocusedCell: () =>
  | Cell<TFeatures, TData, any>
  | undefined;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:270](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L270)

アクティブなセル、つまり直近の操作のアンカーを返します。
除外の操作でのアクティブなセルは、選択されていなくてもフォーカスされます。

#### 戻り値 {#returns-7}

  \| [`Cell`](../type-aliases/Cell.md)\<`TFeatures`, `TData`, `any`\>
  \| `undefined`

***

### getSelectedCellCount {#getselectedcellcount}

```ts
getSelectedCellCount: () => number;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:277](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L277)

選択されているセルの数を返します。

セルごとの `enableCellSelection` 述語関数のために1つずつ数える必要がない限り、長方形の計算で求めます。

#### 戻り値 {#returns-8}

`number`

***

### getSelectedCellIds {#getselectedcellids}

```ts
getSelectedCellIds: () => string[];
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:284](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L284)

選択されているすべてのセルの一意な ID を、行優先の順で返します。

選択を展開するので、選択範囲を1回なめる分のコストがかかります。メモ化されており、呼ばない限り実行されません。

#### 戻り値 {#returns-9}

`string`[]

***

### getSelectedCellRangesData {#getselectedcellrangesdata}

```ts
getSelectedCellRangesData: () => unknown[][][];
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:292](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L292)

最終的な選択の各領域の値を、行優先のグリッドとして返します。

インデックスは `[regionIndex][rowIndex][columnIndex]` の順です。これをクリップボード用のテキストに変換する処理は利用者側に任せています。区切り文字、null の表し方、引用符の規則はアプリケーションが決めることだからです。

#### 戻り値 {#returns-10}

`unknown`[][][]

***

### moveCellSelection {#movecellselection}

```ts
moveCellSelection: (direction) => void;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:297](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L297)

選択を指定した方向に1つ動かし、1つのセルにまとめます。選択できない列は飛ばします。

#### パラメーター {#parameters-1}

##### direction {#direction-1}

[`CellSelectionDirection`](../type-aliases/CellSelectionDirection.md)

#### 戻り値 {#returns-11}

`void`

***

### resetCellSelection {#resetcellselection}

```ts
resetCellSelection: (defaultState?) => void;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:303](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L303)

`cellSelection` を `initialState.cellSelection` に戻します。

`true` を渡すと、初期状態を無視して空の選択に戻します。

#### パラメーター {#parameters-2}

##### defaultState? {#defaultstate}

`boolean`

#### 戻り値 {#returns-12}

`void`

***

### selectAllCells {#selectallcells}

```ts
selectAllCells: () => void;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:307](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L307)

テーブル内の選択できるすべてのセルを、1つの範囲として選択します。

#### 戻り値 {#returns-13}

`void`

***

### selectCellRange {#selectcellrange}

```ts
selectCellRange: (range, opts?) => void;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:311](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L311)

指定した replace / include / exclude のモードで、長方形を選択します。

#### パラメーター {#parameters-3}

##### range {#range}

[`CellSelectionRange`](CellSelectionRange.md)

##### opts? {#opts}

[`SelectCellRangeOptions`](SelectCellRangeOptions.md)

#### 戻り値 {#returns-14}

`void`

***

### setCellSelection {#setcellselection}

```ts
setCellSelection: (updater) => void;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:318](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L318)

次の値かアップデーター関数で、セル選択の状態を更新します。

#### パラメーター {#parameters-4}

##### updater {#updater}

[`Updater`](../type-aliases/Updater.md)\<[`CellSelectionState`](../type-aliases/CellSelectionState.md)\>

#### 戻り値 {#returns-15}

`void`

***

### setFocusedCell {#setfocusedcell}

```ts
setFocusedCell: (rowId, columnId) => void;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:322](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L322)

選択を、指定した座標の1つのセルにまとめます。

#### パラメーター {#parameters-5}

##### rowId {#rowid}

`string`

##### columnId {#columnid}

`string`

#### 戻り値 {#returns-16}

`void`
