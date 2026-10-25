---
id: table_setGrouping
title: table_setGrouping
---

```ts
function table_setGrouping<TFeatures, TData>(table, updater): void;
```

定義元: [features/column-grouping/columnGroupingFeature.utils.ts:148](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.utils.ts#L148)

グループ化のアップデーターを、テーブルのグループ化の変更ハンドラーに通します。

アップデーターには、次の `GroupingState` 配列か、前のグループ化の状態を受け取る関数を指定できます。インスタンスの `table.setGrouping` と同じ動作です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### updater {#updater}

[`Updater`](../../index/type-aliases/Updater.md)\<[`GroupingState`](../../index/type-aliases/GroupingState.md)\>

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setGrouping(table, (old) => [...old, 'status'])
```
