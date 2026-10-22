---
title: あいまい検索フィルター（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React の例を参照してください。

- [あいまい検索](https://tanstack.com/table/latest/docs/framework/react/examples/filters-fuzzy)

### あいまい検索フィルターの準備 {#fuzzy-filtering-setup}

あいまい検索フィルターの機能を使えるようにテーブルを準備する方法は次のとおりです。あいまい検索フィルターの機能を追加すると、関連する API が有効になります。クライアントサイドであいまい検索フィルターとソートを行う場合は、それぞれの機能のあとに `filteredRowModel` と `sortedRowModel` も設定してください。行モデルのスロットは型チェックされるためです。

```tsx
import {
  useTable,
  tableFeatures,
  columnFilteringFeature,
  globalFilteringFeature,
  rowSortingFeature,
  createFilteredRowModel,
  createSortedRowModel,
  metaHelper,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnFilteringFeature,
  globalFilteringFeature,
  rowSortingFeature,
  filteredRowModel: createFilteredRowModel(), // if using client-side filtering
  // manualFiltering: true, // if using manual server-side filtering
  sortedRowModel: createSortedRowModel(), // if using client-side sorting
  // manualSorting: true, // if using manual server-side sorting
  filterFns: { fuzzy: fuzzyFilter },
  sortFns: { fuzzy: fuzzySort },
  filterMeta: metaHelper<FuzzyFilterMeta>(),
})

const table = useTable({
  features,
  columns,
  data,
})
```

> [!NOTE]
> 上の `filterFns` と `sortFns` のレジストリには、このガイドで使う独自の `fuzzy` 関数だけを登録しています。組み込みのレジストリをまるごと展開する書き方（`filterFns: { ...filterFns, fuzzy: fuzzyFilter }`）も使えますが、組み込みの関数がすべてバンドルに含まれてしまいます。使う関数だけを登録するか、登録せずに列オプションの `filterFn` や `sortFn` に関数を直接渡してください。

## あいまい検索フィルター（React）ガイド {#fuzzy-filtering-react-guide}

あいまい検索フィルターは、おおよそ一致するかどうかでデータを絞り込む手法です。完全に一致するデータではなく、指定した値に似たデータを探したいときに役立ちます。

クライアントサイドのあいまい検索フィルターは、独自のフィルター関数を定義すれば実装できます。この関数は行・列 ID（columnId）・フィルター値を受け取り、その行を絞り込み後のデータに含めるかどうかを真偽値で返します。

あいまい検索フィルターはおもにグローバルフィルターと組み合わせて使いますが、個々の列に適用することもできます。ここでは、両方の場合の実装方法を説明します。

> [!NOTE]
> あいまい検索フィルターを使うには、`@tanstack/match-sorter-utils` ライブラリをインストールする必要があります。
> TanStack Match Sorter Utils は、Kent C. Dodds 氏による [match-sorter](https://github.com/kentcdodds/match-sorter) のフォークです。TanStack Table の行ごとにフィルタリングする方式とうまく連携できるように、フォークされました。

match-sorter 系のライブラリを使うかどうかは任意です。ただ、TanStack Match Sorter Utils ライブラリを使うと、あいまい検索フィルターに加えて、ライブラリが返す順位の情報を使ったソートもうまく行えます。これにより、検索クエリに最も近い行から順に並べられます。

### 独自のあいまい検索フィルター関数を定義する {#defining-a-custom-fuzzy-filter-function}

独自のあいまい検索フィルター関数の例を示します。まず、フィルターのメタ情報の形と、それを含む機能の型を定義します。

```typescript
import { rankItem } from '@tanstack/match-sorter-utils'
import type { RankingInfo } from '@tanstack/match-sorter-utils'
import type { FilterFn, RowData, TableFeatures } from '@tanstack/react-table'

interface FuzzyFilterMeta {
  itemRank?: RankingInfo
}

// A features type that carries the filterMeta shape
type FuzzyFeatures = TableFeatures & { filterMeta: FuzzyFilterMeta }

const fuzzyFilter: FilterFn<FuzzyFeatures, RowData> = (
  row,
  columnId,
  value,
  addMeta,
) => {
  // Rank the item
  const itemRank = rankItem(row.getValue(columnId), value)

  // Store the itemRank info
  addMeta?.({ itemRank })

  // Return if the item should be filtered in/out
  return itemRank.passed
}
```

この関数では、`@tanstack/match-sorter-utils` ライブラリの `rankItem` 関数で項目の順位を求めています。次に、その順位の情報を行のフィルターのメタ情報に保存し（`addMeta` コールバックは省略可能なので、オプショナルチェーンで呼び出します）、項目が順位の基準を満たしたかどうかを返します。

このフィルター関数を文字列の名前 `'fuzzy'` で参照し、保存するフィルターのメタ情報に型を付けるには、`tableFeatures` の呼び出しで `filterFns` スロットと `filterMeta` スロットの両方に登録します。

```typescript
import { tableFeatures, metaHelper } from '@tanstack/react-table'

const features = tableFeatures({
  columnFilteringFeature,
  globalFilteringFeature,
  rowSortingFeature,
  filteredRowModel: createFilteredRowModel(),
  sortedRowModel: createSortedRowModel(),
  filterFns: { fuzzy: fuzzyFilter },
  sortFns: { fuzzy: fuzzySort },
  filterMeta: metaHelper<FuzzyFilterMeta>(),
})
```

`declare module` による型の拡張は必要ありません。`filterFns` スロットと `filterMeta` スロットはこの features オブジェクトの中だけで有効で、このオブジェクトで作成したテーブルにしか影響しません。

### あいまい検索フィルターをグローバルフィルターで使う {#using-fuzzy-filtering-with-global-filtering}

あいまい検索フィルターをグローバルフィルターで使うには、`tableFeatures` の `filterFns` スロットにあいまい検索フィルター関数を登録し、テーブルの `globalFilterFn` オプションでそれを参照します。

```typescript
import {
  useTable,
  tableFeatures,
  columnFilteringFeature,
  globalFilteringFeature,
  rowSortingFeature,
  createFilteredRowModel,
  createSortedRowModel,
  metaHelper,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnFilteringFeature,
  globalFilteringFeature,
  rowSortingFeature,
  filteredRowModel: createFilteredRowModel(),
  sortedRowModel: createSortedRowModel(), // needed if you want sorting with fuzzy rank
  filterFns: { fuzzy: fuzzyFilter },
  sortFns: { fuzzy: fuzzySort },
  filterMeta: metaHelper<FuzzyFilterMeta>(),
})

const table = useTable({
  features,
  columns,
  data,
  globalFilterFn: 'fuzzy',
})
```

### あいまい検索フィルターを列フィルターで使う {#using-fuzzy-filtering-with-column-filtering}

あいまい検索フィルターを列フィルターで使うには、（上で示したように）`tableFeatures` の `filterFns` スロットにあいまい検索フィルター関数を登録します。そのうえで、列定義の `filterFn` オプションにあいまい検索フィルターを名前で指定します。

```typescript
const column = [
  {
    accessorFn: (row) => `${row.firstName} ${row.lastName}`,
    id: 'fullName',
    header: 'Full Name',
    cell: (info) => info.getValue(),
    filterFn: 'fuzzy', //using our custom fuzzy filter function
  },
  // other columns...
]
```

この例では、データの firstName フィールドと lastName フィールドを結合した列に、あいまい検索フィルターを適用しています。

#### あいまい検索フィルターと組み合わせたソート {#sorting-with-fuzzy-filtering}

あいまい検索フィルターを列フィルターで使うときは、順位の情報にもとづいてデータをソートしたくなることもあるでしょう。その場合は、独自のソート関数を定義します。

```typescript
import { compareItems } from '@tanstack/match-sorter-utils'
import { sortFn_alphanumeric } from '@tanstack/react-table'
import type { SortFn } from '@tanstack/react-table'

const fuzzySort: SortFn<FuzzyFeatures, Person> = (rowA, rowB, columnId) => {
  let dir = 0

  // Only sort by rank if the column has ranking information
  if (rowA.columnFiltersMeta[columnId]) {
    dir = compareItems(
      rowA.columnFiltersMeta[columnId].itemRank!,
      rowB.columnFiltersMeta[columnId].itemRank!,
    )
  }

  // Provide an alphanumeric fallback for when the item ranks are equal
  return dir === 0 ? sortFn_alphanumeric(rowA, rowB, columnId) : dir
}
```

この関数では、2つの行の順位の情報を比較しています。順位が同じ場合は、英数字順のソートにフォールバックします。

（上の準備の節で示したように）`tableFeatures` の `sortFns` スロットに `fuzzySort` を登録し、列定義で名前で参照します。

```typescript
{
  accessorFn: row => `${row.firstName} ${row.lastName}`,
  id: 'fullName',
  header: 'Full Name',
  cell: info => info.getValue(),
  filterFn: 'fuzzy', // using our custom fuzzy filter function (registered in features)
  sortFn: 'fuzzy', // using our custom fuzzy sort function (registered in features)
}
```

文字列で参照する代わりに、列オプションの `sortFn` に `fuzzySort` を関数として直接渡すこともできます。この場合、登録の手順は不要です。
