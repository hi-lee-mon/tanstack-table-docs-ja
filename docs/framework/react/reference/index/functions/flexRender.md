---
id: flexRender
title: flexRender
---

```ts
function flexRender<TProps>(Comp, props): ReactNode | Element;
```

Defined in: [src/FlexRender.tsx:45](https://github.com/TanStack/table/blob/main/packages/react-table/src/FlexRender.tsx#L45)

If rendering headers, cells, or footers with custom markup, use flexRender instead of `cell.getValue()` or `cell.renderValue()`.

## Type Parameters {#type-parameters}

### TProps {#tprops}

`TProps` *extends* `object`

## Parameters {#parameters}

### Comp {#comp}

[`Renderable`](../type-aliases/Renderable.md)\<`TProps`\>

### props {#props}

`TProps`

## Returns {#returns}

`ReactNode` \| `Element`

## Example {#example}

```ts
flexRender(cell.column.columnDef.cell, cell.getContext())
```
