---
title: ヘッダーガイド
---

このガイドでは、TanStack Table で `header` オブジェクトを取得する方法と、それを操作するさまざまな方法を簡単に説明します。

ヘッダーはセルに相当するものですが、テーブルの `<tbody>` 部分ではなく `<thead>` 部分で使います。

## ヘッダーの取得元 {#where-to-get-headers-from}

ヘッダーは [ヘッダーグループ](./header-groups) から取得します。ヘッダーグループは行に相当するもので、テーブルの `<tbody>` 部分ではなく `<thead>` 部分で使います。

### HeaderGroup のヘッダー {#headergroup-headers}

ヘッダーグループの中では、ヘッダーは `headerGroup.headers` プロパティに配列として格納されています。通常は、この配列を map してヘッダーをレンダーするだけです。

```jsx
<thead>
  {table.getHeaderGroups().map((headerGroup) => {
    return (
      <tr key={headerGroup.id}>
        {headerGroup.headers.map(
          (
            header, // map over the headerGroup headers array
          ) => (
            <th key={header.id} colSpan={header.colSpan}>
              {/* */}
            </th>
          ),
        )}
      </tr>
    )
  })}
</thead>
```

### ヘッダー用のテーブルインスタンス API {#header-table-instance-apis}

使っている機能に応じて、ヘッダーの一覧を取得するための `table` インスタンス API がいくつかあります。もっともよく使うのは `table.getFlatHeaders` で、テーブル内のすべてのヘッダーを平坦な一覧で返します。ほかにも、列の表示切り替えや列の固定の機能と組み合わせて使うと便利な API が少なくとも十数個あります。用途によっては、`table.getStartLeafHeaders` や `table.getEndFlatHeaders` のような API が役に立つでしょう。

## ヘッダーオブジェクト {#header-objects}

ヘッダーオブジェクトは [セル](./cells) オブジェクトに似ていますが、テーブルの `<tbody>` 部分ではなく `<thead>` 部分で使います。ヘッダーオブジェクトはそれぞれ、UI 上の `<th>` などのセル要素に対応させることができます。`header` オブジェクトには、テーブルの状態を操作したり、テーブルの状態に基づいてセルの値を取り出したりするためのプロパティとメソッドがいくつかあります。

### ヘッダー ID {#header-ids}

ヘッダーオブジェクトにはすべて `id` プロパティがあり、テーブルインスタンスの中で一意になります。通常この `id` が必要になるのは、React の key に使う一意な識別子としてか、[パフォーマンス重視の列幅変更のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/column-resizing-performant) にならう場合くらいです。

入れ子やグループ化といった高度なヘッダーのロジックを持たない単純なヘッダーでは、`header.id` は親の `column.id` と同じになります。ただし、ヘッダーがグループ列やプレースホルダーセルの一部である場合は、ヘッダーファミリー、深さ（ヘッダー行の番号）、列 ID、ヘッダーグループ ID から組み立てられた、より複雑な id になります。

### 入れ子・グループ化されたヘッダーのプロパティ {#nested-grouped-headers-properties}

`header` オブジェクトには、ヘッダーが入れ子やグループ化されたヘッダー構造の一部である場合にだけ役立つプロパティがいくつかあります。次のようなものです。

- `colSpan`: ヘッダーがまたぐ列の数です。`<th>` 要素の `colSpan` 属性をレンダーするときに使えます。
- `rowSpan`: ヘッダーセルを縦方向に結合するときに、ヘッダーがまたぐ行の数です。一番深い末端の列よりも浅い末端の列では、本来のヘッダーの上にプレースホルダーヘッダーが連なります。その連なりの一番上にあるプレースホルダーが連なり全体の行数を返し、それに覆われるヘッダー（最下行にある本来の末端のヘッダーも含む）はすべて 0 を返します。`<th>` 要素の `rowSpan` 属性をレンダーするときに使えます。後述の [ヘッダー行の結合](#header-row-spanning) を参照してください。
- `depth`: ヘッダーが属するヘッダーグループの「行番号」です。
- `isPlaceholder`: ヘッダーがプレースホルダーヘッダーなら true になる真偽値のフラグです。プレースホルダーヘッダーは、浅い末端の列の本来のヘッダーより上の行を埋め、どのヘッダー行にもすべての表示中の列が揃うようにします。空のセルとしてレンダーしてヘッダーの格子をそろえるか、`header.rowSpan` を使ってプレースホルダーの連なりを縦にまたがる1つのヘッダーセルに結合してください。
- `placeholderId`: プレースホルダーヘッダーの一意な識別子です。
- `subHeaders`: このヘッダーに属するサブヘッダー（子ヘッダー）の配列です。ヘッダーが末端のヘッダーの場合は空になります。

> [!NOTE]
> `header.index` は、ヘッダーグループ（ヘッダーの行）の中でのインデックス、つまり左から何番目かを指します。ヘッダーグループの「行番号」を指す `header.depth` とは別物です。

### ヘッダーの親オブジェクト {#header-parent-objects}

各ヘッダーは、親の [列](./columns) オブジェクトと親の [ヘッダーグループ](./header-groups) オブジェクトへの参照を持っています。

## そのほかのヘッダー API {#more-header-apis}

ヘッダーには、テーブルの状態を操作するのに便利な API がほかにもいくつか付いています。その多くは列幅と列幅の変更の機能に関するものです。詳しくは [列幅ガイド](../framework/react/guide/column-sizing) と [列幅の変更ガイド](../framework/react/guide/column-resizing) を参照してください。

## ヘッダーのレンダー {#header-rendering}

定義した `header` 列オプションは、文字列、JSX、またはそのどちらかを返す関数のいずれかになりうるので、ヘッダーをレンダーするにはアダプターが提供する `flexRender` ユーティリティを使うのが最善です。これらのケースをすべて処理してくれます。

```jsx
{
  headerGroup.headers.map((header) => (
    <th key={header.id} colSpan={header.colSpan}>
      {/* Handles all possible header column def scenarios for `header` */}
      {flexRender(header.column.columnDef.header, header.getContext())}
    </th>
  ))
}
```

### ヘッダー行の結合 {#header-row-spanning}

列のツリーが不揃いな場合（一部の末端の列がほかより深く入れ子になっている場合）、浅い末端の列ではそれぞれ、本来のヘッダーの上にプレースホルダーヘッダーが連なります。その連なりの一番上にあるプレースホルダーが連なり全体の `rowSpan` を返し、それに覆われるヘッダーはすべて `rowSpan` として 0 を返します。これらのヘッダーセルを縦に結合するには、`rowSpan` が 0 のヘッダーを飛ばし、それ以外を `rowSpan` 属性付きでレンダーします。このやり方は、通常の `header.isPlaceholder` のチェックの代わりになる点に注意してください。結合するプレースホルダーは、空のセルではなく、その列のヘッダーの内容をレンダーします。

```jsx
{
  headerGroup.headers.map((header) =>
    header.rowSpan === 0 ? null : (
      <th key={header.id} colSpan={header.colSpan} rowSpan={header.rowSpan}>
        {flexRender(header.column.columnDef.header, header.getContext())}
      </th>
    ),
  )
}
```

> [!NOTE]
> この方法は `<thead>` 部分専用です。フッターグループはヘッダー行を逆順にレンダーするため、結合するプレースホルダーが、覆うべきセルの下に来てしまいます。`<tfoot>` 部分では、`header.isPlaceholder` で空のセルを出すやり方をそのまま使ってください。

本体のセルで同じ考え方を使いたい場合は、オプションの `cellSpanningFeature` があります。[セル結合ガイド](../framework/react/guide/cell-spanning) を参照してください。
