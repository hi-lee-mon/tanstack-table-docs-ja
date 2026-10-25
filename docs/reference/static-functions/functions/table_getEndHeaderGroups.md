---
id: table_getEndHeaderGroups
title: table_getEndHeaderGroups
---

```ts
function table_getEndHeaderGroups<TFeatures, TData>(table): HeaderGroup<TFeatures, TData>[];
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:399](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L399)

末尾の領域に固定された表示中の列について、ヘッダーグループを作ります。

末端の列は `state.columnPinning.end` の順で読み取られ、固定されていないテーブルと同じヘッダーグループの組み立て処理に渡されます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`HeaderGroup`](../../index/interfaces/HeaderGroup.md)\<`TFeatures`, `TData`\>[]

## 例 {#example}

```ts
const headerGroups = table_getEndHeaderGroups(table)
```
