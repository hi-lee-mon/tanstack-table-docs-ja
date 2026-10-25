---
id: table_getCenterHeaderGroups
title: table_getCenterHeaderGroups
---

```ts
function table_getCenterHeaderGroups<TFeatures, TData>(table): HeaderGroup<TFeatures, TData>[];
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:430](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L430)

固定されていない表示中の列について、ヘッダーグループを作ります。

中央の領域のヘッダーグループを作る前に、先頭と末尾に固定された列 ID を、表示中の末端の列のリストから取り除きます。

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
const headerGroups = table_getCenterHeaderGroups(table)
```
