---
title: セルガイド
---

このガイドでは、TanStack Table で `cell` オブジェクトを取得する方法と、それを操作するさまざまな方法を簡単に説明します。

## セルの取得元 {#where-to-get-cells-from}

セルは [行](./rows) から取得します。説明するまでもありませんね。

使っている機能に応じて、行から適切なセルを取得するための `row` インスタンス API がいくつかあります。よく使うのは `row.getAllCells` か `row.getVisibleCells`（列の表示切り替え機能を使っている場合）ですが、ほかにも似た API がいくつかあります。

## セルオブジェクト {#cell-objects}

セルオブジェクトはそれぞれ、UI 上の `<td>` などのセル要素に対応させることができます。`cell` オブジェクトには、テーブルの状態を操作したり、テーブルの状態に基づいてセルの値を取り出したりするためのプロパティとメソッドがいくつかあります。

### セル ID {#cell-ids}

セルオブジェクトにはすべて `id` プロパティがあり、テーブルインスタンスの中で一意になります。`cell.id` は、親の行の ID と列の ID をアンダースコアでつないだだけのものです。

```js
{
  id: `${row.id}_${column.id}`
}
```

グループ化や集計の機能を使っている場合は、`cell.id` の末尾にさらに文字列が付け加えられます。

### セルの親オブジェクト {#cell-parent-objects}

各セルは、親の [行](./rows) オブジェクトと [列](./columns) オブジェクトへの参照を持っています。

### セルの値にアクセスする {#access-cell-values}

セルからデータの値を取り出すには、`cell.getValue` か `cell.renderValue` のどちらかの API を使うのが推奨の方法です。どちらを使っても、アクセサー関数の結果がキャッシュされ、効率よくレンダーできます。2つの違いは1点だけです。値が undefined のとき、`cell.renderValue` は `renderFallbackValue` を返し、`cell.getValue` は `undefined` を返します。

> [!NOTE]
> `cell.getValue` と `cell.renderValue` は、それぞれ `row.getValue` と `row.renderValue` のショートカットです。

```js
// Access the value for this cell's own column
const value = cell.getValue() // read the cell value
const renderedValue = cell.renderValue() // read the cell value, falling back to `renderFallbackValue`
```

これらの API は引数を取らず、セル自身の列に結び付いています。セルの中から別の列の値を読みたい場合は、`cell.row.getValue('someColumnId')` のように親の行を使ってください。

### どのセルからでも行のほかのデータにアクセスする {#access-other-row-data-from-any-cell}

セルオブジェクトはどれも親の行に結び付いているので、`cell.row.original` を使えば、テーブルで使っている元の行データのどの値にもアクセスできます。

```js
// Even if we are in the scope of a different cell, we can still access the original row data
const firstName = cell.row.original.firstName // { firstName: 'John', lastName: 'Doe' }
```

## そのほかのセル API {#more-cell-apis}

テーブルで使っている機能によっては、セルを操作するための便利な API がほかにも数十個あります。詳しくは、各機能の API ドキュメントやガイドを参照してください。

## セルのレンダー {#cell-rendering}

`cell.renderValue` や `cell.getValue` の API をそのまま使って、テーブルのセルをレンダーすることもできます。ただし、これらの API が出力するのは（アクセサー関数から得た）セルの生の値だけです。列定義で `cell: () => JSX` のオプションを使っている場合は、アダプターが提供する `flexRender` ユーティリティを使うとよいでしょう。

`flexRender` は、追加のマークアップや JSX を含むセルを正しくレンダーし、コールバック関数を正しい引数で呼び出します。

```jsx
import { flexRender } from '@tanstack/react-table'

const columns = [
  {
    accessorKey: 'fullName',
    cell: ({ cell, row }) => {
      return <div><strong>{row.original.firstName}</strong> {row.original.lastName}</div>
    }
    //...
  }
]
//...
<tr>
  {row.getVisibleCells().map(cell => {
    return <td key={cell.id}>{flexRender(cell.column.columnDef.cell, cell.getContext())}</td>
  })}
</tr>
```

### セル結合 {#cell-spanning}

オプションの `cellSpanningFeature` を登録すると、隣り合うセルを1つのセルに結合してレンダーできます。結合幅として `0` を返すセルは別のセルの結合範囲に覆われているので、レンダーせずに飛ばす必要があります。レンダーのやり方の全体は [セル結合ガイド](../framework/react/guide/cell-spanning) を参照してください。
