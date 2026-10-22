---
title: React Compiler ガイド
---

> [!IMPORTANT]
> **TanStack Table V9 は、React Compiler に対応した最初の TanStack Table のバージョンです。**

[React Compiler](https://react.dev/learn/react-compiler/introduction) は、React コンポーネントと、レンダー中に作られる値を自動でメモ化します。Table V9 では、`useTable` を呼び出すコンポーネントもふつうにコンパイルできます。また、`useTable` に渡す値を安定させるためだけに `useMemo` や `useCallback` を使う必要も、たいていはありません。

Table V9 のコードのほとんどは、コンパイラー向けの特別な対応を必要としません。おもな例外は、props として受け取るのが安定した Table のオブジェクト（コアの `table`・`row`・`cell`・`column`・`header` など）だけの、入れ子のコンポーネントです。これらのオブジェクトのメソッドは、オブジェクト自体が変わっていなくても新しい値を返すことがあります。一方コンパイラーは、props が変わっていないことを理由に、その入れ子のコンポーネントの再レンダーを省くことがあります。このような場合は、コンポーネントが読み取る状態について `Subscribe` の境界が必要になります。

## テーブルのために React Compiler を使う価値はあるか {#is-the-react-compiler-worth-it-for-tables}

私たちは、同じ Table V9 のサンプルを React Compiler の有効・無効の両方でビルドする[専用のベンチマーク](https://github.com/KevinVandy/tanstack-table-benchmarks)を管理しています。このベンチマークでは、テーブルを持つコンポーネントがテーブルの状態をすべて購読する場合と、`Subscribe` を使って小さく的を絞って更新する場合を比べています。また、各操作の計測値は、操作ごとに期待どおりの DOM の結果になったことを確かめてから採用しています。

基準となる計測は、元データ 10,000 行、描画する行 100 行、CPU を 4 倍に低速化、ウォームアップ 2 回、順序を交互に入れ替えたサンプル 20 回という条件で行いました。結果は、操作してからレイアウトエフェクトがコミットされるまでの時間の中央値（ミリ秒）です。

| 更新                    | 全体を購読: 無効 → 有効 |         きめ細かい購読: 無効 → 有効 |
| ----------------------- | ----------------------: | ----------------------------------: |
| 無関係な親の更新        |      3.75 → 0.50 (-87%) |                  3.50 → 0.50 (-86%) |
| 1 行を選択              |      4.00 → 1.30 (-68%) |      0.90 → 0.95（実質的に変化なし） |
| ソート                  |      8.35 → 7.40 (-11%) |                   8.00 → 7.35 (-8%) |
| ページ送り              |       8.30 → 8.35 (+1%) |                   8.00 → 8.35 (+4%) |
| データをすべて置き換え  |       8.10 → 8.55 (+6%) |                   8.30 → 8.50 (+2%) |

この結果からは、データグリッドのためだけに React Compiler を有効にする理由は見当たりません。テーブルの操作の多くはわずかしか変わらず、きめ細かい更新はもともと `Subscribe` によって高速でした。最も大きく改善したのは、無関係な親のレンダーがテーブルまで連鎖するのを防いだ点です。コンパイラーを使うかどうかは、アプリケーション全体の必要に応じて決めてください。Table V9 はコンパイラーに対応していますが、入れ子のテーブルコンポーネントでは、以下で説明する明示的な購読が必要になることがあります。

## useMemo と useCallback は削除できるか {#can-i-remove-usememo-and-usecallback}

React Compiler がコンポーネントをうまくコンパイルできていれば、`useTable` に渡す配列・オブジェクト・派生データ・コールバックを安定させるためだけのメモ化は、たいてい削除できます。変化のない子コンポーネントのレンダーを防ぐためだけに `React.memo` を使う必要もありません。

コンパイラーを使う場合、次のコンポーネントでは `columns` や `visiblePeople` を手動でメモ化する必要はありません。

```tsx
function PeopleTable({ people, showInactive }) {
  const columns = columnHelper.columns([
    columnHelper.accessor('firstName', {
      header: 'First Name',
    }),
    columnHelper.accessor('status', {
      header: 'Status',
    }),
  ])

  const visiblePeople = showInactive
    ? people
    : people.filter((person) => person.status === 'active')

  const table = useTable({
    features,
    columns,
    data: visiblePeople,
  })

  // ...
}
```

コンパイラーを使わない場合は、これらの値の参照が安定するように書きます。

```tsx
const columns = useMemo(
  () =>
    columnHelper.columns([
      // ...
    ]),
  [],
)

const visiblePeople = useMemo(
  () =>
    showInactive
      ? people
      : people.filter((person) => person.status === 'active'),
  [people, showInactive],
)
```

`data` と `columns` の参照が安定していることは、引き続き重要です。Table は、これらの同一性をもとに、列や行モデルを作り直すタイミングを判断します。コンパイラーも手動のメモ化も使わずにレンダーのたびに新しい参照を作ると、不要な再計算や、状態の意図しない自動リセットが起きることがあります。

既存のメモ化は、なぜそこにあるのかを確かめずに削除しないでください。コードをコンパイラーなしでも動かす必要がある場合、別の API が特定の同一性を必要とする場合、コンパイラーがそのコンポーネントをコンパイルしない場合、プロファイリングでメモ化が効果を上げていると分かった場合は、メモ化を残してください。

### ドキュメントで手動のメモ化を使い続けている理由 {#why-the-docs-still-use-manual-memoization}

TanStack Table の React のサンプルはすべて React Compiler を通して動かしていますが、サンプルやコード片では今も `useMemo`・`useCallback`・モジュールスコープの定数といった従来の React の書き方を使っています。こうしておけば、コンパイラーを使わないアプリケーションでも、同じコードが正しく動き、役に立つからです。コンポーネントがコンパイルされるなら、その手動のメモ化は Table V9 が追加で求めるものではありません。

### 依存配列は引き続き重要 {#dependency-arrays-still-matter}

React Compiler は、自分で書いた依存配列までは直してくれません。残した `useEffect`・`useMemo`・`useCallback` には、リアクティブな依存値をすべて含める必要があります。古いクロージャーを参照してしまわないように、[`exhaustive-deps` のリントルール](https://react.dev/reference/eslint-plugin-react-hooks/lints/exhaustive-deps)に従ってください。

## Table のオブジェクトを入れ子のコンポーネントに渡す {#passing-table-objects-to-nested-components}

Table V9 では、コアのテーブルインスタンスと、その `column`・`row`・`cell`・`header` オブジェクトの参照が変わりません。ふだんはこれが役に立ちますが、コンパイルされた子コンポーネントは、テーブルの状態が変わる前と後で同じ props のオブジェクトを受け取ることになります。

たとえば、テーブルの本体が次のように選択用のコントロールを描画しているとします。

```tsx
<SelectionCell row={row} />
```

子コンポーネントは、`row` オブジェクトから選択状態を読み取ります。

```tsx
function SelectionCell({ row }: { row: Row<typeof features, Person> }) {
  return (
    <input
      type="checkbox"
      checked={row.getIsSelected()}
      onChange={row.getToggleSelectedHandler()}
    />
  )
}
```

行を選択しても、`row` オブジェクトは置き換わりません。`row` の props が変わらないため、コンパイラーは `SelectionCell` の前回のレンダー結果を再利用することがあります。そうなると `row.getIsSelected()` が再び呼ばれず、チェックボックスの表示が古いままになります。

props として渡すオブジェクトが変わらないまま、次のようなメソッドの結果が変わる場合には、いつでも同じ問題が起こりえます。

- `column.getIsPinned()` と `column.getIsSorted()`
- `row.getIsSelected()` と `row.getIsExpanded()`
- `cell.getIsAggregated()` と `cell.getValue()`
- `header.column.getCanSort()`

`useTable` が直接返す値は、行・セル・列・レンダーコンテキストが使うコアのテーブルオブジェクトとは振る舞いが異なります。

- `useTable` が返す React 向けの値は、オプションが変わったとき、またはそのフックで選択した状態が変わったときに変化します。
- `row.table`・`cell.table`・`column.table` にあるコアのテーブルは、同じ参照のままです。

デフォルトでは、`useTable` は登録されたテーブルの状態をすべて選択します。そのため、そのコンポーネントで直接描画する JSX は、ほかに購読しなくてもふつうは更新されます。別に購読が必要になるのは、入れ子のコンポーネントが安定した Table のオブジェクトだけを受け取り、変化する状態をそのメソッド経由で読み取る場合です。また、`useTable` のセレクターが、描画する UI で使う状態を含んでいない場合にも必要です。セレクターとして `() => null` を渡すと、意図的にテーブルの状態をすべて除外することになります。

## 状態を読み取るコンポーネントの中で購読する {#subscribe-inside-the-component-that-reads-the-state}

テーブルの状態を読み取る入れ子のコンポーネントの中に、`table.Subscribe` か単体の `Subscribe` コンポーネントを置きます。選択の例では、その行の選択値を購読し、その値をもとに描画します。

```tsx
import { Subscribe } from '@tanstack/react-table'

function SelectionCell({ row }: { row: Row<typeof features, Person> }) {
  return (
    <Subscribe
      source={row.table.atoms.rowSelection}
      selector={(rowSelection) => rowSelection[row.id]}
    >
      {(isSelected) => (
        <input
          type="checkbox"
          checked={!!isSelected}
          onChange={row.getToggleSelectedHandler()}
        />
      )}
    </Subscribe>
  )
}
```

これで、`row` の props が同じままでも、このチェックボックスを更新すべきときに購読が React に知らせてくれます。

`<SelectionCell row={row} />` を `Subscribe` で囲んだうえで、選択値を使わないという書き方はしないでください。子コンポーネントは同じ `row` の props を受け取ったままなので、コンパイラーはやはりそれを再利用できてしまいます。購読は子コンポーネントの中に置くか、選択値を props として子コンポーネントに渡し、その props をもとに描画してください。

`useSelector` についても同じです。選択した値はコンポーネントの出力で使うか、子コンポーネントに渡してください。レンダーを強制するためだけに `useSelector` を呼んでも、コンパイラーが安定した Table のオブジェクトのメソッドを再び呼び出すとは限りません。

### 正しさを保てる範囲で最も狭く購読する {#choose-the-narrowest-subscription-that-stays-correct}

描画結果を変えうる、最小限の状態を購読してください。選択の例で必要なのは `rowSelection[row.id]` だけなので、ほかの行が変わってもそのチェックボックスを更新する必要はありません。

コンポーネントが複数の状態の断片に依存する場合は、`table.store` を購読し、セレクターからそれらの断片をすべて返します。状態に依存する Table の呼び出しは、`Subscribe` のレンダー関数の中に置いてください。

```tsx
function TableBody({ table }) {
  return (
    <Subscribe
      source={table.store}
      selector={(state) => ({
        columnFilters: state.columnFilters,
        globalFilter: state.globalFilter,
        pagination: state.pagination,
      })}
    >
      {() => (
        <tbody>
          {table.getRowModel().rows.map((row) => (
            <tr key={row.id}>
              <td>{row.original.firstName}</td>
            </tr>
          ))}
        </tbody>
      )}
    </Subscribe>
  )
}
```

セレクターには、このテーブルの `table.getRowModel()` の結果を変えうる状態の断片をすべて含める必要があります。使っている機能によっては、フィルタリング・ソート・グループ化・展開・ページネーションなどが含まれます。

`table.getRowModel()` への入力は状態だけではありません。`setState` の呼び出し、クエリの再取得、WebSocket のメッセージなどによってテーブルの外から `data` を置き換えても、状態の断片はどれも変わらないため、`Subscribe` のセレクターでは検知できません。本体が `<table.AppTable>` の中で `useTableContext()` からテーブルを読み取る場合は、`useAppTable` を持つコンポーネントが新しいオプションでレンダーされるたびに `AppTable` が新しいテーブルの値を提供するので、追加の配線なしで本体が更新されます。コンパイラーが再レンダーを省きうるコンポーネントを経由して `table` を props で渡す場合は、`data`（または描画する行）も props として渡し、データが変わったときに本体が再びレンダーされるようにしてください。

`table` が `useTable` の返す React 向けの値であれば、`table.Subscribe` を使います。セルやヘッダーのレンダーコンテキストでは、`table` はコアの Table です。この場合は単体の `Subscribe` コンポーネントをインポートし、source に `table.store` か `table.atoms` の値のいずれかを渡してください。

デフォルトですべてのセルに購読を追加することはしないでください。入れ子のコンポーネントが props に表れていない状態を読み取る場合や、プロファイリングで更新をツリーの下のほうへ移すと効果があると分かった場合に追加します。

状態とセレクターの仕組みの全体像は、[テーブルの状態ガイド](./table-state#optimizing-re-renders-with-selectors-and-tablesubscribe)を参照してください。[Basic Subscribe](https://tanstack.com/table/latest/docs/framework/react/examples/basic-subscribe) と [Kitchen Sink](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink) のサンプルでは、これらの書き方を完全なテーブルで示しています。

## Table V8 で use no memo が必要だった理由 {#why-table-v8-needed-use-no-memo}

Table V8 の `useReactTable` は、内部に保持する値を変えながらも、同じテーブルオブジェクトを返していました。このパターンは **内部可変性**（interior mutability）と呼ばれることがあります。`table` オブジェクト自体は変わっていなくても、`table.getRowModel()` のようなメソッドが新しい行を返すことがありました。

React Compiler は、その安定したテーブルの参照をもとに、メソッドの呼び出しや子コンポーネントをキャッシュすることがありました。そのため、テーブル内部の値が変わっても、React が古い結果を再利用して UI が古いままになることがありました。React の [`incompatible-library` リントルールのドキュメント](https://react.dev/reference/eslint-plugin-react-hooks/lints/incompatible-library)では、この問題の例として Table V8 の `useReactTable` API が挙げられています。

回避策は、そのコンポーネントをコンパイラーの対象から外すことでした。

```tsx
function PeopleTable() {
  'use no memo'

  const table = useReactTable({
    columns,
    data,
    getCoreRowModel: getCoreRowModel(),
  })

  // ...
}
```

新しいコンパイラーのツールでは、`useReactTable` を認識して、そのコンポーネントを自動でコンパイル対象から外すこともあります。いずれにしても、そのコンポーネントはコンパイラーの最適化の恩恵を受けられません。

Table V9 では React との連携の仕組みが変わりました。`useTable` は選択した状態に合わせて更新される React 向けの値を返し、安定したコアのテーブルから値を読み取る入れ子のコンポーネントのために、TanStack Store が明示的な購読の仕組みを提供します。
