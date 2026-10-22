---
title: エージェントスキル（TanStack Intent）
id: agent-skills
description: "Use TanStack Intent to wire TanStack Table's bundled Agent Skills into Claude Code, Cursor, GitHub Copilot, Codex, and other AI coding assistants."
keywords:
  - tanstack table
  - tanstack intent
  - agent skills
  - claude code
  - cursor
  - github copilot
  - codex
  - ai coding agents
  - SKILL.md
  - AGENTS.md
---

あなたは TanStack Table を使って開発していて、Claude Code、Cursor、GitHub Copilot、Codex といった AI コーディングエージェントも使っているとします。ところがエージェントは `useReactTable` のような v8 の API を提案し続けたり、機能を明示せずに行モデルを設定したり、v9 にはもう合わないアダプターのパターンで描画したりします。このガイドを終えるころには、テーブルのコードを書くたびにエージェントが TanStack Table に同梱されたスキルを自動で読み込むようになります。しかもそのスキルは、プロジェクトにインストールした TanStack Table のバージョンと常にそろった状態に保たれます。

## エージェントスキルとは {#what-are-agent-skills}

エージェントスキル（Agent Skills）は、npm パッケージに同梱される Markdown 文書（`SKILL.md`）です。AI コーディングエージェントに対して、ライブラリの正しい使い方を伝えます。どの関数を使うべきか、どのパターンを避けるべきか、特定の機能をいつ使うべきか、といった内容です。この形式はオープンな標準で、Claude Code、Cursor、GitHub Copilot、Codex などが対応しています。

TanStack Table はパッケージの中にスキルを入れて公開しています。そのため、ガイダンスはモデルの学習データに固定されたり、エージェントの設定ファイルへ手作業でコピーされたりするのではなく、`npm update` と一緒に最新の状態へ更新されます。

## TanStack Table に同梱されているスキル {#skills-shipped-by-tanstack-table}

エージェントが使えるスキルは、プロジェクトにどのパッケージをインストールしているかで決まります。

| パッケージ | スキル | 教える内容 |
| --- | --- | --- |
| `@tanstack/table-core` | `core`, `table-features`, `table-state`, `custom-features`, `migrate-v8-to-v9` | コアのアーキテクチャ、機能の登録、共有する状態をどこが持つか、プラグインの作り方、移行。オプションの各機能には、`table-features` からリンクされた、必要なときに読むリファレンスがあります。 |
| `@tanstack/<framework>-table` | `getting-started`、`table-state`、対応している場合は移行 | フレームワークでのセットアップ、描画、リアクティブな状態。リファレンスでは、再利用できるアプリ用フック、高度なリアクティビティ、保守されている Query/Virtual との統合を扱います。 |
| `@tanstack/table-devtools` とフレームワーク向け Devtools アダプター | `devtools` | テーブルインスタンスの登録と、機能・状態・オプション・行・列の確認 |
| `@tanstack/match-sorter-utils` | `fuzzy-ranking` | あいまい検索フィルター、ランキングのメタデータ、ランクを考慮したソート |

パッケージをインストールすると、各スキルは `node_modules/<package>/skills/<skill-name>/SKILL.md` に置かれます。その `references/` ディレクトリには、個別の作業向けのガイダンスが入っています。たとえば行選択のガイダンスは `@tanstack/table-core/skills/table-features/references/row-selection.md` にあります。

エントリーポイントは、各リファレンスをいつ読むべきかをエージェントに伝えます。ソートを変更するときはソートのガイダンスを読み込み、行選択や列幅の変更など関係のない機能のリファレンスは読み込みません。フレームワークの状態スキルは、まず共有の状態モデルを読み込み、そのうえでそのフレームワーク固有のリアクティブな読み取りと更新の方法を説明します。

