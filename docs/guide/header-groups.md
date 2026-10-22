---
title: ヘッダーグループガイド
---

この短いガイドでは、TanStack Table でヘッダーグループのオブジェクトを取得し、扱うさまざまな方法を説明します。

## ヘッダーグループとは {#what-are-header-groups}

ヘッダーグループは、単にヘッダーの「行」です。名前に惑わされないでください。本当にそれだけのことです。大半のテーブルではヘッダーの行は1つ（ヘッダーグループが1つ）だけです。ただし、[ヘッダーグループのサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/header-groups)のように列をネストした構造で定義すると、ヘッダーの行が複数（ヘッダーグループが複数）になることがあります。

## ヘッダーグループの取得元 {#where-to-get-header-groups-from}

テーブルインスタンスからヘッダーグループを取得するための `table` インスタンスの API は複数あります。最もよく使うのは `table.getHeaderGroups` です。ただし、使っている機能によっては別の API が必要になることがあります。たとえば列の固定機能を使っている場合は `table.get[Start/Center/End]HeaderGroups` を使います。

## ヘッダーグループのオブジェクト {#header-group-objects}

ヘッダーグループのオブジェクトは [Row](./rows) オブジェクトに似ていますが、より単純です。ヘッダーの行では、本体の行ほど多くのことが起こらないからです。

デフォルトでは、ヘッダーグループが持つプロパティは次の3つだけです。

- `id`: ヘッダーグループの一意な識別子で、深さ（インデックス）から生成されます。React コンポーネントの key として使うのに便利です。
- `depth`: ヘッダーグループの深さで、0 から始まります。すべてのヘッダー行の中での行番号だと考えてください。
- `headers`: このヘッダーグループ（行）に属する [Header](./headers) セルのオブジェクトの配列です。

## ヘッダーセルにアクセスする {#access-header-cells}

ヘッダーグループ内のヘッダーセルを描画するには、ヘッダーグループのオブジェクトの `headers` 配列を map するだけです。

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
