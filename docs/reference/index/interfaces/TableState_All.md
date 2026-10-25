---
id: TableState_All
title: TableState_All
---

定義元: [types/TableState.ts:49](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableState.ts#L49)

登録されたすべての機能の状態スライスを含む、内部用の広い状態の形です。

機能の内部処理で、他の機能が持つ省略可能なスライスを調べる必要があるときに使います。

## 継承元 {#extends}

- `Partial`\<[`TableState_CellSelection`](TableState_CellSelection.md) & [`TableState_ColumnFiltering`](TableState_ColumnFiltering.md) & [`TableState_ColumnGrouping`](TableState_ColumnGrouping.md) & [`TableState_ColumnOrdering`](TableState_ColumnOrdering.md) & [`TableState_ColumnPinning`](TableState_ColumnPinning.md) & [`TableState_ColumnResizing`](TableState_ColumnResizing.md) & [`TableState_ColumnSizing`](TableState_ColumnSizing.md) & [`TableState_ColumnVisibility`](TableState_ColumnVisibility.md) & [`TableState_GlobalFiltering`](TableState_GlobalFiltering.md) & [`TableState_RowExpanding`](TableState_RowExpanding.md) & [`TableState_RowPagination`](TableState_RowPagination.md) & [`TableState_RowPinning`](TableState_RowPinning.md) & [`TableState_RowSelection`](TableState_RowSelection.md) & [`TableState_RowSorting`](TableState_RowSorting.md)\>

## プロパティ {#properties}

### cellSelection? {#cellselection}

```ts
optional cellSelection?: CellSelectionState;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:44](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L44)

#### 継承元のメンバー {#inherited-from}

[`TableState_CellSelection`](TableState_CellSelection.md).[`cellSelection`](TableState_CellSelection.md#cellselection)

***

### columnFilters? {#columnfilters}

```ts
optional columnFilters?: ColumnFiltersState;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:34](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L34)

#### 継承元のメンバー {#inherited-from-1}

[`TableState_ColumnFiltering`](TableState_ColumnFiltering.md).[`columnFilters`](TableState_ColumnFiltering.md#columnfilters)

***

### columnOrder? {#columnorder}

```ts
optional columnOrder?: ColumnOrderState;
```

定義元: [features/column-ordering/columnOrderingFeature.types.ts:28](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L28)

#### 継承元のメンバー {#inherited-from-2}

[`TableState_ColumnOrdering`](TableState_ColumnOrdering.md).[`columnOrder`](TableState_ColumnOrdering.md#columnorder)

***

### columnPinning? {#columnpinning}

```ts
optional columnPinning?: ColumnPinningState;
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:23](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L23)

#### 継承元のメンバー {#inherited-from-3}

[`TableState_ColumnPinning`](TableState_ColumnPinning.md).[`columnPinning`](TableState_ColumnPinning.md#columnpinning)

***

### columnResizing? {#columnresizing}

```ts
optional columnResizing?: columnResizingState;
```

定義元: [features/column-resizing/columnResizingFeature.types.ts:4](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.types.ts#L4)

#### 継承元のメンバー {#inherited-from-4}

[`TableState_ColumnResizing`](TableState_ColumnResizing.md).[`columnResizing`](TableState_ColumnResizing.md#columnresizing)

***

### columnSizing? {#columnsizing}

```ts
optional columnSizing?: ColumnSizingState;
```

定義元: [features/column-sizing/columnSizingFeature.types.ts:5](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.types.ts#L5)

#### 継承元のメンバー {#inherited-from-5}

[`TableState_ColumnSizing`](TableState_ColumnSizing.md).[`columnSizing`](TableState_ColumnSizing.md#columnsizing)

***

### columnVisibility? {#columnvisibility}

```ts
optional columnVisibility?: ColumnVisibilityState;
```

定義元: [features/column-visibility/columnVisibilityFeature.types.ts:9](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-visibility/columnVisibilityFeature.types.ts#L9)

#### 継承元のメンバー {#inherited-from-6}

[`TableState_ColumnVisibility`](TableState_ColumnVisibility.md).[`columnVisibility`](TableState_ColumnVisibility.md#columnvisibility)

***

### expanded? {#expanded}

```ts
optional expanded?: ExpandedState;
```

定義元: [features/row-expanding/rowExpandingFeature.types.ts:10](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.types.ts#L10)

#### 継承元のメンバー {#inherited-from-7}

[`TableState_RowExpanding`](TableState_RowExpanding.md).[`expanded`](TableState_RowExpanding.md#expanded)

***

### globalFilter? {#globalfilter}

```ts
optional globalFilter?: any;
```

定義元: [features/global-filtering/globalFilteringFeature.types.ts:15](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/global-filtering/globalFilteringFeature.types.ts#L15)

#### 継承元のメンバー {#inherited-from-8}

[`TableState_GlobalFiltering`](TableState_GlobalFiltering.md).[`globalFilter`](TableState_GlobalFiltering.md#globalfilter)

***

### grouping? {#grouping}

```ts
optional grouping?: GroupingState;
```

定義元: [features/column-grouping/columnGroupingFeature.types.ts:10](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-grouping/columnGroupingFeature.types.ts#L10)

#### 継承元のメンバー {#inherited-from-9}

[`TableState_ColumnGrouping`](TableState_ColumnGrouping.md).[`grouping`](TableState_ColumnGrouping.md#grouping)

***

### pagination? {#pagination}

```ts
optional pagination?: PaginationState;
```

定義元: [features/row-pagination/rowPaginationFeature.types.ts:15](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.types.ts#L15)

#### 継承元のメンバー {#inherited-from-10}

[`TableState_RowPagination`](TableState_RowPagination.md).[`pagination`](TableState_RowPagination.md#pagination)

***

### rowPinning? {#rowpinning}

```ts
optional rowPinning?: RowPinningState;
```

定義元: [features/row-pinning/rowPinningFeature.types.ts:13](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.types.ts#L13)

#### 継承元のメンバー {#inherited-from-11}

[`TableState_RowPinning`](TableState_RowPinning.md).[`rowPinning`](TableState_RowPinning.md#rowpinning)

***

### rowSelection? {#rowselection}

```ts
optional rowSelection?: RowSelectionState;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:31](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L31)

#### 継承元のメンバー {#inherited-from-12}

[`TableState_RowSelection`](TableState_RowSelection.md).[`rowSelection`](TableState_RowSelection.md#rowselection)

***

### sorting? {#sorting}

```ts
optional sorting?: SortingState;
```

定義元: [features/row-sorting/rowSortingFeature.types.ts:22](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.types.ts#L22)

#### 継承元のメンバー {#inherited-from-13}

[`TableState_RowSorting`](TableState_RowSorting.md).[`sorting`](TableState_RowSorting.md#sorting)
