---
id: Row_ColumnVisibility
title: Row_ColumnVisibility
---

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:78](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L78)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getVisibleCells {#getvisiblecells}

```ts
getVisibleCells: () => Cell<TFeatures, TData, unknown>[];
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:85](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L85)

現在表示されている列について、この行のセルを取得します。

#### 戻り値 {#returns}

[`Cell`](../type-aliases/Cell.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getVisibleCellsByColumnId {#getvisiblecellsbycolumnid}

```ts
getVisibleCellsByColumnId: () => Record<string, Cell<TFeatures, TData, unknown>>;
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:89](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L89)

この行の現在表示されているセルを、列 ID で引けるマップにします。

#### 戻り値 {#returns-1}

`Record`\<`string`, [`Cell`](../type-aliases/Cell.md)\<`TFeatures`, `TData`, `unknown`\>\>
