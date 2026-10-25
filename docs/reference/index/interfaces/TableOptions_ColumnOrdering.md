---
id: TableOptions_ColumnOrdering
title: TableOptions_ColumnOrdering
---

定義元: [features/column-ordering/columnOrderingFeature.types.ts:31](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L31)

## プロパティ {#properties}

### onColumnOrderChange? {#oncolumnorderchange}

```ts
optional onColumnOrderChange?: OnChangeFn<ColumnOrderState>;
```

定義元: [features/column-ordering/columnOrderingFeature.types.ts:37](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L37)

列の並び順の状態が変わったときに、アップデーターを渡して呼び出されます。外部の状態を使う場合は `state.columnOrder` と組み合わせてください。外部のアトムなら、このコールバックなしでスライスを持てます。
