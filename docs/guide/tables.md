---
title: テーブルインスタンスガイド
---

TanStack Table はヘッドレス UI ライブラリです。`table` や「テーブルインスタンス」と言うとき、文字どおりの `<table>` 要素を指しているわけではありません。テーブルの状態と API を取りまとめる、コアのテーブルオブジェクトを指しています。`table` インスタンスは、アダプターのテーブル作成関数（`useTable`、`createTable`、`injectTable`、`constructTable` など）を呼び出して作成します。

これらの関数が返す `table` インスタンスは、テーブルの状態を読み取ったり変更したりするときに操作する中心のオブジェクトです。TanStack Table では、あらゆる処理がこの1か所で行われます。UI をレンダーする段階では、この `table` インスタンスの API を使います。

## テーブルインスタンスを作成する {#creating-a-table-instance}

テーブルインスタンスを作成するには、`columns`、`data`、`features` の3つの `options` が必要です。`features` オプションでは、テーブルが使う機能を宣言します（これによりツリーシェイキングが効き、使うものだけがバンドルされます）。コア行モデルは自動で含まれます。フィルタリング・ソート・ページネーションなどが必要になったら、`tableFeatures()` の呼び出しにスロットとして行モデルのファクトリーを追加します。ほかにも、機能や動作を設定するテーブルオプションが何十個もあります。

### データを定義する {#defining-data}

データは、参照が安定したオブジェクトの配列として定義します。`data` は API のレスポンスやコード内での静的な定義など、どこから来てもかまいません。ただし、無限に再レンダーされるのを防ぐため、参照は安定していなければなりません。TypeScript を使う場合は、データに付けた型が `TData` ジェネリクスとして使われます。詳しくは[データガイド](./data)を参照してください。

### 列を定義する {#defining-columns}

列定義については、前の節の[列定義ガイド](./column-defs)で詳しく説明しています。ここで1点だけ触れておくと、列の型を定義するときは、データに使ったものと同じ `TData` 型を使ってください。

```ts
const features = tableFeatures({}) // Define which features your table uses
const columns: ColumnDef<typeof features, User>[] = [] // Pass User type as TData; use typeof features for TFeatures
//or
const columnHelper = createColumnHelper<typeof features, User>() // Pass both TFeatures and TData in v9
```

列定義では、各列が行データをどう取り出し、どう変換するかを、`accessorKey` または `accessorFn` で TanStack Table に伝えます。詳しくは[列定義ガイド](./column-defs#creating-accessor-columns)を参照してください。

### 機能と行モデルを定義する {#defining-features-and-row-models}

これについては[行モデルガイド](./row-models)でずっと詳しく説明しています。v9 では、テーブルが使う機能を `features` で（`tableFeatures()` を使って）宣言します。行モデルのファクトリーは、その同じ features オブジェクトのスロットに置きます。コア行モデルは常に自動で含まれます。フィルタリング・ソート・ページネーションのない基本的なテーブルなら、空の features オブジェクトを渡します。

```ts
import { tableFeatures, useTable } from '@tanstack/react-table'

const features = tableFeatures({}) // Core features only; add columnFilteringFeature, rowSortingFeature, etc. as needed

const table = useTable({
  features,
  columns,
  data,
})
```


### テーブルインスタンスを初期化する {#initializing-the-table-instance}

`features`、`columns`、`data` を定義したら、基本的なテーブルインスタンスを作成できます。渡したいほかのテーブルオプションもあわせて指定します。

> **フレームワークに関する注記:** テーブル作成関数はフレームワークアダプターごとに異なりますが、どれも同じコアオプションを受け取ります。

```ts
const table = useTable({ features, columns, data })
```


では、`table` インスタンスには何が入っているのでしょうか。テーブルインスタンスでどんな操作ができるのかを見ていきましょう。

## テーブルの状態 {#table-state}

テーブルインスタンスには、`features` が登録した状態のスライスが入っています。各機能は自分が受け持つ状態を登録します。たとえば、行選択の機能は `rowSelection` の状態を、ページネーションの機能は `pagination` の状態を登録します。v9 では、これらのスライスの裏側に TanStack Store のアトムがあります。

- `table.baseAtoms` は、内部用の書き込み可能なアトムです。
- `table.atoms` は、スライスごとの公開用の読み取り専用アトムです。
- `table.store` は、`table.atoms` から派生した、読み取り専用のフラットなストアです。

```ts
table.atoms.rowSelection.get() // read the current row selection state
table.store.state.rowSelection // read the current table state snapshot
table.setRowSelection((old) => ({ ...old })) //set the row selection state
table.resetRowSelection() //reset the row selection state
```

`table.atoms.rowSelection.get()` や `table.store.state.rowSelection` のように直接読み取ると、その時点の値が得られます。フレームワークアダプターは、必要に応じてリアクティブに状態を読み取る独自の API を追加しています。詳しくは、使っているフレームワークのテーブルの状態ガイドで説明しています。

[テーブルの状態ガイド](../framework/react/guide/table-state)


## テーブルの API {#table-apis}

各機能が作る何十ものテーブル API を使って、テーブルの状態をさまざまな方法で読み取ったり変更したりできます。

コアのテーブルインスタンスとほかのすべての機能の API リファレンスは、[リファレンス](../reference/index)にまとめてあります。

## テーブルの行モデル {#table-row-models}

テーブルインスタンスの API には、テーブルインスタンスから行を読み出すための特別なものがあり、これを行モデルと呼びます。TanStack Table には高度な機能があり、生成される行が、最初に渡した `data` の配列とは大きく異なる場合があります。さまざまな行モデルと、その登録方法について詳しくは、[行モデルガイド](./row-models)を参照してください。
