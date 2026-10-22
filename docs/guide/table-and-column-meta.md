---
title: Table and Column Meta Guide
---

Sometimes you need to attach your own arbitrary data or functions to a table or its columns so that they are available anywhere the `table` or `column` instances are available. That is what the `meta` options are for. TanStack Table never reads or writes `meta` itself; it is purely a place for you to pass your own context through the table.

There are two kinds of meta:

- **Table meta** - The `meta` table option. Pass any object and read it back anywhere via `table.options.meta`. A classic use case is passing an `updateData` function down to editable cells.
- **Column meta** - The `meta` property on a column definition. Read it back anywhere a column is available via `column.columnDef.meta`. A classic use case is declaring which filter UI variant a column's header should render.

## Table Meta {#table-meta}

```ts
const table = useTable({
  features,
  columns,
  data,
  meta: {
    updateData: (rowIndex, columnId, value) => {
      // ...
    },
  },
})

// ...later, anywhere the table is available (e.g. inside a cell component)
table.options.meta?.updateData(rowIndex, columnId, newValue)
```


Column meta is set on the column definition and is identical across every adapter:

```ts
const columns = columnHelper.columns([
  columnHelper.accessor('age', {
    header: 'Age',
    meta: {
      filterVariant: 'range',
    },
  }),
])

// ...later, anywhere a column is available (e.g. inside a header component)
const variant = column.columnDef.meta?.filterVariant
```

## Typing Meta Per-Table (Recommended) {#typing-meta-per-table-recommended}

By default, both meta types are empty objects, so to get type safety you declare their shapes yourself. New in v9, you can declare meta types **per feature set** with the type-only `tableMeta` and `columnMeta` slots in your `tableFeatures()` call, using the `metaHelper` utility.

First, define the shapes you want (this is the same in every framework):

```ts
interface MyTableMeta {
  updateData: (rowIndex: number, columnId: string, value: unknown) => void
}

interface MyColumnMeta {
  filterVariant?: 'text' | 'range' | 'select'
}
```

Then declare them on your `features` object:

```ts
import {
  metaHelper,
  rowSortingFeature,
  tableFeatures,
} from '@tanstack/react-table'

const features = tableFeatures({
  rowSortingFeature,
  tableMeta: metaHelper<MyTableMeta>(),
  columnMeta: metaHelper<MyColumnMeta>(),
})
```


That's it. Everywhere this `features` object flows (`useTable`, `createColumnHelper`, `ColumnDef`, `Column`, and so on), the meta types are inferred from `typeof features` with no extra generics to pass around:

```ts
const columnHelper = createColumnHelper<typeof features, Person>()

columnHelper.accessor('age', {
  meta: {
    filterVariant: 'range', // ✅ type-checked against MyColumnMeta
  },
})

// And both meta surfaces are fully typed wherever you read them:
table.options.meta?.updateData // ✅ (rowIndex, columnId, value) => void
column.columnDef.meta?.filterVariant // ✅ 'text' | 'range' | 'select' | undefined
```

Unlike the v8-style declaration merging described below, this scoping is **per-table, not global**: only tables created with this `features` object get these meta types. Different tables in your app can declare entirely different meta shapes by using different `features` objects.

### How the Type-Only Slots Work {#how-the-type-only-slots-work}

The `tableMeta` and `columnMeta` keys are _phantom_ entries. Only their TypeScript types matter. At runtime, the value is an empty object that gets stripped from the table's registered features, so it is never treated as a real feature. The actual meta _values_ are still passed where they always were: the `meta` table option and the `meta` property on column definitions.

`metaHelper<MyMeta>()` simply returns `{}` cast to your meta type. You can write the cast yourself instead:

```ts
const features = tableFeatures({
  rowSortingFeature,
  tableMeta: {} as MyTableMeta,
  columnMeta: {} as MyColumnMeta,
})
```

Both forms are equivalent. Prefer `metaHelper`. It reads as type-only at a glance, and it avoids false positives from the `@typescript-eslint/no-unnecessary-type-assertion` lint rule, which flags the `{} as` form when your meta type has only optional properties (and whose auto-fix would silently erase your meta type).

## Filter Meta (`filterMeta` Slot) {#filter-meta-filtermeta-slot}

The `filterMeta` slot lets you declare the shape of arbitrary metadata that a custom filter function attaches to a row during filtering. This is most useful for filter functions that produce a by-product (such as a ranking score) that you want to read in a column's sort function or cell renderer.

The pattern mirrors `tableMeta` and `columnMeta`: declare your meta interface, register it with `metaHelper`, and then intersect `TableFeatures` with your meta type when annotating your filter and sort functions.

