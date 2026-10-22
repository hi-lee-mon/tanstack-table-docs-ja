---
title: 行のガイド
---

この短いガイドでは、TanStack Table で行オブジェクトを取得し、操作するさまざまな方法を説明します。

## 行の取得元 {#where-to-get-rows-from}

テーブルインスタンスから行を取得するために使える `table` インスタンスの API は複数あります。

### table.getRow {#tablegetrow}

特定の行に `id` でアクセスする必要がある場合は、テーブルインスタンスの API である `table.getRow` を使えます。

```js
const row = table.getRow(rowId)
```

### 行モデル {#row-models}

`table` インスタンスは `row` オブジェクトを生成し、[「行モデル」](./row-models)と呼ばれる便利な配列に格納します。詳しくは[行モデルのガイド](./row-models)で説明していますが、ここでは行モデルにアクセスするよくある方法を紹介します。

#### 行を描画する {#render-rows}

```jsx
<tbody>
  {table.getRowModel().rows.map((row) => (
    <tr key={row.id}>{/* ... */}</tr>
  ))}
</tbody>
```

#### 選択された行を取得する {#get-selected-rows}

```js
const selectedRows = table.getSelectedRowModel().rows
```

## 行オブジェクト {#row-objects}

どの行オブジェクトにも、行のデータと多くの API が含まれています。これらの API を使うと、テーブルの状態を操作したり、テーブルの状態に応じて行からセルを取り出したりできます。

### 行 ID {#row-ids}

どの行オブジェクトにも、テーブルインスタンス内で一意になる `id` プロパティがあります。既定では、`row.id` は行モデルの中で作られる `row.index` と同じです。ただし、各行の `id` を行のデータに含まれる一意の識別子で上書きしたほうが便利な場合もあります。これには `getRowId` テーブルオプションを使います。

```js
const table = useTable({
  features,
  columns,
  data,
  getRowId: (originalRow) => originalRow.uuid, // override the row.id with the uuid from the original row's data
})
```

> [!NOTE]
> グループ化や展開などの一部の機能では、`row.id` の末尾に文字列が追加されます。

### 行番号と表示上のインデックス {#row-numbers-and-display-indexes}

行番号の列を表示するときは、`row.index` ではなく `row.getDisplayIndex()` を使ってください。表示上のインデックスは、フィルタリング、グループ化、ソート、展開を反映した、テーブルの現在の論理的な表示順に従います。`row.index` は、行が作られたときの親の配列の中での位置です。そのため、現在の表示までの処理の流れを反映して変わることはありません。

```js
const rowNumberColumn = columnHelper.display({
  id: 'rowNumber',
  header: '#',
  cell: ({ row }) => {
    const displayIndex = row.getDisplayIndex()
    return displayIndex === -1 ? '' : displayIndex + 1
  },
})
```

`row.getDisplayIndex()` は、ページネーション前の 0 始まりのインデックスを返します。行が現在の表示順に含まれていない場合は `-1` を返します。

> `row._displayIndexCache` は決して直接読まないでください。これは内部実装用のキャッシュで、表示順が再計算されるまでは古い値のままになっていることがあります。`row.getDisplayIndex()` は、キャッシュされた位置を更新して検証してから返します。

### 行の値にアクセスする {#access-row-values}

行のデータの値にアクセスするには、`row.getValue` か `row.renderValue` の API を使う方法をおすすめします。どちらの API を使っても、アクセサー関数の結果がキャッシュされ、描画の効率が保たれます。両者の違いは1つだけです。値が undefined のとき、`row.renderValue` は `renderFallbackValue` を返し、`row.getValue` は `undefined` を返します。

```js
// Access data from any of the columns
const firstName = row.getValue('firstName') // read the row value from the firstName column
const renderedLastName = row.renderValue('lastName') // render the value from the lastName column
```

> [!NOTE]
> `cell.getValue` と `cell.renderValue` は、それぞれ `row.getValue` と `row.renderValue` の API のショートカットです。

### 元の行データにアクセスする {#access-original-row-data}

どの行オブジェクトでも、`row.original` プロパティを通じて、テーブルインスタンスに渡された元の対応する `data` にアクセスできます。`row.original` のデータは、列定義のアクセサーによって一切変更されていません。そのため、アクセサーで何らかのデータ変換をしていても、その変換は `row.original` オブジェクトには反映されません。

```js
// Access any data from the original row
const firstName = row.original.firstName // { firstName: 'John', lastName: 'Doe' }
```

## サブ行 {#sub-rows}

グループ化か展開の機能を使っている場合、行にはサブ行や親の行への参照が含まれることがあります。詳しくは[展開のガイド](../framework/react/guide/expanding)で説明していますが、ここではサブ行を扱うときに役立つプロパティとメソッドを簡単に紹介します。

- `row.subRows`: その行のサブ行の配列です。
- `row.depth`: ルートの行の配列を基準にした、その行の深さです（入れ子やグループ化されている場合）。ルートの行は 0、子の行は 1、孫の行は 2、というように続きます。
- `row.parentId`: その行の親の行（自身の subRows 配列にこの行を含む行）の一意な ID です。
- `row.getParentRow`: 親の行があれば、それを返します。
- `table.getMaxSubRowDepth()`: コア行モデルの中で、構造上もっとも深い深さを返します。結果は、コア行モデルが変わるまでメモ化されます。

## そのほかの行の API {#more-row-apis}

テーブルで使っている機能によっては、行を操作するための便利な API がほかにも数十あります。詳しくは、各機能の API ドキュメントやガイドを参照してください。
