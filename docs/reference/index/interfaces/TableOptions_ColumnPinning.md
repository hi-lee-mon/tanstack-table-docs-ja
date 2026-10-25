---
id: TableOptions_ColumnPinning
title: TableOptions_ColumnPinning
---

定義元: [features/column-pinning/columnPinningFeature.types.ts:26](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L26)

## プロパティ {#properties}

### enableColumnPinning? {#enablecolumnpinning}

```ts
optional enableColumnPinning?: boolean;
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:37](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L37)

列を論理的な先頭と末尾の領域に固定できるようにします。

LTR の言語やレイアウトでは、ふつう先頭は左、末尾は右にあたります。RTL の言語やレイアウトでは、ふつう先頭は右、末尾は左にあたります。

既定値は `true` です。列定義の `enablePinning` で、個別の列を対象から外すこともできます。

***

### onColumnPinningChange? {#oncolumnpinningchange}

```ts
optional onColumnPinningChange?: OnChangeFn<ColumnPinningState>;
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:43](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L43)

列の固定の状態が変わったときに、アップデーターを渡して呼び出されます。外部の状態を使う場合は `state.columnPinning` と組み合わせてください。外部のアトムなら、このコールバックなしでスライスを持てます。
