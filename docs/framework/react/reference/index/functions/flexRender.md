---
id: flexRender
title: flexRender
---

```ts
function flexRender<TProps>(Comp, props): ReactNode | Element;
```

定義元: [src/FlexRender.tsx:45](https://github.com/TanStack/table/blob/main/packages/react-table/src/FlexRender.tsx#L45)

ヘッダー・セル・フッターを独自のマークアップでレンダーする場合は、`cell.getValue()` や `cell.renderValue()` ではなく flexRender を使ってください。

## 型パラメーター {#type-parameters}

### TProps {#tprops}

`TProps` *extends* `object`

## パラメーター {#parameters}

### Comp {#comp}

[`Renderable`](../type-aliases/Renderable.md)\<`TProps`\>

### props {#props}

`TProps`

## 戻り値 {#returns}

`ReactNode` \| `Element`

## 例 {#example}

```ts
flexRender(cell.column.columnDef.cell, cell.getContext())
```
