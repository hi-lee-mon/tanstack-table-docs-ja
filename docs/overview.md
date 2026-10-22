---
title: Overview
---

> [!NOTE]
> If you are upgrading from TanStack Table v8, start with the migration guide for your framework:

- [Migrating to v9](./framework/react/guide/migrating)


TanStack Table is the best way to build your own powerful table and datagrid components with _blazingly fast_ performance, but most importantly, with **100% control over your own design and markup.**

In this new age of AI, where markup can be generated in seconds, the old value proposition of pre-built components (saving you the typing) matters less than ever. What matters now is owning and controlling the result, and that is exactly what TanStack Table gives you.

TanStack Table might be a bit of a different table library than you are used to. It is **_NOT_** a pre-built table component, like you might find from a library like [AG Grid](https://ag-grid.com?utm_source=reacttable&utm_campaign=githubreacttable). Instead, TanStack Table is a headless UI library that gives you the power to build your own fully customizable table and datagrid components the right way with whatever JavaScript libraries, component libraries, or design systems you want. TanStack Table is the _engine_ that you can hook up to your own favorite front-end tech, no matter what you're already using or want to use.

At its core, TanStack Table is **agnostic**. Most table data-processing and state logic is written in framework-agnostic TypeScript, and framework adapters connect that core to your favorite frameworks. Official adapters are provided for React, Preact, Octane, Vue, Solid, Svelte, Angular, Ember, Lit, and Alpine, or you can use the core directly in vanilla JavaScript via `@tanstack/table-core`.

It also **does not care which CSS or component library** you use, and is compatible with anything from Tailwind, Bootstrap, Material UI, ShadCN UI, or even your own custom design system.

## What is "Headless" UI? {#what-is-headless-ui}

**Headless UI** is a term for libraries and utilities that provide the logic, state, processing, and APIs for UI elements and interactions, but **do not provide markup, styles, or pre-built implementations**. The hardest parts of building complex UIs usually revolve around state, events, side effects, and data processing. By removing those concerns from the markup and styles, your logic becomes more modular and reusable, while you keep complete control over the look and feel. When you use a headless library like TanStack Table, the complex work of data processing, state management, and business logic is handled for you, so you can focus on the higher-cardinality decisions that differ across designs and use cases.

> Want to dive deeper? [Read more about Headless UI](https://www.merrickchristensen.com/articles/headless-user-interface-components/).

Here's the difference in practice. With a pre-built table component, you pass props in and style the result from the outside, limited to whatever the component's props and theme APIs allow. With TanStack Table, you create a table instance and use its state and APIs to render your own markup:

```diff
- {/* Pass props into a pre-built component and hope you can style it */}
- <PrebuiltDataGrid
-   data={data}
-   columns={columns}
-   theme={messyThemeOverrides}
-   sx={cssOverridesThatHopefullyWork}
-   positionPagination={"however-my-stakeholders-are-feeling-today"}
- />
+ // Build your own markup from the table instance's state and APIs
+ const table = useTable({ features, columns, data })
+
+ return (
+   <table className="anything-you-want">
+     <thead>
+       {/* need to really customize the functionality in your headers? no problem! */}
+       {table.getHeaderGroups().map((headerGroup) => ( ... ))}
+     </thead>
+     <tbody>
+       {/* want to add virtualization here? no problem! */}
+       {table.getRowModel().rows.map((row) => ( ... ))}
+     </tbody>
+   </table>
+ )
```


## Features {#features}

TanStack Table is packed with features, but you only ever bundle the ones you use. The full v9 package is about 25 KB when minified and Brotli-compressed, but more importantly, it is **modular**! You register only the features and row models that your table actually uses, and your bundler can tree-shake away unused optional capabilities. A basic table bundles just the small core. Because features vary in size and share that core, the exact savings depend on which capabilities you register.

We like to think of TanStack Table as more of a "system" for building tables than just a library, as it is one of the most customizable table libraries ever built. TanStack Table has the following built-in features, plus a custom feature (plugin) system for adding your own state and APIs.

- [Cell Selection](./framework/react/guide/cell-selection) - Select spreadsheet-style rectangular ranges of cells
- [Cell Spanning](./framework/react/guide/cell-spanning) - Merge adjacent body cells across rows or columns
- [Column Filtering](./framework/react/guide/column-filtering) - Filter rows based on search values for a column
- [Column Grouping](./framework/react/guide/grouping) - Group rows by one or more column values
- [Column Ordering](./framework/react/guide/column-ordering) - Dynamically change the order of columns
- [Column Pinning](./framework/react/guide/column-pinning) - Pin (Freeze) columns to the left or right of the table
- [Column Resizing](./framework/react/guide/column-resizing) - Let users resize columns with drag handles
- [Column Sizing](./framework/react/guide/column-sizing) - Dynamically change the size of columns
- [Column Visibility](./framework/react/guide/column-visibility) - Hide/show columns
- [Faceting](./framework/react/guide/column-faceting) - List unique values or min/max values for a column or for the entire table
- [Global Filtering](./framework/react/guide/global-filtering) - Filter rows based on search values for the entire table
- [Row Aggregation](./framework/react/guide/aggregation) - Calculate summary values for grouped, root, or custom row sets
- [Row Expanding](./framework/react/guide/expanding) - Expand/collapse rows (sub-rows)
- [Row Pagination](./framework/react/guide/pagination) - Paginate rows
- [Row Pinning](./framework/react/guide/row-pinning) - Pin (Freeze) rows to the top or bottom of the table
- [Row Selection](./framework/react/guide/row-selection) - Select/deselect rows (checkboxes)
- [Row Sorting](./framework/react/guide/sorting) - Sort rows by column values


## Composition {#composition}

Headless doesn't just mean "bring your own styles". Because you own the markup, the event handlers, and (optionally) the state, TanStack Table composes cleanly with whatever else your table needs:

- **Your own state**: Any slice of table state (sorting, filters, pagination, etc.) can be lifted out of the table and managed however you like: in your framework's state, in a global store, or even in the URL.
- **Your own features**: Custom features let you add your own state and APIs directly to the table instance, right alongside the built-in ones. See the Custom Features guide for your framework.
- **Your own logic**: Anything else (fancy interactions, analytics, drag and drop, etc.) is just code you write around the table. There is no black box to fight against.

This also makes it easy to pair TanStack Table with other TanStack libraries:

- [TanStack Virtual](https://tanstack.com/virtual/latest) - Virtualize thousands of rows or columns without changing any table logic (see the Virtualization guide for your framework)
- [TanStack Query](https://tanstack.com/query/latest) - Fetch and cache server-side data for manual pagination, sorting, and filtering
- [TanStack Form](https://tanstack.com/form/latest) - Build editable cells and inline row editing with validation
- [TanStack Pacer](https://tanstack.com/pacer/latest) - Debounce or throttle filter inputs and other rapid-fire interactions
- [TanStack Hotkeys](https://tanstack.com/hotkeys/latest) - Add type-safe keyboard shortcuts for table navigation and actions
- [TanStack Store](https://tanstack.com/store/latest) - Already powers table state under the hood; provide your own atoms to take full control of any state slice

## Get Started {#get-started}

Ready to build something? Head to the Quick Start for your framework, then explore the runnable examples:

- [React Quick Start](./framework/react/quick-start)
- [Kitchen Sink example](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink) - Most of the built-in features working together in one table

Using a component library? These examples pair TanStack Table with popular React component libraries, with both a basic version and an advanced (kitchen sink) version for each:

- ShadCN (Base UI): [Basic Example](https://tanstack.com/table/latest/docs/framework/react/examples/lib-shadcn-base) | [Advanced Example](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink-shadcn-base)
- ShadCN (Radix UI): [Basic Example](https://tanstack.com/table/latest/docs/framework/react/examples/lib-shadcn-radix) | [Advanced Example](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink-shadcn-radix)
- HeroUI: [Basic Example](https://tanstack.com/table/latest/docs/framework/react/examples/lib-hero-ui) | [Advanced Example](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink-hero-ui)
- React Aria: [Basic Example](https://tanstack.com/table/latest/docs/framework/react/examples/lib-react-aria) | [Advanced Example](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink-react-aria)
- Material UI: [Basic Example](https://tanstack.com/table/latest/docs/framework/react/examples/lib-material-ui) | [Advanced Example](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink-material-ui)
- Mantine: [Basic Example](https://tanstack.com/table/latest/docs/framework/react/examples/lib-mantine) | [Advanced Example](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink-mantine)
- Chakra UI: [Basic Example](https://tanstack.com/table/latest/docs/framework/react/examples/lib-chakra-ui) | [Advanced Example](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink-chakra-ui)

