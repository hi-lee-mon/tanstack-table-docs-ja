---
title: Installation
---

Before we dig in to the API, let's get you set up!

Install your table adapter as a dependency using your preferred package manager:

::: code-group

```sh [npm]
npm install @tanstack/react-table
```

```sh [pnpm]
pnpm add @tanstack/react-table
```

```sh [yarn]
yarn add @tanstack/react-table
```

```sh [bun]
bun add @tanstack/react-table
```

:::


The `@tanstack/react-table` package works with React 18 or newer.


Don't see your favorite framework (or favorite version of your framework) listed? You can always just use the `@tanstack/table-core` package and build your own adapter in your own codebase. Usually, only a thin wrapper is needed to manage state and rendering for your specific framework. Browse the [source code](https://github.com/TanStack/table/tree/main/packages) of all of the other adapters to see how they work.
