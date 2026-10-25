---
id: TableOptions_RowPinning
title: TableOptions_RowPinning
---

定義元: [features/row-pinning/rowPinningFeature.types.ts:16](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L16)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### enableRowPinning? {#enablerowpinning}

```ts
optional enableRowPinning?: boolean | ((row) => boolean);
```

定義元: [features/row-pinning/rowPinningFeature.types.ts:25](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L25)

行を上部または下部の領域に固定できるようにします。

述語関数を渡すと、行ごとに判定できます。既定値は `true` です。

***

### keepPinnedRows? {#keeppinnedrows}

```ts
optional keepPinnedRows?: boolean;
```

定義元: [features/row-pinning/rowPinningFeature.types.ts:29](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L29)

`false` の場合、固定された行も、フィルタリングやページネーションでテーブルから外れると表示されません。`true` の場合、固定された行はフィルタリングやページネーションに関係なく常に表示されます。既定値は `true` です。

***

### onRowPinningChange? {#onrowpinningchange}

```ts
optional onRowPinningChange?: OnChangeFn<RowPinningState>;
```

定義元: [features/row-pinning/rowPinningFeature.types.ts:35](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L35)

行の固定の状態が変わったときに、アップデーターを渡して呼び出されます。外部の状態を使う場合は `state.rowPinning` と組み合わせてください。外部のアトムなら、このコールバックなしでスライスを持てます。
