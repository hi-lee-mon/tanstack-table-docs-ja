---
title: Devtools
id: devtools
---

TanStack Table provides framework-specific devtools adapters that plug into the [TanStack Devtools](https://tanstack.com/devtools) multi-panel UI.

The table devtools let you inspect registered table instances, switch between multiple tables, and inspect features, state, options, rows, and columns in real time.

> [!NOTE]
> By default, the framework adapters only include the live devtools in development mode. In production builds they export no-op implementations unless you opt into the `/production` entrypoints.

## Installation {#installation}

Install the TanStack Devtools host package and the Table adapter for your framework.

```sh
npm install @tanstack/react-devtools @tanstack/react-table-devtools
```


Octane, Lit, Svelte, Alpine, and vanilla do not currently ship dedicated table devtools adapters.

## The Required `key` Table Option {#the-required-key-table-option}

The devtools identify each table by the `key` table option. Registration requires it. If you register a table without a `key`, the devtools log an error (`Missing table key. Add a 'key' option to your table to use devtools.`) and skip the table entirely.

```ts
const table = useTable({
  key: 'users-table', // needed for devtools, omit if you don't want to use the devtools
  features,
  columns,
  data,
})
```

The `key` is also the label shown in the devtools panel selector, so give each table a unique, descriptive key.

## Setup Pattern {#setup-pattern}

The recommended setup has three parts:

1. Give each table a unique `key` option
2. Mount `TanStackDevtools` at the app root with `tableDevtoolsPlugin()`
3. Register each table with `useTanStackTableDevtools(table)` (or `injectTanStackTableDevtools` in Angular) immediately after creating it

If you register multiple tables, the Table panel shows a selector so you can switch between them.

## Setup {#setup}

```tsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import { useTable } from '@tanstack/react-table'
import { TanStackDevtools } from '@tanstack/react-devtools'
import {
  tableDevtoolsPlugin,
  useTanStackTableDevtools,
} from '@tanstack/react-table-devtools'

function App() {
  const table = useTable({
    key: 'users-table', // needed for devtools
    // ...
  })

  useTanStackTableDevtools(table)

  return <AppContent table={table} />
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
    <TanStackDevtools plugins={[tableDevtoolsPlugin()]} />
  </React.StrictMode>,
)
```

See the [React row-selection example](https://tanstack.com/table/latest/docs/framework/react/examples/row-selection).


## Disabling Registration {#disabling-registration}

Each registration function accepts an `enabled` option if you want to conditionally register a table:

```ts
useTanStackTableDevtools(table, { enabled: false })
```


## Production Builds {#production-builds}

If you need the live devtools in production, import from the `/production` entrypoint for your framework package:

```tsx
import {
  tableDevtoolsPlugin,
  useTanStackTableDevtools,
} from '@tanstack/react-table-devtools/production'
```

