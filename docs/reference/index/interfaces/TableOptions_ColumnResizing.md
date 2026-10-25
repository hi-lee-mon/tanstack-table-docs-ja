---
id: TableOptions_ColumnResizing
title: TableOptions_ColumnResizing
---

定義元: [features/column-resizing/columnResizingFeature.types.ts:20](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.types.ts#L20)

## プロパティ {#properties}

### columnResizeDirection? {#columnresizedirection}

```ts
optional columnResizeDirection?: ColumnResizeDirection;
```

定義元: [features/column-resizing/columnResizingFeature.types.ts:34](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.types.ts#L34)

ドラッグの移動量を計算するときに使うリサイズの向きを指定します。既定値は `ltr` です。

***

### columnResizeMode? {#columnresizemode}

```ts
optional columnResizeMode?: ColumnResizeMode;
```

定義元: [features/column-resizing/columnResizingFeature.types.ts:26](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.types.ts#L26)

確定した `columnSizing` の値をいつ更新するかを決めます。`onChange` はリサイズ用のつまみをドラッグしている間に幅を確定し、`onEnd` はリサイズ操作が終わったときに確定します。

***

### enableColumnResizing? {#enablecolumnresizing}

```ts
optional enableColumnResizing?: boolean;
```

定義元: [features/column-resizing/columnResizingFeature.types.ts:30](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.types.ts#L30)

テーブル全体で、列幅の変更を有効または無効にします。

***

### onColumnResizingChange? {#oncolumnresizingchange}

```ts
optional onColumnResizingChange?: OnChangeFn<columnResizingState>;
```

定義元: [features/column-resizing/columnResizingFeature.types.ts:40](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.types.ts#L40)

一時的な `columnResizing` の状態が変わったときに、アップデーターを渡して呼び出されます。外部の状態を使う場合は `state.columnResizing` と組み合わせてください。外部のアトムなら、このコールバックなしでスライスを持てます。
