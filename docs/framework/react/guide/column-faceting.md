---
title: ファセット（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React のサンプルを参照してください。

- [ファセットフィルター](https://tanstack.com/table/latest/docs/framework/react/examples/filters-faceted)
- [バケット分けしたファセットフィルター](https://tanstack.com/table/latest/docs/framework/react/examples/filters-faceted-bucketed)

### ファセットのセットアップ {#faceting-setup}

ファセットの機能を使うためのテーブルのセットアップ方法は次のとおりです。ファセットの機能を追加すると、関連する API が使えるようになります。クライアントサイドのファセットを使う場合は、`filteredRowModel` と `facetedRowModel` も、それぞれの機能の後に設定してください。行モデルのスロットは型チェックされるためです。

```tsx
import {
  useTable,
  tableFeatures,
  columnFacetingFeature,
  columnFilteringFeature,
  createFacetedRowModel,
  createFacetedUniqueValues,
  createFacetedMinMaxValues,
  createFilteredRowModel,
  filterFns,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnFacetingFeature,
  columnFilteringFeature,
  filteredRowModel: createFilteredRowModel(), // if using client-side filtering
  // manualFiltering: true, // if using manual server-side filtering
  facetedRowModel: createFacetedRowModel(), // if using client-side faceting
  facetedUniqueValues: createFacetedUniqueValues(),
  facetedMinMaxValues: createFacetedMinMaxValues(),
  filterFns,
})

const table = useTable({
  features,
  columns,
  data,
})
```

## ファセット（React）ガイド {#faceting-react-guide}

### ファセットとは {#what-is-faceting}

ファセットは、フィルタリングの UI を組み立てるのに使える情報を導き出します。ある列について、ファセットは次のような問いに答えられます。

- どの値が選択肢として残っているか
- 各値は何回出現するか
- 対象の行の中で、最小値と最大値はいくつか
- 独自のファセット計算にはどの行を使えばよいか

たとえばアプリケーションでは、ファセットを使って次のようなプランのフィルターを描画できます。

```text
Plan
☐ Free        128
☐ Pro          47
☐ Enterprise    9
```

プラン名と件数は、テーブルのファセット行モデルから導き出されます。`Region = Europe` のように別の列のフィルターが変わると、プランの件数はその地域の行だけを対象にした値に更新されます。

ファセットがテーブルにフィルターを適用することはありません。ファセットが提供するのは、フィルター UI を組み立てるための値・件数・範囲・行です。フィルターの状態を持ち、選ばれたフィルター値に一致する行を決めるのは、列フィルタリングの機能です。

#### ファセットと行の集計の違い {#faceting-vs-row-aggregation}

ファセットも行の集計もデータを要約しますが、目的が異なります。ファセットは、選べる値・出現回数・数値の範囲といった、フィルターの操作部品のためのメタデータを作ります。行の集計は、合計・平均・総計など、行の集まりから結果の値を計算し、フッターやグループ行に表示します。

ファセットの件数が集計行を作ることはなく、列の `aggregationFn` も使いません。これらの機能は、次のように見分けると分かりやすくなります。

- フィルタリングが答えるのは「どの行が残るか」
- ファセットが答えるのは「どのフィルターの選択肢が残るか」
- 行の集計が答えるのは「これらの行からどんな要約値を計算できるか」

### 列のファセットがフィルターにどう反応するか {#how-column-faceting-responds-to-filters}

列のファセット行モデルには、その列自身のフィルターを除く、適用されているすべてのフィルターを通過した行が含まれます。これにより、ユーザーがファセットを操作している間も、ほかの選択肢を表示し続けられます。

`Region` と `Plan` のフィルターがあるテーブルで考えてみましょう。

1. ユーザーが `Region = Europe` を選びます。
2. `Plan` のファセットは地域のフィルターを適用し、プランの件数を計算し直します。
3. ユーザーが `Plan = Pro` を選びます。
4. テーブルにはヨーロッパの Pro の行だけが表示されます。
5. `Plan` のファセットは自身の `Plan` フィルターを除外するため、選択肢は引き続きヨーロッパのすべての行から計算されます。

ほかのファセットには、選ばれたプランのフィルターが適用されます。たとえば `Status` のファセットは、ヨーロッパの Pro の行だけを対象にするようになります。この仕組みによって、複数のファセットが互いに絞り込み合えます。

クライアントサイドのファセットでこの動作を実現するには、`filteredRowModel` と `facetedRowModel` の両方が必要です。フィルター済みの行モデルがないと、ファセット行モデルはフィルター適用前の行で代用するため、その値はほかの列のフィルターに反応しません。

### ファセットの API {#faceting-apis}

作ろうとしているフィルター UI に合ったファセットの API を使ってください。

| API                               | 結果                                  | よくある用途                                            |
| --------------------------------- | --------------------------------------- | ------------------------------------------------------ |
| `column.getFacetedRowModel()`     | ほかの有効なフィルターを通過した行 | 独自のファセット計算                              |
| `column.getFacetedUniqueValues()` | 値から出現回数への `Map`  | チェックボックス、セレクトメニュー、オートコンプリートの候補 |
| `column.getFacetedMinMaxValues()` | `[min, max]` のタプル、または `undefined`     | 数値入力、範囲スライダー                        |

これらの API は、`tableFeatures` に登録した行モデルのファクトリーによって有効になります。

- クライアントサイドのファセットには `createFacetedRowModel()` が必要です。
- 一意な値と件数には `createFacetedUniqueValues()` が必要です。
- 数値の最小値と最大値には `createFacetedMinMaxValues()` が必要です。

テーブルで使うファクトリーだけを登録してください。このガイドの冒頭にあるセットアップの全体例では、3つすべてを登録しています。

### 一意な値と件数 {#unique-values-and-counts}

`column.getFacetedUniqueValues()` は、キーがファセット値、値が出現回数の `Map` を返します。この Map をソート済みの配列に変換すれば、オートコンプリートやセレクトの操作部品に使えます。

```ts
const suggestions = Array.from(column.getFacetedUniqueValues().entries())
  .sort(([valueA], [valueB]) => String(valueA).localeCompare(String(valueB)))
  .slice(0, 5_000)
```

各要素には、値とその件数の両方が含まれます。

```tsx
return (
  <select>
    {suggestions.map(([value, count]) => (
      <option key={String(value)} value={String(value)}>
        {String(value)} ({count})
      </option>
    ))}
  </select>
)
```

スカラー値の列では通常、1つの行が1つの値を返すため、出現回数はそのまま行数にもなります。列の `getUniqueValues` オプションを定義すると、1つの行から複数のファセット値を返せます。その場合、件数は出現回数を表し、その合計は行数より大きくなることがあります。

```tsx
columnHelper.accessor('tags', {
  header: 'Tags',
  getUniqueValues: (row) => row.tags,
})
```

件数を行数として扱いたい場合は、`getUniqueValues` が1つの行につき同じ値を2回以上返さないようにしてください。

### React でのリアクティブなファセットの操作部品 {#reactive-facet-controls-in-react}

ファセット値は、参照が変わらない `column` オブジェクトを受け取るフィルターコンポーネントの中で読み取ることがよくあります。そのコンポーネントがフィルターの状態を購読するようにして、ほかのファセットが変わったときに更新されるようにしてください。`table.Subscribe` を使うと、購読をファセットの操作部品を描画するコンポーネントの中だけに閉じ込められます。

```tsx
function FacetOptions({ table, column }) {
  return (
    <table.Subscribe selector={(state) => state.columnFilters}>
      {() => {
        const values = Array.from(column.getFacetedUniqueValues().entries())

        return values.map(([value, count]) => (
          <label key={String(value)}>
            <input
              type="checkbox"
              checked={isSelected(value)}
              onChange={() => toggleValue(value)}
            />
            {String(value)} ({count})
          </label>
        ))
      }}
    </table.Subscribe>
  )
}
```

選ばれた値がどの行に一致するかを決めるのは、引き続きその列のフィルター関数です。フィルター関数とフィルターの状態については[列フィルタリングガイド](./column-filtering)を、完全な実装例については[ファセットフィルターのサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/filters-faceted)を参照してください。

### 最小値と最大値 {#minimum-and-maximum-values}

`column.getFacetedMinMaxValues()` は、ほかの有効なフィルターを適用した後に残る数値の範囲を返します。数値が1つもない場合は `undefined` を返します。

```tsx
const [min, max] = column.getFacetedMinMaxValues() ?? [0, 1]

return (
  <input
    type="range"
    min={min}
    max={max}
    value={currentValue}
    onChange={(event) => column.setFilterValue(Number(event.target.value))}
  />
)
```

最小値と最大値は、フィルター UI で選べる値の範囲を表します。選ばれた値や範囲で行をどう絞り込むかは、列のフィルター関数が決めます。

### 連続値のためのバケット分けしたファセット {#bucketed-faceting-for-continuous-values}

生の一意な値が常に役立つとは限りません。日付・ファイルサイズ・所要時間・価格・計測値などは、異なる値が数百、数千と生じることがあります。こうした列は、値を意味のある区分（バケット）に振り分けたほうがフィルターしやすくなります。

```text
Last login
☐ Today
☐ Yesterday
☐ This week
☐ This month
☐ Older
```

列の `getUniqueValues` オプションを使うと、ファセット用にはバケットのキーを返しつつ、描画やほかのテーブル機能には元のアクセサーの値を使い続けられます。

```tsx
type StorageBucket =
  'under-1-gb' | '1-to-10-gb' | '10-to-100-gb' | '100-gb-plus'

const GB = 1024 ** 3

function getStorageBucket(value: number): StorageBucket {
  if (value < GB) return 'under-1-gb'
  if (value < 10 * GB) return '1-to-10-gb'
  if (value < 100 * GB) return '10-to-100-gb'
  return '100-gb-plus'
}

const storageBucketFilter = constructFilterFn({
  resolveDataValue: (value) => getStorageBucket(value as number),
  filter: (bucket, selected: Array<StorageBucket>) => selected.includes(bucket),
  autoRemove: (selected: Array<StorageBucket>) => selected.length === 0,
})

columnHelper.accessor('storageBytes', {
  header: 'Storage',
  getUniqueValues: (row) => [getStorageBucket(row.storageBytes)],
  filterFn: storageBucketFilter,
})
```

ファセットとフィルタリングには、同じバケットの定義を使ってください。そうすれば、表示される件数と、各バケットで選ばれる行が一致します。列は生の数値を保持したままなので、ファセットのためだけに非表示の派生列を作る必要はありません。日付と容量のバケットフィルターの完全な実装は、[バケット分けしたファセットフィルターのサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/filters-faceted-bucketed)を参照してください。

### クライアントサイドのファセットとパフォーマンス {#client-side-faceting-and-performance}

組み込みのクライアントサイドのファセット行モデルはメモ化されています。入力となる行や関係するフィルターの状態が変わったときに計算し直されます。それでも、計算コストはテーブルの行数・列数・一意な値の数に左右されます。

一意な値が多い列では、次の方法を検討してください。

- Map のすべての要素ではなく、先頭の値や関連性の高い値だけを描画する
- 長い一覧を描画する前に、ユーザーが選べる値を検索できるようにする
- 連続値や種類の多い値を、役に立つ範囲のバケットに振り分ける
- データセット全体がブラウザーにない場合は、ファセットをサーバーに移す

大きなファセットの Map を、無関係なコンポーネントで何度もソートしたり変換したりするのは避けてください。ファセットの選択肢は、関係するフィルターの状態を購読するコンポーネントの近くで導き出し、描画してください。

### サーバーサイドの独自ファセット {#custom-server-side-faceting}

フィルタリングをサーバーで行う場合、ブラウザーに読み込まれた行だけでは、完全なファセット値や件数を計算するのに情報が足りないことがあります。その場合は、サーバーでファセットを計算し、独自の `facetedUniqueValues` と `facetedMinMaxValues` のファクトリーを渡してください。

各ファクトリーはテーブルと列 ID を受け取り、ファセットの結果を返す関数を返します。通常の列の API は、サーバーから提供された値を返すようになります。

ファクトリーはテーブルと列ごとに一度だけ解決されますが、各ファクトリーが返す関数は読み取りのたびに実行されます。テーブルはその結果をキャッシュしません。返す関数の中で（シグナル・ストア・`table.options.meta` から）最新の値を読み取るようにすれば、更新されたサーバーのファセットがすぐに反映されます。計算が重い場合は、ファクトリーの中でメモ化してください。

```ts
const facetingQuery = useQuery()

const features = tableFeatures({
  columnFacetingFeature,
  // The returned functions run on every read and table.options stays in
  // sync with the latest render, so read live data through options.meta
  facetedUniqueValues: (table, columnId) => () => {
    const serverFacets = table.options.meta?.serverFacets
    return new Map<string, number>(serverFacets?.uniqueValues[columnId] ?? [])
  },
  facetedMinMaxValues: (table, columnId) => () => {
    return table.options.meta?.serverFacets?.minMaxValues[columnId]
  },
})

const table = useTable({
  features,
  columns,
  meta: { serverFacets: facetingQuery.data },
  data,
})
```

組み込みの列のファセットと同じ動作にするには、ある列のためのサーバーへのクエリで、ほかの有効なフィルターは適用し、その列自身のフィルターは除外してください。こうすると、現在のファセットではほかの選択肢を選べるまま、ファセット同士で互いに絞り込めます。

TanStack Table のファセットの API を使わずに、ファセット値を取得してフィルターコンポーネントに直接渡すこともできます。

### グローバルファセット {#global-faceting}

グローバルファセットは、グローバルフィルタリングの対象になり得るすべての末端の列から値を導き出します。オートコンプリートの候補や、グローバルフィルターに関連するその他のメタデータに役立ちます。グローバルのファセット行モデルは、有効な列フィルターを適用し、グローバルフィルター自体は除外します。

テーブルでグローバルフィルタリングを使う場合は、`globalFilteringFeature` を登録して、行のフィルタリング処理でグローバルフィルターが評価されるようにしてください。列のファセットで使うのと同じファセットのファクトリーが、次のテーブルの API も支えています。

```ts
const globalFacetedRows = table.getGlobalFacetedRowModel().flatRows

const suggestions = Array.from(table.getGlobalFacetedUniqueValues().entries())

const [min, max] = table.getGlobalFacetedMinMaxValues() ?? [0, 1]
```

独自のファセットのファクトリーは、グローバルの要求に対して内部用の列 ID `__global__` を受け取ります。サーバーが列とグローバルで別々のファセット結果を返す場合は、この ID で処理を分けられます。

```ts
const features = tableFeatures({
  columnFacetingFeature,
  facetedUniqueValues: (_table, columnId) => () => {
    if (columnId === '__global__') {
      return new Map(globalFacets.uniqueValues)
    }

    return new Map(columnFacets[columnId]?.uniqueValues)
  },
})
```
