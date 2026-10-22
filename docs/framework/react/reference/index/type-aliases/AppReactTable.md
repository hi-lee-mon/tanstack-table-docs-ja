---
id: AppReactTable
title: AppReactTable
---

```ts
type AppReactTable<TFeatures, TData, TSelected, TTableComponents, TCellComponents, THeaderComponents> = ReactTable<TFeatures, TData, TSelected> & NoInfer<TTableComponents> & object;
```

定義元: [src/createTableHook.tsx:532](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L532)

useAppTable が返す、App ラッパーコンポーネントをすべて備えた拡張テーブル API です。

## 型宣言 {#type-declaration}

### AppCell {#appcell}

```ts
AppCell: AppCellComponent<TFeatures, TData, NoInfer<TCellComponents>>;
```

セルをラップし、cellComponents をあらかじめ結び付けたセルのコンテキストを提供します。
Subscribe の機能を使うための selector を任意で受け取れます。

#### 例 {#example}

```tsx
// Without selector
<table.AppCell cell={cell}>
  {(c) => <td><c.TextCell /></td>}
</table.AppCell>

// With selector - children receives cell and selected state
<table.AppCell cell={cell} selector={(s) => s.columnFilters}>
  {(c, filters) => <td>{filters.length}</td>}
</table.AppCell>
```

### AppFooter {#appfooter}

```ts
AppFooter: AppHeaderComponent<TFeatures, TData, NoInfer<THeaderComponents>>;
```

フッターをラップし、headerComponents をあらかじめ結び付けたヘッダーのコンテキストを提供します。
Subscribe の機能を使うための selector を任意で受け取れます。

#### 例 {#example-1}

```tsx
<table.AppFooter header={footer}>
  {(f) => <td><table.FlexRender footer={footer} /></td>}
</table.AppFooter>
```

### AppHeader {#appheader}

```ts
AppHeader: AppHeaderComponent<TFeatures, TData, NoInfer<THeaderComponents>>;
```

ヘッダーをラップし、headerComponents をあらかじめ結び付けたヘッダーのコンテキストを提供します。
Subscribe の機能を使うための selector を任意で受け取れます。

#### 例 {#example-2}

```tsx
// Without selector
<table.AppHeader header={header}>
  {(h) => <th><h.SortIndicator /></th>}
</table.AppHeader>

// With selector
<table.AppHeader header={header} selector={(s) => s.sorting}>
  {(h, sorting) => <th>{sorting.length} sorted</th>}
</table.AppHeader>
```

### AppTable {#apptable}

```ts
AppTable: AppTableComponent<TFeatures>;
```

テーブルのコンテキストを提供するルートのラッパーコンポーネントです。Subscribe を任意で使えます。

#### 例 {#example-3}

```tsx
// Without selector - children is ReactNode
<table.AppTable>
  <table>...</table>
</table.AppTable>

// With selector - children receives selected state
<table.AppTable selector={(s) => s.pagination}>
  {(pagination) => <div>Page {pagination.pageIndex}</div>}
</table.AppTable>
```

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TData {#tdata}

`TData` *extends* `RowData`

### TSelected {#tselected}

`TSelected`

### TTableComponents {#ttablecomponents}

`TTableComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

### TCellComponents {#tcellcomponents}

`TCellComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

### THeaderComponents {#theadercomponents}

`THeaderComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>
