---
title: 列定義ガイド
---

> [!NOTE]
> このガイドで扱うのは、テーブルの列定義を設定する方法です。テーブルインスタンスの中で生成される実際の [`column`](./columns) オブジェクトについてのガイドでは**ありません**。

列定義は、テーブルを作るうえで最も重要な部分です。列定義は次のことを担います。

- ソート・フィルタリング・グループ化など、あらゆる処理で使われるもとのデータモデルを組み立てる
- データモデルを、テーブルに表示する形に整える
- [ヘッダーグループ](../reference/index/interfaces/HeaderGroup_Core)・[ヘッダー](../reference/index/interfaces/Header_Core)・フッターを作る
- 操作ボタン・チェックボックス・展開ボタン・スパークラインなど、表示だけを目的とした列を作る

## 列定義の種類 {#column-def-types}

ここで挙げる列定義の「種類」は、実際の TypeScript の型ではありません。列定義をおおまかに分類して説明するための呼び方です。

- `Accessor Columns`（アクセサー列）
  - アクセサー列はもとになるデータモデルを持つので、ソート・フィルタリング・グループ化などができます。
- `Display Columns`（表示列）
  - 表示列はデータモデルを**持たない**ので、ソートやフィルタリングなどはできません。その代わり、行の操作ボタン・チェックボックス・展開ボタンなど、任意のコンテンツをテーブルに表示するのに使えます。
- `Grouping Columns`（グループ列）
  - グループ列もデータモデルを**持たない**ので、ソートやフィルタリングなどはできません。ほかの列をひとまとめにするために使います。列グループにはヘッダーやフッターを定義するのが一般的です。

## 列ヘルパー {#column-helpers}

列定義は結局のところただのオブジェクトですが、テーブルのコアからは `createColumnHelper` 関数が公開されています。機能の型と行の型を指定してこの関数を呼び出すと、さまざまな種類の列定義を、できるかぎり高い型安全性で作れるユーティリティが返されます。

v9 の `createColumnHelper` には、2つの型パラメーターが必要です。`features` オブジェクトから得る `TFeatures` と、行の型である `TData` です。機能の型は `typeof features` で取得します。

> [!NOTE]
> `createTableHook` ファクトリーを使う場合は、機能の型があらかじめ結び付けられた `createAppColumnHelper` が返されるので、渡すのは `TData` だけで済みます。[コンポーザブルなテーブルのガイド](../framework/react/guide/composable-tables)を参照してください。

列ヘルパーを作成して使う例を示します。

```tsx
// Define your row shape
type Person = {
  firstName: string
  lastName: string
  age: number
  visits: number
  status: string
  progress: number
}

const features = tableFeatures({}) // or tableFeatures({ rowSortingFeature, ... })
const columnHelper = createColumnHelper<typeof features, Person>()

// Make some columns! Use columnHelper.columns([...]) for better type inference with nested groups
const defaultColumns = columnHelper.columns([
  // Display Column
  columnHelper.display({
    id: 'actions',
    cell: (props) => <RowActions row={props.row} />,
  }),
  // Grouping Column
  columnHelper.group({
    header: 'Name',
    footer: (props) => props.column.id,
    columns: [
      // Accessor Column
      columnHelper.accessor('firstName', {
        cell: (info) => info.getValue(),
        footer: (props) => props.column.id,
      }),
      // Accessor Column
      columnHelper.accessor((row) => row.lastName, {
        id: 'lastName',
        cell: (info) => info.getValue(),
        header: () => <span>Last Name</span>,
        footer: (props) => props.column.id,
      }),
    ],
  }),
  // Grouping Column
  columnHelper.group({
    header: 'Info',
    footer: (props) => props.column.id,
    columns: [
      // Accessor Column
      columnHelper.accessor('age', {
        header: () => 'Age',
        footer: (props) => props.column.id,
      }),
      // Grouping Column
      columnHelper.group({
        header: 'More Info',
        columns: [
          // Accessor Column
          columnHelper.accessor('visits', {
            header: () => <span>Visits</span>,
            footer: (props) => props.column.id,
          }),
          // Accessor Column
          columnHelper.accessor('status', {
            header: 'Status',
            footer: (props) => props.column.id,
          }),
          // Accessor Column
          columnHelper.accessor('progress', {
            header: 'Profile Progress',
            footer: (props) => props.column.id,
          }),
        ],
      }),
    ],
  }),
])
```

## アクセサー列を作る {#creating-accessor-columns}

