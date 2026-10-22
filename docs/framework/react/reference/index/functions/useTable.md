---
id: useTable
title: useTable
---

```ts
function useTable<TFeatures, TData, TSelected>(tableOptions, selector?): ReactTable<TFeatures, TData, TSelected>;
```

定義元: [src/useTable.ts:149](https://github.com/TanStack/table/blob/main/packages/react-table/src/useTable.ts#L149)

TanStack Store のアトムを土台にした React のテーブルインスタンスを作成します。

省略可能な selector は `table.store` から値を取り出します。選び出した値は
`table.state` で公開され、React の再レンダーを判断するために浅い比較が行われます。
selector を省略すると、登録済みのテーブルの状態のスライスをすべて購読します。
対象を絞った購読にしたい場合は、より狭い selector を渡し、ツリーの下位で
`table.Subscribe` を使ってください。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TSelected {#tselected}

`TSelected` = `TableState`\<`TFeatures`\>

## パラメーター {#parameters}

### tableOptions {#tableoptions}

`TableOptions`\<`TFeatures`, `TData`\>

### selector? {#selector}

(`state`) => `TSelected`

## 戻り値 {#returns}

[`ReactTable`](../type-aliases/ReactTable.md)\<`TFeatures`, `TData`, `TSelected`\>

## 例 {#example}

```tsx
const table = useTable(
  {
    features,
    columns,
    data,
  },
  (state) => ({ pagination: state.pagination }),
)

table.state.pagination
```
