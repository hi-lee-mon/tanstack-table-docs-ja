---
title: グローバルフィルタリング（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React のサンプルを参照してください。

- [列フィルター](https://tanstack.com/table/latest/docs/framework/react/examples/filters)
- [あいまい検索](https://tanstack.com/table/latest/docs/framework/react/examples/filters-fuzzy)

### グローバルフィルタリングの準備 {#global-filtering-setup}

テーブルでグローバルフィルタリングの機能を使うための準備は次のとおりです。グローバルフィルタリングは列フィルタリングに依存するため、`globalFilteringFeature` より前に `columnFilteringFeature` を追加します。グローバルフィルタリングの機能を追加すると、関連する API が使えるようになります。クライアントサイドフィルタリングを使う場合は、機能の後に `filteredRowModel` も設定してください。行モデルのスロットは型チェックされるためです。

```tsx
import {
  useTable,
  tableFeatures,
  columnFilteringFeature,
  globalFilteringFeature,
  createFilteredRowModel,
  filterFn_includesString,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnFilteringFeature,
  globalFilteringFeature,
  filteredRowModel: createFilteredRowModel(), // if using client-side filtering
  // manualFiltering: true, // if using manual server-side filtering
  filterFns: { includesString: filterFn_includesString },
})

const table = useTable({
  features,
  columns,
  data,
})
```

> [!NOTE]
> 上の `filterFns` レジストリには、このテーブルで使う組み込みのフィルター関数だけを登録しています。組み込みの `filterFns` レジストリ全体を展開する書き方（`filterFns: { ...filterFns }`）も引き続き使えますが、すべての組み込みフィルター関数がバンドルに含まれてしまいます。使う関数だけを登録するか、登録せずに関数を `globalFilterFn` オプションへ直接渡してください。

## グローバルフィルタリング（React）ガイド {#global-filtering-react-guide}

フィルタリングには、列フィルタリングとグローバルフィルタリングの2種類があります。

このガイドでは、すべての列にまたがって適用されるフィルターであるグローバルフィルタリングを扱います。

### クライアントサイドとサーバーサイドのフィルタリング {#client-side-vs-server-side-filtering}

フィルタリングは、ソートやページネーションと同じデータセットに対して行うべきです。ブラウザーがデータセット全体を持っている場合はクライアントサイドフィルタリングを使います。ブラウザーが1ページ分などの一部しか持っていない場合は、読み込み済みの行だけを意図的にフィルタリングするのでない限り、サーバーサイドフィルタリングを使います。

判断の枠組み、パフォーマンスに影響する要素、データ操作を組み合わせるときの指針については、[クライアントサイドとサーバーサイドのガイド](../../../guide/client-side-vs-server-side)を参照してください。

クライアントサイドのフィルター済み行モデルは、グローバルフィルタリングの入力が変わったときに、ページ番号を自動リセットするフックも呼び出します。ページ番号が実際にリセットされるかどうかは、`autoResetPageIndex`、`autoResetAll`、`manualPagination` の各オプションで決まります。フィルタリングを手動で行い、この行モデルを省略するか迂回している場合は、グローバルフィルターの状態が変わってもこのフックは呼ばれません。必要に応じて、フィルターの変更ハンドラーの中でサーバーサイドのページネーションをリセットしてください。

### 手動のサーバーサイドグローバルフィルタリング {#manual-server-side-global-filtering}

組み込みのクライアントサイドグローバルフィルタリングを使わず、サーバーサイドでグローバルフィルタリングを実装する必要があると判断した場合は、次のようにします。

手動のサーバーサイドグローバルフィルタリングでは、`filteredRowModel` は不要です。代わりに、テーブルに渡す `data` をあらかじめフィルタリングしておきます。ただし、features オブジェクトに `filteredRowModel` を追加している場合は、`manualFiltering` オプションを `true` にすると、テーブルにその行モデルを飛ばさせることができます。

```tsx
import {
  useTable,
  tableFeatures,
  columnFilteringFeature,
  globalFilteringFeature,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnFilteringFeature,
  globalFilteringFeature,
})

const table = useTable({
  features,
  data,
  columns,
  manualFiltering: true,
})
```

注意: 手動のグローバルフィルタリングを使う場合、このガイドの以降で説明するオプションの多くは効果がありません。manualFiltering を true にすると、テーブルインスタンスは渡された行にグローバルフィルタリングの処理を一切適用しません。行はすでにフィルタリング済みであるとみなし、渡されたデータをそのまま使います。

### クライアントサイドのグローバルフィルタリング {#client-side-global-filtering}

組み込みのクライアントサイドグローバルフィルタリングを使う場合は、`globalFilteringFeature`（と、その前提となる `columnFilteringFeature`）および `filteredRowModel` のファクトリーを features に追加します。

```tsx
import {
  useTable,
  tableFeatures,
  columnFilteringFeature,
  globalFilteringFeature,
  createFilteredRowModel,
  filterFn_includesString,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnFilteringFeature,
  globalFilteringFeature,
  filteredRowModel: createFilteredRowModel(),
  filterFns: { includesString: filterFn_includesString },
})

const table = useTable({
  features,
  // other options...
})
```

### グローバルフィルター関数 {#global-filter-function}

`globalFilterFn` オプションで、グローバルフィルタリングに使うフィルター関数を指定します。指定できるのは、`tableFeatures` の `filterFns` スロットに登録したフィルター関数（組み込みでもカスタムでもよい）を参照する文字列か、直接渡すフィルター関数です。

```tsx
const table = useTable({
  features,
  data,
  columns,
  globalFilterFn: 'includesString', // built-in filter function
})
```

組み込みのフィルター関数は、デフォルトで次の12種類から選べます。

- `includesString` - 大文字と小文字を区別せず、文字列を含むか
- `includesStringSensitive` - 大文字と小文字を区別して、文字列を含むか
- `equalsString` - 大文字と小文字を区別せず、文字列が等しいか
- `equals` - 厳密等価 `===`
- `weakEquals` - 緩い等価 `==`
- `arrIncludes` - 行の配列（または文字列）の値が、フィルター値のうち少なくとも1つを含むか
- `arrIncludesAll` - 行の配列の値が、すべてのフィルター値を含むか
- `arrIncludesSome` - 行の配列の値が、フィルター値のうち少なくとも1つを含むか
- `arrHas` - 行のスカラー値が、フィルター値のうち少なくとも1つと等しいか
- `inNumberRange` - 両端を含む `[min, max]` の数値範囲（両端は正規化され、逆順なら入れ替えられる）
- `between` - 両端を含まない最小値〜最大値の範囲（空の端は上限・下限なしとして扱う）
- `betweenInclusive` - 両端を含む最小値〜最大値の範囲（空の端は上限・下限なしとして扱う）

[後述](#custom-global-filter-function)のとおり、独自のグローバルフィルター関数を定義して、`globalFilterFn` テーブルオプションに直接渡すこともできます。

### グローバルフィルターの状態 {#global-filter-state}

`globalFilter` の状態スライスは、現在のグローバルフィルターの値を保持します。通常は検索文字列です（カスタムのグローバルフィルター関数が別の形の値を受け取れるよう、このスライスは `any` 型になっています）。UI を再レンダーさせたいリアクティブな読み取りには `table.state.globalFilter` を使います。イベントハンドラーの中では `table.atoms.globalFilter.get()` で現在のスナップショットを読めますが、この読み取りではコンポーネントが以後の変更を購読しません。

テーブルの外でグローバルフィルターの状態にアクセスしたい場合は、スライスを自分で管理できます。v9 で推奨されるのは、外部のアトムを `atoms` テーブルオプションで渡す方法です。アトムを使うと細かい粒度の購読が保たれ、テーブルを持つコンポーネントを再レンダーさせずに、フィルターの値を別の場所（たとえばサーバーサイドフィルタリング用のクエリキー）で使えます。

```tsx
import { useCreateAtom, useSelector } from '@tanstack/react-store'

const globalFilterAtom = useCreateAtom<string>('')

// subscribe to the atom wherever you need the value (e.g. for a query key)
const globalFilter = useSelector(globalFilterAtom)

const table = useTable({
  features,
  // other options...
  atoms: {
    globalFilter: globalFilterAtom, // table.setGlobalFilter now updates globalFilterAtom
  },
})
```

あるいは、v8 スタイルの `state.globalFilter` と `onGlobalFilterChange` を組み合わせるパターンも引き続き使えます。単純な連携や v8 のコードを移行するときには便利ですが、外部のアトムほど細かい粒度にはなりません。詳しい比較は[テーブルの状態ガイド](./table-state)を参照してください。

```tsx
const [globalFilter, setGlobalFilter] = useState<string>('')

const table = useTable({
  features,
  // other options...
  state: {
    globalFilter,
  },
  onGlobalFilterChange: setGlobalFilter,
})
```

### グローバルフィルターの入力欄を UI に追加する {#adding-global-filter-input-to-ui}

TanStack Table は、グローバルフィルターの入力欄をテーブルに追加しません。ユーザーがテーブルをフィルタリングできるように、自分で UI に追加してください。たとえば、テーブルの上に入力欄を置いて、ユーザーが検索語を入力できるようにします。値は `table.state.globalFilter` でリアクティブに読み取り、`table.setGlobalFilter` で更新します。

```tsx
return (
  <div>
    <input
      value={table.state.globalFilter ?? ''}
      onChange={(e) => table.setGlobalFilter(String(e.target.value))}
      placeholder="Search..."
    />
  </div>
)
```

### カスタムのグローバルフィルター関数 {#custom-global-filter-function}

カスタムのグローバルフィルター関数を使いたい場合は、関数を定義して `globalFilterFn` オプションに渡します。

> [!NOTE]
> グローバルフィルタリングには、あいまい検索フィルターの関数を使うのが定番です。これについては[あいまい検索フィルターのガイド](./fuzzy-filtering)で説明しています。

```tsx
const customFilterFn = (row, columnId, filterValue) => {
  return // true if the row should be included in the filtered rows
}

const table = useTable({
  features,
  // other options...
  globalFilterFn: customFilterFn,
})
```

### グローバルフィルターの初期状態 {#initial-global-filter-state}

テーブルの初期化時にグローバルフィルターの初期状態を設定したい場合は、テーブルの `initialState` オプションの一部としてグローバルフィルターの状態を渡します。ただし、スライスを自分で制御している場合は、外部のアトムや React の state に初期値を設定してください。

```tsx
const table = useTable({
  features,
  // other options...
  initialState: {
    globalFilter: 'search term', // if not controlling globalFilter state, set initial state here
  },
})
```

> [!NOTE]
> `initialState.globalFilter` と、（`atoms` や `state` による）制御された `globalFilter` を同時に使わないでください。制御された値が `initialState.globalFilter` を上書きします。

### グローバルフィルタリングを無効にする {#disable-global-filtering}

デフォルトでは、グローバルフィルタリングはすべての列で有効です。enableGlobalFilter テーブルオプションを使うと、すべての列でグローバルフィルタリングを無効にできます。また、enableFilters テーブルオプションを false にすると、列フィルタリングとグローバルフィルタリングの両方を無効にできます。

グローバルフィルタリングを無効にすると、その列の column.getCanGlobalFilter API は false を返します。

```tsx
const columns = [
  {
    header: () => 'Id',
    accessorKey: 'id',
    enableGlobalFilter: false, // disable global filtering for this column
  },
  //...
]
//...
const table = useTable({
  features,
  // other options...
  columns,
  enableGlobalFilter: false, // disable global filtering for all columns
})
```

### グローバルフィルターの API {#global-filter-apis}

グローバルフィルターの UI をつなぐときに役立つ API がいくつかあります。

- `table.setGlobalFilter` - グローバルフィルターの値を設定します。検索入力欄の `onChange` ハンドラーとつなぐときに便利です。
- `table.resetGlobalFilter` - グローバルフィルターの値を初期状態に戻します。`table.resetGlobalFilter(true)` とすると値を空にします。
- `table.getGlobalFilterFn` - グローバルフィルタリングに現在使われているフィルター関数を返します。
- `table.getGlobalAutoFilterFn` - デフォルトのグローバルフィルター関数（現在は `includesString`）を返します。
- `column.getCanGlobalFilter` - 列がグローバルフィルタリングの対象になるかどうかを返します。どの列が検索対象になっているかをデバッグするときに便利です。
