---
id: CellSelectionBounds
title: CellSelectionBounds
---

定義元: [features/cell-selection/cellSelectionFeature.types.ts:53](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L53)

表示順のインデックス（両端を含む）に解決された範囲です。

角が解決できなくなった範囲は、端に寄せずに除外されます。そのため、角がフィルターで除かれた範囲は、状態には残りますが選択には何も加えません。

## プロパティ {#properties}

### maxColumnIndex {#maxcolumnindex}

```ts
maxColumnIndex: number;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:54](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L54)

***

### maxRowIndex {#maxrowindex}

```ts
maxRowIndex: number;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:55](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L55)

***

### minColumnIndex {#mincolumnindex}

```ts
minColumnIndex: number;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:56](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L56)

***

### minRowIndex {#minrowindex}

```ts
minRowIndex: number;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:57](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L57)