アクセサー列には、`data` 配列の各要素からプリミティブな値を取り出すように設定しなければならない、という独特の特徴があります。

これには3つの方法があります。

- 要素が `objects` の場合は、取り出したい値に対応するオブジェクトのキーを使います。
- 要素が入れ子の `arrays` の場合は、取り出したい値に対応する配列のインデックスを使います。
- 取り出したい値を返すアクセサー関数を使います。

### オブジェクトのキー {#object-keys}

各要素が次の形のオブジェクトだとします。

```tsx
type Person = {
  firstName: string
  lastName: string
  age: number
  visits: number
  status: string
  progress: number
}
```

`firstName` の値は次のように取り出せます。

```tsx

columnHelper.accessor('firstName')

// OR

{
  accessorKey: 'firstName',
}
```

### 深いキー {#deep-keys}

各要素が次の形のオブジェクトだとします。

```tsx
type Person = {
  name: {
    first: string
    last: string
  }
  info: {
    age: number
    visits: number
  }
}
```

`first` の値は次のように取り出せます。

```tsx
columnHelper.accessor('name.first', {
  id: 'firstName',
})

// OR

{
  accessorKey: 'name.first',
  id: 'firstName',
}
```

### 配列のインデックス {#array-indices}

各要素が次の形の配列だとします。

```tsx
type Sales = [Date, number]
```

`number` の値は次のように取り出せます。

```tsx
columnHelper.accessor(row => row[1], {
  id: 'amount',
})

// OR

{
  accessorKey: '1', // string array index
}
```

> [!NOTE]
> 配列のデータで `accessorKey` を使う場合、キーは文字列にする必要があります（数値の `1` ではなく `'1'` のように書きます）。

### アクセサー関数 {#accessor-functions}

各要素が次の形のオブジェクトだとします。

```tsx
type Person = {
  firstName: string
  lastName: string
  age: number
  visits: number
  status: string
  progress: number
}
```

計算したフルネームの値は、次のように取り出せます。

```tsx
columnHelper.accessor(row => `${row.firstName} ${row.lastName}`, {
  id: 'fullName',
})

// OR

{
  id: 'fullName',
  accessorFn: row => `${row.firstName} ${row.lastName}`,
}
```

> 🧠 アクセサーで取り出した値は、ソートやフィルタリングなどに使われることを覚えておいてください。そのため、アクセサー関数は意味のある形で扱えるプリミティブな値を返すようにしましょう。オブジェクトや配列のようなプリミティブでない値を返す場合は、それを扱える適切なフィルター・ソート・グループ化の関数が必要になります。場合によっては自分で用意しなければなりません。😬

## 一意な列 ID {#unique-column-ids}

列は、次の3つの方法で一意に識別されます。

- オブジェクトのキーか配列のインデックスでアクセサー列を定義した場合は、そのキーやインデックスが列の識別に使われます。
  - オブジェクトのキーに含まれるピリオド（`.`）は、アンダースコア（`_`）に置き換えられます。
- アクセサー関数でアクセサー列を定義した場合は、次のどちらかで識別されます。
  - 列の `id` プロパティが列の識別に使われます。または、
  - プリミティブな `string` のヘッダーを指定した場合は、そのヘッダーの文字列が列の識別に使われます。

> 🧠 覚え方は簡単です。アクセサー関数で列を定義するなら、文字列のヘッダーか、一意な `id` プロパティのどちらかを指定してください。

## 動的な列定義 {#dynamic-column-definitions}

列定義はハードコードする必要はありません。データの形が事前に分からない場合（任意の API レスポンス、ユーザーがアップロードした CSV ファイル、ユーザーが設定できるレポートなど）は、実行時にデータそのものから列定義を生成できます。

> 🧠 用語についての注意: アクセサー関数は、上の `fullName` の例のように、形が分かっている行の中で計算した（「派生した」）値を作ります。一方、動的な列定義は、行の形が分からないときに列の集合そのものを生成します。この2つの手法は互いに補い合う関係にあります。

推論のもとになる静的な行の型がないので、行の型は汎用的なレコードにして、ただのオブジェクトとして列定義を組み立てます。推論の対象となる既知の形がないので、ここでは列ヘルパーを使う利点はありません。

```tsx
type DynamicRow = Record<string, unknown>

const columns: Array<ColumnDef<typeof features, DynamicRow>> = data.length
  ? Object.keys(data[0]).map((key) => ({
      accessorKey: key,
      header: formatHeader(key), // e.g. 'firstName' -> 'First Name'
      cell: (info) => String(info.getValue() ?? ''), // values are unknown, so coerce for rendering
    }))
  : []
```

