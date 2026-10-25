---
id: Row_ColumnGrouping
title: Row_ColumnGrouping
---

定義元: [features/column-grouping/columnGroupingFeature.types.ts:59](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L59)

## プロパティ {#properties}

### \_groupingValuesCache {#_groupingvaluescache}

```ts
_groupingValuesCache: Record<string, any>;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:60](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L60)

***

### getGroupingValue {#getgroupingvalue}

```ts
getGroupingValue: (columnId) => unknown;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:64](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L64)

列 ID について、この行のグループ化に使う値を読み取ります。

#### パラメーター {#parameters}

##### columnId {#columnid}

`string`

#### 戻り値 {#returns}

`unknown`

***

### getIsGrouped {#getisgrouped}

```ts
getIsGrouped: () => boolean;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:68](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L68)

この行がグループ行かどうかを判定します。

#### 戻り値 {#returns-1}

`boolean`

***

### groupingColumnId? {#groupingcolumnid}

```ts
optional groupingColumnId?: string;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:72](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L72)

この行がグループ化されている場合、グループ化の基準になった列の id です。

***

### groupingValue? {#groupingvalue}

```ts
optional groupingValue?: unknown;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:76](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L76)

この行がグループ化されている場合、このグループに含まれるすべての行に共通する `groupingColumnId` の一意な値です。
