---
title: 列フィルタリング（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React のサンプルを参照してください。

- [列フィルター](https://tanstack.com/table/latest/docs/framework/react/examples/filters)
- [ファセットフィルター](https://tanstack.com/table/latest/docs/framework/react/examples/filters-faceted)
- [バケット分けしたファセットフィルター](https://tanstack.com/table/latest/docs/framework/react/examples/filters-faceted-bucketed)
- [あいまい検索](https://tanstack.com/table/latest/docs/framework/react/examples/filters-fuzzy)

### 列フィルタリングのセットアップ {#column-filtering-setup}

列フィルタリングの機能を使うためのテーブルのセットアップ方法は次のとおりです。列フィルタリングの機能を追加すると、関連する API が使えるようになります。クライアントサイドでフィルタリングする場合は、その機能の後ろに `filteredRowModel` も設定してください。行モデルのスロットは型チェックの対象になるためです。

```tsx
import {
  useTable,
  tableFeatures,
  columnFilteringFeature,
  createFilteredRowModel,
  filterFn_includesString,
  filterFn_inNumberRange,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnFilteringFeature,
  filteredRowModel: createFilteredRowModel(), // if using client-side filtering
  // manualFiltering: true, // if using manual server-side filtering
  filterFns: {
    includesString: filterFn_includesString,
    inNumberRange: filterFn_inNumberRange,
  },
})

const table = useTable({
  features,
  columns,
  data,
})
```

> [!NOTE]
> 上の `filterFns` レジストリには、このテーブルで使う組み込みのフィルター関数だけを並べています。組み込みの `filterFns` レジストリ全体を展開する書き方（`filterFns: { ...filterFns }`）も引き続き使えますが、組み込みのフィルター関数がすべてバンドルに含まれてしまいます。使う関数だけを登録するか、登録せずに関数を `filterFn` 列オプションへ直接渡してください。

## 列フィルタリング（React）ガイド {#column-filtering-react-guide}

フィルタリングには、列フィルタリングとグローバルフィルタリングの 2 種類があります。

このガイドでは列フィルタリングを扱います。列フィルタリングは、1 つの列のアクセサーの値に対して適用するフィルターです。

TanStack Table は、クライアントサイドのフィルタリングと、手動のサーバーサイドのフィルタリングの両方に対応しています。このガイドでは、両方の実装方法とカスタマイズ方法を説明し、ユースケースに合うのはどちらかを判断する手助けをします。

### クライアントサイドとサーバーサイドのフィルタリング {#client-side-vs-server-side-filtering}

フィルタリングは、ソートやページネーションと同じデータセットに対して行うべきです。ブラウザーがデータセット全体を持っているならクライアントサイドのフィルタリングを使います。1 ページ分などデータの一部しか持っていないなら、読み込み済みの行だけをフィルタリングするのが意図どおりである場合を除き、サーバーサイドのフィルタリングを使います。

判断の枠組み全体、パフォーマンスに関わる要素、データ操作を組み合わせるときの指針については、[クライアントサイドとサーバーサイドのガイド](../../../guide/client-side-vs-server-side)を参照してください。

クライアントサイドのフィルター済み行モデルは、列フィルタリングの入力が変わったときに、ページ番号を自動リセットするフックも呼び出します。ページ番号が実際にリセットされるかどうかは、`autoResetPageIndex`、`autoResetAll`、`manualPagination` の各オプションで決まります。フィルタリングを手動で行い、この行モデルを省略するか迂回している場合は、列フィルターの状態が変わってもこのフックは呼ばれません。必要に応じて、フィルターの変更ハンドラーの中でサーバーサイドのページネーションをリセットしてください。

### 手動のサーバーサイドフィルタリング {#manual-server-side-filtering}

組み込みのクライアントサイドのフィルタリングではなく、サーバーサイドのフィルタリングを実装する必要があると判断した場合の方法は次のとおりです。

手動のサーバーサイドフィルタリングでは `filteredRowModel` は不要です。その代わり、テーブルに渡す `data` をあらかじめフィルタリングしておきます。ただし、features オブジェクトに `filteredRowModel` を追加済みの場合は、`manualFiltering` オプションを `true` にすると、テーブルにその行モデルを使わせないようにできます。

```tsx
const features = tableFeatures({ columnFilteringFeature })

const table = useTable({
  features,
  data,
  columns,
  manualFiltering: true,
})
```

> [!NOTE]
> 手動フィルタリングを使う場合、このガイドの以降で説明するオプションの多くは効果がありません。`manualFiltering` を `true` にすると、テーブルインスタンスは渡された行にフィルタリングの処理を一切適用しません。行はすでにフィルタリング済みだとみなし、渡された `data` をそのまま使います。

### クライアントサイドのフィルタリング {#client-side-filtering}

組み込みのクライアントサイドのフィルタリング機能を使う場合は、`columnFilteringFeature` と `filteredRowModel` のファクトリーを features に追加します。TanStack Table から `createFilteredRowModel` と、必要なフィルター関数をインポートしてください。

```tsx
import {
  useTable,
  tableFeatures,
  columnFilteringFeature,
  createFilteredRowModel,
  filterFn_includesString,
  filterFn_inNumberRange,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnFilteringFeature,
  filteredRowModel: createFilteredRowModel(),
  filterFns: {
    includesString: filterFn_includesString,
    inNumberRange: filterFn_inNumberRange,
  },
})

const table = useTable({
  features,
  data,
  columns,
})
```

### 列フィルターの状態 {#column-filter-state}

クライアントサイドとサーバーサイドのどちらのフィルタリングを使う場合でも、TanStack Table が提供する列フィルターの状態管理を活用できます。フィルターの状態を変更・操作したり、列フィルターの状態を取得したりするためのテーブル API や列 API が数多く用意されています。

列フィルタリングの状態は、次の形のオブジェクトの配列として定義されています。

```ts
interface ColumnFilter {
  id: string
  value: unknown
}
type ColumnFiltersState = ColumnFilter[]
```

列フィルターの状態はオブジェクトの配列なので、複数の列フィルターを同時に適用できます。

#### 列フィルターの状態を読み取る {#accessing-column-filter-state}

UI の再レンダーにつなげたいリアクティブな読み取りには、`table.state.columnFilters`（`useTable` のセレクターで選んだもの）か `table.Subscribe` を使います。イベントハンドラーなど、レンダー以外のコードでは `table.atoms.columnFilters.get()` で現在のスナップショットを読み取れます。ただし、この読み取りではコンポーネントが以降の変更を購読しません。

```tsx
const table = useTable({
  features,
  columns,
  data,
  //...
})

table.state.columnFilters // reactive read in render
table.atoms.columnFilters.get() // snapshot read in event handlers
```

テーブルの外から列フィルターの状態にアクセスしたい場合は、次に説明するように列フィルターの状態を「制御」できます。

### 制御された列フィルターの状態 {#controlled-column-filter-state}

アプリケーションの他の場所から列フィルターの状態に手軽にアクセスしたい場合は、列フィルターの状態スライスを自分で持つことができます。v9 で推奨される方法は、外部のアトムを `atoms` テーブルオプションで渡すことです。アトムなら細かい粒度の購読が保たれるため、テーブルを持つコンポーネントを再レンダーさせることなく、フィルターの値を別の場所（サーバーサイドフィルタリングのクエリーキーなど）で使えます。

```tsx
import { useCreateAtom, useSelector } from '@tanstack/react-store'

const columnFiltersAtom = useCreateAtom<ColumnFiltersState>([]) // can set initial column filter state here

// subscribe to the atom wherever you need the value (e.g. for a query key)
const columnFilters = useSelector(columnFiltersAtom)

const table = useTable({
  features,
  columns,
  data,
  //...
  atoms: {
    columnFilters: columnFiltersAtom, // table filter APIs now update columnFiltersAtom
  },
})
```

v8 スタイルの `state.columnFilters` と `onColumnFiltersChange` を組み合わせるパターンも、引き続き使えます。単純な連携や v8 のコードを移行するときには便利ですが、外部のアトムに比べると購読の粒度は粗くなります。詳しい比較は[テーブルの状態のガイド](./table-state)を参照してください。

```tsx
const [columnFilters, setColumnFilters] = useState<ColumnFiltersState>([])
//...
const table = useTable({
  features,
  columns,
  data,
  //...
  state: {
    columnFilters,
  },
  onColumnFiltersChange: setColumnFilters,
})
```

#### 列フィルターの初期状態 {#initial-column-filter-state}

列フィルターの状態を自前の状態管理やスコープで制御する必要はないものの、列フィルターの初期状態は設定したい場合は、`state` の代わりに `initialState` テーブルオプションを使えます。

```tsx
const table = useTable({
  features,
  columns,
  data,
  //...
  initialState: {
    columnFilters: [
      {
        id: 'name',
        value: 'John', // filter the name column by 'John' by default
      },
    ],
  },
})
```

> [!NOTE]
> `initialState.columnFilters` と `state.columnFilters` を同時に使わないでください。制御された `state.columnFilters` の値が `initialState.columnFilters` を上書きします。

### フィルター関数（FilterFns） {#filterfns}

列ごとに独自のフィルタリングの処理を持たせられます。TanStack Table が提供するフィルター関数から選ぶことも、自分で作ることもできます。

デフォルトで、次の 18 個の組み込みフィルター関数から選べます。

- `includesString` - 大文字と小文字を区別しない文字列の部分一致
- `includesStringSensitive` - 大文字と小文字を区別する文字列の部分一致
- `startsWith` - 大文字と小文字を区別しない文字列の前方一致
- `endsWith` - 大文字と小文字を区別しない文字列の後方一致
- `equalsString` - 大文字と小文字を区別しない文字列の完全一致
- `equalsStringSensitive` - 大文字と小文字を区別する文字列の完全一致
- `equals` - 厳密等価 `===`
- `weakEquals` - 緩い等価 `==`
- `empty` - 行の値が nullish か、空白文字だけである（フィルター値はオン・オフのフラグ）
- `notEmpty` - 行の値が nullish でも空白文字だけでもない（フィルター値はオン・オフのフラグ）
- `arrIncludes` - 行の配列（または文字列）の値が、フィルター値のうち少なくとも 1 つを含む
- `arrIncludesAll` - 行の配列の値が、フィルター値をすべて含む
- `arrIncludesSome` - 行の配列の値が、フィルター値のうち少なくとも 1 つを含む
- `arrHas` - 行のスカラー値が、フィルター値のうち少なくとも 1 つと等しい
- `inNumberRange` - 両端を含む `[min, max]` の数値範囲（両端は正規化され、逆順なら入れ替えられる）
- `inDateRange` - 両端を含む `[min, max]` の日付範囲。`Date` オブジェクト、タイムスタンプ、日付文字列を受け付ける（空の端は上限・下限なしとして扱う）
- `between` - 両端を含まない min/max の範囲（空の端は上限・下限なしとして扱う）
- `betweenInclusive` - 両端を含む min/max の範囲（空の端は上限・下限なしとして扱う）

独自のカスタムフィルター関数も定義できます。`filterFn` 列オプションにインラインで書くか、`tableFeatures` の `filterFns` レジストリスロットに名前付きで登録します。

#### カスタムフィルター関数 {#custom-filter-functions}

> [!NOTE]
> これらのフィルター関数は、クライアントサイドのフィルタリングでのみ実行されます。

カスタムフィルター関数を `tableFeatures` の `filterFns` スロットに登録する場合も、`filterFn` 列オプションに直接渡す場合も、シグネチャは次のようにします。

```ts
const myCustomFilterFn: FilterFn<typeof features, MyData> = (
  row, // Row<typeof features, MyData>
  columnId: string,
  filterValue: any,
  addMeta?: (meta: FilterMeta) => void,
): boolean => ...
```

フィルター関数はどれも次のものを受け取ります。

- フィルタリング対象の行
- 行の値を取り出すための columnId
- フィルター値

そして、行をフィルター後の行に含めるなら `true`、取り除くなら `false` を返します。

```tsx
const myCustomFilterFn: FilterFn<typeof features, MyData> = (
  row,
  columnId,
  filterValue,
) => {
  return // true or false based on your custom logic
}

const features = tableFeatures({
  columnFilteringFeature,
  filteredRowModel: createFilteredRowModel(),
  filterFns: {
    includesString: filterFn_includesString,
    inNumberRange: filterFn_inNumberRange,
    myCustomFilterFn,
    startsWith: startsWithFilterFn, // defined elsewhere
  },
})

const columns = [
  {
    header: () => 'Name',
    accessorKey: 'name',
    filterFn: 'includesString', // use built-in filter function
  },
  {
    header: () => 'Age',
    accessorKey: 'age',
    filterFn: 'inNumberRange',
  },
  {
    header: () => 'Birthday',
    accessorKey: 'birthday',
    filterFn: 'myCustomFilterFn', // reference a custom filter function registered in features
  },
  {
    header: () => 'Profile',
    accessorKey: 'profile',
    // use custom filter function directly
    filterFn: (row, columnId, filterValue) => {
      return // true or false based on your custom logic
    },
  },
]
//...
const table = useTable({
  features,
  columns,
  data,
})
```

> **TypeScript に関する注意:** `filterFn: 'myCustomFilterFn'` のような文字列での参照を型チェックに通すには、（上の例のように）関数を `tableFeatures` の `filterFns` スロットに登録してください。あるいは、関数を `filterFn` 列オプションに直接渡せば、レジストリを使わずに済みます。登録の完全な例は [あいまい検索のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/filters-fuzzy)を参照してください。

##### フィルター関数の動作をカスタマイズする {#customize-filter-function-behavior}

フィルター関数にいくつかのプロパティを付け加えて、動作をカスタマイズできます。

- `filterFn.resolveFilterValue` - 任意の `filterFn` に付け加えられる、省略可能な「ぶら下げ」メソッドです。フィルター値をフィルター関数に渡す前に、変換・サニタイズ・整形できます。テーブルはこのメソッドを（行ごとではなく）フィルターごとに 1 回だけ適用するので、コストの高い前処理を置く場所としても適しています。

- `filterFn.resolveDataValue` - 省略可能な「ぶら下げ」メソッドで、各行の値をフィルター値と比較する前に正規化します。`constructFilterFn` ヘルパーで作ったフィルター関数はすべてこのメソッドを尊重します。組み込みのフィルター関数もすべてこのヘルパーで作られています。

- `filterFn.autoRemove` - 任意の `filterFn` に付け加えられる、省略可能な「ぶら下げ」メソッドです。フィルター値を受け取り、そのフィルター値をフィルターの状態から取り除くべきなら `true` を返します。たとえば、真偽値のようなフィルターでは、フィルター値が `false` になったらテーブルの状態からフィルター値を取り除きたい場合があります。このメソッドを指定すると、その判定が最優先されます。このメソッドが残すと判定した値は、デフォルトの判定では取り除かれるはずの空文字列であっても、フィルターの状態に残ります。なお、フィルター値が `undefined` の場合は、常にフィルターが解除されます。

`constructFilterFn` ヘルパーは、値どうしを比較する関数と、上で説明した省略可能なリゾルバーから、フィルター関数を組み立てます。

```tsx
const startsWithFilterFn = constructFilterFn({
  // compare the (resolved) row value against the (resolved) filter value
  filter: (dataValue, filterValue) =>
    Boolean(dataValue?.startsWith(filterValue)),
  // normalize the filter value once, before any rows are tested
  resolveFilterValue: (value) => String(value).toLowerCase().trim(),
  // normalize each row's value before it reaches the comparator
  resolveDataValue: (value) => String(value ?? '').toLowerCase(),
  // remove the filter value from filter state if it is falsy (empty string in this case)
  autoRemove: (value) => !value,
})
```

比較を `filter` に、正規化をリゾルバーに分けておくと、既存のフィルター関数の変種が欲しくなったときに役立ちます。定義は返された関数に付いているので、`constructFilterFn` で作ったフィルター関数ならどれでも展開して、違う部分だけを上書きできます。たとえば、ダイアクリティカルマークも無視する `includesString`（"eric" で検索すると "Éric" にも一致する）は次のように書けます。

```tsx
const normalize = (value: unknown) =>
  String(value ?? '')
    .toLowerCase()
    .normalize('NFD')
    .replace(/\p{Diacritic}/gu, '')

const includesStringIgnoreDiacritics = constructFilterFn({
  ...filterFn_includesString, // reuse the comparator and autoRemove behavior
  resolveFilterValue: normalize,
  resolveDataValue: normalize,
})
```

この変種は、他のカスタムフィルター関数と同じように、`filterFns` レジストリに名前付きで登録するか、`filterFn` 列オプションに直接渡して使います。

> [!NOTE]
> テーブルは、行の判定を始める前に、フィルターごとに 1 回 `resolveFilterValue` を適用します。フィルター関数を（テーブルの外で）直接呼び出す場合は、フィルター値を自分で解決してください: `myFilterFn(row, columnId, myFilterFn.resolveFilterValue?.(rawValue) ?? rawValue)`。

### 列フィルタリングをカスタマイズする {#customize-column-filtering}

列フィルタリングの動作をさらにカスタマイズするためのテーブルオプションや列オプションが、数多く用意されています。

#### 列フィルタリングを無効にする {#disable-column-filtering}

デフォルトでは、すべての列で列フィルタリングが有効です。`enableColumnFilters` テーブルオプションや `enableColumnFilter` 列オプションを使うと、すべての列または特定の列で列フィルタリングを無効にできます。また、`enableFilters` テーブルオプションを `false` にすると、列フィルタリングとグローバルフィルタリングの両方を無効にできます。

ある列で列フィルタリングを無効にすると、その列の `column.getCanFilter` API は `false` を返します。

```tsx
const columns = [
  {
    header: () => 'Id',
    accessorKey: 'id',
    enableColumnFilter: false, // disable column filtering for this column
  },
  //...
]
//...
const table = useTable({
  features,
  columns,
  data,
  enableColumnFilters: false, // disable column filtering for all columns
})
```

#### サブ行のフィルタリング（展開） {#filtering-sub-rows-expanding}

展開、グループ化、集計などの機能を使うときに、列フィルタリングの動作をカスタマイズするためのテーブルオプションがいくつか追加で用意されています。

##### 末端の行からフィルタリングする {#filter-from-leaf-rows}

デフォルトでは、フィルタリングは親の行から下に向かって行われます。そのため、親の行がフィルターで除外されると、その子のサブ行もすべて除外されます。ユーザーにサブ行ではなく最上位の行だけを検索させたい場合は、ユースケースによってはこれが望ましい動作です。また、これが最もパフォーマンスの良い選択肢でもあります。

一方、親の行が除外されるかどうかに関係なく、サブ行もフィルタリング・検索の対象にしたい場合は、`filterFromLeafRows` テーブルオプションを `true` にします。このオプションを `true` にすると、フィルタリングは末端の行から上に向かって行われます。つまり、子や孫の行のうち 1 つでも残っていれば、その親の行も残ります。

```tsx
const features = tableFeatures({
  columnFilteringFeature,
  rowExpandingFeature,
  filteredRowModel: createFilteredRowModel(),
  expandedRowModel: createExpandedRowModel(),
  filterFns: {
    includesString: filterFn_includesString,
    inNumberRange: filterFn_inNumberRange,
  },
})

const table = useTable({
  features,
  columns,
  data,
  filterFromLeafRows: true, // filter and search through sub-rows
})
```

##### 末端の行をフィルタリングする最大の深さ {#max-leaf-row-filter-depth}

デフォルトでは、ツリー内のすべての行がフィルタリングの対象になります。ルートレベルの親の行か、親の行の子である末端の行かは問いません。`maxLeafRowFilterDepth` テーブルオプションを `0` にすると、フィルタリングはルートレベルの親の行にだけ適用され、サブ行はすべてフィルタリングされないまま残ります。同様に、このオプションを `1` にすると、フィルタリングは 1 階層下までの子の行にだけ適用されます。それ以降も同じです。

親の行がフィルターを通過しているあいだ、そのサブ行がフィルターで除外されないようにしたい場合は、`maxLeafRowFilterDepth: 0` を使います。

```tsx
const features = tableFeatures({
  columnFilteringFeature,
  rowExpandingFeature,
  filteredRowModel: createFilteredRowModel(),
  expandedRowModel: createExpandedRowModel(),
  filterFns: {
    includesString: filterFn_includesString,
    inNumberRange: filterFn_inNumberRange,
  },
})

const table = useTable({
  features,
  columns,
  data,
  maxLeafRowFilterDepth: 0, // only filter root level parent rows out
})
```

### 列フィルターの API {#column-filter-apis}

列フィルターの状態を操作したり、UI コンポーネントにつないだりするための列 API とテーブル API が数多く用意されています。使える API と、よくある使い道の一覧は次のとおりです。

- `table.setColumnFilters` - 列フィルターの状態全体を新しい状態で上書きします。
- `table.resetColumnFilters` - 「すべてクリア／フィルターをリセット」ボタンに便利です。

- **`column.getFilterValue`** - 入力欄のデフォルトの初期フィルター値を取得するときや、フィルター入力欄にフィルター値を直接渡すときに便利です。
- **`column.setFilterValue`** - フィルター入力欄を `onChange` や `onBlur` ハンドラーにつなぐときに便利です。

- `column.getCanFilter` - フィルター入力欄の有効・無効を切り替えるときに便利です。
- `column.getIsFiltered` - 列が現在フィルタリングされていることを示す目印を表示するときに便利です。
- `column.getFilterIndex` - 現在のフィルターが何番目に適用されているかを表示するときに便利です。

- `column.getAutoFilterFn` - フィルター関数が指定されていない列のデフォルトのフィルター関数を見つけるために、内部で使われます。
- `column.getFilterFn` - 現在使われているフィルターモードやフィルター関数を表示するときに便利です。
