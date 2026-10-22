---
title: TanStack Table V9 への移行（React）
---

## TanStack Table V9 の新機能 {#whats-new-in-tanstack-table-v9}

TanStack Table V9 では、性能が大きく向上し、数百件のバグが修正され、機能の追加と刷新が行われ、テーブルを組み立てて管理するための任意のヘルパーも加わりました。大規模なリリースですが、ヘッドレスという考え方、テーブルの中核となるロジック、列定義、描画のパターンはこれまでとほとんど変わりません。主な変更点は次のとおりです。

### 1. 性能の向上 {#1-better-performance}

- **メモリ使用量の削減**: 中核のアーキテクチャが、テーブルを構成するオブジェクト間でより多くの振る舞いを共有するようになりました。大きなテーブルでは、メモリを最大 90% 削減できる場合があります。
- **クライアントサイドの行モデルの高速化**: ソート、フィルタリング、集計の処理でアルゴリズムとメモ化が改善され、多くの場面で 40〜70% ほど速くなっています。
- **列幅の変更の高速化**: 同じアーキテクチャとメモ化の改善によって、列幅の変更も速くなりました。

### 2. 状態管理の刷新（後方互換あり） {#2-state-management-overhaul-backward-compatible}

- **React Compiler への対応**: 状態の仕組みが [TanStack Store](https://tanstack.com/store) の上に作られたため、React Compiler の下でもテーブルが正しく動くようになりました。[React Compiler ガイド](./react-compiler)を参照してください。
- **きめ細かな購読**: 状態の各スライスを、`table.atoms`、`table.store`、`table.state`、セレクター、`table.Subscribe` を通じて個別に読み取れます。
- **外部の状態やアトム**: これまでどおり `state` と `on[State]Change` を使うこともできますし、新しい `atoms` オプションで書き込み可能なアトムを渡し、スライスごとに状態を自分で持つこともできます。

### 3. 型安全性の向上 {#3-type-safety-improvements}

- **新しい型ヘルパーと刷新された型ヘルパー**: 列の定義、カスタムのフィルター・ソート・集計、列とテーブルの meta、共有するテーブルオプションやコンポーネントなどを定義するためのヘルパーがそろっています。
- **テーブルごとの meta 型**: `tableMeta`、`columnMeta`、`filterMeta` のスロットを使うと、共有のインターフェースをグローバルに拡張しなくても、特定のテーブルだけに meta の型を付けられます。**グローバルな宣言のマージ（declaration merging）はもう必要ありません！**
- **機能に応じて現れる API**: API は対応する機能を登録したときにだけ存在します。また、`tableFeatures()` は機能同士の前提条件を型のレベルで検査します。

### 4. ツリーシェイキングと拡張性 {#4-tree-shaking-and-extensibility}

- **使う機能だけをインポートする**: ソートだけが必要なテーブルには、フィルタリングやページネーションなど使わない機能のコードが含まれません。バンドルされる JS は 5kb から始まり、必要な機能の分だけが加わります。
- **ツリーシェイク可能な行モデルと関数**: 行モデルのファクトリーと `filterFns` / `sortFns` / `aggregationFns` は `tableFeatures()` に置くようになったため、使わない処理のコードを取り除けます。
- **カスタム機能も同じ仕組みで動く**: 自作の機能プラグインでも、組み込みの機能と同じように状態、オプション、API を登録できます。[カスタム機能ガイド](./custom-features.md)を参照してください。

### 5. 組み立てやすさ {#5-composability}

- `tableOptions`: 機能、行モデル、デフォルトのオプションを含む、再利用できるテーブル設定を組み立てます。
- `createTableHook`: アプリ全体で使い回すテーブルのパターンが必要なときに、機能とコンポーネントをあらかじめ結び付けたカスタムのテーブルフックを作ります。[composable-tables（createTableHook）ガイド](./composable-tables.md)を参照してください。

### 6. 新しい機能と刷新された機能 {#6-new-and-refreshed-features}

- **新しい機能**
  - **セル選択**: `cellSelectionFeature` は、スプレッドシートのような長方形のセル範囲選択を追加します。ドラッグでの選択、Shift による範囲の拡張、離れた複数の範囲の選択に対応しています。[セル選択ガイド](./cell-selection.md)を参照してください。
  - **セル結合**: `cellSpanningFeature` は、本体のセルを行や列をまたいで結合します（`spanRows` / `spanColumns`。結合を考慮したセル選択にも対応）。また、ヘッダーグループが `header.rowSpan` を計算するようになったため、階層の浅い列が複数のヘッダー行にまたがれるようになりました。[セル結合ガイド](./cell-spanning.md)を参照してください。
- **刷新された機能**
  - **より高機能に**: 集計、行選択、列の固定、列幅の変更は、いずれもできることが増えました（1つの列に複数の集計定義を持てる、Shift による範囲選択、論理的な `start`/`end` による固定など）。
  - **新しいコア API**: `table.getMaxSubRowDepth()` や `row.getDisplayIndex()` といった新しいテーブル API と行 API が加わり、コア機能がより充実しました。

### 7. モダンなビルド {#7-modern-builds}

- **ESM のみ**: UMD と CJS のビルドは廃止されました。パッケージはモダンな ESM として配布されます。
- **TypeScript のターゲットは `ES2022`**: コンパイル結果は ES2022 を対象にするようになりました。
- **インストールサイズの縮小**: 公開パッケージに `src` やソースマップを含めなくなったため、インストール時の容量が減りました。

### うれしい知らせ: ほとんどのアップグレードはオプトイン {#the-good-news-most-upgrades-are-opt-in}

Table V9 は大きなアップグレードですが、**すべてを一度に取り入れる必要はありません**。

- **描画の最適化はまだしたくない？** 特別なことは何もしなくてかまいません。デフォルトのセレクターは登録されたすべての状態を選択するので、描画は Table V8 と同じように動きます。
- **ツリーシェイキングのことは考えたくない？** `stockFeatures` をインポートすれば、Table V8 と同じようにすべての機能が含まれます。
- **テーブルのマークアップはほとんど変わりません。** `<table>`、`<thead>`、`<tr>`、`<td>` などの描画方法はこれまでと同じです。

主な変更は、`useTable` フックで**テーブルをどう定義するか**です。具体的には、新しい `features` オプションと、行モデルのファクトリーを登録する場所が変わりました。

---

## レガシー API による手早い移行 {#quick-legacy-migration}

少しずつ移行したい場合のために、`useLegacyTable` フックという一時的な近道を用意しています。このフックは Table V8 形式の API を受け付けつつ、内部では Table V9 を使います。**これは非推奨**で、移行を一時的に助けるためだけのものです。デフォルトですべての機能を含むため、バンドルは Table V8 のときよりもさらに大きくなります。

レガシー API は別のエクスポートにまとめられています。中核のユーティリティは `@tanstack/react-table` から、レガシー専用の API は `@tanstack/react-table/legacy` からインポートしてください。

```tsx
import { flexRender } from '@tanstack/react-table'
import {
  useLegacyTable,
  getCoreRowModel,
  getFilteredRowModel,
  getSortedRowModel,
  getPaginationRowModel,
  legacyCreateColumnHelper,
} from '@tanstack/react-table/legacy'
```

詳しい説明、サンプル、型ヘルパーについては [useLegacyTable ガイド](./use-legacy-table.md)を参照してください。

---

このガイドの残りでは、Table V9 の API へ完全に移行し、その機能を活かす方法を扱います。

## 中核の破壊的変更 {#core-breaking-changes}

### フックの名前の変更 {#hook-rename}

いちばん大きな変更は、`useReactTable` が `useTable` になったことです。これで TanStack のすべてのライブラリとフックの命名がそろいました。

```tsx
// Table V8
import { useReactTable } from '@tanstack/react-table'
const table = useReactTable(options)

// Table V9
import { useTable } from '@tanstack/react-table'
const table = useTable(options)
```

### 必須になった新しいテーブルオプション `features` {#new-required-features-table-option}

Table V9 では、テーブルが使う機能を明示的に宣言する必要があります。機能、行モデル、行モデルで使う処理関数（"Fns"）は、新しいテーブルオプション `features` に定義します。

Table V8 では、すべての機能がバンドルされ、`useReactTable` フックに含まれていました。Table V9 では、必要なものだけをインポートします。

```tsx
// Table V8
import {
  useReactTable,
  getCoreRowModel,
  getSortedRowModel,
  sortingFns,
} from '@tanstack/react-table'

const table = useReactTable({
  columns,
  data,
  getCoreRowModel: getCoreRowModel(),
  getSortedRowModel: getSortedRowModel(),
  sortingFns,
})

// Table V9
import {
  useTable,
  tableFeatures,
  rowSortingFeature,
  createSortedRowModel,
  sortFns,
} from '@tanstack/react-table'

// All table options that concern including code modules (features, row models, Fns, etc.)
const features = tableFeatures({
  rowSortingFeature, // new - import and pass the feature you want to use
  sortedRowModel: createSortedRowModel(), // now row models are defined on the features object
  sortFns, // now Fns are defined on the features object
  // ...more features, row models, etc.
})

const table = useTable({
  features, // new required option
  columns,
  data,
})
```

#### 近道: `stockFeatures` で Table V8 と同じ振る舞いにする {#shortcut-use-stockfeatures-for-table-v8-like-behavior}

（Table V8 のように）何も考えずにすべての機能を使いたい場合は、`stockFeatures` をインポートします。

```tsx
import { useTable, stockFeatures } from '@tanstack/react-table'

const table = useTable({
  features: stockFeatures, // All features included - just like Table V8 (though larger bundle now)
  columns,
  data,
})
```

#### 利用できる機能 {#available-features}

| 機能              | インポート名              |
| ----------------- | ------------------------- |
| 列のファセット    | `columnFacetingFeature`   |
| 列フィルタリング  | `columnFilteringFeature`  |
| 列のグループ化    | `columnGroupingFeature`   |
| 列の並べ替え      | `columnOrderingFeature`   |
| 列の固定          | `columnPinningFeature`    |
| 列幅の変更        | `columnResizingFeature`   |
| 列幅              | `columnSizingFeature`     |
| 列の表示切り替え  | `columnVisibilityFeature` |
| グローバルフィルタリング | `globalFilteringFeature`  |
| 行の集計          | `rowAggregationFeature`   |
| 行の展開          | `rowExpandingFeature`     |
| 行のページネーション | `rowPaginationFeature`    |
| 行の固定          | `rowPinningFeature`       |
| 行選択            | `rowSelectionFeature`     |
| 行のソート        | `rowSortingFeature`       |

### 行モデルのファクトリー {#row-model-factories}

行モデルは、データを処理する（フィルタリング、ソート、ページネーションなど）関数です。Table V9 では、行モデルのファクトリーを独立したテーブルオプションではなく、`tableFeatures({})` の呼び出しの中に置きます。処理関数のレジストリ（`filterFns`、`sortFns`、`aggregationFns`）も features に登録します。こうすることでツリーシェイキングが効きやすくなり、実際に登録した行モデルのコードと、フィルター・ソート・集計の関数だけがバンドルされます。

行モデルのスロットは型で検査されます。そのため、各行モデルは同じ `tableFeatures` の呼び出しの中で、対応する機能より後に指定する必要があります。

| Table V8 のオプション      | Table V9 の `tableFeatures` スロット | Table V9 のファクトリー関数   |
| -------------------------- | ----------------------------- | ----------------------------- |
| `getCoreRowModel()`        | （自動）                      | 不要。常に含まれる            |
| `getFilteredRowModel()`    | `filteredRowModel`            | `createFilteredRowModel()`    |
| `getSortedRowModel()`      | `sortedRowModel`              | `createSortedRowModel()`      |
| `getPaginationRowModel()`  | `paginatedRowModel`           | `createPaginatedRowModel()`   |
| `getExpandedRowModel()`    | `expandedRowModel`            | `createExpandedRowModel()`    |
| `getGroupedRowModel()`     | `groupedRowModel`             | `createGroupedRowModel()`     |
| `getFacetedRowModel()`     | `facetedRowModel`             | `createFacetedRowModel()`     |
| `getFacetedMinMaxValues()` | `facetedMinMaxValues`         | `createFacetedMinMaxValues()` |
| `getFacetedUniqueValues()` | `facetedUniqueValues`         | `createFacetedUniqueValues()` |

```tsx
import {
  tableFeatures,
  createFilteredRowModel,
  createSortedRowModel,
  createGroupedRowModel,
  filterFns, // Built-in filter functions
  sortFns, // Built-in sort functions
  aggregationFns, // Built-in aggregation functions
} from '@tanstack/react-table'

const features = tableFeatures({
  columnFilteringFeature,
  rowSortingFeature,
  rowAggregationFeature,
  columnGroupingFeature,
  rowPaginationFeature,
  filteredRowModel: createFilteredRowModel(),
  sortedRowModel: createSortedRowModel(),
  groupedRowModel: createGroupedRowModel(),
  paginatedRowModel: createPaginatedRowModel(),
  filterFns,
  sortFns,
  aggregationFns,
})

const table = useTable({
  features,
  columns,
  data,
})
```

#### レジストリ全体よりも関数を個別にインポートする {#prefer-individual-fn-imports-over-full-registries}

レジストリとしてエクスポートされている `filterFns`、`sortFns`、`aggregationFns` は非推奨になりました。代わりに、`filterFn_*`、`sortFn_*`、`aggregationFn_*` の関数を個別にインポートし、使うものだけを登録してください（あるいは、登録せずに列定義へ関数を直接渡すこともできます）。レジストリ全体も引き続き使えますが、展開して渡すと組み込みの関数がすべてバンドルに入ります。文字列で指定する名前（デフォルトの `'auto'` を含む）は、登録済みの関数にしか解決されません。

```tsx
// Before: registers every built-in function
import { filterFns, sortFns } from '@tanstack/react-table'

const features = tableFeatures({
  // ...other features and row models
  filterFns,
  sortFns,
})

// After: registers only the functions you use
import {
  filterFn_includesString,
  sortFn_alphanumeric,
  sortFn_text,
} from '@tanstack/react-table'

const features = tableFeatures({
  // ...other features and row models
  filterFns: { includesString: filterFn_includesString },
  sortFns: { alphanumeric: sortFn_alphanumeric, text: sortFn_text },
})
```

### インスタンスのメソッドはそのインスタンスから呼び出す {#instance-methods-must-be-called-on-their-instance}

Table V9 では、行、セル、列、ヘッダーなどのテーブルオブジェクトのメソッドは、オブジェクトごとにアロー関数として作られるのではなく、オブジェクトのプロトタイプで共有されます。これによりメモリ使用量は改善しますが、メソッドを分割代入で取り出すと、インスタンスを操作するのに必要な `this` のコンテキストが失われます。

```tsx
// Table V8 - worked because getValue closed over the row object
const { getValue } = row
const value = getValue('name')

// Table V9 - call the method on the instance
const value = row.getValue('name')
```

これは行、セル、列、ヘッダーと、それに関連するインスタンスの API に当てはまります。テーブルインスタンスそのものは対象外です。テーブルオブジェクトからメソッドを分割代入で取り出しているコードや、メソッドを単独のコールバックとして受け渡しているコードを見直してください。`row.getValue('name')`、`cell.getContext()`、`column.getCanSort()`、`header.getContext()` のように、元のオブジェクトを通して呼び出すのがおすすめです。

また、これらのメソッドはプロトタイプに置かれるようになったため、`Object.keys(instance)`、オブジェクトのスプレッド構文、`JSON.stringify` では自身のプロパティとして現れません。`{ ...row }` のような浅いコピーでは、行のデータはコピーされますが、行のメソッドはコピーされません。それでも、JavaScript がプロトタイプチェーンをたどってメソッドを探すため、通常どおり呼び出せます。

---

## 状態管理の変更 {#state-management-changes}

Table V9 の状態の仕組みは [TanStack Store](https://tanstack.com/store) の上に作られており、テーブルインスタンスには状態を読み取る窓口が3つあります。

| 窓口                  | 型                                                                                                               | 使いどころ                                                                                                                                                                            |
| --------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `table.state`         | `TSelected`（デフォルトでは登録されたテーブルの状態すべて。カスタムの `useTable` セレクターを渡した場合はその戻り値の形） | `useTable` で描画するコンポーネントの中では、これがいちばん扱いやすい窓口です。                                                                                                      |
| `table.store`         | `ReadonlyStore<TableState>`                                                                                      | テーブルの状態全体を、フレームワークに依存しないフラットなストアとして持ちます。一度だけ読むなら `table.store.state` を使い、きめ細かく購読するなら `useSelector` / `table.Subscribe` と組み合わせます。 |
| `table.atoms.<slice>` | `ReadonlyAtom<TableState[slice]>`                                                                                | スライスごとの読み取り専用アトムです。再レンダーの範囲をできるだけ狭くしたいときは、1つのスライス（例: `table.atoms.sorting`）だけを購読します。                                     |

書き込みのための対応物（ほとんどは内部用）:

| 窓口                      | 型                           | 使いどころ                                                                                                                                     |
| ------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `table.baseAtoms.<slice>` | `Atom<TableState[slice]>`    | ライブラリ内部の書き込み先です。通常は直接触らず、`table.setSorting(...)` や `table.setPagination(...)` などを使います。                       |
| `options.atoms`           | `Partial<{ [slice]: Atom }>` | 任意のスライスに自分の書き込み可能なアトムを渡すと、その状態を外部で管理できます。後述の[外部アトム](#external-atoms-advanced)を参照してください。 |

### 状態へのアクセス {#accessing-state}

Table V8 では `table.getState()` で状態にアクセスしていました。Table V9 ではアクセスの仕方が変わります。

```tsx
// Table V8
const state = table.getState()
const { sorting, pagination } = table.getState()

// Table V9 (RECOMMENDED) - via table.state (full selected state by default)
const table = useTable({
  features,
  columns,
  data,
})
const { sorting, pagination } = table.state

// Table V9 - via the store (full state)
const fullState = table.store.state
const { sorting, pagination } = table.store.state

// Table V9 - via table.state with a custom selector
const selectedTable = useTable(options, (state) => ({
  sorting: state.sorting,
  pagination: state.pagination,
}))
// Now selectedTable.state only contains sorting and pagination
const { sorting, pagination } = selectedTable.state

// Table V9 - via a single slice atom (framework-agnostic, ideal for fine-grained subscriptions)
const sorting = table.atoms.sorting.get()
```

#### テーブルオプション onStateChange の削除 {#onstatechange-table-option-removed}

Table V9 ではテーブルオプション `onStateChange` が削除されました。ただし、状態のスライスごとの `on[State]Change` ハンドラーは引き続き使えます。

どの状態の変化でも引き上げたり監視したりしたい場合は、`table.store` を購読します。

```tsx
const unsubscribe = table.store.subscribe((state) => {
  console.log(state)
})
```

### `table.Subscribe` による描画の最適化 {#optimized-rendering-with-tablesubscribe}

状態管理でいちばん大きな改善は `table.Subscribe` です。これによって、きめ細かなリアクティビティが実現します。

```tsx
function MyTable() {
  const table = useTable(
    {
      features,
      columns,
      data,
    },
    (state) => ({}), // default is state => state - this opts out of all default re-renders in favor of manual subscriptions down below
  )

  return (
    <table.Subscribe
      selector={(state) => ({
        sorting: state.sorting,
        pagination: state.pagination,
      })}
    >
      {({ sorting, pagination }) => (
        // This only re-renders when sorting or pagination changes
        <div>
          <table>{/* ... */}</table>
          <div>Page {pagination.pageIndex + 1}</div>
        </div>
      )}
    </table.Subscribe>
  )
}
```

### デフォルト: Table V8 と同じく状態全体を購読する {#default-table-v8-style-full-state-subscription}

デフォルトのセレクターのままでも、Table V8 と同じ振る舞いになります。つまり、登録されたテーブルの状態のどれかが変わると、コンポーネントが再レンダーされます。

```tsx
const table = useTable({
  features,
  columns,
  data,
})

// table.state contains the full registered state
const { sorting, pagination, columnFilters } = table.state
```

`(state) => state` を渡すのはデフォルトと同じなので、もう必要ありません。`table.state` に特定のスライスだけを入れたいときはカスタムのセレクターを渡します。テーブルの状態が変わっても親を再レンダーさせたくないときは、`() => null` を渡し、ツリーの下のほうで `table.Subscribe` を使います。

### 制御された状態 {#controlled-state}

Table V8 形式の `state` + `on[State]Change` による制御された状態のパターンは引き続き使え、単純な組み込みでは今でも手軽です。ただし、Table V9 で新しく書くコードでは、外部アトムで状態のスライスを持つ方法（後述の[外部アトム](#external-atoms-advanced)を参照）をおすすめします。React を経由して状態を写し取らなくても、きめ細かく購読できるからです。

```tsx
const [sorting, setSorting] = useState<SortingState>([])
const [pagination, setPagination] = useState<PaginationState>({
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

### スライスごとのアトムの購読 {#per-slice-atom-subscriptions}

状態の各スライスはそれぞれ専用のアトムに支えられているため、コンポーネントに1つのスライスだけを購読させ、他の状態が変わっても再レンダーしないようにできます。`@tanstack/react-store` の `useSelector` を `table.atoms.<slice>` と組み合わせて使います。

```tsx
import { useSelector } from '@tanstack/react-store'

function PaginationFooter({ table }) {
  // Re-renders only when pagination changes. Sorting, filtering, selection, etc. are all ignored.
  const pagination = useSelector(table.atoms.pagination)

  return <div>Page {pagination.pageIndex + 1}</div>
}
```

これが最も範囲の狭い購読方法です。`table.Subscribe` は `table.store.state` 全体から選択しますが、スライスごとのアトムを読む場合は、変更時に状態全体のスナップショットを組み立てる処理すら省けます。

> `table.atoms` **と** `table.Subscribe` **の使い分け:** どちらも再レンダーをきめ細かくできます。複数のスライスを1つの描画ブロックにまとめて渡したいときは `table.Subscribe` が便利です。コンポーネントが1つのスライスにしか関心がないときや、テーブル以外のコードに購読元を渡すときは `table.atoms.<slice>` が便利です。

### 外部アトム（応用） {#external-atoms-advanced}

応用的なパターン（複数のテーブルでスライスを共有する、アトムベースのライブラリと連携する、スライスを永続化の仕組みにつなぐなど）のために、Table V9 では新しい `atoms` オプションで書き込み可能なアトムを渡し、**状態のスライスを個別に自分で持つ**ことができます。[Basic External Atoms のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/basic-external-atoms)を参照してください。

```tsx
import { useCreateAtom, useSelector } from '@tanstack/react-store'
import {
  useTable,
  tableFeatures,
  rowSortingFeature,
  rowPaginationFeature,
  createSortedRowModel,
  createPaginatedRowModel,
  sortFns,
} from '@tanstack/react-table'
import type { PaginationState, SortingState } from '@tanstack/react-table'

const features = tableFeatures({ rowSortingFeature, rowPaginationFeature })

function MyTable({ data, columns }) {
  // Create stable external atoms for the slices you want to own.
  const sortingAtom = useCreateAtom<SortingState>([])
  const paginationAtom = useCreateAtom<PaginationState>({
    pageIndex: 0,
    pageSize: 10,
  })

  // Subscribe to each atom independently for fine-grained reactivity.
  const sorting = useSelector(sortingAtom)
  const pagination = useSelector(paginationAtom)

  const table = useTable({
    features,
    columns,
    data,
    // Per-slice external atoms. The library writes directly to these,
    // bypassing the internal baseAtoms for those slices.
    atoms: {
      sorting: sortingAtom,
      pagination: paginationAtom,
    },
  })

  // Table writes like table.setPageIndex(2) go straight to `paginationAtom`.
  // Any other subscriber of `paginationAtom` will see the update too.
  // ...
}
```

#### 外部アトムと `state`・`on*Change` の関係 {#how-external-atoms-interact-with-state-and-onchange}

あるスライスに外部アトムを登録すると、次のように動きます。

- **読み取り**: 派生した `table.atoms[slice]` も `table.store.state[slice]` も、あなたの外部アトムから読み取ります。
- **書き込み**: ライブラリによる書き込み（例: `table.setSorting(...)`、`column.toggleSorting()`）は、外部アトムの `set()` に直接届きます。対応する `onSortingChange` ハンドラーは**必要ありません**。アトムを持っていること自体が購読になるからです。
- **優先順位**: `options.atoms[key]` と `options.state[key]` の両方を渡した場合は、アトムが優先されます。どちらも渡さない場合、Table V9 は内部の `baseAtoms[key]`（Table V8 と同じく、テーブル自身が管理する状態）を使います。
- **リセット**: `table.reset()` は外部アトムを**クリアしません**。アトムを持っているのはあなたなので、いつリセットするかもあなたが決めます。必要なら `myAtom.set(defaultValue)` を自分で呼んでください。

#### 外部アトムと制御された状態の選び方 {#when-to-choose-external-atoms-vs-controlled-state}

| パターン                                                | 使いどころ                                                                                                                                                    |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 内部の状態（`state` も `atoms` も渡さない）             | いちばん簡単な方法です。テーブルがすべてを管理します。                                                                                                        |
| `state` + `on*Change`（Table V8 形式の制御された状態）  | フレームワークで一般的な状態（React の `useState`、シグナルなど）にスライスを持たせたいとき。                                                                 |
| `atoms` オプション                                      | React の状態とテーブルの間で状態を写し合う手間をかけずに、アトムベースの使い勝手（コンポーネントをまたいだ購読、`useSelector`、`useAtom`）を得たいとき。      |

---

## 機能ごとの破壊的変更 {#feature-by-feature-breaking-changes}

### ソート {#sorting}

ソート関連の API は、一貫性を持たせるために名前が変わりました。

| Table V8                          | Table V9                 |
| --------------------------------- | ------------------------ |
| `sortingFn`（列定義のオプション） | `sortFn`                 |
| `column.getSortingFn()`           | `column.getSortFn()`     |
| `column.getAutoSortingFn()`       | `column.getAutoSortFn()` |
| `SortingFn` 型                    | `SortFn` 型              |
| `SortingFns` インターフェース     | `SortFns` インターフェース |
| `sortingFns`（組み込み関数）      | `sortFns`                |

列定義を次のように更新してください。

```tsx
// Table V8
const columns = [
  {
    accessorKey: 'name',
    sortingFn: 'alphanumeric', // or custom function
  },
]

// Table V9
const columns = [
  {
    accessorKey: 'name',
    sortFn: 'alphanumeric', // or custom function
  },
]
```

### 列の固定 {#column-pinning}

V9 では、列の固定で使う用語が、V8 の物理的な `left`/`right` から論理的な `start`/`end` に変わりました。左から右へ書く（LTR）言語やレイアウトでは、通常 `start` が左、`end` が右に当たります。右から左へ書く（RTL）言語やレイアウトでは、通常 `start` が右、`end` が左に当たります。非推奨の別名は用意されていません。

| V8                                   | V9                                   |
| ------------------------------------ | ------------------------------------ |
| `columnPinning.left`                 | `columnPinning.start`                |
| `columnPinning.right`                | `columnPinning.end`                  |
| `column.pin('left')`                 | `column.pin('start')`                |
| `column.pin('right')`                | `column.pin('end')`                  |
| `column.getIsPinned() === 'left'`    | `column.getIsPinned() === 'start'`   |
| `column.getIsPinned() === 'right'`   | `column.getIsPinned() === 'end'`     |
| `row.getLeftVisibleCells()`          | `row.getStartVisibleCells()`         |
| `row.getRightVisibleCells()`         | `row.getEndVisibleCells()`           |
| `table.getLeftHeaderGroups()`        | `table.getStartHeaderGroups()`       |
| `table.getRightHeaderGroups()`       | `table.getEndHeaderGroups()`         |
| `table.getLeftLeafColumns()`         | `table.getStartLeafColumns()`        |
| `table.getRightLeafColumns()`        | `table.getEndLeafColumns()`          |
| `table.getLeftVisibleLeafColumns()`  | `table.getStartVisibleLeafColumns()` |
| `table.getRightVisibleLeafColumns()` | `table.getEndVisibleLeafColumns()`   |
| `table.getLeftTotalSize()`           | `table.getStartTotalSize()`          |
| `table.getRightTotalSize()`          | `table.getEndTotalSize()`            |
| `column.getStart('left')`            | `column.getStart('start')`           |
| `column.getAfter('right')`           | `column.getAfter('end')`             |
| `column.getIndex('left')`            | `column.getIndex('start')`           |
| `column.getIndex('right')`           | `column.getIndex('end')`             |

この名前の変更は、テーブルの論理的な領域を表すためのものです。DOM の書字方向を自動で扱うわけではありません。sticky による列の固定では、`insetInlineStart` や `insetInlineEnd` のような CSS の論理プロパティを使うのがおすすめです。テーブルオプション `columnResizeDirection` は変わっていません。

また、`enablePinning` オプションは別々のオプションに分かれました。

```tsx
// Table V8
enablePinning: true

// Table V9
enableColumnPinning: true
enableRowPinning: true
```

### 列幅と列幅の変更の分離 {#column-sizing-vs-column-resizing-split}

Table V8 では、列幅と列幅の変更が1つの機能にまとまっていました。Table V9 では、ツリーシェイキングを効きやすくするために別々の機能に分かれています。

| Table V8                          | Table V9                                        |
| --------------------------------- | ----------------------------------------------- |
| `ColumnSizing`（まとまった機能）  | `columnSizingFeature` + `columnResizingFeature` |
| `columnSizingInfo` 状態           | `columnResizing` 状態                           |
| `setColumnSizingInfo()`           | `setColumnResizing()`                           |
| `onColumnSizingInfoChange` オプション | `onColumnResizingChange` オプション         |

ユーザー操作による列幅の変更は不要で、列幅（固定の幅）だけが必要なら、`columnSizingFeature` だけをインポートすれば済みます。ドラッグで列幅を変える機能が必要なら、両方をインポートします。

```tsx
import {
  columnSizingFeature,
  columnResizingFeature,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnSizingFeature,
  columnResizingFeature, // Only if you need interactive resizing
})
```

### グループ化と集計 {#grouping-and-aggregation}

集計は列のグループ化から独立した、単独の機能になりました。`stockFeatures` には引き続き両方が含まれているので、これを使っているテーブルでは機能の登録を変える必要はありません。機能を明示的に宣言している場合は、列で `aggregationFn`、`aggregatedCell`、`getAggregationValue`、`cell.getIsAggregated` のいずれかを使うなら `rowAggregationFeature` を追加してください。`columnGroupingFeature` と `groupedRowModel` は、行のグループ化もするときだけ追加します。

```ts
const features = tableFeatures({
  rowAggregationFeature,
  columnGroupingFeature, // only for grouped rows
  groupedRowModel: createGroupedRowModel(),
  aggregationFns: { sum: aggregationFn_sum },
})
```

カスタムの集計関数は、呼び出し可能な関数から、コンテキストを受け取る定義の形に変わりました。

```ts
// Table V8/earlier V9 betas
const total = (columnId, leafRows, childRows) =>
  leafRows.reduce((sum, row) => sum + row.getValue(columnId), 0)

// Current V9
const total = constructAggregationFn({
  aggregate: ({ rows, getValue }) =>
    rows.reduce((sum, row) => sum + Number(getValue(row)), 0),
})
```

以前は関数ごとに `childRows` と `leafRows` のどちらを使うかを選んでいましたが、これは深さに応じて選ばれる1つの `context.rows` に置き換わりました。深さは列のオプション `maxAggregationDepth` で制御します。デフォルト（`0`）では、V8 と同じく直下の子のグループを集計します。末端の行を集計するには `Infinity` を指定します。

`column.getAggregationValue()` は、位置で指定する引数ではなく、1つのオプションオブジェクトを受け取るようになりました。

```ts
// Table V8/earlier V9 betas
column.getAggregationValue(rows, maxDepth)

// Current V9
column.getAggregationValue({ rows, maxDepth })
```

1つの列で複数の定義を実行できるようになったため、`column.getAggregationFn()` は `column.getAggregationFns()` になりました。また、呼び出し可能な関数を表していた従来の `AggregationFn`/`CreatedAggregationFn` 型は、`AggregationFnDef` に置き換わりました。

新しい機能の詳しい説明は、[グループ化ガイド](./grouping)と[集計ガイド](./aggregation)を参照してください。

### 行選択 {#row-selection}

> [!WARNING]
> **小さな破壊的変更:** `rowSelectionFeature` が有効な場合、`row.getToggleSelectedHandler()` はデフォルトで、両端を含む Shift による範囲選択を有効にするようになりました。このハンドラーにつないだ既存のチェックボックスや行は、通常の操作で起点（アンカー）を設定し、Shift を押しながらの操作で、現在の表示順での範囲を選択または選択解除します。`row.toggleSelected()` を直接呼ぶ場合の動きは変わりません。
>
> 以前の、範囲選択をしないハンドラーの動きを保ちたい場合は、`enableRowRangeSelection: false` を設定してください。ハンドラーには、Shift の状態を直接、または `nativeEvent` を通じて参照できるイベントを渡す必要があります。[Shift による範囲選択](./row-selection.md#shift-range-selection)を参照してください。

「一部の行が選択されている」かどうかの判定は、「少なくとも1行が選択されている」という意味に単純化されました。

| API                                 | Table V8                                            | Table V9                                      |
| ----------------------------------- | --------------------------------------------------- | --------------------------------------------- |
| `table.getIsSomeRowsSelected()`     | 一部の行が選択され、かつ全行は選択されていないときに `true` | 少なくとも1行が選択されているときに `true` |
| `table.getIsSomePageRowsSelected()` | ページ内の一部の行が選択され、かつページ内の全行は選択されていないときに `true` | ページ内で少なくとも1行が選択されているときに `true` |

Table V8 では、すべての行が選択されると `false` を返していました。Table V9 では `true` のままです。これらを使って「すべて選択」チェックボックスの中間状態（indeterminate）を切り替えている場合は、対応する「すべて選択済み」の判定と組み合わせ、全選択になったら中間状態が解除されるようにしてください。

`getIsSomeRowsSelected() && !getIsAllRowsSelected()`

### 行 API と内部 API の変更 {#row-and-internal-api-changes}

一部の行 API は、非公開から公開に変わりました。

| Table V8                                 | Table V9                               |
| ---------------------------------------- | -------------------------------------- |
| `row._getAllCellsByColumnId()`（非公開） | `row.getAllCellsByColumnId()`（公開）  |

`_` で始まるそれ以外の内部 API は、すべて削除されました。これらを使っていた場合は、対応する公開 API を使ってください。

- 削除: `table._getPinnedRows()`
- 削除: `table._getFacetedRowModel()`
- 削除: `table._getFacetedMinMaxValues()`
- 削除: `table._getFacetedUniqueValues()`

---

## 列ヘルパーの変更 {#column-helper-changes}

`createColumnHelper` 関数は、`TData` に加えて `TFeatures` 型パラメーターも必要になりました。

```tsx
// Table V8
import { createColumnHelper } from '@tanstack/react-table'

const columnHelper = createColumnHelper<Person>()

// Table V9
import {
  createColumnHelper,
  tableFeatures,
  rowSortingFeature,
} from '@tanstack/react-table'

const features = tableFeatures({ rowSortingFeature })
const columnHelper = createColumnHelper<typeof features, Person>()
```

### 新しいヘルパーメソッド `columns()` {#new-columns-helper-method}

Table V9 では、列の配列を包んで型推論を改善する `columns()` ヘルパーが加わりました。Table V8 では `TValue` が常に型安全とは限らず、特にグループ列では、入れ子になった列の型が失われたり広がったりすることがありました。`columns()` ヘルパーは可変長タプル型を使って列ごとの `TValue` 型を保つため、入れ子の構造全体を通して `info.getValue()` やセルの描画関数に正しい型が付きます。

```tsx
const columnHelper = createColumnHelper<typeof features, Person>()

// Wrap your columns array for better type inference
const columns = columnHelper.columns([
  columnHelper.accessor('firstName', {
    header: 'First Name',
    cell: (info) => info.getValue(),
  }),
  columnHelper.accessor('lastName', {
    id: 'lastName',
    header: () => <span>Last Name</span>,
    cell: (info) => <i>{info.getValue()}</i>,
  }),
  columnHelper.display({
    id: 'actions',
    header: 'Actions',
    cell: (info) => <button>Edit</button>,
  }),
])
```

---

## 描画の変更 {#rendering-changes}

### `flexRender` 関数 {#flexrender-function}

`flexRender` 関数は引き続き存在し、これまでと同じように動きます。

```tsx
import { flexRender } from '@tanstack/react-table'

// Still works in Table V9
flexRender(cell.column.columnDef.cell, cell.getContext())
flexRender(header.column.columnDef.header, header.getContext())
```

### 新しい `FlexRender` コンポーネントと `<table.FlexRender />` コンポーネント {#new-flexrender-and-tableflexrender--component}

Table V9 では、テーブルインスタンスに付いた、より簡潔なコンポーネントベースの方法が加わりました。

```tsx
const table = useTable({ /* ... */ })

// Instead of:
{flexRender(header.column.columnDef.header, header.getContext())}

// You can use:
<table.FlexRender header={header} />
<table.FlexRender cell={cell} />
<table.FlexRender footer={footer} />
// or
import { FlexRender } from '@tanstack/react-table'
<FlexRender header={header} />
<FlexRender cell={cell} />
<FlexRender footer={footer} />
```

従来の `flexRender` 関数よりも、ずっと使いやすくなっているはずです！

---

## ユーティリティ `tableOptions()` {#the-tableoptions-utility}

`tableOptions()` ヘルパーを使うと、テーブルオプションを型安全に組み立てられます。テーブルの設定にスプレッド構文で展開できる、再利用可能な部分的な設定を作るのに便利です。

### 基本的な使い方 {#basic-usage}

```tsx
import {
  tableOptions,
  tableFeatures,
  rowSortingFeature,
} from '@tanstack/react-table'

const features = tableFeatures({ rowSortingFeature })

// Create a reusable options object with features pre-configured
const baseOptions = tableOptions({
  features,
  debugTable: process.env.NODE_ENV === 'development',
})

// Use in your table; columns, data, and other options can be added
const table = useTable({
  ...baseOptions,
  columns,
  data,
})
```

### 部分的なオプションを組み合わせる {#composing-partial-options}

`tableOptions()` を使えば、部分的な設定を作るときに必須のフィールド（`data`、`columns`、`features` など）を省略できます。

```tsx
// Row model factories and fns registries are registered on the features object
const features = tableFeatures({
  rowSortingFeature,
  columnFilteringFeature,
  sortedRowModel: createSortedRowModel(),
  filteredRowModel: createFilteredRowModel(),
  sortFns,
  filterFns,
})

// Partial options without data or columns
const featureOptions = tableOptions({
  features,
  getRowId: (row) => row.id,
  manualPagination: true,
  manualSorting: true,
  manualFiltering: true,
})

// Another partial without features (inherits from spread)
const paginationDefaults = tableOptions({
  initialState: {
    pagination: { pageIndex: 0, pageSize: 25 },
  },
})

// Combine them
const table = useTable({
  ...featureOptions,
  ...paginationDefaults,
  columns,
  data,
})
```

### `createTableHook` と組み合わせる {#using-with-createtablehook}

`tableOptions()` は、組み立て可能なテーブルのファクトリーを作る `createTableHook` と相性がよいです。

```tsx
const features = tableFeatures({
  rowSortingFeature,
  rowPaginationFeature,
  sortedRowModel: createSortedRowModel(),
  paginatedRowModel: createPaginatedRowModel(),
  sortFns,
})

const sharedOptions = tableOptions({ features })

const { useAppTable } = createTableHook(sharedOptions)
```

---

## `createTableHook`: 組み立て可能なテーブルのパターン {#createtablehook-composable-table-patterns}

**これは応用的で、使うかどうかは任意の機能です。** `createTableHook` を使う必要はなく、ほとんどの用途では `useTable` で十分です。[TanStack Form](https://tanstack.com/form) の `createFormHook` を知っているなら、`createTableHook` もほぼ同じように動きます。設定をあらかじめ結び付けたカスタムフックを作り、それを多くのテーブルで使い回せます。

同じ設定を共有するテーブルが複数あるアプリケーションでは、`createTableHook` を使うと、機能（行モデルのファクトリーを含む）と再利用するコンポーネントを一度だけ定義すれば済みます。

```tsx
// hooks/table.ts
import {
  createTableHook,
  tableFeatures,
  columnFilteringFeature,
  rowSortingFeature,
  rowPaginationFeature,
  createFilteredRowModel,
  createSortedRowModel,
  createPaginatedRowModel,
  filterFns,
  sortFns,
} from '@tanstack/react-table'

// Import your reusable components
import { PaginationControls, SortIndicator, TextCell } from './components'

// Features and row model factories defined once
const features = tableFeatures({
  columnFilteringFeature,
  rowSortingFeature,
  rowPaginationFeature,
  filteredRowModel: createFilteredRowModel(),
  sortedRowModel: createSortedRowModel(),
  paginatedRowModel: createPaginatedRowModel(),
  filterFns,
  sortFns,
})

export const {
  useAppTable,
  createAppColumnHelper,
  useTableContext,
  useCellContext,
  useHeaderContext,
} = createTableHook({
  features,

  // Default table options
  debugTable: process.env.NODE_ENV === 'development',

  // Register reusable components
  tableComponents: { PaginationControls },
  cellComponents: { TextCell },
  headerComponents: { SortIndicator },
})
```

### `useAppTable` を使う {#using-useapptable}

```tsx
// features/users.tsx
import { useAppTable, createAppColumnHelper } from './hooks/table'

const columnHelper = createAppColumnHelper<Person>()

const columns = columnHelper.columns([
  columnHelper.accessor('firstName', {
    header: 'First Name',
    cell: ({ cell }) => <cell.TextCell />, // Pre-bound component!
  }),
])

function UsersTable({ data }: { data: Person[] }) {
  const table = useAppTable({
    columns,
    data,
    // features (including row model factories) already configured!
  })

  return (
    <table.AppTable>
      <table>
        <thead>
          {table.getHeaderGroups().map((headerGroup) => (
            <tr key={headerGroup.id}>
              {headerGroup.headers.map((h) => (
                <table.AppHeader header={h} key={h.id}>
                  {(header) => (
                    <th>
                      <header.FlexRender />
                      <header.SortIndicator />
                    </th>
                  )}
                </table.AppHeader>
              ))}
            </tr>
          ))}
        </thead>
        <tbody>
          {table.getRowModel().rows.map((row) => (
            <tr key={row.id}>
              {row.getAllCells().map((c) => (
                <table.AppCell cell={c} key={c.id}>
                  {(cell) => (
                    <td>
                      <cell.FlexRender />
                    </td>
                  )}
                </table.AppCell>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
      <table.PaginationControls />
    </table.AppTable>
  )
}
```

### コンポーネント向けのコンテキストフック {#context-hooks-for-components}

`createTableHook` で登録したコンポーネントは、自分のコンテキストにアクセスできます。

```tsx
// components/SortIndicator.tsx
import { useHeaderContext } from './hooks/table'

export function SortIndicator() {
  const header = useHeaderContext()
  const sorted = header.column.getIsSorted()

  if (!sorted) return null
  return sorted === 'asc' ? ' 🔼' : ' 🔽'
}

// components/TextCell.tsx
import { useCellContext } from './hooks/table'

export function TextCell() {
  const cell = useCellContext()
  return <span>{cell.getValue() as string}</span>
}

// components/PaginationControls.tsx
import { useTableContext } from './hooks/table'

export function PaginationControls() {
  const table = useTableContext()

  return (
    <table.Subscribe selector={(s) => s.pagination}>
      {(pagination) => (
        <div>
          <button onClick={() => table.previousPage()}>Previous</button>
          <span>Page {pagination.pageIndex + 1}</span>
          <button onClick={() => table.nextPage()}>Next</button>
        </div>
      )}
    </table.Subscribe>
  )
}
```

---

## TypeScript の変更のまとめ {#typescript-changes-summary}

### 型のジェネリクス {#type-generics}

ほとんどの型で `TFeatures` パラメーターが必要になりました。

```tsx
// Table V8
type Column<TData>
type ColumnDef<TData>
type Table<TData>
type Row<TData>
type Cell<TData, TValue>

// Table V9
type Column<TFeatures, TData, TValue>
type ColumnDef<TFeatures, TData, TValue>
type Table<TFeatures, TData>
type Row<TFeatures, TData>
type Cell<TFeatures, TData, TValue>
```

### `typeof features` を使う {#using-typeof-features}

`TFeatures` 型を得るいちばん簡単な方法は `typeof` を使うことです。

```tsx
const features = tableFeatures({
  rowSortingFeature,
  columnFilteringFeature,
})

// Use typeof to get the type
type MyFeatures = typeof features

const columns: ColumnDef<typeof features, Person>[] = [...]

function Filter({ column }: { column: Column<typeof features, Person, unknown> }) {
  // ...
}
```

### `StockFeatures` を使う {#using-stockfeatures}

`useTable` で `stockFeatures` を使う場合は、`StockFeatures` 型を使います。

```tsx
import type { StockFeatures, ColumnDef } from '@tanstack/react-table'

const columns: ColumnDef<StockFeatures, Person>[] = [...]
```

### `TableMeta`/`ColumnMeta` の型付けの変更 {#tablemetacolumnmeta-typing-changes}

宣言のマージはもう必要ありません！（使い続けたい場合は、引き続き使えます）

`TableMeta` や `ColumnMeta` を拡張するためのグローバルな宣言のマージは、Table V8 とまったく同じように動きます。必要な変更はジェネリクスの形を更新することだけです。どちらのインターフェースも、最初の型パラメーターとして `TFeatures` を受け取るようになりました。

```tsx
// Table V8
declare module '@tanstack/react-table' {
  interface ColumnMeta<TData, TValue> {
    customProperty: string
  }
}

// Table V9 - TFeatures is now the first parameter
declare module '@tanstack/react-table' {
  interface ColumnMeta<TFeatures, TData, TValue> {
    customProperty: string
  }
}
```

meta の型をこれまでどおりグローバルに宣言し続けたい場合は、これだけで済みます。

さらに Table V9 では、宣言のマージを使わずに meta の型を**テーブルごとに**宣言する新しい方法も選べます。`features` オプションで型専用の `tableMeta`/`columnMeta` スロットを使うと、その `features` オブジェクトで作ったテーブルにだけ影響します。

```tsx
const features = tableFeatures({
  rowSortingFeature,
  columnMeta: metaHelper<{ customProperty: string }>(),
})
```

両方の方法について詳しくは、新しい[テーブルと列の meta ガイド](../../../guide/table-and-column-meta)を参照してください。

### `FilterFns`/`SortFns`/`AggregationFns`/`FilterMeta` の拡張はレジストリのスロットに置き換え {#filterfnssortfnsaggregationfnsfiltermeta-augmentation-replaced-by-registry-slots}

Table V8 では、カスタム関数を文字列で参照できるようにする（`filterFn: 'fuzzy'` のように）には、`declare module` で `FilterFns` インターフェースを拡張する必要がありました。フィルターの meta に型を付けるには、`FilterMeta` の拡張も必要でした。Table V9 では、対応するレジストリのスロットに関数を登録するだけで、グローバルな拡張なしにその両方を済ませられます。

```tsx
// Table V8
declare module '@tanstack/react-table' {
  interface FilterFns {
    fuzzy: FilterFn<unknown>
  }
  interface FilterMeta {
    itemRank: RankingInfo
  }
}

// Table V9 - register in the slot; the key becomes a valid string value
interface FuzzyFilterMeta {
  itemRank?: RankingInfo
}

const features = tableFeatures({
  columnFilteringFeature,
  filteredRowModel: createFilteredRowModel(),
  filterFns: { fuzzy: fuzzyFilter },
  filterMeta: metaHelper<FuzzyFilterMeta>(),
})

// 'fuzzy' now typechecks in column defs for tables using these features
columnHelper.accessor('name', { filterFn: 'fuzzy' })
```

同じパターンは、`sortFns`（`sortFn` の文字列値用）と `aggregationFns`（`aggregationFn` の文字列値用）にも当てはまります。完全な例は[あいまい検索フィルターガイド](./fuzzy-filtering.md)を参照してください。

### `RowData` 型の制限 {#rowdata-type-restriction}

`RowData` 型の制約が厳しくなりました。

```tsx
// Table V8 - very permissive
type RowData = unknown

// Table V9 - must be a record or array
type RowData = Record<string, any> | Array<any>
```

この変更で型安全性が高まります。珍しいデータ型を渡していた場合は、データが `Record<string, any>` または `Array<any>` に合っているか確認してください。

---

## 移行チェックリスト {#migration-checklist}

- [ ] インポートを更新する: `useReactTable` → `useTable`
- [ ] `tableFeatures()` で `features` を定義する（または `stockFeatures` を使う）
- [ ] `get*RowModel()` オプションを `tableFeatures` のスロットに移す（例: `filteredRowModel: createFilteredRowModel()`）
- [ ] `filterFns` / `sortFns` / `aggregationFns` のレジストリを `tableFeatures` のスロットとして登録する（行モデルのファクトリーは引数を取らなくなった）
- [ ] 分割代入で取り出した行・セル・列・ヘッダーのメソッドを、インスタンスからの呼び出しに置き換える（例: `row.getValue('name')`）
- [ ] 列定義の `sortingFn` を `sortFn` に名前変更する
- [ ] 列の固定を `start`/`end` の用語に更新する（`columnPinning.start`、`column.pin('end')`、`getStart*`/`getEnd*` の API）
- [ ] `enablePinning` を使っている場合は、`enableColumnPinning`/`enableRowPinning` に置き換える
- [ ] 状態 `columnSizingInfo` を `columnResizing` に名前変更する（関連するオプションも）
- [ ] 呼び出し可能なカスタム集計関数を、`constructAggregationFn({ aggregate, merge? })` による定義に変換する
- [ ] 状態へのアクセスを更新する: `table.getState()` → `table.store.state` または `table.state`
- [ ] TypeScript の型に `TFeatures` ジェネリクスを加える
- [ ] `createColumnHelper<TData>()` を `createColumnHelper<TFeatures, TData>()` に更新する
- [ ] `TableMeta`/`ColumnMeta` の宣言のマージを使っている場合は、拡張に `TFeatures` ジェネリクスを加える（テーブルごとの `tableMeta`/`columnMeta` の機能スロットに切り替えてもよい）
- [ ] `FilterFns`/`SortFns`/`AggregationFns` の `declare module` による拡張をレジストリのスロットへの登録に、`FilterMeta` の拡張を `filterMeta` スロットに置き換える
- [ ] （任意）描画を最適化するために `table.Subscribe` を加える
- [ ] （任意）再レンダーを最小限にするために、`table.atoms.<slice>` + `useSelector` で個々のスライスを購読する
- [ ] （任意）新しい `atoms` オプションで書き込み可能なアトムを渡し、特定の状態のスライスを外部で管理する
- [ ] （任意）組み立て可能な設定のために `tableOptions()` を使う
- [ ] （任意）再利用できるテーブルのパターンのために `createTableHook` に移行する

---

## サンプル {#examples}

Table V9 のパターンが実際に動く様子は、次のサンプルで確認できます。

- [Basic useTable](https://tanstack.com/table/latest/docs/framework/react/examples/basic-use-table) - 新しい `useTable` フックを使ったシンプルなテーブル
- [Basic useLegacyTable](https://tanstack.com/table/latest/docs/framework/react/examples/basic-use-legacy-table) - `useLegacyTable` を使った移行の例
- [Basic useAppTable](https://tanstack.com/table/latest/docs/framework/react/examples/basic-use-app-table) - `createTableHook` の使用例
- [Basic External State](https://tanstack.com/table/latest/docs/framework/react/examples/basic-external-state) - 従来どおりの `state` + `on*Change` による制御された状態
- [Basic External Atoms](https://tanstack.com/table/latest/docs/framework/react/examples/basic-external-atoms) - `useCreateAtom` と `atoms` オプションで状態のスライスを持つ例
- [Filters](https://tanstack.com/table/latest/docs/framework/react/examples/filters) - 新しい API によるフィルタリング
- [Sorting](https://tanstack.com/table/latest/docs/framework/react/examples/sorting) - 新しい API によるソート
- [組み立て可能なテーブル](https://tanstack.com/table/latest/docs/framework/react/examples/composable-tables) - `createTableHook` の応用パターン
- [Kitchen Sink](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink) - すべての機能を組み合わせた例
