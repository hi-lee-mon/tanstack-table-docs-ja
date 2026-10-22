---
title: グループ化（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React のサンプルを参照してください。

- [グループ化](https://tanstack.com/table/latest/docs/framework/react/examples/grouping)

> [!NOTE]
> `columnGroupingFeature` と `rowAggregationFeature` は、別々の機能になりました。どちらか一方だけを登録することも、グループ化した行で集計値も計算したい場合は両方を登録することもできます。集計の設定については[集計ガイド](./aggregation)を参照してください。

### グループ化のセットアップ {#grouping-setup}

グループ化の機能を使うためのテーブルのセットアップ方法は次のとおりです。グループ化の機能を追加すると、関連する API が使えるようになります。クライアントサイドでグループ化する場合は、その機能の後ろに `groupedRowModel` も設定してください。行モデルのスロットは型チェックされるためです。

```tsx
import {
  useTable,
  tableFeatures,
  columnGroupingFeature,
  createGroupedRowModel,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnGroupingFeature,
  groupedRowModel: createGroupedRowModel(), // if using client-side grouping
  // manualGrouping: true, // if using manual server-side grouping
})

const table = useTable({
  features,
  columns,
  data,
})
```

## グループ化（React）ガイド {#grouping-react-guide}

TanStack Table のグループ化は列に適用する機能で、特定の列をもとにテーブルの行を分類・整理できます。大量のデータがあり、それを何らかの基準でまとめたい場合に便利です。

グループ化は列の順序にも影響します。列を並べ替えうるテーブルの機能は3つあり、次の順に適用されます。

1. [列の固定](./column-pinning) - 固定している場合、列は先頭に固定された列、中央（固定されていない列）、末尾に固定された列に分かれます。
2. 手動の[列の並べ替え](./column-ordering) - 手動で指定した列の順序が適用されます。
3. **グループ化** - グループ化が有効で、グループ化の状態が設定されていて、`tableOptions.groupedColumnMode` が `'reorder' | 'remove'` の場合、グループ化した列が列の並びの先頭に移動します。

### クライアントサイドとサーバーサイドのグループ化 {#client-side-vs-server-side-grouping}

グループがすべての行を表すべきときは、グループ化はデータセット全体を対象にする必要があります。ブラウザーがデータセット全体を持っている場合は、クライアントサイドのグループ化を使います。サーバーが1ページ分などの一部のデータしか返さない場合や、グループ化と集計をサーバーで行う必要がある場合は、手動のサーバーサイドのグループ化を使います。

判断の枠組み全体、パフォーマンスの要因、データ操作を組み合わせる際の指針については、[クライアントサイドとサーバーサイドのガイド](../../../guide/client-side-vs-server-side)を参照してください。

クライアントサイドのグループ化行モデルは、入力が変わるとページ番号と展開状態の自動リセット用フックを呼び出します。それらの状態が実際にリセットされるかどうかは、`autoResetPageIndex`、`autoResetExpanded`、`autoResetAll`、`manualPagination`、`manualExpanding` の各オプションで決まります。グループ化を手動で行い、この行モデルを省略または迂回している場合、グループ化の状態が変わってもこれらのフックは呼ばれません。必要に応じて、グループ化の変更ハンドラーの中で、依存するサーバーサイドの状態をリセットしてください。

### クライアントサイドのグループ化 {#client-side-grouping}

グループ化の機能を使うには、`columnGroupingFeature` と `groupedRowModel` のファクトリーを features に追加します。グループ化行モデルは、グループ化の状態に基づいて行をグループ化する役割を担います。

```tsx
import {
  useTable,
  tableFeatures,
  columnGroupingFeature,
  createGroupedRowModel,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnGroupingFeature,
  groupedRowModel: createGroupedRowModel(),
})

const table = useTable({
  features,
  // other options...
})
```

グループ化の状態が設定されていると、テーブルは該当する行を、グループ化した行の subRows として追加します。グループ化した行は、最初に該当した行と同じ位置でテーブルの行に追加されます。該当した行そのものは、テーブルの行から取り除かれます。
ユーザーがグループ化した行を展開・折りたためるようにするには、展開の機能を使います。

```tsx
const features = tableFeatures({
  columnGroupingFeature,
  rowExpandingFeature,
  groupedRowModel: createGroupedRowModel(),
  expandedRowModel: createExpandedRowModel(),
})

const table = useTable({
  features,
  // other options...
})
```

### グループ化の状態 {#grouping-state}

グループ化の状態は文字列の配列で、各文字列はグループ化に使う列の ID です。配列内の文字列の順序が、グループ化の順序になります。たとえばグループ化の状態が ['column1', 'column2'] なら、テーブルはまず column1 でグループ化し、次に各グループの中で column2 でグループ化します。グループ化の状態は setGrouping 関数で操作できます。

```tsx
table.setGrouping(['column1', 'column2'])
```

resetGrouping 関数を使うと、グループ化の状態を初期状態に戻すこともできます。

```tsx
table.resetGrouping()
```

初期設定では、列をグループ化するとその列はテーブルの先頭に移動します。この動作は groupedColumnMode オプションで変えられます。'reorder' にすると、グループ化した列はテーブルの先頭に移動します。'remove' にすると、グループ化した列はテーブルから取り除かれます。false にすると、グループ化した列は移動も削除もされません。

```tsx
const table = useTable({
  features,
  // other options...
  groupedColumnMode: 'reorder',
})
```

### 手動のグループ化 {#manual-grouping}

サーバーサイドでグループ化する場合は、manualGrouping オプションで手動のグループ化を有効にできます。このオプションを true にすると、テーブルは getGroupedRowModel() で行を自動的にグループ化しなくなります。代わりに、テーブルに渡す前に行をグループ化しておくことが求められます。

```tsx
const features = tableFeatures({ columnGroupingFeature })

const table = useTable({
  features,
  // other options...
  manualGrouping: true,
})
```

> [!NOTE]
> 現時点では、TanStack Table でサーバーサイドのグループ化を手軽に実現する方法はあまり知られていません。実現するには、セルの独自レンダリングを数多く書く必要があります。

### 制御されたグループ化の状態 {#controlled-grouping-state}

アプリケーションのほかの場所でグループ化の状態にアクセスする必要がある場合は、`grouping` の状態スライスを自分で管理できます。v9 で推奨する方法は、テーブルオプション `atoms` で外部のアトムを渡すことです。アトムを使うと細かい粒度の購読が保たれ、テーブルを持つコンポーネントを再レンダーさせることなく、アプリのどこからでも（サーバーサイドのグループ化に使うクエリキーの中などで）グループ化の値を読み取れます。

```tsx
import { useCreateAtom, useSelector } from '@tanstack/react-store'
import type { GroupingState } from '@tanstack/react-table'

const groupingAtom = useCreateAtom<GroupingState>([])

// subscribe to the atom wherever you need the value
const grouping = useSelector(groupingAtom)

const table = useTable({
  features,
  // other options...
  atoms: {
    grouping: groupingAtom, // grouping APIs now update groupingAtom
  },
})
```

あるいは、v8 スタイルの `state.grouping` と `onGroupingChange` を組み合わせるパターンも引き続き使えます。単純な連携や v8 のコードを移行するときには便利ですが、外部のアトムに比べると粒度が粗くなります。詳しい比較は[テーブルの状態ガイド](./table-state)を参照してください。

```tsx
const [grouping, setGrouping] = useState<GroupingState>([])

const table = useTable({
  features,
  // other options...
  state: {
    grouping,
  },
  onGroupingChange: setGrouping,
})
```

### グループ化の API {#grouping-apis}

列は、グループ化の切り替えやグループ化の UI 作成に使う API を公開しています。

```tsx
column.toggleGrouping()
column.getToggleGroupingHandler()
column.getCanGroup()
column.getIsGrouped()
column.getGroupedIndex()
```

行は、グループ化した行のレンダーに使うヘルパーを公開しています。

```tsx
row.getIsGrouped()
row.getGroupingValue(columnId)
row.groupingColumnId
row.groupingValue
```

セルは、グループ化とプレースホルダーに関するヘルパーを公開しています。

```tsx
cell.getIsGrouped()
cell.getIsPlaceholder()
```

テーブルインスタンスは、グループ化後とグループ化前の行モデルを公開しています。

```tsx
table.getGroupedRowModel()
table.getPreGroupedRowModel()
```

グループ化の状態を直接更新するには、`table.setGrouping` と `table.resetGrouping` を使います。
