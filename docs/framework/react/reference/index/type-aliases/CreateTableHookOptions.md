---
id: CreateTableHookOptions
title: CreateTableHookOptions
---

```ts
type CreateTableHookOptions<TFeatures, TTableComponents, TCellComponents, THeaderComponents> = Omit<TableOptions<TFeatures, any>, "columns" | "data" | "store" | "state" | "initialState"> & object;
```

定義元: [src/createTableHook.tsx:248](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L248)

コンポーネントとテーブルオプションの既定値をあらかじめ結び付けたテーブルフックを作るためのオプションです。
'columns' | 'data' | 'store' | 'state' | 'initialState' を除く、すべての TableOptions を継承します。

## 型宣言 {#type-declaration}

### cellComponents? {#cellcomponents}

```ts
optional cellComponents?: TCellComponents;
```

セルインスタンスにアクセスする必要があるセル単位のコンポーネントです。
AppCell の children に渡されるセルオブジェクトから使えます。
これらのコンポーネントの中では `useCellContext()` を使ってください。

#### 例 {#example}

```ts
{ TextCell, NumberCell, DateCell, CurrencyCell }
```

### cellContext? {#cellcontext}

```ts
optional cellContext?: Context<Cell<any, any, any>>;
```

セルインスタンス用の独自の React コンテキストです。`cellComponents` の中で使います。

#### 参照 {#see}

CreateTableHookOptions.tableContext

### headerComponents? {#headercomponents}

```ts
optional headerComponents?: THeaderComponents;
```

ヘッダーインスタンスにアクセスする必要があるヘッダー単位のコンポーネントです。
AppHeader/AppFooter の children に渡されるヘッダーオブジェクトから使えます。
これらのコンポーネントの中では `useHeaderContext()` を使ってください。

#### 例 {#example-1}

```ts
{ SortIndicator, ColumnFilter, ResizeHandle }
```

### headerContext? {#headercontext}

```ts
optional headerContext?: Context<Header<any, any, any>>;
```

ヘッダーインスタンス用の独自の React コンテキストです。
`headerComponents`（およびフッターのコンポーネント）の中で使います。

#### 参照 {#see-1}

CreateTableHookOptions.tableContext

### tableComponents? {#tablecomponents}

```ts
optional tableComponents?: TTableComponents;
```

テーブルインスタンスにアクセスする必要があるテーブル単位のコンポーネントです。
useAppTable が返すテーブルオブジェクトから直接使えます。
これらのコンポーネントの中では `useTableContext()` を使ってください。

#### 例 {#example-2}

```ts
{ PaginationControls, GlobalFilter, RowCount }
```

### tableContext? {#tablecontext}

```ts
optional tableContext?: Context<ReactTable<any, any>>;
```

テーブルインスタンス用の独自の React コンテキストです（`tableComponents` の中で
`useContext` を使って読み取ります）。省略可能で、既定ではモジュールスコープで共有されるコンテキストを使います。
このテーブルのコンテキストをほかのテーブルから切り離す必要があるとき（たとえばテーブルの中に別のテーブルを入れ子にするとき）にだけ、
`createContext` で作った独自のコンテキストを渡してください。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TTableComponents {#ttablecomponents}

`TTableComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

### TCellComponents {#tcellcomponents}

`TCellComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>

### THeaderComponents {#theadercomponents}

`THeaderComponents` *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>
