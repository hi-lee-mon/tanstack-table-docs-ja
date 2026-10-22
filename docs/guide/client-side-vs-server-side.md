---
title: クライアントサイドとサーバーサイドのガイド
---

## サンプル {#examples}

- [TanStack Query との組み合わせ](https://tanstack.com/table/latest/docs/framework/react/examples/with-tanstack-query)


> [!IMPORTANT]
> TanStack Table は、クライアントサイドとサーバーサイドのどちらの行処理にも対応しています。

もう少し正確に言うと、TanStack Table では、フィルタリング、グループ化、ソート、展開、集計、ファセット、ページネーションといった機能のデータ処理を、自前のバックエンドやそのほかの手動の方法で行えます。

TanStack Table は、クライアントサイドの[行モデル](./row-models)による処理で、ブラウザー上で行のフィルタリング、グループ化、ソート、展開、集計、ファセット、ページネーションを行えます。また、実際のデータ処理はサーバーに任せ、それらの機能の状態の管理だけを受け持つこともできます。どちらが適しているかは、ブラウザーが受け取るデータの量、そのデータの転送と処理にかかるコスト、提供したい体験によって決まります。

どちらを選ぶにしても、基本的にはどちらか一方に決める必要があります。機能ごとにクライアントサイドとサーバーサイドの行処理を混ぜて使うことは、実際にはほぼできません。このガイドでは、すべての機能に共通するこの判断について説明します。各機能を実装するためのオプションや行モデルは、機能ごとのガイドで説明しています。

## 要件に合ういちばん単純な方法から始める {#start-with-the-simplest-approach-that-fits}

通常、いちばん単純なのはクライアントサイドでの処理です。これは、処理を TanStack Table に任せる方法です。テーブル用のデータセットを丸ごと取得して TanStack Table に渡し、必要な行モデルを有効にします。そうすれば、フィルタリング、ソート、ページネーションは、追加のリクエストなしですぐに反映されます。

データセットが大きいと思うと、クライアントサイドでの処理を候補から外したくなるかもしれません。しかし、数千行程度のテーブルなら、ブラウザーで十分に扱えることがよくあります。TanStack Table のサンプルでは、もっと大きなデータセットで負荷試験をしています。実際、TanStack Table のすべての機能は、クライアントサイドの 100 万行で負荷試験をしており、実用的な性能が出ることを想定しています。実際の性能は、列の数、各行の大きさと形、アクセサーや機能の関数が行う処理の量、ユーザーが使う端末によって変わります。実際に近いデータと、想定する端末で試してください。

以前のバージョンの TanStack Table では、100 万行あたりでメモリの問題が出始めていました。しかし[オブジェクトのプロトタイプを使うリファクタリング](https://tanstack.com//blog/tanstack-table-v9-memory-performance)によって、今ではクライアントサイドで最大 1500 万行まで余裕をもって扱えると言えるようになりました。あなたのユースケースで 1500 万行を読み込むのが現実的でしょうか。おそらく違うでしょう。それでも、TanStack Table がクライアントサイドで多くの行を扱う余力を持っていることは知っておいてください。

通常、次のような場合はサーバーサイドでの処理のほうが適しています。

- データセットを丸ごと取得すると、時間やコストがかかりすぎる、またはメモリを大量に使う。
- ブラウザーが受け取るのは、1ページ分などの行の一部だけである。
- クエリ、権限、ビジネスルールをバックエンドで強制する必要がある。
- データの更新が頻繁で、全件をダウンロードしてもすぐに古くなってしまう。
- バックエンドのほうが、インデックスを使った検索、ソート、グループ化、集計を効率よく行える。

トレードオフを評価するときは、次のことを測ってください。

1. サーバーがデータセット全体を問い合わせるのにかかる時間とコスト。
2. 行数だけでなく、転送されるペイロードのサイズ。
3. ブラウザーのメモリ使用量と、行モデルの計算にかかる時間。
4. 状態が変わるたびにリクエストを待つことによる、操作上のコスト。

今の時点でどちらの方法も使えるなら、クライアントサイドから始めるとデータの流れを小さく保てます。関係するテーブルの状態を自分で持っておけば、あとで処理をサーバーに移すのも簡単になります。

## データセット全体にかかる操作の一貫性を保つ {#keep-dataset-wide-operations-consistent}

フィルタリング、グループ化、ソート、ページネーションは、通常、同じデータセットに対する1つの処理の流れ（パイプライン）を表しています。サーバーがデータセットの一部しか送らない場合、クライアントサイドの操作は読み込まれた行だけしか処理できません。

たとえば、サーバーサイドでページネーションしたあとにクライアントサイドでソートすると、条件に合うすべての行ではなく、現在のページだけがソートされます。サーバーサイドでページネーションしたあとにクライアントサイドでフィルタリングすると、現在のページの行は隠せても、ほかのページにある一致する行は見つけられません。こうした結果は、たいてい誤解を招きます。

原則として、サーバーがページネーションを受け持つなら、結果全体に適用すべきフィルタリング、グループ化、ソート、集計もサーバーが受け持つべきです。対象範囲が狭くなることを意図している場合は、両方を混ぜても問題ありません。たとえば、サーバーから渡された各グループの中で行に順位を付ける、といった場合です。その場合は、対象範囲を UI で明確に示してください。

ファセットにも同じ配慮が必要です。サーバーから渡された1ページ分のデータから計算したファセットの件数は、そのページのことしか表していません。フィルタリング後のデータセット全体を表す必要がある場合は、ファセットをサーバーで計算してください。

## 「手動（manual）」の意味 {#what-manual-means}

TanStack Table では、サーバーサイドでのデータ処理を「手動（manual）」と呼びます。テーブル自身がその変換を行わないからです。`manual*` オプションは、データの取得も変換もしません。その機能については、渡されたデータを処理済みのものとして使うよう、テーブルに伝えるだけです。

| 操作                        | 手動オプション      | クライアントサイドの行モデルまたは実装  |
| --------------------------- | ------------------- | --------------------------------------- |
| 列フィルターとグローバルフィルター | `manualFiltering`   | `filteredRowModel`                      |
| グループ化                  | `manualGrouping`    | `groupedRowModel`                       |
| 集計値                      | `manualAggregation` | `aggregationFn` によるローカルでのフォールバック |
| ソート                      | `manualSorting`     | `sortedRowModel`                        |
| 展開                        | `manualExpanding`   | `expandedRowModel`                      |
| ページネーション            | `manualPagination`  | `paginatedRowModel`                     |

ファセットもサーバーから渡された結果に対応していますが、`manual*` オプションではなく独自のファクトリーを使います。機能ごとの詳細は、[集計](../framework/react/guide/aggregation)と[ファセット](../framework/react/guide/column-faceting#custom-server-side-faceting)のガイドを参照してください。

使わないクライアントサイドの行モデルは省略できます。共有のテーブル設定に行モデルが含まれている場合は、対応する `manual*` オプションを指定すると、テーブルはその行モデルを使わずに処理を飛ばします。機能自体は有効のままにしておけるので、テーブルはその機能の状態と API を引き続き提供します。

## サーバーサイドでの典型的なデータの流れ {#a-typical-server-side-data-flow}

サーバーサイドで処理する場合、フィルタリング、グループ化、ソート、集計、ページネーションのロジックは、アプリケーションに合ったバックエンドの言語、SQL のクエリ層、データベースの API、サービスの構成の中で書きます。

TanStack Table はデータの取得も行いません。テーブルの状態をバックエンドに送り、返ってきた行をテーブルに渡すのはアプリケーションの役目です。データ取得の方法は好きなものを使えます。宣言的なデータ取得、キャッシュ、読み込み中の状態、リクエストのライフサイクル管理がほしい場合は、[TanStack Query](https://tanstack.com/query/latest) がとてもよい相棒になります。TanStack Query は、制御された TanStack Table の状態と自然に組み合わせられます。

サーバーサイドで処理する手順は次のとおりです。

1. データ取得のコードから読めるように、関係するフィルター、グループ化、ソート、ページネーションの状態を自分で持つ。
2. サーバーが受け持つ状態の値を、すべてリクエストまたはクエリキーに含める。
3. 対応する `manual*` オプションを有効にする。
4. サーバーから返された処理済みの行を `data` に渡す。
5. 手動でページネーションする場合は、わかっていれば `rowCount` か `pageCount` も渡す。
6. フィルター、グループ化、ソート、ページサイズが変わったときは、ページ番号をリセットするか、妥当な値か確認する。
7. 前回の結果を残しておくか、読み込み中の状態を表示するかを意図して決める。また、遅れて返ってきた古いレスポンスが新しい結果を上書きしないようにする。

`manualPagination` を指定すると、既定で `autoResetPageIndex` が無効になります。

より一般的に言うと、自動リセットの副作用は、それを呼び出す行モデルが再計算されたときに実行されます。クライアントサイドのフィルタリング、グループ化、ソートの行モデルは、関係する状態が変わったあと、通常はページ番号のリセットを呼び出します。それらの行モデルを省略した完全に手動のサーバーサイド構成では、制御された状態が変わってもリセットのフックは実行されません。代わりに、下の例のように、対応する変更コールバックの中で依存する状態をリセットしてください。なお、返されたデータが処理されるとき、コアのデータの変更によって一部の自動リセットが起きることはあります。

テーブルは引き続き状態を管理し、イベントハンドラーを提供します。その状態をデータ取得の層とつなぐのはアプリケーションです。完全なパターンは、フレームワークごとのテーブルの状態ガイドと、TanStack Query と組み合わせたサンプルを参照してください。

- [テーブルの状態](../framework/react/guide/table-state)
- [TanStack Query との組み合わせ](https://tanstack.com/table/latest/docs/framework/react/examples/with-tanstack-query)


行選択、展開、そのほかの行の状態をリクエストをまたいで保持する必要がある場合は、`getRowId` にバックエンドの安定した識別子を使ってください。ページ内での相対的な行のインデックスでは、サーバーのレスポンスをまたいで同じレコードを確実に識別できません。

### サーバー用の行モデルが組み込まれていない理由 {#why-no-built-in-server-row-models}

TanStack Table は、同期的に動くテーブルの状態管理ライブラリです。クライアントサイドの行モデルは、すでにメモリ上にあるデータを同期的に変換します。一方、状態と API は、ユーザーが求めているフィルタリング、ソート、ページネーションを表します。データの取得やバックエンドでのクエリの実行は、テーブルの外で行われます。

バックエンドの設計や、フロントエンドとバックエンドのあいだの取り決め（コントラクト）には、正しいやり方が無数にあります。REST のクエリパラメーター、GraphQL の入力、RPC 呼び出し、SQL ビルダー、データベースの SDK、ストリーミングのレスポンスなどです。サーバー用の行モデルを組み込むと、こうした選択について特定の考え方を押し付けることになります。TanStack Table は、どんなバックエンドの技術スタックや API 設計とも組み合わせられるように、この境界をあえてアプリケーションに任せています。

実際には、サーバーサイドの行処理をクライアント側で取りまとめる役割を [TanStack Query](https://tanstack.com/query/latest) が担います。自前のデータ取得層で同じ役割を果たすこともできます。この層は、制御されたテーブルの状態を監視し、その状態を API のコントラクトに従って送信し、結果をキャッシュし、返ってきた行をテーブルに戻します。たとえば React と組み合わせる場合は、サーバーが受け持つ状態の値をすべて、クエリキーとクエリ関数の両方に渡せます。

#### `useQuery` を使ったページ番号によるページネーション {#page-index-pagination-with-usequery}

```tsx
const features = tableFeatures({
  columnFilteringFeature,
  globalFilteringFeature,
  rowPaginationFeature,
  rowSortingFeature,
  // Client-side filtering, sorting, and pagination row models are not
  // required because those operations are handled manually on the server.
  // Omitting the filtered and sorted row models also omits their page-reset
  // hooks, so pagination is reset in the change handlers below.
})

const [sorting, setSorting] = useState<SortingState>([])
const [globalFilter, setGlobalFilter] = useState('')
const [pagination, setPagination] = useState<PaginationState>({
  pageIndex: 0,
  pageSize: 10,
})

const dataQuery = useQuery({
  queryKey: ['people', { sorting, globalFilter, pagination }],
  queryFn: () => fetchPeople({ sorting, globalFilter, pagination }),
  placeholderData: keepPreviousData,
})

const table = useTable(
  {
    features,
    columns,
    data: dataQuery.data?.rows ?? [],
    rowCount: dataQuery.data?.rowCount,
    state: { sorting, globalFilter, pagination },
    onSortingChange: (updater) => {
      setSorting(updater)
      setPagination((previous) => ({ ...previous, pageIndex: 0 })) // reset page index when sorting changes
    },
    onGlobalFilterChange: (updater) => {
      setGlobalFilter(updater)
      setPagination((previous) => ({ ...previous, pageIndex: 0 })) // reset page index when global filter changes
    },
    onPaginationChange: setPagination,
    manualFiltering: true,
    manualSorting: true,
    manualPagination: true,
  },
  (state) => state,
)
```

ここでは、`fetchPeople` がアプリケーションのフロントエンドとバックエンドのあいだのコントラクトを定義しています。操作を正しい順序で適用し、要求された行と、フィルタリング後の総件数 `rowCount` を返すのは、引き続きバックエンドの役目です。

#### `useInfiniteQuery` を使ったカーソルによるページネーション {#cursor-based-pagination-with-useinfinitequery}

総行数の計算や、任意のページへのジャンプに対応するのが高くつく場合は、カーソルによるページネーションが便利な代替手段になります。バックエンドはページ番号の代わりにカーソルを受け取り、現在の行、`nextCursor`、次のページがあるかどうかを返します。本番環境のカーソルは中身の意味を持たない値であることが多いですが、ID が一意でバックエンドの並び順が決定的なら、最後の行の安定した ID をカーソルとして使うこともできます。

TanStack Query の `useInfiniteQuery` は、カーソルのつながりをキャッシュします。TanStack Table は `pagination.pageIndex` を使って、キャッシュされたページのうち1つを選べます。アプリケーションは、ユーザーがキャッシュより先に進んだときだけ新しいページを取得します。

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
    pageCount: -1, // the cursor API does not expose a total page count
    state: { sorting, globalFilter, pagination },
    onSortingChange: (updater) => {
      setSorting(updater)
      setPagination((previous) => ({ ...previous, pageIndex: 0 }))
    },
    onGlobalFilterChange: (updater) => {
      setGlobalFilter(updater)
      setPagination((previous) => ({ ...previous, pageIndex: 0 }))
    },
    onPaginationChange: setPagination,
    manualFiltering: true,
    manualSorting: true,
    manualPagination: true,
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

「次へ」ボタンには `canNextPage` を使ってください。`pageCount: -1` の場合、テーブルの `getCanNextPage()` では、サーバーが最後まで到達したかどうかがわかりません。一度取得したページは、追加のリクエストなしで再表示できます。総数がわからないので `lastPage()` が移動先にできる有限のページはなく、`getCanLastPage()` は `false` を返します。ソート、フィルタリング、ページサイズが変わったときは、新しいクエリが最初のカーソルから始まるように `pageIndex` を `0` にリセットしてください。

## 描画は別の判断 {#rendering-is-a-separate-decision}

データの処理と描画は、別々の問題を解決します。

- ページネーションは、一度に表示する行の数を制限します。クライアントとサーバーのどちらでも行えます。
- 仮想化は、ブラウザーにすでに読み込まれた行のうち、見えている部分だけを描画します。

仮想化を使えば、クライアントサイドの大きなデータセットでも低いコストで描画できます。しかし、取得するデータの量や、そのデータセットをフィルタリング・ソートする処理の量は減りません。データセット全体が大きすぎて読み込めない場合は、サーバーサイドでの操作か、少しずつ取得する方法を使ってください。そのうえで、読み込んだ結果がまだ大きく描画のコストが高いなら、仮想化を加えます。

## 方法を選ぶ {#choosing-an-approach}

ブラウザーがデータセット全体を無理なく取得して保持でき、ローカルですぐに反応する操作に価値がある場合は、クライアントサイドでの処理を使ってください。データセット全体を読み込むべきでない、または読み込めない場合や、正となる結果をバックエンドが決める必要がある場合は、サーバーサイドでの処理を使ってください。

サーバーサイドでの処理を選ぶということは、実装を自分で用意するということです。TanStack Table はユーザーが求めていることを表す状態と API を提供しますが、その状態を処理するのはバックエンドのコードや SQL であり、リクエストとレスポンスを運ぶのはデータ取得のコードです。TanStack Table のサーバーサイドのモデルや、組み込みのデータ取得層は関わりません。この分離によって、TanStack Table はどんなバックエンドとも組み合わせられます。データ取得とキャッシュの層の管理に助けがほしい場合は、TanStack Query を任意で組み合わせられます。

どちらの方法を選ぶ場合も、現実的なデータで処理の流れ全体を試してください。ネットワークでの転送、ブラウザーのメモリ、行モデルの計算、DOM の描画、バックエンドのクエリのコストは、それぞれ別のボトルネックです。最適な境界は、そのすべてをユーザーにとって許容できる範囲に収められるものです。