```ts
import {
  metaHelper,
  tableFeatures,
  columnFilteringFeature,
  globalFilteringFeature,
  rowSortingFeature,
  rowPaginationFeature,
  createFilteredRowModel,
  createSortedRowModel,
  createPaginatedRowModel,
  sortFn_alphanumeric,
} from '@tanstack/react-table'
import type {
  FilterFn,
  SortFn,
  RowData,
  TableFeatures,
} from '@tanstack/react-table'
import { rankItem, type RankingInfo } from '@tanstack/match-sorter-utils'

// 1. Define the metadata shape your filter function will attach
interface FuzzyFilterMeta {
  itemRank?: RankingInfo
}

// 2. Intersect with TableFeatures to get a fully typed features surface
type FuzzyFeatures = TableFeatures & { filterMeta: FuzzyFilterMeta }

// 3. Annotate your filter and sort functions against the extended features type
const fuzzyFilter: FilterFn<FuzzyFeatures, RowData> = (
  row,
  columnId,
  value,
  addMeta,
) => {
  const itemRank = rankItem(row.getValue(columnId), value)
  addMeta({ itemRank })
  return itemRank.passed
}

const fuzzySort: SortFn<FuzzyFeatures, Person> = (rowA, rowB, columnId) => {
  let dir = 0
  if (rowA.columnFiltersMeta[columnId]) {
    dir = compareItems(
      rowA.columnFiltersMeta[columnId]?.itemRank!,
      rowB.columnFiltersMeta[columnId]?.itemRank!,
    )
  }
  return dir === 0 ? sortFn_alphanumeric(rowA, rowB, columnId) : dir
}

// 4. Register everything on tableFeatures(), including the filterMeta slot
const features = tableFeatures({
  columnFilteringFeature,
  globalFilteringFeature,
  rowSortingFeature,
  rowPaginationFeature,
  filteredRowModel: createFilteredRowModel(),
  sortedRowModel: createSortedRowModel(),
  paginatedRowModel: createPaginatedRowModel(),
  filterFns: { fuzzy: fuzzyFilter },
  sortFns: { fuzzy: fuzzySort },
  filterMeta: metaHelper<FuzzyFilterMeta>(),
})
```

> [!NOTE]
> the `filterFns` and `sortFns` slots above register only the functions this table uses. The full built-in registries (`filterFns`, `sortFns`, `aggregationFns` exported from the package) can still be spread into these slots, but they are deprecated because they put every built-in function in your bundle. Import individual functions such as `sortFn_alphanumeric` instead, or pass functions directly in your column definitions.

Now `columnFiltersMeta` on every row is typed as `FuzzyFilterMeta` for tables built from this `features` object. The `filterMeta` slot is, like `tableMeta` and `columnMeta`, a phantom type-only entry. `metaHelper<FuzzyFilterMeta>()` returns `{}` at runtime and is stripped from the registered features.

See the [React filters-fuzzy example](https://tanstack.com/table/latest/docs/framework/react/examples/filters-fuzzy) for a complete, runnable implementation.

## Typing Meta Globally with Declaration Merging (v8 Style) {#typing-meta-globally-with-declaration-merging-v8-style}

The v8 approach of extending the `TableMeta` and `ColumnMeta` interfaces with module augmentation still works in v9. The only change from v8 is the generics shape: `TFeatures` is now the first type parameter on both interfaces.

```ts
import type { CellData, RowData, TableFeatures } from '@tanstack/react-table'

declare module '@tanstack/react-table' {
  interface TableMeta<TFeatures extends TableFeatures, TData extends RowData> {
    updateData: (rowIndex: number, columnId: string, value: unknown) => void
  }

  interface ColumnMeta<
    TFeatures extends TableFeatures,
    TData extends RowData,
    TValue extends CellData = CellData,
  > {
    filterVariant?: 'text' | 'range' | 'select'
  }
}
```


The trade-off with declaration merging is that it is **global**. Every table in your entire project gets the same meta types, whether or not a given table actually provides that meta. If you have many tables with different needs, the per-table slots above are a better fit.

The two approaches resolve with a simple precedence: if a `features` object declares a `tableMeta` or `columnMeta` slot, that slot's type is used for tables created with those features, _replacing_ (not merging with) the globally declared interface. Tables whose features declare no slot fall back to the declaration-merged interfaces.

## When to Use Custom Features Instead {#when-to-use-custom-features-instead}

Meta is intentionally simple: a typed bag of values you carry through the table. If you find yourself wanting real table _options_ with defaults, new _state_, or new _APIs_ on the table instance (e.g. `table.toggleDensity()`), consider writing a [custom feature](../framework/react/guide/custom-features) instead. Custom features plug into the same `features` option, get the same `typeof features` type inference, and can declare their own options, state, and instance methods. Meta was never designed to do any of that.
