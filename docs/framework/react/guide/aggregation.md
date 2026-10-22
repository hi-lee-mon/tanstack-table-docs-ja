---
title: 集計（React）ガイド
---

## サンプル {#examples}

- [集計](https://tanstack.com/table/latest/docs/framework/react/examples/aggregation)
- [グループ化した集計](https://tanstack.com/table/latest/docs/framework/react/examples/grouped-aggregation)

集計は列のグループ化とは独立した機能です。列で合計や集計値を計算するときは、必ず `rowAggregationFeature` を登録してください。`columnGroupingFeature` は、テーブルで行もグループ化する場合にだけ別途追加します。

## 集計のセットアップ {#aggregation-setup}

登録するのは、名前で参照する組み込み関数だけで構いません。定義を列に直接渡す場合は、レジストリへの登録は不要です。

```tsx
import {
  rowAggregationFeature,
  aggregationFn_count,
  aggregationFn_extent,
  aggregationFn_mean,
  aggregationFn_sum,
  tableFeatures,
  useTable,
} from '@tanstack/react-table'

const features = tableFeatures({
  rowAggregationFeature,
  aggregationFns: {
    count: aggregationFn_count,
    extent: aggregationFn_extent,
    mean: aggregationFn_mean,
    sum: aggregationFn_sum,
  },
})

const table = useTable({
  features,
  columns,
  data,
})
```

集計機能はグループ化された行モデルを必要としません。そのため、グループ化をしない普通のテーブルでも、総計や、行の一部を対象にした独自の合計を出せます。

すべての組み込み関数を含む `aggregationFns` レジストリも互換性のために引き続き使えますが、組み込み関数がすべてバンドルされます。`stockFeatures` を使うテーブルにはすでに `rowAggregationFeature` が含まれています。ただし、列オプションで名前を指定する場合は、その名前に対応する定義を登録する必要があります。

## 列の集計 {#column-aggregations}

列には集計を1つ、または配列で複数指定できます。1つだけ指定するとスカラー値を返します。複数指定すると、集計名または記述子（descriptor）の `id` をキーとするオブジェクトを返します。

```ts
columnHelper.accessor('amount', {
  aggregationFn: 'sum',
})

columnHelper.accessor('score', {
  aggregationFn: ['count', 'mean', { id: 'range', aggregationFn: 'extent' }],
})
```

文字列による指定はこれまでどおり使えます。結果に安定した独自のキーやオプションが必要な場合は、記述子を使ってください。

スカラーの `aggregationFn` には、登録済みの名前、`'auto'`、またはインラインの定義を指定できます。集計の配列では、各要素に一意で安定した id が必要です。id の重複、記述子の id の欠落、未登録の名前があると、開発時に警告が出ます。該当するキーは残り、値は `undefined` になります。

複数の集計結果は、型を指定して読み取れます。

```ts
const scoreColumn = columnHelper.accessor('score', {
  aggregationFn: ['count', 'mean', { id: 'range', aggregationFn: 'extent' }],
  footer: ({ column }) => {
    const result = column.getAggregationValue<{
      count: number
      mean: number | undefined
      range: [number | undefined, number | undefined]
    }>()

    return `${result.count} values; mean ${result.mean}; range ${result.range}`
  },
})
```

## 総計と行の一部の集計 {#grand-totals-and-row-subsets}

`column.getAggregationValue()` を引数なしで呼ぶと、デフォルトの「グループ化前の行モデル」を集計します。フィルタリングは反映されますが、グループ化・ソート・展開・ページネーションはこのデフォルトの合計を変えません。

```ts
footer: ({ column }) => column.getAggregationValue<number>().toLocaleString()
```

別の行の集合を対象にするには、任意の行モデルの行を含むオプションオブジェクトを1つ渡します。

```ts
column.getAggregationValue({ rows: table.getCoreRowModel().rows })
column.getAggregationValue({ rows: table.getRowModel().rows })
column.getAggregationValue({ rows: table.getFilteredSelectedRowModel().rows })
column.getAggregationValue({ rows: table.getCoreRowModel().rows.slice(0, 3) })
column.getAggregationValue({ rows: table.getCoreRowModel().rows, maxDepth: 1 })
```

深さは、渡した行の配列を基準にした相対値です。`0` はそれらのルート行を、`1` はその直下のサブ行を選びます。以降も同様です。選択の結果は、重複のない「最前線（frontier）」になります。つまり、最大の深さに届く前に終わる枝からは、その枝で最も深い行が使われます。`Infinity` を指定すると末端の行を選びます。

キャッシュされるデフォルトの呼び出しの深さは、列の `maxAggregationDepth` で設定します（デフォルトは `0`）。明示的に上書きしたい場合は、オプションオブジェクトで `maxDepth` を渡します。列に設定したすべての集計は、同じ選択された行を受け取ります。行を明示的に渡した呼び出しは毎回再計算されます。デフォルトの呼び出しは、行モデル・深さ・レジストリ・列の集計オプションに基づいてキャッシュされます。

`table.getMaxSubRowDepth()` は、コア行モデルの構造上の最大の深さを返します。サブ行の最前線のうち最も深いものより1段手前で止めるには、次のようにします。

```ts
const maxDepth = Math.max(0, table.getMaxSubRowDepth() - 1)
column.getAggregationValue({
  rows: table.getCoreRowModel().rows,
  maxDepth,
})
```

## グループ化した集計 {#grouped-aggregation}

グループ化した集計は、2つの独立した機能を組み合わせて実現します。両方を登録し、グループ化された行モデルのスロットを追加したうえで、グループごとの値を出したい列に集計関数を設定します。

```ts
const features = tableFeatures({
  rowAggregationFeature,
  columnGroupingFeature,
  groupedRowModel: createGroupedRowModel(),
  aggregationFns: { sum: aggregationFn_sum },
})

columnHelper.accessor('visits', {
  aggregationFn: 'sum',
  aggregatedCell: ({ getValue }) => getValue<number>().toLocaleString(),
  footer: ({ column }) => column.getAggregationValue<number>().toLocaleString(),
})
```

列オプション `aggregatedCell` は、グループ化によって生成された合成の行に集計値を描画します。グループの集計セルかどうかは `cell.getIsAggregated()` で判定します。フッターの描画には、アダプターの通常のフッターレンダラーを使います。グループ化だけを使うテーブルでは `cell.getIsAggregated()` は公開されません。このメソッドは `rowAggregationFeature` に属しているためです。

## 独自の集計定義 {#custom-aggregation-definitions}

独自の集計は、コンテキストを受け取る形の定義です。`rows` には `maxDepth` で選ばれた重複のない最前線が入り、`getValue(row)` で現在の列の値を読み取れます。

```ts
const joined = constructAggregationFn<any, any, string, string>({
  aggregate: ({ rows, getValue }) =>
    rows
      .map((row) => getValue(row))
      .filter(Boolean)
      .join(', '),
})
```

コンテキストには `column`、`columnId`、`maxDepth`、`table` も含まれます。グループ化した集計の最中は、さらに `groupingRow` と `subRows` も含まれます。ルートの集計や、呼び出し側が行を渡した集計では、これらのプロパティは含まれません。グループ化の深さは `groupingRow.depth` です。`subRows` にはそのグループ化レベルの直下の行が入るため、深さで選ばれた `rows` の代わりに、直下のサブ行を明示的に使う集計も書けます。

```ts
const subRowCount = constructAggregationFn<any, any, unknown, number>({
  aggregate: ({ subRows, rows }) => (subRows ?? rows).length,
})
```

最も末端のグループ化レベルでは、`subRows` には直下のデータ行が入ります。入れ子になったレベルでは、直下の合成サブ行グループが入ります。組み込みの集計定義はすべて、深さで選ばれた同じ `rows` を使います。`subRows` は、独自の定義でグループ行の直下の構造上の子を意図して使いたいときのために用意されています。

計算済みのサブ行の結果を組み合わせたほうが効率よく求められる結果には、`merge` 関数を指定します。

```ts
const sum = constructAggregationFn<any, any, unknown, number>({
  aggregate: ({ rows, getValue }) =>
    rows.reduce((total, row) => {
      const value = getValue(row)
      return total + (typeof value === 'number' ? value : 0)
    }, 0),
  merge: ({ subRowResults }) =>
    subRowResults.reduce((total, value) => total + value, 0),
})
```

`merge` では、`subRowResults[i]` は `subRows[i]` について先に計算された集計結果です。`merge` がない場合、入れ子のグループ化では、グループの深さで選ばれた `rows` と直下の `subRows` の両方を渡して `aggregate` を呼びます。このコンテキストを受け取る形は、以前の呼び出し可能な集計シグネチャと、その `fromRows` と `resolveDataValue` プロパティを置き換えるものです。両方の行の集合には引き続きアクセスできます。

## サーバーや外部から値を渡す {#providing-server-or-external-values}

列は、ローカルで計算する前に集計値の要求を処理できます。

```ts
const amountColumn = columnHelper.accessor('amount', {
  aggregationFn: 'sum',
  getAggregationValue: ({ rows }) => {
    if (rows !== undefined) return undefined // use local fallback for overrides
    return { value: serverTotals.amount }
  },
})
```

`{ value }` を返すと、その要求は処理済みとみなされます。`{ value: undefined }` を返した場合も同じです。`undefined` を返すと、ローカルでの計算にフォールバックします。同じプロバイダーを `defaultColumn` に設定すると、すべての列で共有できます。

`manualAggregation: true` を設定すると、`column.getAggregationValue()` のローカルでのフォールバックが無効になります。これは、グループ化された行モデルを実行するかどうかを制御する `manualGrouping` とは別の設定です。データ処理の流れ全体をどこで実行するかの選び方は、[クライアントサイドとサーバーサイドのガイド](../../../guide/client-side-vs-server-side)を参照してください。

## 組み込みの定義 {#built-in-definitions}

- `sum`: 数値を合計します。数値以外は0として扱います。
- `count`: 行数を数えます。
- `min` / `max`: 数値または Date の最小値・最大値を求めます。
- `extent`: `[min, max]` を返します。入力が空の場合は `[undefined, undefined]` を返します。
- `mean`: null でない数値、および数値として扱える値の平均を求めます。
- `median`: すべての行の値が数値である必要があります。
- `unique` / `uniqueCount`: JavaScript の `Set` の仕様に従います。
- `first` / `last`: 位置に応じた値を返します。null や undefined の値もそのまま返します。

`aggregationFn: 'auto'` は、コア行の最初の値を調べます。数値なら登録済みの `sum`、Date なら登録済みの `extent` に解決され、それ以外の値では集計は解決されません。

## Web Worker {#web-workers}

Worker で処理するグループ化された行モデルは、明示的に設定されたグループの集計を Worker 内で先に計算します。一方、`column.getAggregationValue()` の最終的な合計は、選択された行モデルに対してメインスレッドで実行されます。Worker の境界をまたぐ集計結果は、構造化複製（structured clone）できる値である必要があります。セットアップ方法と制限については、[Worker 行モデルのガイド](../../../guide/worker-row-models)を参照してください。
