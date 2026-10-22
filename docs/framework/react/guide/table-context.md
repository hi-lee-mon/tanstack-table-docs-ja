---
title: テーブルコンテキストガイド
---

[`createTableHook`](./composable-tables) で再利用可能なコンポーネントを登録すると、そのコンポーネントは現在のテーブル・セル・ヘッダーを props ではなく React のコンテキストから読み取ります。このガイドでは、そのコンテキストの仕組み、完全な型安全性を保ったまま読み取る方法、そしてネストしたテーブルのような高度なケースで分離されたコンテキストを作る方法を説明します。

## コンテキストの提供のされ方 {#how-the-context-is-provided}

コンテキストに値を載せるのは、`useAppTable` が返すコンポーネントです。

- `<table.AppTable>` は現在のテーブルインスタンスを提供します。
- `<table.AppCell cell={cell}>` は現在のセルインスタンスを提供します。
- `<table.AppHeader header={header}>` と `<table.AppFooter header={footer}>` は現在のヘッダーインスタンスを提供します。

登録した `tableComponents`、`cellComponents`、`headerComponents` は、対応するフックでそれらのインスタンスを読み取ります。

```tsx
function PaginationControls() {
  const table = useTableContext() // the table provided by <table.AppTable>
  return <button onClick={() => table.nextPage()}>Next</button>
}

function TextCell() {
  const cell = useCellContext<string>() // the cell provided by <table.AppCell>
  return <span>{cell.getValue()}</span>
}

function SortIndicator() {
  const header = useHeaderContext() // the header provided by <table.AppHeader>
  return header.column.getIsSorted() ? '🔼' : null
}
```

読み取ったインスタンスは、ラッパーが描画に使っているものと同じです。`App*` コンポーネントと登録したコンポーネントで、すでに拡張されています。たとえば、テーブルコンポーネントの中では `table.PaginationControls` や `table.AppCell` が、セルコンポーネントの中では `cell.TextCell` や `cell.FlexRender` が使えます。

> [!TIP]
> テーブルにたどり着くだけなら、テーブルコンテキストは要らないことがよくあります。`cell`、`header`、`row`、`column` の各インスタンスは、自分のテーブルへの参照（`cell.table`、`header.table`、`row.table`、`column.table`）を持っているからです。そのため、セルやヘッダーのコンポーネントの中では、`useTableContext()` を呼ばなくても、手元のインスタンスから直接テーブルを読めます（例: `cell.table.nextPage()`）。インスタンス同士もつながっている（`cell.row`、`cell.column`、`header.column`、`row.getAllCells()`）ので、インスタンスが1つあれば、たいていは必要なものまでたどれます。`useTableContext()` を使うのは、単独のツールバーやページネーションのコントロールのように、起点になるインスタンスを持たないコンポーネントのときです。

## フックは createTableHook の結果からインポートする {#import-the-hooks-from-your-createtablehook-result}

> [!IMPORTANT]
> 型安全性を最大限に得るには、`useTableContext`、`useCellContext`、`useHeaderContext` を `createTableHook` を呼んだのと同じモジュールからインポートしてください。これらのフックは `TFeatures` **と** 登録したコンポーネントのマップの両方を知っているので、`table.PaginationControls`、`cell.TextCell`、`header.SortIndicator` のすべてに型が付きます。

```tsx
// hooks/table.ts
export const {
  useAppTable,
  createAppColumnHelper,
  useTableContext, // <- typed with TFeatures + your tableComponents
  useCellContext, //  <- typed with TFeatures + your cellComponents
  useHeaderContext, // <- typed with TFeatures + your headerComponents
} = createTableHook({
  features,
  tableComponents,
  cellComponents,
  headerComponents,
})
```

## 独自のコンテキストでインスタンスを渡す {#passing-instances-through-your-own-context}

`createTableHookContexts` は、`createTableHook` とは別に単独で使っても、props のバケツリレー（prop drilling）を避けるのに役立ちます。`column`、`row`、`cell`、`header` の各インスタンスは**安定した参照**です（TanStack Table が React Compiler のメモ化で頼りにしているのと同じ安定性です）。どれをコンテキストに載せても、サブツリーの深い場所で読み取れます。テーブルの状態が変わっても参照は変わらないので、コンテキストの値も同じままで、購読側のコンポーネントが状態の変化で再レンダーされることはありません。

