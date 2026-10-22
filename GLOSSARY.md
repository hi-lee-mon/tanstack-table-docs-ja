---
title: 用語集
---

# 用語集（GLOSSARY）

翻訳ではこの用語集に合わせて訳語をそろえます。API 名・識別子・パッケージ名は訳しません。

## そのまま表記するもの

- TanStack Table, TanStack Virtual, TanStack Query, TanStack Form, TanStack Router, TanStack Store, TanStack Intent
- React, React Compiler, TypeScript, JavaScript, JSX, DOM, HTML, CSS, API, SSR, URL, JSON
- `useTable`, `createTableHook`, `FlexRender`, `tableFeatures` などのコード識別子
- パッケージ名: `@tanstack/react-table`, `@tanstack/table-core` など
- 機能名をコードとして書いている箇所（`rowSortingFeature` など）

## 日英対応表

| English | 日本語 | 補足 |
|---|---|---|
| table instance | テーブルインスタンス | |
| table | テーブル | |
| column / row / cell | 列 / 行 / セル | |
| header / header group | ヘッダー / ヘッダーグループ | |
| footer | フッター | |
| column definition / column def | 列定義 | `columnDef` はコードのまま |
| accessor | アクセサー | `accessorKey` `accessorFn` はコードのまま |
| leaf column / leaf header | 末端の列 / 末端のヘッダー | |
| row model | 行モデル | |
| core row model | コア行モデル | |
| sub rows | サブ行 | |
| feature | 機能 | `features` オプションを指すときは `features` と書く |
| stock features | 標準機能 | |
| core features | コア機能 | |
| plugin | プラグイン | |
| adapter | アダプター | |
| slot | スロット | `features` オプション内の登録枠を指す |
| state | 状態 | |
| table state | テーブルの状態 | |
| controlled state | 制御された状態 | 「外部で管理する状態」と補ってもよい |
| initial state | 初期状態 | |
| atom | アトム | |
| store | ストア | |
| selector | セレクター | |
| subscribe / subscription | 購読する / 購読 | |
| re-render | 再レンダー | |
| render | レンダー / 描画 | 文脈で選ぶ |
| headless | ヘッドレス | |
| markup | マークアップ | |
| hook | フック | |
| context | コンテキスト | |
| memoize / memoization | メモ化する / メモ化 | |
| derived | 派生した | |
| reactive / reactivity | リアクティブ / リアクティビティ | |
| updater | アップデーター | `Updater` 型はコードのまま |
| tree-shaking / tree-shakable | ツリーシェイキング / ツリーシェイク可能 | |
| bundle size | バンドルサイズ | |
| opt-in | オプトイン（明示的に有効にする） | |
| client-side / server-side | クライアントサイド / サーバーサイド | |
| sorting | ソート | |
| filtering / filter | フィルタリング / フィルター | |
| column filter / global filter | 列フィルター / グローバルフィルター | |
| fuzzy filtering | あいまい検索フィルター | |
| faceting / faceted values | ファセット / ファセット値 | |
| grouping | グループ化 | |
| aggregation | 集計 | |
| expanding | 展開 | |
| pagination / page index / page size | ページネーション / ページ番号 / ページサイズ | |
| pinning / pinned | 固定 / 固定された | |
| row selection / cell selection | 行選択 / セル選択 | |
| cell spanning | セル結合 | |
| column sizing / column resizing | 列幅 / 列幅の変更 | |
| column visibility | 列の表示切り替え | |
| column ordering | 列の並べ替え | |
| virtualization | 仮想化 | |
| escape hatch | 抜け道（escape hatch） | |
| kitchen sink | 全部入り（kitchen sink） | サンプル名はそのまま |
| migration / migrate | 移行 / 移行する | |
| legacy | レガシー | |
| deprecated | 非推奨 | |
| experimental | 実験的 | |
| type helper | 型ヘルパー | |
| type parameter / generic | 型パラメーター / ジェネリクス | |
| devtools | Devtools | |

## TypeDoc の定型句

React API リファレンス（`docs/framework/react/reference/**`）に出てくる定型の見出しと文言の訳です。

| English | 日本語 |
|---|---|
| Defined in: | 定義元: |
| Type Parameters | 型パラメーター |
| Parameters | パラメーター |
| Returns | 戻り値 |
| Properties | プロパティ |
| Call Signature | 呼び出しシグネチャ |
| Type Declaration | 型宣言 |
| Deprecated | 非推奨 |
| Example / Examples | 例 |
| Remarks | 備考 |
| Extends / Extended by | 継承元 / 継承先 |
| Functions / Interfaces / Type Aliases / Variables | 関数 / インターフェース / 型エイリアス / 変数 |
