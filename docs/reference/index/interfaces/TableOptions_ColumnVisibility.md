---
id: TableOptions_ColumnVisibility
title: TableOptions_ColumnVisibility
---

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:12](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L12)

## プロパティ {#properties}

### enableHiding? {#enablehiding}

```ts
optional enableHiding?: boolean;
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:16](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L16)

列を非表示にできるようにするかどうかです。既定値は `true` です。

***

### onColumnVisibilityChange? {#oncolumnvisibilitychange}

```ts
optional onColumnVisibilityChange?: OnChangeFn<ColumnVisibilityState>;
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:22](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L22)

列の表示の状態が変わったときに、アップデーターを渡して呼び出されます。外部の状態を使う場合は `state.columnVisibility` と組み合わせてください。外部のアトムなら、このコールバックなしでスライスを持てます。