Intent はエントリーポイントを一覧にし、要求された `SKILL.md` を1つずつ読み込みます。エージェントは、そこに書かれた前提の指示に従い、関係するリファレンスを読みます。core をインストールした React プロジェクトでは、Table のエントリーポイントが8つあります。Devtools やほかにインストールしたライブラリは、それぞれ独自のエントリーを追加します。

## ステップ1: TanStack Table をインストールする {#step-1-install-tanstack-table}

まだの場合は、使っているフレームワーク用のアダプターをインストールします。パッケージの一覧は [インストール](./installation) を参照してください。

```bash
pnpm add @tanstack/react-table
```

フレームワーク用のアダプターは `@tanstack/table-core` を依存関係としてインストールします。そのため、インストーラーからはフレームワーク固有のスキルとコアのスキルの両方が使えます。

## ステップ2: `intent install` を実行する {#step-2-run-intent-install}

プロジェクトのルートで次を実行します。

```bash
npx @tanstack/intent@latest install
```

CLI は、スキルを読み込むための軽量なガイダンスをエージェントの設定ファイルに書き込みます。このガイダンスは、プロジェクトにインストールされたパッケージからスキルを見つけ、ある程度の規模の作業を始める前にいちばん関係の深いスキルを読み込むよう、エージェントに指示します。

既定では、ガイダンスは `AGENTS.md` に書き込まれます。CLI は次のファイルも更新できます。

- Claude Code 用の `CLAUDE.md`
- Cursor 用の `.cursorrules`
- GitHub Copilot 用の `.github/copilot-instructions.md`

## ステップ3: 生成されたガイダンスを確認する {#step-3-review-the-generated-guidance}

install コマンドは、次のような `intent-skills` ブロックを追記します（ファイルがなければ作成します）。

```markdown
<!-- intent-skills:start -->

## Skill Loading

Before editing files for a substantial task:

- Run `npx @tanstack/intent@latest list` from the workspace root to see available local skills.
- If a listed skill matches the task, run `npx @tanstack/intent@latest load <package>#<skill>` before changing files.
- Use the loaded `SKILL.md` guidance while making the change.
- Monorepos: when working across packages, run the skill check from the workspace root and prefer the local skill for the package being changed.
- Multiple matches: prefer the most specific local skill for the package or concern you are changing; load additional skills only when the task spans multiple packages or concerns.

