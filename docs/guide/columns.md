---
title: 列ガイド
---

> [!NOTE]
> このガイドで扱うのは、テーブルインスタンスの中で生成される実際の `column` オブジェクトです。テーブルの[列定義](./column-defs)を設定する方法については扱いません。

この短いガイドでは、TanStack Table で `column` オブジェクトを取得して操作するさまざまな方法を説明します。

## 列をどこから取得するか {#where-to-get-columns-from}

`column` オブジェクトはさまざまな場所で見つかります。ヘッダーやセルといった他のオブジェクトに付いていることが多く、`table` インスタンスのいくつかの API からも取得できます。

### ヘッダーオブジェクトとセルオブジェクト {#header-and-cell-objects}

`table` インスタンスの API に手を伸ばす前に、本当に必要なのは `columns` ではなく[ヘッダー](./headers)や[セル](./cells)ではないかを考えてください。テーブルのマークアップを描画しているなら、列ではなくヘッダーやセルを返す API を使いたい場面がほとんどでしょう。列オブジェクト自体は、ヘッダーやセルを描画するためのものではありません。`header` オブジェクトと `cell` オブジェクトがこれらの `column` オブジェクトへの参照を持っており、そこから UI の描画に必要な情報を導き出します。

```js
const column = cell.column // get column from cell
const column = header.column // get column from header
```

### 列を取得する table インスタンスの API {#column-table-instance-apis}

テーブルインスタンスから列を取得するのに使える `table` インスタンスの API は、何十個もあります。どの API を使うかは、テーブルでどの機能を使っているか、そしてユースケースによって決まります。

#### 列を1つ取得する {#get-column}

ID を指定して列を1つ取得したいだけなら、`table.getColumn` API を使えます。

```js
const column = table.getColumn('firstName')
```

#### 列をまとめて取得する {#get-columns}

いちばん単純な列の API は `table.getAllColumns` で、テーブル内のすべての列のリストを返します。ただし、この API と並んで、他の機能やテーブルの状態の影響を受ける列の API が何十個もあります。`table.getAllFlatColumns`、`table.getAllLeafColumns`、`table.getCenterLeafColumns`、`table.getStartVisibleLeafColumns` は、列の表示切り替えや列の固定の機能と組み合わせて使うことがある列の API のほんの一例です。

## 列オブジェクト {#column-objects}

列オブジェクトは、テーブルの UI を直接描画するためのものではありません。そのため、テーブル内の `<th>` 要素や `<td>` 要素と1対1で対応しているわけではありません。それでも、テーブルの状態を操作するのに使える便利なプロパティやメソッドを数多く持っています。

### 列 ID {#column-ids}

すべての列は、対応する[列定義](./column-defs)で定義された一意の `id` を持たなければなりません。通常、この `id` は自分で定義するか、列定義の `accessorKey` プロパティや `header` プロパティから導き出されます。

### ColumnDef {#columndef}

列オブジェクトからは、その列の作成に使われた元の `columnDef` オブジェクトへの参照を常に参照できます。

### 入れ子・グループ化された列のプロパティ {#nested-grouped-columns-properties}

`column` オブジェクトのプロパティの中には、その列が入れ子になった列構造やグループ化された列構造の一部である場合にだけ役立つものがいくつかあります。次のようなプロパティです。

- `columns`: グループ列に属する子の列の配列です。
- `depth`: その列グループが属するヘッダーグループの「行番号」です。
- `parent`: その列の親の列です。最上位の列の場合は `undefined` になります。

## その他の列の API {#more-column-apis}

テーブルの状態を操作したり、テーブルの状態に基づいてテーブルからセルの値を取り出したりするのに使える列の API は、何十個もあります。詳しくは、各機能の列の API のドキュメントを参照してください。

## 列の描画 {#column-rendering}

`headers` や `cells` を描画するのに、必ずしも `column` オブジェクトを直接使う必要はありません。上で説明したとおり、代わりに [`header`](./headers) オブジェクトと [`cell`](./cells) オブジェクトを使ってください。

ただし、列の表示切り替えメニューのようなものとして、UI のどこか別の場所に列の一覧を描画したいだけなら、列の配列を map して、いつもどおりに UI を描画すれば十分です。
