---
id: TableOptions_ColumnGrouping
title: TableOptions_ColumnGrouping
---

定義元: [features/column-grouping/columnGroupingFeature.types.ts:95](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L95)

## プロパティ {#properties}

### enableGrouping? {#enablegrouping}

```ts
optional enableGrouping?: boolean;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:99](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L99)

このテーブルで列をグループ化できるようにします。

***

### groupedColumnMode? {#groupedcolumnmode}

```ts
optional groupedColumnMode?: false | "reorder" | "remove";
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:103](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L103)

既定では、グループ化した列は自動で列の並びの先頭に移されます。取り除きたい場合やそのままにしておきたい場合は、ここで該当するモードを指定してください。

***

### manualGrouping? {#manualgrouping}

```ts
optional manualGrouping?: boolean;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:107](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L107)

手動のグループ化を有効にします。このオプションを `true` にすると、テーブルは `getGroupedRowModel()` で行を自動でグループ化せず、テーブルに渡す前に行を自分でグループ化しておくことを前提にします。
サーバーサイドでグループ化と集計をする場合に便利です。

***

### onGroupingChange? {#ongroupingchange}

```ts
optional onGroupingChange?: OnChangeFn<GroupingState>;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:113](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L113)

グループ化の状態が変わったときに、アップデーターを渡して呼び出されます。外部の状態を使う場合は `state.grouping` と組み合わせてください。外部のアトムなら、このコールバックなしでスライスを持てます。
