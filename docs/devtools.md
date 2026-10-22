---
title: Devtools
id: devtools
---

TanStack Table は、フレームワークごとの Devtools アダプターを提供しています。これらは [TanStack Devtools](https://tanstack.com/devtools) の複数パネル UI に組み込んで使います。

テーブルの Devtools を使うと、登録したテーブルインスタンスを調べたり、複数のテーブルを切り替えたり、機能・状態・オプション・行・列をリアルタイムに確認したりできます。

> [!NOTE]
> 初期設定では、フレームワークアダプターが実際に動く Devtools を含めるのは開発モードのときだけです。本番ビルドでは何もしない実装（no-op）をエクスポートします。ただし、`/production` エントリーポイントを明示的に選んだ場合は別です。

## インストール {#installation}

TanStack Devtools のホストパッケージと、使っているフレームワーク向けの Table アダプターをインストールします。

```sh
npm install @tanstack/react-devtools @tanstack/react-table-devtools
```


Octane、Lit、Svelte、Alpine、vanilla には、現時点でテーブル専用の Devtools アダプターがありません。

## 必須のテーブルオプション `key` {#the-required-key-table-option}

Devtools は、テーブルオプション `key` で各テーブルを識別します。登録には `key` が必須です。`key` を指定せずにテーブルを登録すると、Devtools はエラー（`Missing table key. Add a 'key' option to your table to use devtools.`）をログに出し、そのテーブルを丸ごとスキップします。

```ts
const table = useTable({
  key: 'users-table', // needed for devtools, omit if you don't want to use the devtools
  features,
  columns,
  data,
})
```

`key` は Devtools パネルのセレクターに表示されるラベルにもなります。テーブルごとに、重複せず内容が分かる key を付けてください。

## セットアップの手順 {#setup-pattern}

推奨するセットアップは次の3つです。

1. 各テーブルに重複しない `key` オプションを付ける
2. アプリのルートに `tableDevtoolsPlugin()` を渡した `TanStackDevtools` をマウントする
3. 各テーブルを作成した直後に、`useTanStackTableDevtools(table)`（Angular では `injectTanStackTableDevtools`）で登録する

複数のテーブルを登録すると、Table パネルにセレクターが表示され、テーブルを切り替えられます。

## セットアップ {#setup}

```tsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import { useTable } from '@tanstack/react-table'
import { TanStackDevtools } from '@tanstack/react-devtools'
import {
  tableDevtoolsPlugin,
  useTanStackTableDevtools,
} from '@tanstack/react-table-devtools'

function App() {
  const table = useTable({
    key: 'users-table', // needed for devtools
    // ...
  })

  useTanStackTableDevtools(table)

  return <AppContent table={table} />
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
    <TanStackDevtools plugins={[tableDevtoolsPlugin()]} />
  </React.StrictMode>,
)
```

[React の行選択のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/row-selection)も参照してください。


## 登録を無効にする {#disabling-registration}

どの登録関数も `enabled` オプションを受け取ります。条件に応じてテーブルを登録したいときに使います。

```ts
useTanStackTableDevtools(table, { enabled: false })
```


## 本番ビルド {#production-builds}

本番環境でも実際に動く Devtools が必要な場合は、使っているフレームワークパッケージの `/production` エントリーポイントからインポートします。

```tsx
import {
  tableDevtoolsPlugin,
  useTanStackTableDevtools,
} from '@tanstack/react-table-devtools/production'
```

