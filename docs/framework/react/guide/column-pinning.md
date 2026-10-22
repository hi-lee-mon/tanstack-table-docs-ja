---
title: 列の固定（React）ガイド
---

## サンプル {#examples}

実装をすぐに見たい場合は、次の React のサンプルを参照してください。

- [列の固定](https://tanstack.com/table/latest/docs/framework/react/examples/column-pinning)
- [テーブルを分割する列の固定](https://tanstack.com/table/latest/docs/framework/react/examples/column-pinning-split)
- [sticky による列の固定](https://tanstack.com/table/latest/docs/framework/react/examples/column-pinning-sticky)

### 列の固定のセットアップ {#column-pinning-setup}

列の固定の機能を使うためのテーブルのセットアップ方法は次のとおりです。列の固定の機能を追加すると、関連する API が使えるようになります。

```tsx
import {
  useTable,
  tableFeatures,
  columnPinningFeature,
} from '@tanstack/react-table'

const features = tableFeatures({ columnPinningFeature })

const table = useTable({
  features,
  columns,
  data,
})
```

## 列の固定（React）ガイド {#column-pinning-react-guide}

TanStack Table には、テーブルの UI で列の固定を実装するのに役立つ状態と API があります。列の固定は複数の方法で実装できます。固定した列をそれぞれ別のテーブルに分ける方法もあれば、すべての列を同じテーブルに置いたまま、固定の状態に従って列を正しい順に並べ、sticky な CSS で列を先頭または末尾に固定する方法もあります。

`start` と `end` は論理的な固定領域です。LTR（左から右に書く）の言語やレイアウトでは、通常 `start` が左、`end` が右に当たります。RTL（右から左に書く）の言語やレイアウトでは、通常 `start` が右、`end` が左に当たります。

### 列の固定が列の順序に与える影響 {#how-column-pinning-affects-column-order}

列を並べ替える可能性のあるテーブルの機能は3つあり、次の順に適用されます。

1. **列の固定** - 固定している場合、列は先頭に固定された列、中央（固定されていない）の列、末尾に固定された列に分けられます。
2. 手動の[列の並べ替え](./column-ordering) - 手動で指定した列の順序が適用されます。
3. [グループ化](./grouping) - グループ化が有効で、グループ化の状態がアクティブであり、かつ `tableOptions.groupedColumnMode` が `'reorder' | 'remove'` に設定されている場合、グループ化された列が列の並びの先頭に移動します。

固定された列の順序を変える方法は、`columnPinning.start` と `columnPinning.end` の状態そのものを変えることだけです。`columnOrder` の状態は、固定されていない（「中央」の）列の順序にしか影響しません。

### 列の固定の状態 {#column-pinning-state}

`columnPinning` の状態を自分で管理するかどうかは任意です。状態を永続化する機能を追加するのでなければ、通常は必要ありません。TanStack Table は、列の固定の状態をすでに追跡しています。必要であれば、`columnPinning` の状態もほかのテーブルの状態と同じように管理してください。

v9 で状態の一部（スライス）を自分で持つ場合に推奨される方法は、外部のアトムをテーブルの `atoms` オプションに渡すことです。外部のアトムを使うと、アプリのどこからでも細かい単位で購読できます。また、テーブルを持つコンポーネントを再レンダーさせずに、ほかのコードから固定の状態を読み書きできます。

```tsx
import { useCreateAtom, useSelector } from '@tanstack/react-store'
import {
  useTable,
  tableFeatures,
  columnPinningFeature,
} from '@tanstack/react-table'
import type { ColumnPinningState } from '@tanstack/react-table'

const features = tableFeatures({ columnPinningFeature })

const columnPinningAtom = useCreateAtom<ColumnPinningState>({
  start: [],
  end: [],
})

const columnPinning = useSelector(columnPinningAtom) // subscribe wherever it is needed

const table = useTable({
  features,
  //...
  atoms: {
    columnPinning: columnPinningAtom,
  },
  //...
})
```

v8 と同じ `state.columnPinning` と `onColumnPinningChange` を組み合わせるパターンも、引き続き使えます。単純な統合や v8 のコードを移行するときには便利ですが、外部のアトムほど細かい単位では購読できません。詳しい比較は[テーブルの状態のガイド](./table-state)を参照してください。

```tsx
const [columnPinning, setColumnPinning] = useState<ColumnPinningState>({
  start: [],
  end: [],
})

const table = useTable({
  features,
  //...
  state: {
    columnPinning,
    //...
  },
  onColumnPinningChange: setColumnPinning,
  //...
})
```

### 列をデフォルトで固定する {#pin-columns-by-default}

よくあるのが、一部の列を最初から固定しておきたいという場面です。これは、固定する列の columnId で `columnPinning` の状態を初期化するか、テーブルオプションの `initialState` を使うことで実現できます。

```tsx
const table = useTable({
  features,
  //...
  initialState: {
    columnPinning: {
      start: ['expand-column'],
      end: ['actions-column'],
    },
    //...
  },
  //...
})
```

### 列の固定に役立つ API {#useful-column-pinning-apis}

> [!NOTE]
> これらの API は、`columnPinningFeature` を使っているときに利用できます。

列の固定を実装するのに役立つ Column API のメソッドがいくつかあります。

- `column.getCanPin`: 列を固定できるかどうかを判定します。
- `column.pin`: 列を先頭または末尾に固定します。固定の解除にも使います。
- `column.getIsPinned`: 列がどこに固定されているかを判定します。
- `column.getPinnedIndex`: 固定された列グループの中での、その列のインデックスを読み取ります。
- `column.getStart`: 固定された列に設定する正しい `start` の CSS 値を得ます。
- `column.getAfter`: 固定された列に設定する正しい `end` の CSS 値を得ます。
- `column.getIsLastColumn`: 列が固定されたグループの最後の列かどうかを判定します。box-shadow を付けるときに便利です。
- `column.getIsFirstColumn`: 列が固定されたグループの最初の列かどうかを判定します。box-shadow を付けるときに便利です。

固定の状態を直接更新するには `table.setColumnPinning` を使います。`table.resetColumnPinning` を使うと `initialState.columnPinning` に戻せます。`true` を渡すと、固定された列の配列を両方とも空にします。

```tsx
table.setColumnPinning({
  start: ['firstName'],
  end: ['actions'],
})

table.resetColumnPinning()
table.resetColumnPinning(true)
```

テーブルインスタンスには、領域ごとに固定された列とヘッダーを取得するヘルパーがあります。

```tsx
table.getStartLeafColumns()
table.getCenterLeafColumns()
table.getEndLeafColumns()

table.getStartVisibleLeafColumns()
table.getCenterVisibleLeafColumns()
table.getEndVisibleLeafColumns()

table.getStartHeaderGroups()
table.getCenterHeaderGroups()
table.getEndHeaderGroups()

table.getStartFooterGroups()
table.getCenterFooterGroups()
table.getEndFooterGroups()

table.getStartFlatHeaders()
table.getCenterFlatHeaders()
table.getEndFlatHeaders()

table.getStartLeafHeaders()
table.getCenterLeafHeaders()
table.getEndLeafHeaders()
```

`table.getPinnedLeafColumns(position)` で固定された末端の列を、`table.getPinnedVisibleLeafColumns(position)` で表示中の固定された末端の列を、領域を指定して取得することもできます。

```tsx
table.getPinnedLeafColumns('start')
table.getPinnedLeafColumns('center')
table.getPinnedLeafColumns('end')

table.getPinnedVisibleLeafColumns('start')
table.getPinnedVisibleLeafColumns('center')
table.getPinnedVisibleLeafColumns('end')
```

固定された列があるかどうかは `table.getIsSomeColumnsPinned()` で確認できます。`'start'` または `'end'` を渡すと、片側だけを確認できます。

### テーブルを分割する列の固定 {#split-table-column-pinning}

sticky な CSS で列を固定するだけなら、ほとんどの場合は `table.getHeaderGroups` と `row.getVisibleCells` メソッドを使って、いつもどおりにテーブルを描画すれば十分です。

一方、固定した列をそれぞれ別のテーブルに分ける場合は、`table.getStartHeaderGroups`、`table.getCenterHeaderGroups`、`table.getEndHeaderGroups`、`row.getStartVisibleCells`、`row.getCenterVisibleCells`、`row.getEndVisibleCells` の各メソッドを使って、そのテーブルに関係する列だけを描画できます。
