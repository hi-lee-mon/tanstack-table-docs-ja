---
title: 列の並べ替え（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React のサンプルを参照してください。

- [列の並べ替え](https://tanstack.com/table/latest/docs/framework/react/examples/column-ordering)
- [列のドラッグ＆ドロップ](https://tanstack.com/table/latest/docs/framework/react/examples/column-dnd)

### 列の並べ替えのセットアップ {#column-ordering-setup}

列の並べ替え機能を使うためのテーブルの設定方法は次のとおりです。列の並べ替え機能を追加すると、関連する API が使えるようになります。

```tsx
import {
  useTable,
  tableFeatures,
  columnOrderingFeature,
} from '@tanstack/react-table'

const features = tableFeatures({ columnOrderingFeature })

const table = useTable({
  features,
  columns,
  data,
})
```

## 列の並べ替え（React）ガイド {#column-ordering-react-guide}

既定では、列は `columns` 配列に定義した順に並びます。ただし、`columnOrder` 状態を使えば列の順序を手動で指定できます。列の固定やグループ化といったほかの機能も、列の順序に影響することがあります。

### 列の順序に影響するもの {#what-affects-column-order}

列の順序を変えうるテーブルの機能は3つあり、次の順に適用されます。

1. [列の固定](./column-pinning) - 固定している場合、列は先頭に固定された列、中央（固定されていない列）、末尾に固定された列に分けられます。
2. 手動の**列の並べ替え** - 手動で指定した列の順序が適用されます。
3. [グループ化](./grouping) - グループ化が有効で、グループ化の状態が有効になっており、かつ `tableOptions.groupedColumnMode` が `'reorder' | 'remove'` に設定されている場合、グループ化された列が列の並びの先頭に移動します。

> [!NOTE]
> 列の固定と併用している場合、`columnOrder` 状態は固定されていない列にだけ影響します。

### 列の順序の状態 {#column-order-state}

`columnOrder` 状態を指定しなければ、TanStack Table は `columns` 配列での列の順序をそのまま使います。列の順序を指定したい場合は、文字列の列 ID の配列を `columnOrder` 状態に渡します。

#### 列の順序の既定値 {#default-column-order}

列の最初の順序を指定するだけでよければ、テーブルオプション `initialState` に `columnOrder` 状態を指定するだけで済みます。

```tsx
const features = tableFeatures({ columnOrderingFeature })

const table = useTable({
  features,
  //...
  initialState: {
    columnOrder: ['columnId1', 'columnId2', 'columnId3'],
  },
  //...
})
```

> [!NOTE]
> テーブルオプション `state` でも `columnOrder` 状態を指定している場合、`initialState` は効果を持ちません。個々の状態は `initialState` か `state` のどちらか一方だけで指定し、両方には指定しないでください。

#### 列の順序の状態を管理する {#managing-column-order-state}

列の順序を動的に変えたい場合や、テーブルの初期化後に列の順序を設定したい場合は、ほかのテーブルの状態と同じように `columnOrder` 状態を管理できます。

v9 では、状態の一部を自分で持つ方法として、テーブルの `atoms` オプションに外部のアトムを渡すやり方を推奨しています。外部のアトムを使うと、アプリのどこからでも細かい単位で購読できます。また、テーブルを持つコンポーネントを再レンダーさせることなく、ほかのコードから列の順序を読み書きできます。

```tsx
import { useCreateAtom, useSelector } from '@tanstack/react-store'
import {
  useTable,
  tableFeatures,
  columnOrderingFeature,
} from '@tanstack/react-table'
import type { ColumnOrderState } from '@tanstack/react-table'

const features = tableFeatures({ columnOrderingFeature })

const columnOrderAtom = useCreateAtom<ColumnOrderState>([
  'columnId1',
  'columnId2',
  'columnId3',
])

const columnOrder = useSelector(columnOrderAtom) // subscribe wherever it is needed

const table = useTable({
  features,
  //...
  atoms: {
    columnOrder: columnOrderAtom,
  },
  //...
})
```

v8 と同じように `state.columnOrder` と `onColumnOrderChange` を組み合わせるパターンも、引き続き使えます。単純な連携や v8 のコードを移行するときには便利ですが、外部のアトムほど細かい単位では購読できません。詳しい比較は [テーブルの状態ガイド](./table-state) を参照してください。

```tsx
const features = tableFeatures({ columnOrderingFeature })

const [columnOrder, setColumnOrder] = useState<ColumnOrderState>([
  'columnId1',
  'columnId2',
  'columnId3',
])
//...
const table = useTable({
  features,
  //...
  state: {
    columnOrder,
    //...
  },
  onColumnOrderChange: setColumnOrder,
  //...
})
```

### 列を並べ替える {#reordering-columns}

ユーザーが列を並べ替えられる UI がテーブルにある場合は、使っているドラッグ＆ドロップの仕組みのドロップイベントを `table.setColumnOrder` につなぎます。公式の [列のドラッグ＆ドロップのサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/column-dnd) では、DnD Kit の `arrayMove` ユーティリティを使ってこれを実現しています。

```tsx
import { arrayMove } from '@dnd-kit/sortable'
import type { DragEndEvent } from '@dnd-kit/core'

// reorder columns after drag & drop
function handleDragEnd(event: DragEndEvent) {
  const { active, over } = event
  if (over && active.id !== over.id) {
    table.setColumnOrder((prevColumnOrder) => {
      const oldIndex = prevColumnOrder.indexOf(active.id as string)
      const newIndex = prevColumnOrder.indexOf(over.id as string)
      return arrayMove(prevColumnOrder, oldIndex, newIndex) // splice util
    })
  }
}
```

`table.setColumnOrder` は、`columnOrder` 状態をテーブルが内部で管理している場合でも、`state` と `onColumnOrderChange` で制御している場合でも、外部のアトムで自分で持っている場合でも、同じように動きます。

### 列の並べ替えの API {#column-ordering-apis}

列の順序の状態を直接更新するには `table.setColumnOrder` を使います。`table.resetColumnOrder` を使うと順序を `initialState.columnOrder` に戻せます。`true` を渡すと順序の状態を空にします。

```tsx
table.setColumnOrder(['lastName', 'firstName', 'age'])
table.resetColumnOrder()
table.resetColumnOrder(true)
```

列には、列の固定・手動の並べ替え・グループ化を適用したあとの現在の位置を読み取るヘルパーがあります。

```tsx
column.getIndex()
column.getIndex('start')
column.getIndex('center')
column.getIndex('end')

column.getIsFirstColumn()
column.getIsLastColumn()
```

これらのヘルパーは、列の境界にスタイルを付けるときや、現在描画されている順序を知る必要があるドラッグ＆ドロップのターゲットを作るときに役立ちます。

#### ドラッグ＆ドロップによる列の並べ替えのおすすめ（React） {#drag-and-drop-column-reordering-suggestions-react}

TanStack Table は、どのドラッグ＆ドロップの仕組みを使うかについて特定の方針を持っていません。いくつかおすすめを挙げます。

1. ライブラリを使いたい場合は [DnD Kit](https://dndkit.com/) を使ってください。公式の [列のドラッグ＆ドロップ](https://tanstack.com/table/latest/docs/framework/react/examples/column-dnd) と [行のドラッグ＆ドロップ](https://tanstack.com/table/latest/docs/framework/react/examples/row-dnd) のサンプルもこれを使っています（`@dnd-kit/core`、`@dnd-kit/sortable`、`@dnd-kit/modifiers`、`@dnd-kit/utilities` パッケージ）。モジュール化されており、React の Strict Mode でも動作し、セマンティックな `<table>` マークアップともうまく組み合わせられます。

2. 依存関係をまったく増やしたくない場合は、ブラウザーネイティブのドラッグイベント（`onDragStart`、`onDragEnter`、`onDragEnd`）と自前の状態を組み合わせる方法を検討してください。とても軽量にできますが、モバイルでタッチ操作にきちんと対応するには追加の作業が必要です。[Material React Table](https://www.material-react-table.com/docs/examples/column-ordering) は、DnD ライブラリに依存せずにこの方法で TanStack Table の列の並べ替えを実装しており、そのソースコードはよい参考になります。

3. ほかの DnD ライブラリを検討する場合は、採用を決める前に、保守の状況、React のバージョンとの互換性（とくに Strict Mode）、バンドルサイズ、`<table>` マークアップをどの程度うまく扱えるかを確認してください。`react-dnd` や `react-beautiful-dnd` といった古いライブラリは、もう活発には開発されていません。その系統の API を好む場合は、Atlassian の [Pragmatic drag and drop](https://atlassian.design/components/pragmatic-drag-and-drop/about) が `react-beautiful-dnd` の後継として活発に保守されています。
