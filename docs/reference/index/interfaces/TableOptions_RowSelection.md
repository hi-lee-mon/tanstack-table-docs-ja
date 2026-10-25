---
id: TableOptions_RowSelection
title: TableOptions_RowSelection
---

定義元: [features/row-selection/rowSelectionFeature.types.ts:34](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L34)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### enableMultiRowSelection? {#enablemultirowselection}

```ts
optional enableMultiRowSelection?: boolean | ((row) => boolean);
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:48](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L48)

行を他の行と一緒に選択できるようにします。

述語関数を渡すと、行ごとに判定できます。既定値は `true` です。

***

### enableRowRangeSelection? {#enablerowrangeselection}

```ts
optional enableRowRangeSelection?: boolean;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:42](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L42)

`row.getToggleSelectedHandler()` を通して、両端を含む行の範囲を選択できるようにします。既定値は `true` です。

***

### enableRowSelection? {#enablerowselection}

```ts
optional enableRowSelection?: boolean | ((row) => boolean);
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:54](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L54)

行を選択できるようにします。

述語関数を渡すと、行ごとに判定できます。既定値は `true` です。

***

### enableSubRowSelection? {#enablesubrowselection}

```ts
optional enableSubRowSelection?: boolean | ((row) => boolean);
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:62](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L62)

親の行を選択したときに、そのサブ行も選択するかどうかを制御します。

述語関数を渡すと、行ごとに判定できます。展開やグループ化の機能と組み合わせるときに特に便利で、既定値は `true` です。
全選択と、すべて選択されているかを返す getter も、サブ行の選択を禁止している親の子孫は対象から外します。

***

### isRowRangeSelectionEvent? {#isrowrangeselectionevent}

```ts
optional isRowRangeSelectionEvent?: (event) => boolean;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:70](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L70)

行選択のハンドラーのイベントで、直近のハンドラー操作から数えた両端を含む範囲を、選択するか選択解除するかを決めます。

既定では、イベント自体または `event.nativeEvent` に `shiftKey` があるイベントを、範囲選択のイベントとして扱います。

#### パラメーター {#parameters}

##### event {#event}

`unknown`

#### 戻り値 {#returns}

`boolean`

***

### onRowSelectionChange? {#onrowselectionchange}

```ts
optional onRowSelectionChange?: OnChangeFn<RowSelectionState>;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:76](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L76)

行選択の状態が変わったときに、アップデーターを渡して呼び出されます。外部の状態を使う場合は `state.rowSelection` と組み合わせてください。外部のアトムなら、このコールバックなしでスライスを持てます。
