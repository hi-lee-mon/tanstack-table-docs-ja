---
id: TableOptions_CellSelection
title: TableOptions_CellSelection
---

定義元: [features/cell-selection/cellSelectionFeature.types.ts:89](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L89)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### autoResetCellSelection? {#autoresetcellselection}

```ts
optional autoResetCellSelection?: boolean;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:102](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L102)

`data` が変わるたびに、セル選択を `initialState.cellSelection` に戻します。既定値は `true` です。

範囲は行 ID と列 ID で保存されます。そのため、リセットしないと、新しいデータになったときに選択がもう存在しない行を指したままになったり、新しいデータがたまたま同じ ID を使っていると気づかないうちにセルが選択し直されたりします。
データが変わっても範囲を残したい場合は `false` にしてください。なお、`autoResetAll` はこの設定より優先されます。

***

### enableCellRangeSelection? {#enablecellrangeselection}

```ts
optional enableCellRangeSelection?: boolean;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:107](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L107)

Shift キーを押しながらのクリックやドラッグで、両端を含むセルの範囲を選択できるようにします。既定値は `true` です。

***

### enableCellSelection? {#enablecellselection}

```ts
optional enableCellSelection?: boolean | ((cell) => boolean);
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:114](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L114)

セルを選択できるようにします。

述語関数を渡すと、セルごとに判定できます。列定義側でも `enableCellSelection: false` で対象から外せます。既定値は `true` です。

***

### enableCellSelectionDrag? {#enablecellselectiondrag}

```ts
optional enableCellSelectionDrag?: boolean;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:119](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L119)

セルの上をドラッグして選択を広げられるようにします。既定値は `true` です。

***

### enableMultiCellRangeSelection? {#enablemulticellrangeselection}

```ts
optional enableMultiCellRangeSelection?: boolean;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:123](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L123)

修飾キーを使った操作で範囲を追加・差し引きできるようにします。既定値は `true` です。

***

### isCellRangeSelectionEvent? {#iscellrangeselectionevent}

```ts
optional isCellRangeSelectionEvent?: (event) => boolean;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:131](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L131)

選択を始めるイベントで、選択を置き換えるのではなく、アクティブな範囲を広げるかどうかを決めます。

既定では、イベント自体または `event.nativeEvent` に `shiftKey` があるイベントを、範囲選択のイベントとして扱います。

#### パラメーター {#parameters}

##### event {#event}

`unknown`

#### 戻り値 {#returns}

`boolean`

***

### isMultiCellRangeSelectionEvent? {#ismulticellrangeselectionevent}

```ts
optional isMultiCellRangeSelectionEvent?: (event) => boolean;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:139](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L139)

選択を始めるイベントで、新しい長方形を追加するか差し引くかを決めます。どちらになるかは、開始したセルが選択されているかどうかで決まります。

既定では、イベント自体または `event.nativeEvent` に `ctrlKey` か `metaKey` があるイベントを、複数範囲のイベントとして扱います。

#### パラメーター {#parameters-1}

##### event {#event-1}

`unknown`

#### 戻り値 {#returns-1}

`boolean`

***

### onCellSelectionChange? {#oncellselectionchange}

```ts
optional onCellSelectionChange?: OnChangeFn<CellSelectionState>;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:148](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L148)

セル選択の状態が変わったときに、アップデーターを渡して呼び出されます。外部の状態を使う場合は `state.cellSelection` と組み合わせてください。外部のアトムなら、このコールバックなしでスライスを持てます。

ドラッグでは、通過したセルごとに変更が1回ずつ発生します。それが問題になる場合は、`table.atoms.cellSelection` を購読して、より細かい単位で読み取ってください。