注意点が2つあります。

- **参照を安定させる。** 列の配列は、データが実際に変わったときだけ作り直してください（たとえば React では `data` をキーにした `useMemo`、ほかのフレームワークでは `computed` やメモ化を使います）。レンダーのたびに列定義を作り直すと、テーブルはすべての列を処理し直すことになります。
- **実行時に型を判定する。** 値の型は `unknown` なので、キーごとにサンプルの値を調べて、型に合ったオプションを選びます。数値・日付・真偽値に適した `sortFn` と `filterFn`、そしてそれに合ったフィルターの UI です。後述するように関数を登録した名前で指定できるので、判定した型による単純な分岐で済みます。

データ型の判定、型ごとのソート関数とフィルター関数、列のファセットを使った型ごとのフィルターコンポーネントまで含めた完全な実装は、[動的な列のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/basic-dynamic-columns)（すべてのフレームワークアダプターで用意されています）を参照してください。

## 列の整形と描画 {#column-formatting--rendering}

デフォルトでは、列のセルにはデータモデルの値が文字列として表示されます。この動作は、独自の描画処理を指定して上書きできます。それぞれの描画処理には、セル・ヘッダー・フッターに関する情報が渡されます。描画処理は、JSX・コンポーネント・文字列など、フレームワークアダプターが描画できるものを返します。何を返せるかは、使っているアダプターによって異なります。

使える整形用の関数（フォーマッター）は次のとおりです。

- `cell`: セルの整形に使います。
- `aggregatedCell`: 集計されたセルの整形に使います。
- `header`: ヘッダーの整形に使います。
- `footer`: フッターの整形に使います。

### セルの整形 {#cell-formatting}

`cell` プロパティに関数を渡すと、独自のセルのフォーマッターを指定できます。セルの値には `props.getValue()` 関数でアクセスします。

```tsx
columnHelper.accessor('firstName', {
  cell: (props) => <span>{props.getValue().toUpperCase()}</span>,
})
```

セルのフォーマッターには `row` オブジェクトと `table` オブジェクトも渡されるので、セルの値以外の情報も使ってセルの表示を整えられます。次の例では、アクセサーに `firstName` を指定しつつ、元の行オブジェクトにあるユーザー ID を先頭に付けて表示しています。

```tsx
columnHelper.accessor('firstName', {
  cell: (props) => (
    <span>{`${props.row.original.id} - ${props.getValue()}`}</span>
  ),
})
```

### 集計されたセルの整形 {#aggregated-cell-formatting}

行がグループ化されているときは、通常のセルの代わりに集計されたセルが描画されます。詳しくは、すべてのフレームワークアダプター向けに用意されている[グループ化ガイド](../framework/react/guide/grouping)で説明しています。

### ヘッダーとフッターの整形 {#header--footer-formatting}

ヘッダーとフッターからは行のデータにアクセスできませんが、独自のコンテンツを表示する考え方は同じです。

## 列定義での機能のオプション {#feature-options-on-column-defs}

列定義には、アクセサーとフォーマッターのほかに、テーブルで有効にしている機能ごとの列単位のオプションも指定できます。よく使うものには、`sortFn`・`filterFn`・`aggregationFn` や、`enableSorting`・`enableColumnFilter` といった有効化のフラグがあります。

```tsx
columnHelper.accessor('age', {
  sortFn: 'basic', // a name typed from the sortFns registry in tableFeatures
  filterFn: 'inNumberRange', // a name typed from the filterFns registry
  sortDescFirst: true,
})
```

v9 では、これらのオプションに渡せる文字列の名前は、`tableFeatures` に含めた関数のレジストリ（`sortFns`・`filterFns`・`aggregationFns` など）から型付けされます。レジストリにない名前を渡すと型エラーになります。独自の関数は、その場で直接渡すことも、自分で決めた名前で登録することもできます。レジストリによってこれらの型がどう決まるかは[型ヘルパーガイド](./helpers)を、使えるオプションの一覧はそれぞれの機能のガイドを参照してください。

## 列のメタ情報 {#column-meta}

列定義には `meta` プロパティも指定できます。これを使うと、任意のデータを強い型付きで列に付けられます（たとえば、フィルターの種類や判定したデータ型など）。`metaHelper` で型を付ける方法について詳しくは、[テーブルと列のメタ情報ガイド](./table-and-column-meta)を参照してください。
