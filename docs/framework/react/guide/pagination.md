---
title: ページネーション（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React のサンプルを参照してください。

- [ページネーション](https://tanstack.com/table/latest/docs/framework/react/examples/pagination)

### ページネーションのセットアップ {#pagination-setup}

ページネーションの機能を使うためのテーブルのセットアップ方法は次のとおりです。ページネーションの機能を追加すると、関連する API が使えるようになります。クライアントサイドでページネーションする場合は、その機能の後ろに `paginatedRowModel` も設定してください。行モデルのスロットは型チェックされるためです。

```tsx
import {
  useTable,
  tableFeatures,
  rowPaginationFeature,
  createPaginatedRowModel,
} from '@tanstack/react-table'

const features = tableFeatures({
  rowPaginationFeature,
  paginatedRowModel: createPaginatedRowModel(), // if using client-side pagination
  // manualPagination: true, // if using manual server-side pagination
})

const table = useTable({
  features,
  columns,
  data,
})
```

## ページネーション（React）ガイド {#pagination-react-guide}

TanStack Table は、クライアントサイドとサーバーサイドのどちらのページネーションも十分にサポートしています。このガイドでは、テーブルにページネーションを実装するさまざまな方法を順に説明します。

### クライアントサイドのページネーション {#client-side-pagination}

クライアントサイドのページネーションを使うとは、取得する `data` にテーブルの行が**_すべて_**含まれ、テーブルインスタンスがフロントエンドでページネーションの処理を行うということです。

#### クライアントサイドのページネーションを使うべきか {#should-you-use-client-side-pagination}

ブラウザーがデータセット全体を取得して保持できるなら、たいていはクライアントサイドのページネーションがいちばん簡単です。データセット全体の問い合わせ・転送・ブラウザーでの保持にコストがかかりすぎる場合は、サーバーサイドのページネーションを使います。

行数だけで境目が決まるわけではありません。判断の枠組み全体、パフォーマンスの要因、フィルタリングやソートをページネーションと整合させる方法については、[クライアントサイドとサーバーサイドのガイド](../../../guide/client-side-vs-server-side)を参照してください。

#### 代わりに仮想化を使うべきか {#should-you-use-virtualization-instead}

仮想化（ウィンドウイングとも呼ばれます）は、見えている行だけをマウントすることでレンダーの負荷を減らします。ただし、仮想化したデータはブラウザー内に存在したままです。クライアントサイドやサーバーサイドのページネーションを補うことはできますが、データセット全体が大きすぎて読み込めない場合に、サーバーサイドでの処理の代わりになるものではありません。

この違いについては[クライアントサイドとサーバーサイドのガイド](../../../guide/client-side-vs-server-side#rendering-is-a-separate-decision)を、仮想化の API については [TanStack Virtual](https://tanstack.com/virtual/latest) を参照してください。

#### ページネーション行モデル {#pagination-row-model}

TanStack Table に組み込まれたクライアントサイドのページネーションを使いたい場合は、`rowPaginationFeature` と `paginatedRowModel` のファクトリーを features に追加します。

```tsx
import {
  useTable,
  tableFeatures,
  rowPaginationFeature,
  createPaginatedRowModel,
} from '@tanstack/react-table'

const features = tableFeatures({
  rowPaginationFeature,
  paginatedRowModel: createPaginatedRowModel(),
})

const table = useTable({
  features,
  columns,
  data,
})
```

### 手動のサーバーサイドのページネーション {#manual-server-side-pagination}

サーバーサイドのページネーションを使うと決めた場合は、次のように実装できます。

サーバーサイドのページネーションには、ページネーション行モデルは必要ありません。ただし、共有コンポーネントの中で、行モデルを必要とするほかのテーブルのためにそれを渡している場合でも、`manualPagination` オプションを `true` にすればクライアントサイドのページネーションを無効にできます。`manualPagination` を `true` にすると、テーブルインスタンスは内部で `table.getPrePaginatedRowModel` の行モデルを使うようになり、渡された `data` がすでにページ分割済みであるとみなします。

#### ページ数と行数 {#page-count-and-row-count}

バックエンドに全部で何行・何ページあるかは、教えない限りテーブルインスタンスには分かりません。テーブルオプションの `rowCount` か `pageCount` のどちらかを渡して、全部で何ページあるかをテーブルインスタンスに伝えてください。`rowCount` を渡した場合、テーブルインスタンスは `rowCount` と `pageSize` から内部で `pageCount` を計算します。`pageCount` がすでに分かっているなら、直接渡してもかまいません。ページ数が分からない場合は、`pageCount` に `-1` を渡します。このとき、テーブルは終端を検出できないため `getCanNextPage()` は `true` を返し、`getCanPreviousPage()` は現在の `pageIndex` によって決まり、有限の最終ページが分からないため `getCanLastPage()` は `false` を返します。

```tsx
import {
  useTable,
  tableFeatures,
  rowPaginationFeature,
} from '@tanstack/react-table'

const features = tableFeatures({ rowPaginationFeature })

const table = useTable({
  features,
  columns,
  data,
  manualPagination: true, // turn off client-side pagination
  rowCount: dataQuery.data?.rowCount, // pass in the total row count so the table knows how many pages there are (pageCount calculated internally if not provided)
  // pageCount: dataQuery.data?.pageCount, // alternatively directly pass in pageCount instead of rowCount
})
```

> [!NOTE]
> `manualPagination` オプションを `true` にすると、テーブルインスタンスは渡された `data` がすでにページ分割済みであるとみなします。

#### TanStack Query を使う {#using-tanstack-query}

リクエストのライフサイクルは TanStack Query に任せ、制御されたページネーションの状態は TanStack Table が受け持つ、という分担ができます。下の2つのパターンをどちらも含む完全なサンプルとして、[TanStack Query との組み合わせのサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/with-tanstack-query)を参照してください。

##### `useQuery` を使ったページ番号方式のページネーション {#page-index-pagination-with-usequery}

ページネーションの状態をクエリキーに含め、要求された行と合計の `rowCount` を返し、その両方をテーブルに渡します。

```tsx
const dataQuery = useQuery({
  queryKey: ['people', 'offset', pagination, sorting, globalFilter],
  queryFn: () => fetchPeople({ pagination, sorting, globalFilter }),
  placeholderData: keepPreviousData,
})

const table = useTable(
  {
    features,
    columns,
    data: dataQuery.data?.rows ?? [],
    rowCount: dataQuery.data?.rowCount,
    state: { pagination, sorting, globalFilter },
    onPaginationChange: setPagination,
    manualPagination: true,
    manualSorting: true,
    manualFiltering: true,
  },
  (state) => state,
)
```

合計の行数が分かっているので、ページ数の表示、ページ番号による移動、`lastPage()` が使えます。

##### `useInfiniteQuery` を使ったカーソル方式のページネーション {#cursor-based-pagination-with-useinfinitequery}

カーソル方式の API は通常、現在の行、中身を解釈しない前提の `nextCursor`、次のページがあるかどうかを返します。ID が一意で、サーバー側の並び順が安定しているなら、最後の行の ID をカーソルにできます。

```tsx
const dataQuery = useInfiniteQuery({
  queryKey: ['people', 'cursor', pagination.pageSize, sorting, globalFilter],
  queryFn: ({ pageParam }) =>
    fetchPeople({
      cursor: pageParam,
      pageSize: pagination.pageSize,
      sorting,
      globalFilter,
    }),
  initialPageParam: null,
  getNextPageParam: (lastPage) => lastPage.nextCursor,
})

const currentPage = dataQuery.data?.pages[pagination.pageIndex]
const hasCachedNextPage = Boolean(
  dataQuery.data?.pages[pagination.pageIndex + 1],
)
const canNextPage = hasCachedNextPage || Boolean(currentPage?.hasNextPage)

const table = useTable(
  {
    features,
    columns,
    data: currentPage?.rows ?? [],
    pageCount: -1, // the cursor API does not expose a total
    state: { pagination, sorting, globalFilter },
    onPaginationChange: setPagination,
    manualPagination: true,
    manualSorting: true,
    manualFiltering: true,
  },
  (state) => state,
)

async function goToNextPage() {
  const nextPageIndex = pagination.pageIndex + 1

  if (!dataQuery.data?.pages[nextPageIndex]) {
    const result = await dataQuery.fetchNextPage()
    if (!result.data?.pages[nextPageIndex]) return
  }

  table.nextPage()
}
```

「次へ」ボタンには `canNextPage` を使ってください。`pageCount` が `-1` のとき、`getCanNextPage()` は終端に達したかどうかを判断できないためです。取得済みのページは残るので、前のページに戻れます。カーソル方式の API では最終ページが分からないため、`getCanLastPage()` は `false` を返します。「最後へ」ボタンは無効のままにしておきましょう。ソート・フィルタリング・ページサイズが変わったら、新しいクエリが最初のカーソルから始まるように、`pageIndex` を `0` に戻してください。

### ページネーションの状態 {#pagination-state}

クライアントサイドのページネーションと手動のサーバーサイドのページネーションのどちらを使っていても、組み込みの `pagination` の状態と API を使えます。

`pagination` の状態は、次のプロパティを持つオブジェクトです。

- `pageIndex`: 現在のページ番号（0 始まり）。
- `pageSize`: 現在のページサイズ。

UI の再レンダーにつなげたいリアクティブな読み取りには、`table.state.pagination` を使います。イベントハンドラーの中では `table.atoms.pagination.get()` で現在のスナップショットを読み取れますが、この読み取りでは、コンポーネントがその後の変更を購読することにはなりません。

テーブルの外で `pagination` の状態にアクセスする必要がある場合（よくあるのはサーバーサイドのクエリキーです）は、そのスライスを自分で管理できます。v9 で推奨する方法は、テーブルオプション `atoms` で外部のアトムを渡すことです。アトムを使うと細かい粒度の購読が保たれ、テーブルを持つコンポーネントを再レンダーさせることなく、ページネーションの値をクエリキーに使えます。

```tsx
import { useCreateAtom, useSelector } from '@tanstack/react-store'
import {
  useTable,
  tableFeatures,
  rowPaginationFeature,
  createPaginatedRowModel,
  type PaginationState,
} from '@tanstack/react-table'

const features = tableFeatures({ rowPaginationFeature })

const paginationAtom = useCreateAtom<PaginationState>({
  pageIndex: 0, // initial page index
  pageSize: 10, // default page size
})

// subscribe to the atom wherever you need the value (e.g. for a query key)
const pagination = useSelector(paginationAtom)

const table = useTable({
  features,
  columns,
  data,
  atoms: {
    pagination: paginationAtom, // table pagination APIs now update paginationAtom
  },
})
```

あるいは、v8 スタイルの `state.pagination` と `onPaginationChange` を組み合わせるパターンも引き続き使えます。単純な連携や v8 のコードを移行するときには便利ですが、外部のアトムに比べると粒度が粗くなります。詳しい比較は[テーブルの状態ガイド](./table-state)を参照してください。

```tsx
const [pagination, setPagination] = useState<PaginationState>({
  pageIndex: 0, // initial page index
  pageSize: 10, // default page size
})

const table = useTable({
  features,
  columns,
  data,
  onPaginationChange: setPagination,
  state: {
    pagination,
  },
})
```

また、`pagination` の状態を自分のスコープで管理する必要はないものの、`pageIndex` と `pageSize` に別の初期値を設定したい場合は、`initialState` オプションを使えます。

```tsx
const table = useTable({
  features,
  columns,
  data,
  initialState: {
    pagination: {
      pageIndex: 2, // custom initial page index
      pageSize: 25, // custom default page size
    },
  },
})
```

> [!NOTE]
> `pagination` のスライスを、`atoms`・`state`・`initialState` の複数のオプションに**渡さないでください**。制御された値（`atoms` または `state`）が `initialState` を上書きします。どれか1つだけを使ってください。

### ページネーションのオプション {#pagination-options}

手動のサーバーサイドのページネーションで役立つ `manualPagination`・`pageCount`・`rowCount` の各オプション（[前述](#manual-server-side-pagination)）のほかに、知っておくと役立つテーブルオプションがもう1つあります。

#### ページ番号の自動リセット {#auto-reset-page-index}

初期設定では、`data` の更新、フィルターの変更、ソートの変更、グループ化の変更などでクライアントサイドの行モデルが再計算されるたびに、`pageIndex` が `0` に戻ります。この動作は `manualPagination` が `true` のときは自動的に無効になりますが、テーブルオプション `autoResetPageIndex` に真偽値を明示的に指定すれば上書きできます。すべての自動リセットをまとめて無効（または有効）にする、全体用のテーブルオプション `autoResetAll` もあります。

> [!NOTE]
> 自動リセットが実行されるのは、リセットのきっかけになるクライアントサイドの行モデルが含まれていて、それが再計算されたときだけです。手動のサーバーサイドのテーブルで、フィルタリング・ソート・グループ化などの該当する行モデルを省いている場合、その制御された状態を変えてもページ番号はリセットされません。`autoResetPageIndex` や `autoResetAll` が `true` でも同じです。対応する変更ハンドラーの中で、`pageIndex` を自分でリセットしてください。

```tsx
const table = useTable({
  features,
  columns,
  data,
  autoResetPageIndex: false, // turn off auto reset of pageIndex
  // autoResetAll: false, // or turn off all auto resets at once
})
```

`autoResetPageIndex: false` を設定するよくある理由は、テーブルを表示したままデータを編集するケース（セルのインライン編集など）です。編集のたびに `data` が更新されて行モデルが再計算されるため、そのままではユーザーが最初のページに引き戻されてしまいます。このオプションを固定値の `false` にしておけば、行モデルが再計算されても現在のページが保たれます。展開の機能も使っている場合は、編集で展開した行が折りたたまれないように、`autoResetExpanded: false` も併せて設定してください。

ただし、`autoResetPageIndex` を無効にした場合は、空のページが表示されないように、`pageIndex` を自分でリセットする処理を追加する必要があるかもしれません。

### ページネーションの API {#pagination-apis}

テーブルインスタンスには、ページネーションの UI コンポーネントをつなぎ込むのに役立つ API がいくつかあります。

#### ページネーションのボタン用 API {#pagination-button-apis}

- `getCanPreviousPage`: 最初のページにいるときに「前のページ」ボタンを無効にするのに使います。
- `getCanNextPage`: これ以上ページがないときに「次のページ」ボタンを無効にするのに使います。
- `getCanLastPage`: 有限の最終ページが分からないときに「最後のページ」ボタンを無効にするのに使います。
- `previousPage`: 前のページに移動するのに使います。（ボタンのクリックハンドラー）
- `nextPage`: 次のページに移動するのに使います。（ボタンのクリックハンドラー）
- `firstPage`: 最初のページに移動するのに使います。（ボタンのクリックハンドラー）
- `lastPage`: 最後のページに移動するのに使います。（ボタンのクリックハンドラー）
- `setPageIndex`: 「指定ページへ移動」の入力欄に使います。
- `resetPageIndex`: テーブルの状態を元のページ番号に戻すのに使います。
- `setPageSize`: 「ページサイズ」の入力欄やセレクトボックスに使います。
- `resetPageSize`: テーブルの状態を元のページサイズに戻すのに使います。
- `setPagination`: ページネーションの状態をまとめて設定するのに使います。
- `resetPagination`: テーブルの状態を元のページネーションの状態に戻すのに使います。

> [!NOTE]
> これらのページネーションの API は、`rowPaginationFeature` を使っているときに利用できます。

```tsx
<Button
  onClick={() => table.firstPage()}
  disabled={!table.getCanPreviousPage()}
>
  {'<<'}
</Button>
<Button
  onClick={() => table.previousPage()}
  disabled={!table.getCanPreviousPage()}
>
  {'<'}
</Button>
<Button
  onClick={() => table.nextPage()}
  disabled={!table.getCanNextPage()}
>
  {'>'}
</Button>
<Button
  onClick={() => table.lastPage()}
  disabled={!table.getCanLastPage()}
>
  {'>>'}
</Button>
<select
  value={table.state.pagination.pageSize}
  onChange={e => {
    table.setPageSize(Number(e.target.value))
  }}
>
  {[10, 20, 30, 40, 50].map(pageSize => (
    <option key={pageSize} value={pageSize}>
      {pageSize}
    </option>
  ))}
</select>
```

#### ページネーションの情報用 API {#pagination-info-apis}

- `getPageCount`: 総ページ数を表示するのに使います。
- `getRowCount`: 総行数を表示するのに使います。
