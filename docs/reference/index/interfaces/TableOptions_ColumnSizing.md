---
id: TableOptions_ColumnSizing
title: TableOptions_ColumnSizing
---

定義元: [features/column-sizing/columnSizingFeature.types.ts:48](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L48)

## プロパティ {#properties}

### onColumnSizingChange? {#oncolumnsizingchange}

```ts
optional onColumnSizingChange?: OnChangeFn<ColumnSizingState>;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:54](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L54)

確定した列幅の状態が変わったときに、アップデーターを渡して呼び出されます。外部の状態を使う場合は `state.columnSizing` と組み合わせてください。外部のアトムなら、このコールバックなしでスライスを持てます。
