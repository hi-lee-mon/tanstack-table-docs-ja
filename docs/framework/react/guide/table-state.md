---
title: テーブルの状態（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の例を参照してください。

- [useTable の基本例](https://tanstack.com/table/latest/docs/framework/react/examples/basic-use-table)
- [外部アトムの基本例](https://tanstack.com/table/latest/docs/framework/react/examples/basic-external-atoms)
- [外部の状態の基本例](https://tanstack.com/table/latest/docs/framework/react/examples/basic-external-state)
- [Subscribe の基本例](https://tanstack.com/table/latest/docs/framework/react/examples/basic-subscribe)
- [TanStack Query との併用例](https://tanstack.com/table/latest/docs/framework/react/examples/with-tanstack-query)

## テーブルの状態（React）ガイド {#table-state-react-guide}

> **TanStack Table をひと言で表すなら、「テーブルの状態を取りまとめる大きな状態管理の調整役」です。**

このガイドの内容は、TanStack Table がどう動くのか、そしてどう扱えば最良の結果が得られるのかを理解するための基礎になります。

### 外部で状態を管理する必要はあるか {#do-you-need-to-manage-external-state}

通常、テーブルの状態を自分で管理する必要は**ありません**。`initialState`、`atoms`、`state`、または `on[State]Change` 系のテーブルオプションに何も渡さなければ、TanStack Table は状態を内部で管理します。

ただし、内部のテーブルの状態の扱い方をカスタマイズしたい場面や、状態を自分のスコープに引き上げたい場面もあります。TanStack Table では、アプリにとって重要な状態の一部（スライス）を読み取ったり、購読したり、自分で所有したりできます。このガイドでは、React でテーブルの状態がどう動くか、どう読み取るか、そして外部アトムや外部の状態をいつ使うべきかを説明します。

### v9 における状態 {#state-in-v9}

TanStack Table v9 では、状態管理を TanStack Store を中心に作り直しました。TanStack Store は `alien-signals` の実装を使っており、派生した状態を高いパフォーマンスで扱えます。TanStack Table にとってこれは、独立した状態のアトムからテーブルの状態全体のストアを派生させられること、そして React のコンポーネントが実際に必要とするテーブルの状態の一部だけを購読できることを意味します。

テーブルインスタンスには、状態に関わる窓口がいくつかあります。

- `table.baseAtoms` は、解決済みの初期状態から作られる、内部の書き込み可能なアトムです。
- `table.atoms` は、登録された状態スライスごとに公開される、読み取り専用の派生アトムです。
- `table.store` は、登録されたすべての `table.atoms` をまとめて派生させた、読み取り専用でフラットな TanStack Store です。
- `table.state` は React 専用の、選択された状態です。`useTable` の第2引数に渡したセレクターが返す値が入ります。

以前のバージョンからの重要な変更点は、テーブルの状態がアトム単位になったことです。React では、選択した状態全体、選択した状態の一部、あるいは `table.atoms.rowSelection` のような単一のアトムを購読できます。

### 機能に基づく状態 {#feature-based-state}

状態スライスは、`features` に登録された機能の分だけ作られます。これにより TanStack Table はツリーシェイク可能になり、TypeScript による状態の型推論もより正確になります。

たとえば `features` に `rowPaginationFeature` が含まれていれば、TypeScript はページネーションの状態に関する API と `table.atoms.pagination` を公開します。`features` に `rowPaginationFeature` が含まれていなければ、`pagination` は `table.atoms`、`table.store.state`、`table.state`、`initialState`、`state`、`atoms` のいずれでも使えないはずです。

```tsx
const features = tableFeatures({
  rowPaginationFeature,
  rowSortingFeature,
  paginatedRowModel: createPaginatedRowModel(),
  sortedRowModel: createSortedRowModel(),
  sortFns,
})

const table = useTable({
  features,
  columns,
  data,
})

table.atoms.pagination.get()
table.atoms.sorting.get()

// table.atoms.rowSelection // TypeScript error unless rowSelectionFeature is registered
```

この機能に基づく型付けは、組み込みの機能にも、カスタム機能が提供する状態にも同じように適用されます。

### テーブルの状態にアクセスする {#accessing-table-state}

テーブルの状態を読み取るときには、次の2つの問いを区別します。

- 現在の値だけが必要なのか。
- それとも、その値が変わったときにこの React コンポーネントを再レンダーすべきなのか。

現在の値が欲しいだけなら、アトムやストアを直接読み取ります。リアクティブに描画したいなら、セレクターによる購読を使います。

#### 購読せずに状態を読み取る {#reading-state-without-subscribing}

現在の状態の値を読み取るいちばん簡単で高速な方法は、対応するアトムを読み取ることです。

```tsx
const pagination = table.atoms.pagination.get()
const sorting = table.atoms.sorting.get()
```

フラットなストアの現在のスナップショットを読み取ることもできます。

```tsx
const tableState = table.store.state
const pagination = table.store.state.pagination
```

これらの読み取りは React の購読ではありません。レンダー中に `table.atoms.pagination.get()` や `table.store.state.pagination` を呼ぶと現在の値は読み取れますが、その後に値が変わっても、ほかの何かがレンダーを引き起こさない限り、そのコンポーネントは自動では再レンダーされません。UI をテーブルの状態の変化にリアクティブに追従させたい場合は、`useTable` による状態の選択、`table.Subscribe`、あるいは TanStack Store の `useSelector` フックを使ってください。

#### useTable でリアクティブな状態を読み取る {#reading-reactive-state-with-usetable}

`useTable` の第2引数は TanStack Store のセレクターです。デフォルトのセレクターは、実質的に登録済みのテーブルの状態をすべて選択します。そのため `table.state` には状態全体が入り、選択された状態のどれかが変わるとコンポーネントが再レンダーされます。

独自のセレクターを渡せば、`table.state` に入るのを、再レンダーのきっかけにしたいリアクティブな状態の値だけに絞れます。React アダプターは選択された値を浅く比較します。デフォルトのセレクターは、登録済みのテーブルの状態をすべて選択します。

```tsx
const table = useTable(
  {
    features,
    columns,
    data,
  },
  (state) => ({
    pagination: state.pagination,
  }),
)

table.state.pagination
```

大きなテーブルでは、親のテーブルコンポーネントをテーブルの状態による再レンダーから外し、ツリーのより下の階層で購読することもできます。

```tsx
const table = useTable(
  {
    features,
    columns,
    data,
  },
  () => null,
)
```

このパターンでは、親コンポーネントはテーブルの状態が変わっても再レンダーされません。リアクティブな読み取りは、UI が実際にそれを必要とする場所で `table.Subscribe` の中に置いてください。

#### セレクターと table.Subscribe で再レンダーを最適化する {#optimizing-re-renders-with-selectors-and-tablesubscribe}

テーブルの状態による再レンダーを React ツリーの特定の場所で起こしたいときは、`table.Subscribe` を使います。大きなテーブルや描画コストの高いテーブルで役立ちますが、通常はデフォルトの `useTable` セレクターで目に見えるパフォーマンスの問題が出てから手を伸ばすものです。

`source` プロパティを渡さない場合、`table.Subscribe` は `table.store` を購読し、セレクターが必須になります。`source` プロパティを渡すと、`table.atoms.rowSelection` のような単一のアトムやストアを直接購読できます。

```tsx
const table = useTable(
  {
    features,
    columns,
    data,
  },
  () => null,
)

return (
  <table.Subscribe
    selector={(state) => ({
      columnFilters: state.columnFilters,
      globalFilter: state.globalFilter,
      pagination: state.pagination,
    })}
  >
    {() => (
      <tbody>
        {table.getRowModel().rows.map((row) => (
          <tr key={row.id}>...</tr>
        ))}
      </tbody>
    )}
  </table.Subscribe>
)
```

単一のアトムを直接購読し、そこから1つの値を選択することもできます。

```tsx
<table.Subscribe
  source={table.atoms.rowSelection}
  selector={(rowSelection) => rowSelection[row.id]}
>
  {(isSelected) => (
    <input
      type="checkbox"
      checked={!!isSelected}
      onChange={row.getToggleSelectedHandler()}
    />
  )}
</table.Subscribe>
```

高度な購読パターンを使うには、どのテーブル API がどの状態スライスに依存しているかを理解しておく必要があります。たとえば、行モデルはフィルタリング・ソート・ページネーションに依存することがありますが、行選択のチェックボックス1つは、その行の選択状態の値だけがあれば足りるかもしれません。まずはデフォルトのセレクターから始め、描画コストが問題になる箇所でセレクターと `table.Subscribe` を使って最適化してください。

#### React Compiler との互換性のための Subscribe {#subscribe-for-react-compiler-compatibility}

TanStack Table v9 は React Compiler と互換性があります。ただし、入れ子になったコンポーネントでは、参照が変わらない `column`・`row`・`cell`・`header` オブジェクトの陰に、リアクティブな状態の読み取りが隠れてしまうことがあります。専用の [React Compiler ガイド](./react-compiler)では、v8 から何が変わったか、コンパイラを使う場合にいつ手動のメモ化を外せるか、依存配列がどう影響を受けるか、そして入れ子のコンポーネントをリアクティブに保つために `table.Subscribe` やスタンドアロンの `Subscribe` をどこで使うかを説明しています。

### テーブルの状態を設定する {#setting-table-state}

テーブルの状態を直接設定する必要は、ほぼありません。TanStack Table の各機能は、それぞれの状態を操作するための専用 API を公開しています。これらの API は機能自身のルールや関連する更新を守ってくれるため、変更を加えるいちばん安全な方法です。

たとえば、ページネーションの状態を自分で書き換える代わりに、ページネーションの API を使います。

```tsx
table.nextPage()
table.previousPage()
table.setPageIndex(0)
table.setPageSize(25)
```

ほかの機能でも考え方は同じです。内部の状態オブジェクトを手で編集する代わりに、`table.setSorting(...)`、`table.setColumnFilters(...)`、`column.toggleVisibility()`、`row.toggleSelected()` のような API を使ってください。

開始時の値を設定したいだけなら、`initialState` を使います。状態スライスを初期値に戻したいなら、その機能のリセット API を使います。

どうしても状態スライスを直接書き換える必要がある場合、内部で所有されている状態に対する低レベルの書き込み口は、対応するベースアトムです。

```tsx
table.baseAtoms.pagination.set((old) => ({
  ...old,
  pageIndex: 0,
}))
```

ベースアトムへの直接の書き込みは、めったに行うべきではありません。スライスを `atoms` で渡した外部アトムが所有している場合は、代わりにその外部アトムに書き込んでください。`table.atoms.pagination` が読み取るのは外部アトムであり、内部のベースアトムではありません。

### 初期状態をカスタマイズする {#custom-initial-state}

一部のテーブルの状態について開始時の値だけを変えたいなら、`initialState` を使います。この場合も、その状態を自分で管理する必要はありません。

`initialState` が適用されるのは、登録済みの状態スライスだけです。テーブルの初期状態を作るのに使われるほか、`table.resetSorting()` や `table.resetPagination()` といったリセット API でも使われます。後から `initialState` オブジェクトを変更しても、テーブルの状態はリセットされません。

```tsx
const table = useTable({
  features,
  columns,
  data,
  initialState: {
    sorting: [
      {
        id: 'age',
        desc: true,
      },
    ],
    pagination: {
      pageIndex: 0,
      pageSize: 25,
    },
  },
})
```

> [!NOTE]
> 意図的にどちらかを優先させたい場合を除き、同じ状態スライスを複数の所有場所で指定しないでください。たとえば `pagination` のようなスライスなら、`initialState.pagination`、`atoms.pagination`、`state.pagination` のうちちょうど1つを信頼できる唯一の情報源にしてください。外部アトムは外部の `state` より優先されます。外部の `state` は、テーブル内部のベースアトムへ同期されます。

#### 初期状態にリセットする {#resetting-to-initial-state}

機能ごとのリセット API は、デフォルトでは `table.initialState` に戻します。多くのリセット API は `true` も受け付け、その場合はその機能の空の状態（デフォルトの状態）に戻します。

```tsx
table.resetSorting()
table.resetPagination()
table.resetPagination(true)
```

`resetPagination()` のようなスライス単位のリセット API は、その機能の状態アップデーターを通して更新するため、外部で所有されているアトムも更新できます。一方、コアの `table.reset()` API は内部のベースアトムをリセットします。そのため、外部アトムが所有する状態をリセットする主な手段としては使わないでください。

### 制御された状態 {#controlled-state}

アプリケーションの別の場所からテーブルの状態に手軽にアクセスしたい場合は、個々の状態スライスを制御できます。v9 では、外部アトムを使う方法が推奨されています。外部アトムならアトム単位の状態モデルが保たれ、React は必要なスライスだけを正確に購読できるからです。

#### 外部アトム {#external-atoms}

アプリがテーブルの状態スライスを1つ以上所有すべき場合は、外部アトムを使います。TanStack Store の `useCreateAtom` で参照が変わらない書き込み可能なアトムを作り、テーブルの `atoms` オプションに渡します。アプリのほかの場所では、`useSelector` でそのアトムを購読します。

これは、サーバーサイドでデータを取得する場合にとくに役立ちます。ページネーション・ソート・フィルターはクエリキーに含めることが多く、外部アトムを使えば、テーブルの状態全体を React の状態として引き上げなくても、アプリとテーブルでそれらの値を共有できます。

```tsx
import { useCreateAtom, useSelector } from '@tanstack/react-store'
import {
  rowPaginationFeature,
  tableFeatures,
  useTable,
  type PaginationState,
} from '@tanstack/react-table'

const features = tableFeatures({
  rowPaginationFeature,
})

function App() {
  const paginationAtom = useCreateAtom<PaginationState>({
    pageIndex: 0,
    pageSize: 10,
  })

  const pagination = useSelector(paginationAtom)

  const dataQuery = useQuery({
    queryKey: ['data', pagination],
    queryFn: () => fetchData(pagination),
  })

  const table = useTable({
    features,
    columns,
    data: dataQuery.data?.rows ?? [],
    rowCount: dataQuery.data?.rowCount,
    atoms: {
      pagination: paginationAtom,
    },
    manualPagination: true,
  })

  // table pagination APIs update paginationAtom
}
```

あるスライスに `atoms` オプションを使う場合、対応する `on[State]Change` オプションを追加する必要はありません。たとえば `atoms.pagination` を渡すと、テーブルのページネーション API はそのアトムを直接更新します。

#### 外部の状態 {#external-state}

従来の `state` と `on[State]Change` を組み合わせるパターンも引き続き使えます。単純な連携や v8 のコードを移行するときには便利ですが、外部アトムほど細かい単位では制御できません。React の状態を更新すると、それを所有するコンポーネントが再レンダーされます。アトムの購読ならツリーのより下の階層に置けますが、この再レンダーは `useTable` のセレクターで同じように避けることはできません。

外部の状態でスライスを制御するには、状態の値と対応するコールバックの両方を渡します。

```tsx
const [sorting, setSorting] = React.useState<SortingState>([])
const [pagination, setPagination] = React.useState<PaginationState>({
  pageIndex: 0,
  pageSize: 10,
})

const table = useTable({
  features,
  columns,
  data,
  state: {
    sorting,
    pagination,
  },
  onSortingChange: setSorting,
  onPaginationChange: setPagination,
})
```

v8 形式の `onStateChange` オプション（状態全体に対する単一のコールバック）は、v9 でなくなりました。`useTable` でも `useLegacyTable` でもサポートされていません。スライスごとの `on[State]Change` コールバックを `state.<slice>` と組み合わせて使うか、`atoms` オプションで外部アトムを使ってください。どうしてもすべての状態変化を監視したい場合は、`table.store` を直接購読してください。

##### 状態変化のコールバック {#on-state-change-callbacks}

`on[State]Change` コールバックは、対応するスライスを `state` オプションで制御しているときに役立ちます。これらは React の状態のセッターと同じように動きます。アップデーターは生の値でも、前の値を受け取って次の値を返す関数でもかまいません。

`on[State]Change` コールバックを指定する場合は、対応する値も `state` に指定してください。たとえば `onSortingChange` は `state.sorting` と組み合わせます。

```tsx
const [sorting, setSorting] = React.useState<SortingState>([])

const table = useTable({
  features,
  columns,
  data,
  state: {
    sorting,
  },
  onSortingChange: setSorting,
})
```

コールバックの中に処理を加えたい場合は、渡されたアップデーターが関数なのか値なのかを確認します。

```tsx
const [pagination, setPagination] = React.useState<PaginationState>({
  pageIndex: 0,
  pageSize: 10,
})

const table = useTable({
  features,
  columns,
  data,
  state: {
    pagination,
  },
  onPaginationChange: (updater) => {
    setPagination((old) => {
      const next = updater instanceof Function ? updater(old) : updater

      // side effects or validation can happen here

      return next
    })
  },
})
```

### 状態の型 {#state-types}

TanStack Table の複雑な状態の多くには、インポートして使える専用の TypeScript の型があります。React の状態、外部アトム、テーブルの状態を扱うヘルパー関数などで役立ちます。

```tsx
import {
  useTable,
  type PaginationState,
  type RowSelectionState,
  type SortingState,
  type TableState,
} from '@tanstack/react-table'

const [sorting, setSorting] = React.useState<SortingState>([
  {
    id: 'age',
    desc: true,
  },
])
```

`TableState<typeof features>` は、そのテーブルに登録された機能から推論されます。

```tsx
const features = tableFeatures({
  rowPaginationFeature,
  rowSortingFeature,
})

type MyTableState = TableState<typeof features>
```

1つのスライスのためにローカルの状態や外部アトムを作るときは、`SortingState`、`PaginationState`、`RowSelectionState` のような機能ごとの状態の型を使うことをおすすめします。