`createContext` を自前で書く代わりに、`createTableHookContexts` を使ってください。コンテキストと、それに対応する `TFeatures` の型付きフックをまとめて返してくれるので、値の型を書き直したり、`useContext` のガードを自分で書いたりせずに済みます（このユーティリティのもう1つの使い方である、コンテキストを `createTableHook` に渡す方法は、後述の[createTableHookContexts によるスコープ付きコンテキスト](#scoped-contexts-with-createtablehookcontexts)を参照してください）。

```tsx
// cell-slot-context.ts
export const { cellContext, useCellContext } =
  createTableHookContexts<typeof features>()

// provide the (stable) cell once, near where you render it
function CellSlot({ cell }: { cell: Cell<typeof features, Person, unknown> }) {
  return (
    <cellContext.Provider value={cell}>
      <DeeplyNestedCellUI />
    </cellContext.Provider>
  )
}

// read it anywhere below, no prop drilling
function DeeplyNestedCellUI() {
  const cell = useCellContext() // typed with your TFeatures
  return <span>{/* ... */}</span>
}
```

> [!IMPORTANT]
> 状態に依存するメソッドの読み取り結果が古くなるのは、まさにこの安定性のせいです。コンテキストから受け取ったインスタンスで `header.column.getIsSorted()`、`cell.row.getIsSelected()`、`cell.getValue()` などを読むコンポーネントは、その状態が変わっても、それだけでは再レンダーされません。こうしたメソッドの読み取りは `Subscribe` のレンダーコールバックで包むか、`useSelector` で選んだ値から直接描画して、UI にリアクティブな依存関係を明示してください。[ネストしたコンポーネントで Subscribe を使う](./react-compiler#use-subscribe-in-nested-components)を参照してください。

ただし `table` オブジェクトは例外です。`useTable` は、選択した状態が変わるたびに、React 向けの新しい `table` 参照を返します。これは、`table` に依存する JSX を React Compiler に無効化させるための意図した動作です。デフォルトのセレクターでは、登録されたテーブルの状態が変わるたびに参照が変わります。セレクターを絞れば、選んだ部分が更新されたときだけ変わります。したがって `table` は安定したコンテキストの値では**ありません**。独自のコンテキストでテーブルを提供すると、提供側のコンポーネントが新しいラッパーで再レンダーされるたびに、購読側も再レンダーされます。安定したハンドルを下へ渡したいなら、`table.store` や `table.atoms.rowSelection` のような特定のアトム（これらは安定しています）を提供して `Subscribe` / `useSelector` で読み取るか、コアのテーブルを ref に保持してください。

## デフォルトの共有コンテキスト {#the-default-shared-context}

デフォルトでは、コンテキストを自分で作ったり接続したりする必要はありません。`createTableHook` は、自身の `AppTable`/`AppCell`/`AppHeader` プロバイダーを、モジュールスコープの共有コンテキストに接続します。返されるフックも、同じコンテキストから読み取ります。コンテキストがモジュールスコープにあるので、ローカル開発中のホットモジュールリプレースメントをまたいでも、その同一性は保たれます。そのため、コンポーネントを編集しても、プロバイダーと購読側が食い違ったコンテキストを指す状態にはなりません。

独立したテーブル同士は、通常のプロバイダーのスコープによって分離されます。`<table.AppTable>` はそれぞれ自分のテーブルインスタンスを提供し、購読側は最も近いプロバイダーから読み取ります。異なるテーブルを横に並べて描画しても、別々のルートで描画しても、追加の設定なしで動きます。

## createTableHookContexts によるスコープ付きコンテキスト {#scoped-contexts-with-createtablehookcontexts}

共有コンテキストが問題になるのは、あるテーブルのプロバイダーを別のテーブルのプロバイダーの中に**ネスト**し、その重なった部分にある購読側が、意図したプロバイダーではなく最も近い（内側の）プロバイダーから読み取ってしまう場合だけです。このケースでは、`createTableHookContexts` で分離されたコンテキストを作り、`createTableHook` に渡してください。

```tsx
// scoped-table-context.ts (no component imports)
import { createTableHookContexts, tableFeatures } from '@tanstack/react-table'

export const features = tableFeatures({/* ... */})

export const {
  tableContext,
  cellContext,
  headerContext,
  useTableContext,
  useCellContext,
  useHeaderContext,
} = createTableHookContexts<typeof features>()
```

```tsx
// table.ts
import { createTableHook } from '@tanstack/react-table'
import {
  cellContext,
  features,
  headerContext,
  tableContext,
} from './scoped-table-context'

export const { useAppTable } = createTableHook({
  features,
  tableContext, // <- providers now use these scoped contexts
  cellContext,
  headerContext,
  tableComponents: {/* ... */},
})
```

`createTableHookContexts` は呼ぶたびに新しいコンテキスト一式を返します。そのため、それぞれ独自のスコープ付きコンテキストを使う2つのテーブル構成は、互いの値を読み取ることなくネストできます。

### スコープ付きコンテキストで使うフック {#which-hooks-to-use-with-scoped-contexts}

`createTableHookContexts` も `useTableContext`/`useCellContext`/`useHeaderContext` を返しますが、これらは `TFeatures` だけで型付けされています。登録したコンポーネントのマップは後で `createTableHook` の中で定義されるため、それを知りません。したがって、次のようにします。

- 最も豊かな型を得るには、`createTableHook` の呼び出しが返すフックを優先してください（`tableComponents`/`cellComponents`/`headerComponents` に型が付きます）。
- `createTableHookContexts` のフックは、`createTableHook` の結果をインポートできないモジュールからコンテキストを読む必要があるときだけ使ってください。

これは TanStack Form の `createFormHookContexts` と同じ考え方です。そちらでもコンテキストのフックは意図的にゆるい型になっていて、強く型付けされた経路は form/field のコンポーネント側にあります。

## これを使う場面 {#when-to-use-this}

- よくあるケースでは特別なことは何もしなくてかまいません。デフォルトの共有コンテキストが、単一のテーブルにも、互いに独立した複数のテーブルにも対応します。
- `createTableHookContexts` を使うのは、異なるテーブル構成をネストしていてコンテキストを分離する必要があるときか、コンポーネントを含まないモジュールからコンテキストを読みたいときだけにしてください。
