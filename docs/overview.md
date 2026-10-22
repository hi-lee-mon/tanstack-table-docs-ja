---
title: 概要
---

> [!NOTE]
> TanStack Table v8 からアップグレードする場合は、お使いのフレームワーク向けの移行ガイドから始めてください。

- [v9 への移行](./framework/react/guide/migrating)


TanStack Table は、強力なテーブルやデータグリッドのコンポーネントを自作するための最適な手段です。_驚くほど高速_に動作しますが、何より重要なのは、**デザインとマークアップを 100% 自分で制御できる**ことです。

マークアップを数秒で生成できる AI の時代になり、既製のコンポーネントが持っていた「入力の手間を省く」という従来の価値は、かつてないほど小さくなりました。いま大切なのは、出来上がるものを自分のものとして所有し、制御することです。TanStack Table が提供するのは、まさにそれです。

TanStack Table は、これまで使ってきたテーブルライブラリとは少し毛色が違うかもしれません。[AG Grid](https://ag-grid.com?utm_source=reacttable&utm_campaign=githubreacttable) のようなライブラリが提供する既製のテーブルコンポーネントでは**ありません**。TanStack Table はヘッドレス UI ライブラリです。好きな JavaScript ライブラリ、コンポーネントライブラリ、デザインシステムを使って、自由にカスタマイズできるテーブルやデータグリッドのコンポーネントを正しいやり方で自作できます。TanStack Table は、今使っている、あるいはこれから使いたいフロントエンド技術が何であれ、そこにつないで使える_エンジン_です。

TanStack Table の根幹は、特定の技術に**依存しない**ことです。テーブルのデータ処理や状態のロジックの大部分は、フレームワークに依存しない TypeScript で書かれており、フレームワークアダプターがそのコアをお好みのフレームワークにつなぎます。公式アダプターは React、Preact、Octane、Vue、Solid、Svelte、Angular、Ember、Lit、Alpine 向けに用意されています。`@tanstack/table-core` を使えば、素の JavaScript からコアを直接使うこともできます。

また、**どの CSS やコンポーネントライブラリを使うかも問いません**。Tailwind、Bootstrap、Material UI、ShadCN UI はもちろん、独自のデザインシステムとも組み合わせられます。

## 「ヘッドレス」UI とは {#what-is-headless-ui}

**ヘッドレス UI** とは、UI 要素やインタラクションのためのロジック、状態、処理、API を提供する一方で、**マークアップやスタイル、既製の実装は提供しない**ライブラリやユーティリティを指す言葉です。複雑な UI を作るときに難しいのは、たいてい状態、イベント、副作用、データ処理まわりです。これらの関心事をマークアップやスタイルから切り離すと、ロジックはモジュール化されて再利用しやすくなり、見た目や操作感は完全に自分で制御できます。TanStack Table のようなヘッドレスライブラリを使えば、データ処理、状態管理、ビジネスロジックといった複雑な作業はライブラリが引き受けてくれます。そのため、デザインやユースケースごとに異なる、より細かな判断に集中できます。

> もっと詳しく知りたい方は、[ヘッドレス UI についての記事](https://www.merrickchristensen.com/articles/headless-user-interface-components/)をお読みください。

実際にどう違うのかを見てみましょう。既製のテーブルコンポーネントでは、props を渡し、出来上がったものを外側からスタイリングします。できることは、そのコンポーネントの props やテーマ API が許す範囲に限られます。TanStack Table では、テーブルインスタンスを作成し、その状態と API を使って自分のマークアップをレンダーします。

```diff
- {/* Pass props into a pre-built component and hope you can style it */}
- <PrebuiltDataGrid
-   data={data}
-   columns={columns}
-   theme={messyThemeOverrides}
-   sx={cssOverridesThatHopefullyWork}
-   positionPagination={"however-my-stakeholders-are-feeling-today"}
- />
+ // Build your own markup from the table instance's state and APIs
+ const table = useTable({ features, columns, data })
+
+ return (
+   <table className="anything-you-want">
+     <thead>
+       {/* need to really customize the functionality in your headers? no problem! */}
+       {table.getHeaderGroups().map((headerGroup) => ( ... ))}
+     </thead>
+     <tbody>
+       {/* want to add virtualization here? no problem! */}
+       {table.getRowModel().rows.map((row) => ( ... ))}
+     </tbody>
+   </table>
+ )
```


## 機能 {#features}

TanStack Table には多くの機能が詰め込まれていますが、バンドルされるのは実際に使う機能だけです。v9 のパッケージ全体は、minify して Brotli 圧縮すると約 25 KB です。しかしそれ以上に重要なのは、**モジュール化されている**ことです。テーブルで実際に使う機能と行モデルだけを登録すれば、使わないオプションの機能はバンドラーがツリーシェイキングで取り除きます。基本的なテーブルなら、バンドルされるのは小さなコアだけです。機能ごとにサイズが異なり、どれも同じコアを共有するため、実際にどれだけ削減できるかは登録する機能によって変わります。

私たちは TanStack Table を、単なるライブラリというより、テーブルを作るための「システム」だと考えています。これまでに作られたテーブルライブラリの中でも、指折りのカスタマイズ性を持っているからです。TanStack Table には次の機能が組み込まれています。さらに、独自の状態や API を追加するためのカスタム機能（プラグイン）の仕組みもあります。

- [セル選択](./framework/react/guide/cell-selection) - スプレッドシートのように、セルを長方形の範囲で選択する
- [セル結合](./framework/react/guide/cell-spanning) - 本体の隣り合うセルを、行方向または列方向に結合する
- [列フィルタリング](./framework/react/guide/column-filtering) - 列ごとの検索値で行を絞り込む
- [列のグループ化](./framework/react/guide/grouping) - 1つ以上の列の値で行をグループ化する
- [列の並べ替え](./framework/react/guide/column-ordering) - 列の順序を動的に変更する
- [列の固定](./framework/react/guide/column-pinning) - 列をテーブルの左端または右端に固定する
- [列幅の変更](./framework/react/guide/column-resizing) - ユーザーがドラッグハンドルで列幅を変えられるようにする
- [列幅](./framework/react/guide/column-sizing) - 列の幅を動的に変更する
- [列の表示切り替え](./framework/react/guide/column-visibility) - 列を表示・非表示にする
- [ファセット](./framework/react/guide/column-faceting) - 列またはテーブル全体について、一意な値や最小値・最大値を一覧する
- [グローバルフィルタリング](./framework/react/guide/global-filtering) - テーブル全体に対する検索値で行を絞り込む
- [行の集計](./framework/react/guide/aggregation) - グループ化した行、ルートの行、または任意の行の集合について集計値を計算する
- [行の展開](./framework/react/guide/expanding) - 行（サブ行）を展開・折りたたむ
- [行のページネーション](./framework/react/guide/pagination) - 行をページに分ける
- [行の固定](./framework/react/guide/row-pinning) - 行をテーブルの上端または下端に固定する
- [行選択](./framework/react/guide/row-selection) - 行を選択・選択解除する（チェックボックス）
- [行のソート](./framework/react/guide/sorting) - 列の値で行をソートする


## 組み合わせ {#composition}

ヘッドレスとは、単に「スタイルは自分で用意する」という意味ではありません。マークアップもイベントハンドラーも、（必要なら）状態も自分のものなので、TanStack Table はテーブルに必要な他の要素ときれいに組み合わせられます。

- **自分の状態**: テーブルの状態のどの部分（ソート、フィルター、ページネーションなど）でも、テーブルの外に持ち上げて好きなように管理できます。フレームワークの状態でも、グローバルなストアでも、URL でもかまいません。
- **自分の機能**: カスタム機能を使うと、独自の状態や API をテーブルインスタンスに直接追加できます。組み込みの機能と同じように並べて使えます。詳しくは、お使いのフレームワーク向けのカスタム機能のガイドを参照してください。
- **自分のロジック**: それ以外のこと（凝ったインタラクション、アナリティクス、ドラッグ＆ドロップなど）は、テーブルのまわりに自分で書くコードにすぎません。相手にしなければならないブラックボックスはありません。

そのため、TanStack Table は他の TanStack ライブラリとも組み合わせやすくなっています。

- [TanStack Virtual](https://tanstack.com/virtual/latest) - テーブルのロジックを一切変えずに、数千の行や列を仮想化する（お使いのフレームワーク向けの仮想化のガイドを参照）
- [TanStack Query](https://tanstack.com/query/latest) - 手動のページネーション、ソート、フィルタリングのために、サーバーサイドのデータを取得してキャッシュする
- [TanStack Form](https://tanstack.com/form/latest) - バリデーション付きで、編集できるセルや行のインライン編集を作る
- [TanStack Pacer](https://tanstack.com/pacer/latest) - フィルターの入力など、立て続けに起こるインタラクションをデバウンスまたはスロットルする
- [TanStack Hotkeys](https://tanstack.com/hotkeys/latest) - テーブルの移動や操作に、型安全なキーボードショートカットを追加する
- [TanStack Store](https://tanstack.com/store/latest) - もともと内部でテーブルの状態を支えています。独自のアトムを渡せば、状態のどの部分でも完全に制御できます

## はじめる {#get-started}

さっそく作ってみませんか？ お使いのフレームワーク向けのクイックスタートに進み、実際に動くサンプルを見てみてください。

- [React クイックスタート](./framework/react/quick-start)
- [全部入り（Kitchen Sink）のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink) - 組み込みの機能のほとんどを1つのテーブルで組み合わせたもの

コンポーネントライブラリを使っていますか？ 次のサンプルは、TanStack Table を人気の React コンポーネントライブラリと組み合わせたものです。それぞれ基本版と応用版（全部入り）があります。

- ShadCN (Base UI): [基本のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/lib-shadcn-base) | [応用のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink-shadcn-base)
- ShadCN (Radix UI): [基本のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/lib-shadcn-radix) | [応用のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink-shadcn-radix)
- HeroUI: [基本のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/lib-hero-ui) | [応用のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink-hero-ui)
- React Aria: [基本のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/lib-react-aria) | [応用のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink-react-aria)
- Material UI: [基本のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/lib-material-ui) | [応用のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink-material-ui)
- Mantine: [基本のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/lib-mantine) | [応用のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink-mantine)
- Chakra UI: [基本のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/lib-chakra-ui) | [応用のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/kitchen-sink-chakra-ui)