<!-- intent-skills:end -->
```

このブロックは設定ファイルの先頭近くに置いてください。そうすれば、エージェントは作業固有の指示より先にこのブロックを目にします。

同じコマンドを使えば、Table のスキルを自分で確認したり読み込んだりできます。

```bash
npx @tanstack/intent@latest list
npx @tanstack/intent@latest load @tanstack/react-table#getting-started
npx @tanstack/intent@latest load @tanstack/table-core#table-features
```

ソートについては、読み込んだエントリーポイントにある `references/sorting.md` へのリンクをたどります。load コマンドは Markdown の相対リンクを、インストール済みのパッケージを基準に解決します。パッケージマネージャーが依存関係を入れ子のパスに置いている場合も同様です。

作業とスキルの対応を明示したい場合は、`npx @tanstack/intent@latest install --map` を実行します。マッピングモードでは、インストール済みの Intent 対応パッケージを調べ、`id`、`run`、`for` からなる簡潔なエントリーを管理対象のブロックに書き込みます。

## ステップ4: 連携できているか確かめる {#step-4-confirm-its-wired-up}

コーディングエージェントで新しいセッションを開き、TanStack Table を使って何か作るよう頼んでみてください。たとえば「_TanStack Table v9 で、ソートとページネーションができる React のテーブルを作って_」のように頼みます。

次のようになっていれば連携できています。

- エージェントが v8 の `useReactTable()` API ではなく `useTable()` を使う。
- 機能と行モデルのスロットが `tableFeatures()` で明示的に宣言されている。
- 静的なデータ、列、機能が安定した参照を保っている。
- v8 の描画パターンをコピーするのではなく、アダプターの現行の描画 API を使っている。
- ヘッドレスなモデルと状態は Table が受け持ち、マークアップ、スタイル、操作、アクセシビリティはアプリケーション側が受け持っている。

それでもエージェントが v8 のパターンに戻ってしまう場合は、設定ファイルを開き直して `intent-skills` ブロックがあるか確認してください。また、`intent list` を実行してインストール済みの Table パッケージが検出されているか確かめたり、`intent load` で該当するガイダンスを直接確認したりすることもできます。

## スキルを最新に保つ {#keeping-skills-current}

スキルはパッケージごとにバージョン管理されています。TanStack Table のパッケージを更新すると、`node_modules` 配下の `SKILL.md` ファイルも一緒に更新されます。CLI を再実行する必要はありません。明示的なマッピングを使っている場合は、Table の Devtools アダプターなど別の Intent 対応パッケージを追加したあとや、マッピングを更新したいときに、`npx @tanstack/intent@latest install --map` を再実行してください。

### 古いスキルのマッピングを更新する {#update-older-skill-mappings}

情報を段階的に開示する構成（progressive disclosure）になったことで、機能ごと・組み合わせ方ごとに分かれていたスキル ID は、リファレンスに置き換えられました。エージェントの設定に古い ID が残っている場合は、次のように更新してください。

| 古いスキル ID | 置き換え先のエントリーポイントとリファレンス |
| --- | --- |
| `@tanstack/table-core#sorting`、`#row-selection`、その他のオプション機能のスキル | `@tanstack/table-core#table-features`、次に該当する機能のリファレンス |
| `@tanstack/table-core#client-vs-server` | `@tanstack/table-core#table-features`、次に `references/client-vs-server.md` |
| `@tanstack/table-core#typescript` または `#api-not-found` | `@tanstack/table-core#core`、次に該当するリファレンス |
| `@tanstack/<framework>-table#create-table-hook` | アダプターの `getting-started`、次に `references/create-table-hook.md` |
| `@tanstack/<framework>-table#with-tanstack-query` または `#with-tanstack-virtual` | アダプターの `getting-started`、次に該当する統合のリファレンス |

`package.json#intent.skills` で古いスキル ID を個別に許可している場合は、`npx @tanstack/intent@latest install --review` を実行し、置き換え先と、それに必要な前提のスキルを選んでください。パッケージ単位で許可している場合は、新しいエントリーポイントが自動的に含まれます。許可を更新したあとは、`npx @tanstack/intent@latest install --map` で明示的なマッピングを作り直してください。移動したスキルのファイルを直接指している場合も、新しいパスに直す必要があります。

コアの状態についてのガイダンスは `@tanstack/table-core#table-state` として提供されています。アダプターの状態スキルと移行スキルの ID は、引き続き使えます。移行スキルには確認用のチェックリストがすべて残っており、プロジェクトで使っている API の詳しい対応表へのリンクもあります。

## CLI を使わずにスキルを使う {#using-skills-without-the-cli}

スキルを自分で組み込みたい場合は、任意のエージェント設定ファイルから `node_modules` 内のスキルを直接参照します。最低限必要なのは、該当するファイルへの参照だけです。

```markdown
When working on TanStack React Table code, read and follow:
node_modules/@tanstack/react-table/skills/getting-started/SKILL.md
```

CLI の利用をおすすめします。インストール済みのパッケージを自動で見つけ、エージェントスキルの標準とも整合が取れるからです。とはいえ、その下にあるファイルのパス自体は変わらないので、直接参照しても問題ありません。

## さらに学ぶ {#learn-more}

- [TanStack Intent のドキュメント](https://tanstack.com/intent/latest/docs/overview): CLI の完全なリファレンスです。`scaffold`、`validate`、ライブラリのメンテナー向けの CI 設定も載っています。
- [エージェントスキルのレジストリ](https://tanstack.com/intent/registry): ほかの Intent 対応パッケージを探せます。
