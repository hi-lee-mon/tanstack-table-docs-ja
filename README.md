# TanStack Table v9 ドキュメント日本語翻訳（非公式・React）

[TanStack Table](https://tanstack.com/table/latest) v9 の公式ドキュメントのうち、React 向けのページを日本語に訳した学習用リポジトリです。

> ⚠️ これは非公式の翻訳です。正確な最新情報は必ず原文を参照してください。

## 収録内容

| ディレクトリ | 内容 | 翻訳 |
|---|---|---|
| `docs/overview.md` ほか | 概要・インストール・Devtools・エージェントスキル | 日本語 |
| [`docs/guide/`](docs/guide/) | コアガイド（列定義・行モデル・テーブルインスタンスなど14本） | 日本語 |
| [`docs/framework/react/`](docs/framework/react/) | React 向けクイックスタート・ガイド27本・React API リファレンス | 日本語 |
| [`docs/reference/`](docs/reference/) | コア API リファレンス（TypeDoc の自動生成。約700ファイル） | 英語のまま |

出典は [TanStack/table](https://github.com/TanStack/table) `main` ブランチの `docs/` です。翻訳対象のコミットはサイトのフッターに表示しています。

## 原文からの変更点

- フレームワークごとに切り替わる箇所は React の内容だけを残しています
- サンプル集（examples）は収録していません。サイドバーから公式サイトのサンプルへリンクしています
- このリポジトリに含まれないページへのリンクは、公式サイトの URL に置き換えています

## 読み方

- はじめての人は [`docs/overview.md`](docs/overview.md) → [`docs/installation.md`](docs/installation.md) → [`docs/framework/react/quick-start.md`](docs/framework/react/quick-start.md) の順がおすすめです
- v8 からの移行は [`docs/framework/react/guide/migrating.md`](docs/framework/react/guide/migrating.md) を参照してください
- 訳語の対応は [`GLOSSARY.md`](GLOSSARY.md)、翻訳の決まりは [`TRANSLATING.md`](TRANSLATING.md) にまとめています

## サイトとして読む

```sh
npm ci
npm run docs:dev
```

## ライセンス・帰属

- 原文の著作権は Tanner Linsley（TanStack）に帰属します。原文は MIT License で公開されており、翻訳も同じライセンスに従います。全文は [`LICENSE.md`](LICENSE.md) を参照してください
- 翻訳は学習目的の非公式なものです
