---
title: FlexRender（React）ガイド
---

列定義の `header`、`cell`、`footer`、`aggregatedCell` には、素の React ノードもレンダラーコンポーネントも書けます。TanStack Table のレンダリング用ユーティリティを使えば、それぞれの値が正しく解釈され、型の付いたテーブルのコンテキストも受け取れます。

## `FlexRender` と `flexRender` の違い {#flexrender-vs-flexrender}

おすすめはコンポーネントのラッパーである `FlexRender` です。`cell`、`header`、`footer` のうち、テーブルのオブジェクトをちょうど1つだけ渡してください。すると、対応する列定義とコンテキストを `FlexRender` が選びます。

```tsx
{
  table.getHeaderGroups().map((headerGroup) => (
    <tr key={headerGroup.id}>
      {headerGroup.headers.map((header) => (
        <th key={header.id}>
          {header.isPlaceholder ? null : <table.FlexRender header={header} />}
        </th>
      ))}
    </tr>
  ))
}

{
  table.getRowModel().rows.map((row) => (
    <tr key={row.id}>
      {row.getVisibleCells().map((cell) => (
        <td key={cell.id}>
          <table.FlexRender cell={cell} />
        </td>
      ))}
    </tr>
  ))
}
```

アダプターは `FlexRender` をテーブルインスタンスに付けています。直接インポートして使うこともできます。

```tsx
import { FlexRender } from '@tanstack/react-table'

const footerContent = <FlexRender footer={header} />
```

セルの場合、`FlexRender` は次のように振る舞います。セルが集計されていれば `aggregatedCell` を描画し、集計用のレンダラーがなければ `cell` で代用します。グループ化のプレースホルダーセルには何も描画しません。

`flexRender` はより低レベルな関数です。描画できる値とその props がすでに手元にあるときに使います。

```tsx
import { flexRender } from '@tanstack/react-table'

flexRender(cell.column.columnDef.cell, cell.getContext())
```

`flexRender` は、React コンポーネント（クラスコンポーネント、`memo`、`forwardRef` を含む）と、作成済みの React ノードを区別します。ただし、`cell` と `aggregatedCell` のどちらを使うかは選ばず、グループ化のプレースホルダーも抑止しません。こうしたテーブル固有の判断は `FlexRender` ラッパーが受け持ちます。

## 列のレンダラーコンポーネント {#column-renderer-components}

レンダラー関数は React コンポーネントとして扱われ、適切なコンテキストを props として受け取ります。

```tsx
const columns = columnHelper.columns([
  columnHelper.accessor('name', {
    header: ({ column }) => <button>{column.id}</button>,
    cell: ({ getValue }) => <strong>{getValue()}</strong>,
  }),
])
```

アクセサーの値だけが必要なら、`cell.getValue()` か `cell.renderValue()` を使ってください。列定義を描画するときは `FlexRender` を使います。`FlexRender` は静的なノードにもコンポーネントのレンダラーにも対応し、コンテキストをすべて渡すからです。

プレースホルダーのヘッダーをどう扱うかはレイアウトの判断なので、自動では抑止されません。複数列にまたがるヘッダーのためにプレースホルダーへ意図して中身を入れる場合を除き、`header.isPlaceholder` を確認してください。フッターグループにも `Header` オブジェクトが入っているので、フッターの各ヘッダーは `footer` プロパティに渡します。
