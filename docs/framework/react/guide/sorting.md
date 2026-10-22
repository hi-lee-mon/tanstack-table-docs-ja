---
title: ソート（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React のサンプルを参照してください。

- [ソート](https://tanstack.com/table/latest/docs/framework/react/examples/sorting)

### ソートのセットアップ {#sorting-setup}

ソート機能を使うためのテーブルのセットアップ方法を示します。ソート機能を追加すると、関連する API が使えるようになります。クライアントサイドのソートを使う場合は、機能の後に `sortedRowModel` もセットアップしてください。行モデルのスロットは型チェックされるためです。

```tsx
import {
  useTable,
  tableFeatures,
  rowSortingFeature,
  createSortedRowModel,
  sortFn_alphanumeric,
  sortFn_text,
  sortFn_datetime,
} from '@tanstack/react-table'

const features = tableFeatures({
  rowSortingFeature,
  sortedRowModel: createSortedRowModel(), // if using client-side sorting
  // manualSorting: true, // if using manual server-side sorting
  sortFns: {
    alphanumeric: sortFn_alphanumeric,
    text: sortFn_text,
    datetime: sortFn_datetime,
  },
})

const table = useTable({
  features,
  columns,
  data,
})
```

> [!NOTE]
> 組み込みの登録一式をまるごと展開する書き方（`sortFns: { ...sortFns }`）もまだ使えますが、すべての組み込みソート関数がバンドルに含まれてしまいます。使う関数だけを登録するか、`sortFn` 列オプションに関数を直接渡すことをおすすめします。デフォルトの `sortFn: 'auto'` は、列のデータ型に応じて登録済みの `alphanumeric`、`text`、`datetime` のいずれかに解決されるので、列が必要とする関数は登録しておいてください。

## ソート（React）ガイド {#sorting-react-guide}

TanStack Table は、ソートに関するほぼあらゆるユースケースに対応する手段を提供しています。このガイドでは、組み込みのクライアントサイドのソート機能をカスタマイズするためのさまざまなオプションと、クライアントサイドのソートをやめて手動のサーバーサイドのソートに切り替える方法を説明します。

### ソートの状態 {#sorting-state}

ソートの状態は、次の形をしたオブジェクトの配列として定義されています。

```tsx
type ColumnSort = {
  id: string
  desc: boolean
}
type SortingState = ColumnSort[]
```

ソートの状態は配列なので、複数の列で同時にソートできます。複数列ソートのカスタマイズについては、[後述](#multi-sorting) を参照してください。

#### ソートの状態にアクセスする {#accessing-sorting-state}

UI を再レンダーさせたいリアクティブな読み取りには、`table.state.sorting`（`useTable` のセレクターで選択したもの）か `table.Subscribe` を使います。イベントハンドラーなどレンダー以外のコードでは、`table.atoms.sorting.get()` で現在のスナップショットを読み取れます。ただし、この読み取りではコンポーネントがその後の変更を購読することはありません。

```tsx
const table = useTable({
  features,
  columns,
  data,
  //...
})

table.state.sorting // reactive read in render
table.atoms.sorting.get() // snapshot read in event handlers
```

ただし、テーブルの外でソートの状態にアクセスする必要がある場合は、次のようにソートの状態を「制御」できます。

#### 制御されたソートの状態 {#controlled-sorting-state}

アプリケーションのほかの部分からソートの状態に簡単にアクセスしたい場合は、ソートの状態のスライスを自分で持つことができます。v9 で推奨される方法は、外部のアトムを `atoms` テーブルオプションで渡すことです。アトムなら細かい粒度の購読がそのまま保たれ、テーブルを持つコンポーネントを再レンダーさせることなく、ソートの値をほかの場所（サーバーサイドのソートのためのクエリキーなど）で使えます。

```tsx
import { useCreateAtom, useSelector } from '@tanstack/react-store'

const sortingAtom = useCreateAtom<SortingState>([]) // can set initial sorting state here

// subscribe to the atom wherever you need the value (e.g. for a query key)
const sorting = useSelector(sortingAtom)

const table = useTable({
  features,
  columns,
  data,
  //...
  atoms: {
    sorting: sortingAtom, // table sorting APIs now update sortingAtom
  },
})
```

あるいは、v8 方式の `state.sorting` と `onSortingChange` の組み合わせも引き続きサポートされています。単純な連携や v8 のコードを移行するときには便利ですが、外部のアトムほど細かい粒度にはなりません。詳しい比較は [テーブルの状態ガイド](./table-state) を参照してください。

```tsx
const [sorting, setSorting] = useState<SortingState>([])
//...
const table = useTable({
  features,
  columns,
  data,
  //...
  state: {
    sorting,
  },
  onSortingChange: setSorting,
})
```

#### ソートの初期状態 {#initial-sorting-state}

ソートの状態を自前の状態管理やスコープで制御する必要はないものの、ソートの初期状態だけは設定したい場合は、`state` の代わりに `initialState` テーブルオプションを使えます。

```tsx
const table = useTable({
  features,
  columns,
  data,
  //...
  initialState: {
    sorting: [
      {
        id: 'name',
        desc: true, // sort by name in descending order by default
      },
    ],
  },
})
```

> [!NOTE]
> `initialState.sorting` と `state.sorting` を同時に使わないでください。制御された `state.sorting` の値が `initialState.sorting` を上書きします。

### クライアントサイドとサーバーサイドのソート {#client-side-vs-server-side-sorting}

ソートは、フィルタリングやページネーションと同じデータセットに対して行うべきです。サーバーが1ページ分やフィルター済みの一部だけを返す場合、クライアントサイドのソートは読み込まれた行だけをソートし、データセット全体はソートしません。

判断の枠組みの全体と、クライアントサイドとサーバーサイドの処理を意図的に混ぜるケースについては、[クライアントサイドとサーバーサイドのガイド](../../../guide/client-side-vs-server-side) を参照してください。

クライアントサイドのソート済み行モデルは、ソートの入力が変わったときにページ番号の自動リセットのフックも呼び出します。ページ番号が実際にリセットされるかどうかは、`autoResetPageIndex`、`autoResetAll`、`manualPagination` の各オプションによって決まります。ソートを手動で行い、この行モデルを省略または迂回している場合は、ソートの状態が変わってもこのフックは呼ばれません。必要に応じて、ソートの変更ハンドラーの中でサーバーサイドのページネーションをリセットしてください。

### 手動のサーバーサイドのソート {#manual-server-side-sorting}

バックエンドのロジックで独自のサーバーサイドのソートだけを使うつもりなら、ソート済み行モデルを渡す必要はありません。ソート済み行モデルを渡しているけれど無効にしたい場合は、`manualSorting` テーブルオプションを使えます。

```tsx
import { useCreateAtom, useSelector } from '@tanstack/react-store'

const features = tableFeatures({ rowSortingFeature }) // feature needed for sorting state/APIs

const sortingAtom = useCreateAtom<SortingState>([])

// subscribe to the sorting state for your server-side query
const sorting = useSelector(sortingAtom)
//...
const table = useTable({
  features,
  columns,
  data,
  manualSorting: true, // use pre-sorted row model instead of sorted row model
  atoms: {
    sorting: sortingAtom,
  },
})
```

ソートの状態を（外部のアトム、または `state.sorting` と `onSortingChange` の組み合わせで）自分のスコープに引き上げる方法は、前述の [制御されたソートの状態](#controlled-sorting-state) の節で説明しています。

> [!NOTE]
> `manualSorting` を `true` にすると、テーブルは渡されたデータがすでにソート済みであるとみなし、ソートを一切適用しません。

### クライアントサイドのソート {#client-side-sorting}

クライアントサイドのソートを実装するには、`rowSortingFeature` と `sortedRowModel` のファクトリーを機能に追加します。`createSortedRowModel` と、使う個々のソート関数を TanStack Table からインポートしてください。

```tsx
import {
  useTable,
  tableFeatures,
  rowSortingFeature,
  createSortedRowModel,
  sortFn_alphanumeric,
  sortFn_text,
  sortFn_datetime,
} from '@tanstack/react-table'

const features = tableFeatures({
  rowSortingFeature,
  sortedRowModel: createSortedRowModel(),
  sortFns: {
    alphanumeric: sortFn_alphanumeric,
    text: sortFn_text,
    datetime: sortFn_datetime,
  },
})

const table = useTable({
  features,
  columns,
  data,
})
```

### ソートの RowModelFns {#sorting-rowmodelfns}

すべての列のデフォルトのソート関数は、列のデータ型から推論されます。ただし、特定の列で使うソート関数を正確に指定しておくと便利なこともあります。とくに、データに null になりうる値や標準的でないデータ型が含まれる場合です。

`sortFn` 列オプションを使えば、列ごとにカスタムのソート関数を指定できます。

デフォルトでは、6つの組み込みソート関数から選べます。

- `alphanumeric` - 英数字が混在する値を、大文字と小文字を区別せずにソートします。遅いですが、文字列に自然順でソートすべき数字が含まれる場合はより正確です。
- `alphanumericCaseSensitive` - 英数字が混在する値を、大文字と小文字を区別してソートします。遅いですが、文字列に自然順でソートすべき数字が含まれる場合はより正確です。
- `text` - テキスト（文字列）の値を、大文字と小文字を区別せずにソートします。速いですが、文字列に自然順でソートすべき数字が含まれる場合は正確さが落ちます。
- `textCaseSensitive` - テキスト（文字列）の値を、大文字と小文字を区別してソートします。速いですが、文字列に自然順でソートすべき数字が含まれる場合は正確さが落ちます。
- `datetime` - 時刻でソートします。値が `Date` オブジェクトの場合に使います。
- `basic` - 基本的な（標準の）`a > b ? 1 : a < b ? -1 : 0` という比較でソートします。もっとも高速なソート関数ですが、もっとも正確とは限りません。

独自のカスタムソート関数を定義することもできます。`sortFn` 列オプションにインラインで書くか、`createSortedRowModel` に渡すソート関数の登録先に名前付きで登録します。

#### カスタムのソート関数 {#custom-sorting-functions}

カスタムのソート関数は、`createSortedRowModel` に渡す登録先に登録する場合でも、`sortFn` 列オプションに直接渡す場合でも、次のシグネチャにする必要があります。

```tsx
//optionally use the SortFn to infer the parameter types
const myCustomSortFn: SortFn<TFeatures, TData> = (
  rowA: Row<TFeatures, TData>,
  rowB: Row<TFeatures, TData>,
  columnId: string,
) => {
  return //-1, 0, or 1 - access any row data using rowA.original and rowB.original
}
```

> [!NOTE]
> 比較関数は、列が降順か昇順かを考慮する必要はありません。そのロジックは行モデルが受け持ちます。`sortFn` の関数は、一貫した比較を返しさえすれば十分です。

どのソート関数も2つの行と列 ID を受け取り、列 ID を使って2つの行を比較し、昇順を基準に `-1`、`0`、`1` のいずれかを返すことが求められます。早見表は次のとおりです。

| 戻り値 | 昇順での意味 |
| ------ | --------------- |
| `-1`   | `a < b`         |
| `0`    | `a === b`       |
| `1`    | `a > b`         |

```tsx
const myCustomSortFn: SortFn<typeof features, MyData> = (
  rowA,
  rowB,
  columnId,
) =>
  rowA.original[columnId] > rowB.original[columnId]
    ? 1
    : rowA.original[columnId] < rowB.original[columnId]
      ? -1
      : 0

const features = tableFeatures({
  rowSortingFeature,
  sortedRowModel: createSortedRowModel(),
  sortFns: {
    alphanumeric: sortFn_alphanumeric,
    datetime: sortFn_datetime,
    myCustomSortFn,
  },
})

const columns = [
  {
    header: () => 'Name',
    accessorKey: 'name',
    sortFn: 'alphanumeric', // use built-in sorting function by name
  },
  {
    header: () => 'Age',
    accessorKey: 'age',
    sortFn: 'myCustomSortFn', // reference a custom sorting function registered in features
  },
  {
    header: () => 'Birthday',
    accessorKey: 'birthday',
    sortFn: 'datetime', // recommended for date columns
  },
  {
    header: () => 'Profile',
    accessorKey: 'profile',
    // use custom sorting function directly
    sortFn: (rowA, rowB, columnId) => {
      return rowA.original.someProperty - rowB.original.someProperty
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

> **TypeScript に関する注意:** `sortFn: 'myCustomSortFn'` のような文字列での参照を型チェックに通すには、（上の例のように）`tableFeatures` の `sortFns` スロットに関数を登録してください。あるいは、`sortFn` 列オプションに関数を直接渡せば、登録先をまったく使わずに済みます。

#### ソート関数の振る舞いをカスタマイズする {#customize-sorting-function-behavior}

ソート関数には、オプションで関数自体に付けるプロパティを1つ指定できます。

- `sortFn.resolveDataValue` - 2つの値を比較する前に、各行の値を正規化します。`constructSortFn` ヘルパーで作ったすべてのソート関数で有効で、組み込みのソート関数もすべてこれに含まれます。

`constructSortFn` ヘルパーは、値どうしを比較する関数（`sort`）と、このオプションのリゾルバーからソート関数を組み立てます。比較を `sort` に、正規化を `resolveDataValue` に分けておけば、既存のソート関数の変種を作るときはリゾルバーを差し替えるだけで済みます。定義は返される関数に付いているので、`constructSortFn` で作ったソート関数ならどれでも展開して、違う部分だけを上書きできます。

たとえば、ダイアクリティカルマーク（アクセント記号など）を無視する `alphanumeric` を作れば、「Éric Bernard」は「Zak O'Sullivan」の後ではなく「Eric Brandon」の隣に並びます。

```tsx
const stripDiacritics = (value: string) =>
  value.normalize('NFD').replace(/\p{Diacritic}/gu, '')

const alphanumericIgnoreDiacritics = constructSortFn({
  ...sortFn_alphanumeric, // reuse the comparator
  resolveDataValue: (value) =>
    stripDiacritics(sortFn_alphanumeric.resolveDataValue!(value)),
})

const features = tableFeatures({
  rowSortingFeature,
  sortedRowModel: createSortedRowModel(),
  sortFns: { alphanumeric: sortFn_alphanumeric, alphanumericIgnoreDiacritics },
})
```

新しいソート関数を一から定義するときも、同じやり方が使えます。

```tsx
const byLastName = constructSortFn({
  sort: (dataValueA, dataValueB) =>
    dataValueA === dataValueB ? 0 : dataValueA > dataValueB ? 1 : -1,
  resolveDataValue: (value) =>
    String(value ?? '')
      .split(' ')
      .at(-1) ?? '',
})
```

### ソートをカスタマイズする {#customize-sorting}

ソートの UX や振る舞いをさらにカスタマイズするためのテーブルオプションと列オプションがたくさんあります。

#### ソートを無効にする {#disable-sorting}

`enableSorting` 列オプションまたはテーブルオプションを使うと、特定の列またはテーブル全体でソートを無効にできます。

```tsx
const columns = [
  {
    header: () => 'ID',
    accessorKey: 'id',
    enableSorting: false, // disable sorting for this column
  },
  {
    header: () => 'Name',
    accessorKey: 'name',
  },
  //...
]
//...
const table = useTable({
  features,
  columns,
  data,
  enableSorting: false, // disable sorting for the entire table
})
```

#### ソートの方向 {#sorting-direction}

`toggleSorting` 系の API で列のソートを切り替えていくとき、最初のソート方向はデフォルトで、文字列の列なら昇順、数値の列なら降順です。この振る舞いは `sortDescFirst` 列オプションまたはテーブルオプションで変えられます。

```tsx
const columns = [
  {
    header: () => 'Name',
    accessorKey: 'name',
    sortDescFirst: true, //sort by name in descending order first (default is ascending for string columns)
  },
  {
    header: () => 'Age',
    accessorKey: 'age',
    sortDescFirst: false, //sort by age in ascending order first (default is descending for number columns)
  },
  //...
]
//...
const table = useTable({
  features,
  columns,
  data,
  sortDescFirst: true, //sort by all columns in descending order first (default is ascending for string columns and descending for number columns)
})
```

> [!NOTE]
> null になりうる値を含む列では、`sortDescFirst` 列オプションを明示的に設定したほうがよいかもしれません。列に null になりうる値が含まれていると、テーブルはその列が数値か文字列かを正しく判断できないことがあります。

#### ソートを反転する {#invert-sorting}

ソートの反転は、デフォルトのソート方向を変えることとは違います。ある列で `invertSorting` 列オプションが `true` の場合、「desc/asc」のソートの状態は通常どおり切り替わりますが、実際の行の並びは反転します。順位（1位、2位、3位）やゴルフのスコアのように、数値が小さいほど良いという逆向きの尺度を持つ値に便利です。

```tsx
const columns = [
  {
    header: () => 'Rank',
    accessorKey: 'rank',
    invertSorting: true, // invert the sorting for this column. 1st -> 2nd -> 3rd -> ... even if "desc" sorting is applied
  },
  //...
]
```

#### undefined の値のソート {#sort-undefined-values}

undefined の値は、`sortUndefined` 列オプションまたはテーブルオプションに応じて、リストの先頭か末尾に並べられます。この振る舞いは、ユースケースに合わせてカスタマイズできます。

指定しない場合、`sortUndefined` のデフォルト値は `1` で、undefined の値は低い優先度（降順）でソートされます。昇順の場合、undefined はリストの末尾に来ます。

- `'first'` - undefined の値をリストの先頭に寄せます
- `'last'` - undefined の値をリストの末尾に寄せます
- `false` - undefined の値を特別扱いせず、ほかの値と同じようにソート関数に渡します。undefined の扱いはソート関数の責任になります
- `-1` - undefined の値を高い優先度（昇順）でソートします（昇順の場合、undefined はリストの先頭に来ます）
- `1` - undefined の値を低い優先度（降順）でソートします（昇順の場合、undefined はリストの末尾に来ます）

> [!NOTE]
> `'first'` と `'last'` のオプションは v9 で使えます。

```tsx
const columns = [
  {
    header: () => 'Rank',
    accessorKey: 'rank',
    sortUndefined: -1, // 'first' | 'last' | 1 | -1 | false
  },
]
```

#### ソートの解除 {#sorting-removal}

デフォルトでは、列のソートの状態を切り替えていく途中でソートを解除できるようになっています。この振る舞いは `enableSortingRemoval` テーブルオプションで無効にできます。常に少なくとも1つの列がソートされているようにしたい場合に便利です。

`getToggleSortingHandler` または `toggleSorting` の API を使ったときのデフォルトの振る舞いでは、ソートの状態は次のように切り替わります（最初の方向は、[前述](#sorting-direction) のとおり列のデータ型と `sortDescFirst` オプションによって決まります。ここでは文字列の列の例を示します）。

`'none' -> 'asc' -> 'desc' -> 'none' -> 'asc' -> 'desc' -> ...`

ソートの解除を無効にすると、最初にソートした後は `'none'` の状態が飛ばされます。

`'none' -> 'asc' -> 'desc' -> 'asc' -> 'desc' -> ...`

列がいったんソートされ、`enableSortingRemoval` が `false` であれば、その列のソートを切り替えてもソートが解除されることはありません。ただし、ユーザーが別の列でソートし、それが複数列ソートのイベントでない場合は、前の列のソートは解除され、新しい列だけにソートが適用されます。

> 常に少なくとも1つの列がソートされているようにしたい場合は、`enableSortingRemoval` を `false` にしてください。

```tsx
const table = useTable({
  features,
  columns,
  data,
  enableSortingRemoval: false, // disable the ability to remove sorting on columns (sorting can never return to 'none' once applied)
})
```

#### 複数列ソート {#multi-sorting}

`column.getToggleSortingHandler` API を使っている場合、複数の列で同時にソートする機能はデフォルトで有効です。ユーザーが `Shift` キーを押しながら列のヘッダーをクリックすると、テーブルはすでにソートされている列に加えて、その列でもソートします。`column.toggleSorting` API を使う場合は、複数列ソートを使うかどうかを手動で渡す必要があります（`column.toggleSorting(desc, multi)`）。

##### 複数列ソートを無効にする {#disable-multi-sorting}

`enableMultiSort` 列オプションまたはテーブルオプションを使うと、特定の列またはテーブル全体で複数列ソートを無効にできます。特定の列で複数列ソートを無効にすると、その列でソートしたときに既存のソートがすべてその列のソートに置き換わります。

```tsx
const columns = [
  {
    header: () => 'Created At',
    accessorKey: 'createdAt',
    enableMultiSort: false, // always sort by just this column if sorting by this column
  },
  //...
]
//...
const table = useTable({
  features,
  columns,
  data,
  enableMultiSort: false, // disable multi-sorting for the entire table
})
```

##### 複数列ソートのきっかけをカスタマイズする {#customize-multi-sorting-trigger}

デフォルトでは、`Shift` キーで複数列ソートになります。この振る舞いは `isMultiSortEvent` テーブルオプションで変えられます。カスタム関数から `true` を返せば、すべてのソートイベントで複数列ソートにすることもできます。

```tsx
const table = useTable({
  features,
  columns,
  data,
  isMultiSortEvent: (e) => true, // normal click triggers multi-sorting
  //or
  isMultiSortEvent: (e) => e.ctrlKey || e.shiftKey, // also use the `Ctrl` key to trigger multi-sorting
})
```

##### 複数列ソートの上限 {#multi-sorting-limit}

デフォルトでは、同時にソートできる列の数に上限はありません。`maxMultiSortColCount` テーブルオプションで上限を設定できます。

```tsx
const table = useTable({
  features,
  columns,
  data,
  maxMultiSortColCount: 3, // only allow 3 columns to be sorted at once
})
```

##### 複数列ソートの解除 {#multi-sorting-removal}

デフォルトでは、複数列ソートを解除できるようになっています。この振る舞いは `enableMultiRemove` テーブルオプションで無効にできます。

```tsx
const table = useTable({
  features,
  columns,
  data,
  enableMultiRemove: false, // disable the ability to remove multi-sorts
})
```

### データが変わったときにソートをリセットする {#reset-sorting-when-data-changes}

デフォルトでは、`data` オプションが変わってもソートの状態は保たれます。新しいデータの参照が処理されるたびにソートをリセットしたい場合は、`autoResetSorting: true` を設定します。リセットすると `initialState.sorting` に戻り、初期値が指定されていなければ空のソートの状態になります。

このオプションが反応するのはデータの変更だけです。ソート、フィルター、グループ化を変えてもリセットは起きません。グローバルな `autoResetAll` オプションを明示的に設定すると、`autoResetSorting` より優先されます。

このオプションを手動（サーバーサイド）のソートと組み合わせるときは注意してください。サーバーのレスポンスは通常 `data` を置き換えるので、リセットを有効にすると、そのレスポンスを要求したソートの状態がすぐに消えてしまうことがあります。

### ソートの API {#sorting-apis}

UI やほかのロジックとつなぐために使える、ソート関連の API がたくさんあります。ソートの API の一覧と、それぞれの使い道を示します。

- `table.setSorting` - ソートの状態を直接設定します。
- `table.resetSorting` - ソートの状態を初期状態に戻すか、空にします。

- `column.getCanSort` - 列のソート UI を有効・無効にするのに便利です。
- `column.getIsSorted` - 列のソート状態を視覚的に示すインジケーターを表示するのに便利です。

- `column.getToggleSortingHandler` - 列のソート UI をつなぐのに便利です。ソートの矢印（アイコンボタン）やメニュー項目、あるいは列のヘッダーセル全体に付けます。このハンドラーは正しい引数で `column.toggleSorting` を呼び出します。
- `column.toggleSorting` - 列のソート UI をつなぐのに便利です。`column.getToggleSortingHandler` の代わりに使う場合は、複数列ソートを使うかどうかを手動で渡す必要があります（`column.toggleSorting(desc, multi)`）。
- `column.clearSorting` - 特定の列の「ソートを解除」ボタンやメニュー項目に便利です。

- `column.getNextSortingOrder` - 列が次にどの方向でソートされるかを表示するのに便利です（ツールチップ、メニュー項目、aria-label などで asc/desc/解除を示す）。
- `column.getFirstSortDir` - 列が最初にどの方向でソートされるかを表示するのに便利です（ツールチップ、メニュー項目、aria-label などで asc/desc を示す）。
- `column.getAutoSortDir` - 列の最初のソート方向が昇順か降順かを判定します。
- `column.getAutoSortFn` - ソート関数が指定されていない場合に、列のデフォルトのソート関数を見つけるために内部で使われます。
- `column.getSortFn` - 列で実際に使われているソート関数を返します。

- `column.getCanMultiSort` - 列の複数列ソート UI を有効・無効にするのに便利です。
- `column.getSortIndex` - 複数列ソートのときに、その列のソート順（1番目、2番目、3番目など、何番目にソートされる列か）をバッジやインジケーターで表示するのに便利です。
