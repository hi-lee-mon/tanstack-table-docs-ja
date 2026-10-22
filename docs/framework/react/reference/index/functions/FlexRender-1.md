---
id: FlexRender
title: FlexRender
---

```ts
function FlexRender<TFeatures, TData, TValue>(props):
  | string
  | number
  | bigint
  | boolean
  | Iterable<ReactNode, any, any>
  | Promise<AwaitedReactNode>
  | Element
  | null
  | undefined;
```

定義元: [src/FlexRender.tsx:97](https://github.com/TanStack/table/blob/main/packages/react-table/src/FlexRender.tsx#L97)

`flexRender` を簡単に使えるようにしたコンポーネントのラッパーです。ヘッダー・セル・フッターを独自のマークアップで描画するときに、このユーティリティコンポーネントを使います。
渡せる props は1つ（`cell`、`header`、`footer` のいずれか）だけです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### props {#props}

[`FlexRenderProps`](../type-aliases/FlexRenderProps.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

  \| `string`
  \| `number`
  \| `bigint`
  \| `boolean`
  \| `Iterable`\<`ReactNode`, `any`, `any`\>
  \| `Promise`\<`AwaitedReactNode`\>
  \| `Element`
  \| `null`
  \| `undefined`

## 例 {#example}

```tsx
<FlexRender cell={cell} />
<FlexRender header={header} />
<FlexRender footer={footer} />
```

これは、次のように `flexRender` を直接呼び出す代わりになります。
```tsx
flexRender(cell.column.columnDef.cell, cell.getContext())
flexRender(header.column.columnDef.header, header.getContext())
flexRender(footer.column.columnDef.footer, footer.getContext())
```
