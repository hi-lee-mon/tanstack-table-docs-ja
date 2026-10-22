---
id: Subscribe
title: Subscribe
---

## 呼び出しシグネチャ {#call-signature}

```ts
function Subscribe<TSourceValue>(props): ReactNode | Promise<ReactNode>;
```

定義元: [src/Subscribe.ts:122](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L122)

テーブルの状態を購読できる React コンポーネントです。

テーブルの状態のうち特定の部分だけを対象に、状態変化による再レンダーをオプトインしたいときに便利です。

`useTable` から得られる `table.Subscribe` を使える場合は、そちらを優先してください。`table.Subscribe` はオーバーロードを使っているため、JSX の文脈的型付けが効きます。このスタンドアロンのコンポーネントは、`props` に共用体型を使っています。

### 型パラメーター {#type-parameters}

#### TSourceValue {#tsourcevalue}

`TSourceValue`

### パラメーター {#parameters}

#### props {#props}

[`SubscribePropsWithSourceIdentity`](../type-aliases/SubscribePropsWithSourceIdentity.md)\<`TSourceValue`\>

### 戻り値 {#returns}

`ReactNode` \| `Promise`\<`ReactNode`\>

### 例 {#examples}

```tsx
// As a standalone component — full store
<Subscribe source={table.store} selector={(state) => ({ rowSelection: state.rowSelection })}>
  {({ rowSelection }) => (
    <div>Selected rows: {Object.keys(rowSelection).length}</div>
  )}
</Subscribe>
```

```tsx
// Entire source (atom or store) — no selector
<Subscribe source={table.atoms.rowSelection}>
  {(rowSelection) => <div>...</div>}
</Subscribe>
```

```tsx
// Project source value (e.g. one row’s selection)
<Subscribe
  source={table.atoms.rowSelection}
  selector={(rowSelection) => rowSelection?.[row.id]}
>
  {(selected) => <tr data-selected={!!selected}>...</tr>}
</Subscribe>
```

```tsx
// As table.Subscribe (table instance method)
<table.Subscribe selector={(state) => ({ rowSelection: state.rowSelection })}>
  {({ rowSelection }) => (
    <div>Selected rows: {Object.keys(rowSelection).length}</div>
  )}
</table.Subscribe>
```

## 呼び出しシグネチャ {#call-signature-1}

```ts
function Subscribe<TSourceValue, TSelected>(props): ReactNode | Promise<ReactNode>;
```

定義元: [src/Subscribe.ts:125](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L125)

テーブルの状態を購読できる React コンポーネントです。

テーブルの状態のうち特定の部分だけを対象に、状態変化による再レンダーをオプトインしたいときに便利です。

`useTable` から得られる `table.Subscribe` を使える場合は、そちらを優先してください。`table.Subscribe` はオーバーロードを使っているため、JSX の文脈的型付けが効きます。このスタンドアロンのコンポーネントは、`props` に共用体型を使っています。

### 型パラメーター {#type-parameters-1}

#### TSourceValue {#tsourcevalue-1}

`TSourceValue`

#### TSelected {#tselected}

`TSelected`

### パラメーター {#parameters-1}

#### props {#props-1}

[`SubscribePropsWithSourceWithSelector`](../type-aliases/SubscribePropsWithSourceWithSelector.md)\<`TSourceValue`, `TSelected`\>

### 戻り値 {#returns-1}

`ReactNode` \| `Promise`\<`ReactNode`\>

### 例 {#examples-1}

```tsx
// As a standalone component — full store
<Subscribe source={table.store} selector={(state) => ({ rowSelection: state.rowSelection })}>
  {({ rowSelection }) => (
    <div>Selected rows: {Object.keys(rowSelection).length}</div>
  )}
</Subscribe>
```

```tsx
// Entire source (atom or store) — no selector
<Subscribe source={table.atoms.rowSelection}>
  {(rowSelection) => <div>...</div>}
</Subscribe>
```

```tsx
// Project source value (e.g. one row’s selection)
<Subscribe
  source={table.atoms.rowSelection}
  selector={(rowSelection) => rowSelection?.[row.id]}
>
  {(selected) => <tr data-selected={!!selected}>...</tr>}
</Subscribe>
```

```tsx
// As table.Subscribe (table instance method)
<table.Subscribe selector={(state) => ({ rowSelection: state.rowSelection })}>
  {({ rowSelection }) => (
    <div>Selected rows: {Object.keys(rowSelection).length}</div>
  )}
</table.Subscribe>
```

## 呼び出しシグネチャ {#call-signature-2}

```ts
function Subscribe<TFeatures, TSelected>(props): ReactNode | Promise<ReactNode>;
```

定義元: [src/Subscribe.ts:128](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L128)

テーブルの状態を購読できる React コンポーネントです。

テーブルの状態のうち特定の部分だけを対象に、状態変化による再レンダーをオプトインしたいときに便利です。

`useTable` から得られる `table.Subscribe` を使える場合は、そちらを優先してください。`table.Subscribe` はオーバーロードを使っているため、JSX の文脈的型付けが効きます。このスタンドアロンのコンポーネントは、`props` に共用体型を使っています。

### 型パラメーター {#type-parameters-2}

#### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

#### TSelected {#tselected-1}

`TSelected`

### パラメーター {#parameters-2}

#### props {#props-2}

[`SubscribePropsWithStore`](../type-aliases/SubscribePropsWithStore.md)\<`TFeatures`, `TSelected`\>

### 戻り値 {#returns-2}

`ReactNode` \| `Promise`\<`ReactNode`\>

### 例 {#examples-2}

```tsx
// As a standalone component — full store
<Subscribe source={table.store} selector={(state) => ({ rowSelection: state.rowSelection })}>
  {({ rowSelection }) => (
    <div>Selected rows: {Object.keys(rowSelection).length}</div>
  )}
</Subscribe>
```

```tsx
// Entire source (atom or store) — no selector
<Subscribe source={table.atoms.rowSelection}>
  {(rowSelection) => <div>...</div>}
</Subscribe>
```

```tsx
// Project source value (e.g. one row’s selection)
<Subscribe
  source={table.atoms.rowSelection}
  selector={(rowSelection) => rowSelection?.[row.id]}
>
  {(selected) => <tr data-selected={!!selected}>...</tr>}
</Subscribe>
```

```tsx
// As table.Subscribe (table instance method)
<table.Subscribe selector={(state) => ({ rowSelection: state.rowSelection })}>
  {({ rowSelection }) => (
    <div>Selected rows: {Object.keys(rowSelection).length}</div>
  )}
</table.Subscribe>
```
