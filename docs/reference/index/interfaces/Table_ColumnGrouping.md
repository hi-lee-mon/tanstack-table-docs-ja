---
id: Table_ColumnGrouping
title: Table_ColumnGrouping
---

定義元: [features/column-grouping/columnGroupingFeature.types.ts:118](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L118)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### \_orderGroupedColumns {#_ordergroupedcolumns}

```ts
_orderGroupedColumns: (columns) => Column<TFeatures, TData, unknown>[];
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:128](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L128)

**`Internal`**

グループ化された末端の列を、`groupedColumnMode` の設定どおりに移動します。列の並べ替えの機能が登録されていない場合、末端の列の並び順はこれを使います。

#### パラメーター {#parameters}

##### columns {#columns}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

#### 戻り値 {#returns}

[`Column`](../type-aliases/Column.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### resetGrouping {#resetgrouping}

```ts
resetGrouping: (defaultState?) => void;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:136](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L136)

`grouping` を `initialState.grouping` に戻します。

`true` を渡すと、初期状態を無視して `[]` に戻します。

#### パラメーター {#parameters-1}

##### defaultState? {#defaultstate}

`boolean`

#### 戻り値 {#returns-1}

`void`

***

### setGrouping {#setgrouping}

```ts
setGrouping: (updater) => void;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:140](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L140)

次の順序付きの ID 配列かアップデーター関数で、グループ化の状態を更新します。

#### パラメーター {#parameters-2}

##### updater {#updater}

[`Updater`](../type-aliases/Updater.md)\<[`GroupingState`](../type-aliases/GroupingState.md)\>

#### 戻り値 {#returns-2}

`void`
