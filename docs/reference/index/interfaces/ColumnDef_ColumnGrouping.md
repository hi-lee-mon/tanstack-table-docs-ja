---
id: ColumnDef_ColumnGrouping
title: ColumnDef_ColumnGrouping
---

定義元: [features/column-grouping/columnGroupingFeature.types.ts:13](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L13)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### enableGrouping? {#enablegrouping}

```ts
optional enableGrouping?: boolean;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:22](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L22)

この列をグループ化の状態に加えられるようにします。

既定値は `true` です。テーブル側の `enableGrouping` でもグループ化が許可されている必要があります。

***

### getGroupingValue? {#getgroupingvalue}

```ts
optional getGroupingValue?: (originalRow, index, row) => any;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:29](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L29)

この列で行をグループ化するときに使う値を返します。

省略した場合、グループ化には、この列の `accessorKey` または `accessorFn` から得た値を使います。

#### パラメーター {#parameters}

##### originalRow {#originalrow}

`TData`

##### index {#index}

`number`

##### row {#row}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns}

`any`
