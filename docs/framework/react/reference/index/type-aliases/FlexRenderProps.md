---
id: FlexRenderProps
title: FlexRenderProps
---

```ts
type FlexRenderProps<TFeatures, TData, TValue> =
  | {
  cell: Cell<TFeatures, TData, TValue>;
  footer?: never;
  header?: never;
}
  | {
  cell?: never;
  footer?: never;
  header: Header<TFeatures, TData, TValue>;
}
  | {
  cell?: never;
  footer: Header<TFeatures, TData, TValue>;
  header?: never;
};
```

定義元: [src/FlexRender.tsx:63](https://github.com/TanStack/table/blob/main/packages/react-table/src/FlexRender.tsx#L63)

`flexRender` を簡単に使えるようにしたコンポーネントのラッパーです。このユーティリティコンポーネントを使うと、ヘッダー、セル、フッターを独自のマークアップで描画できます。
渡せる props は 1 つ（`cell`、`header`、`footer` のいずれか）だけです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TValue {#tvalue}

`TValue` *extends* `CellData` = `CellData`

## 例 {#examples}

```ts
<FlexRender cell={cell} />
```

```ts
<FlexRender header={header} />
```

```ts
<FlexRender footer={footer} />
```
