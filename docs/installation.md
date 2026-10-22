---
title: インストール
---

API を詳しく見ていく前に、まずは環境を整えましょう。

お好みのパッケージマネージャーで、テーブルのアダプターを依存関係としてインストールします。

::: code-group

```sh [npm]
npm install @tanstack/react-table
```

```sh [pnpm]
pnpm add @tanstack/react-table
```

```sh [yarn]
yarn add @tanstack/react-table
```

```sh [bun]
bun add @tanstack/react-table
```

:::


`@tanstack/react-table` パッケージは React 18 以降で動作します。


お使いのフレームワーク（またはそのバージョン）が一覧にありませんか？ その場合でも、`@tanstack/table-core` パッケージを使えば、自分のコードベースの中で独自のアダプターを作れます。たいていは、そのフレームワークで状態とレンダーを管理する薄いラッパーがあれば十分です。他のアダプターがどう動いているかは、それぞれの[ソースコード](https://github.com/TanStack/table/tree/main/packages)で確認できます。
