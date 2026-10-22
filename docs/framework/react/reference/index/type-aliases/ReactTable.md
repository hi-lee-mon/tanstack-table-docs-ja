---
id: ReactTable
title: ReactTable
---

```ts
type ReactTable<TFeatures, TData, TSelected> = Omit<Table<TFeatures, TData>, "store"> & object;
```

定義元: [src/useTable.ts:29](https://github.com/TanStack/table/blob/main/packages/react-table/src/useTable.ts#L29)

## 型宣言 {#type-declaration}

### FlexRender {#flexrender}

```ts
FlexRender: <TValue>(props) => ReactNode;
```

ヘッダー、セル、フッターを独自のマークアップで描画する React コンポーネントです。
flexRender を手動で呼び出す代わりに、このユーティリティコンポーネントを使ってください。

#### 型パラメーター {#type-parameters}

##### TValue {#tvalue}

`TValue` *extends* `CellData` = `CellData`

#### パラメーター {#parameters}

##### props {#props}

[`FlexRenderProps`](FlexRenderProps.md)\<`TFeatures`, `TData`, `TValue`\>

#### 戻り値 {#returns}

`ReactNode`

#### 例 {#example}

```tsx
<table.FlexRender cell={cell} />
<table.FlexRender header={header} />
<table.FlexRender footer={footer} />
```

これは、次のように `flexRender` を直接呼び出す書き方に代わるものです。
```tsx
flexRender(cell.column.columnDef.cell, cell.getContext())
flexRender(header.column.columnDef.header, header.getContext())
flexRender(footer.column.columnDef.footer, footer.getContext())
```

### state {#state}

```ts
readonly state: Readonly<TSelected>;
```

テーブルの状態のうち、選択された部分です。この状態は、`useTable` の第 2 引数に渡した
セレクター関数で選択されたものなので、テーブルの状態全体と
構造が一致しないことがあります。

#### 例 {#example-1}

```ts
const table = useTable(options, (state) => ({ globalFilter: state.globalFilter })) // only globalFilter is part of the selected state

console.log(table.state.globalFilter)
```

### ~~store~~ {#store}

```ts
readonly store: Table<TFeatures, TData>["store"];
```

#### 非推奨 {#deprecated}

レンダー中の読み取りには `table.state` を、
スライスのスナップショットには `table.atoms.<slice>.get()` を、
明示的な購読には `table.Subscribe` / `useSelector(table.store, selector)` を使ってください。
`table.store.state` は現在の値のスナップショットなので、
レンダーのコードで誤用しやすいです。

### Subscribe {#subscribe}

```ts
Subscribe: {
<TSourceValue>  (props): ReactNode | Promise<ReactNode>;
<TSourceValue, TSubSelected>  (props): ReactNode | Promise<ReactNode>;
<TSubSelected>  (props): ReactNode | Promise<ReactNode>;
};
```

（1 つのユニオン型ではなく）オーバーロードにしているのは、JSX の中で `selector` のコールバックに
正しい文脈上の型を付けるためです。2 つの `selector` シグネチャのユニオン型にすると、暗黙の `any` に退化してしまいます。

`selector` **なし**で source を指定する場合を別のオーバーロードにしているのは、children が `TSourceValue` を
（恒等射影として）受け取れるようにするためです。1 つのオーバーロードで `selector` を省略可能にすると、`TSubSelected` は
source から推論されず、デフォルトの `unknown` になってしまいます。

`TSourceValue` が `source` から推論されるように、**source** を取るオーバーロードを先に並べています。

#### 呼び出しシグネチャ {#call-signature}

```ts
<TSourceValue>(props): ReactNode | Promise<ReactNode>;
```

##### 型パラメーター {#type-parameters-1}

###### TSourceValue {#tsourcevalue}

`TSourceValue`

##### パラメーター {#parameters-1}

###### props {#props-1}

###### children {#children}

((`state`) => `ReactNode`) \| `ReactNode`

###### selector? {#selector}

`undefined`

###### source {#source}

[`SubscribeSource`](SubscribeSource.md)\<`TSourceValue`\>

##### 戻り値 {#returns-1}

`ReactNode` \| `Promise`\<`ReactNode`\>

#### 呼び出しシグネチャ {#call-signature-1}

```ts
<TSourceValue, TSubSelected>(props): ReactNode | Promise<ReactNode>;
```

##### 型パラメーター {#type-parameters-2}

###### TSourceValue {#tsourcevalue-1}

`TSourceValue`

###### TSubSelected {#tsubselected}

`TSubSelected`

##### パラメーター {#parameters-2}

###### props {#props-2}

###### children {#children-1}

((`state`) => `ReactNode`) \| `ReactNode`

###### selector {#selector-1}

(`state`) => `TSubSelected`

###### source {#source-1}

[`SubscribeSource`](SubscribeSource.md)\<`TSourceValue`\>

##### 戻り値 {#returns-2}

`ReactNode` \| `Promise`\<`ReactNode`\>

#### 呼び出しシグネチャ {#call-signature-2}

```ts
<TSubSelected>(props): ReactNode | Promise<ReactNode>;
```

##### 型パラメーター {#type-parameters-3}

###### TSubSelected {#tsubselected-1}

`TSubSelected`

##### パラメーター {#parameters-3}

###### props {#props-3}

`Omit`\<[`SubscribePropsWithStore`](SubscribePropsWithStore.md)\<`TFeatures`, `TSubSelected`\>, `"source"`\>

##### 戻り値 {#returns-3}

`ReactNode` \| `Promise`\<`ReactNode`\>

## 型パラメーター {#type-parameters-4}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TSelected {#tselected}

`TSelected` = `TableState`\<`TFeatures`\>
