---
title: 行選択（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React のサンプルを参照してください。

- [行選択](https://tanstack.com/table/latest/docs/framework/react/examples/row-selection)

### 行選択のセットアップ {#row-selection-setup}

行選択の機能を使うためのテーブルのセットアップ方法を示します。行選択の機能を追加すると、関連する API が使えるようになります。

```tsx
import {
  useTable,
  tableFeatures,
  rowSelectionFeature,
} from '@tanstack/react-table'

const features = tableFeatures({ rowSelectionFeature })

const table = useTable({
  features,
  columns,
  data,
})
```

## 行選択（React）ガイド {#row-selection-react-guide}

行選択の機能は、どの行が選択されているかを追跡し、さまざまな方法で行の選択を切り替えられるようにします。よくある使い方を見ていきましょう。

### 行選択の状態にアクセスする {#access-row-selection-state}

行選択の状態は、テーブルインスタンスがすでに管理しています。行選択の状態や選択された行には、いくつかの API からアクセスできます。

- `table.state.rowSelection` - 行選択の状態をリアクティブに返します（`useTable` のセレクターで選ばれます）
- `getSelectedRowModel()` - 選択された行を返します
- `getFilteredSelectedRowModel()` - フィルタリング後の選択された行を返します
- `getGroupedSelectedRowModel()` - グループ化とソートの後の選択された行を返します

```ts
console.log(table.state.rowSelection) //get the row selection state - { 1: true, 2: false, etc... }
console.log(table.getSelectedRowModel().rows) //get full client-side selected rows
console.log(table.getFilteredSelectedRowModel().rows) //get filtered client-side selected rows
console.log(table.getGroupedSelectedRowModel().rows) //get grouped client-side selected rows
```

イベントハンドラーなど描画以外のコードでは、`table.atoms.rowSelection.get()` で現在のスナップショットを読むこともできます。この読み取りでは、コンポーネントはその後の変更を購読しません。描画する箇所では `table.state.rowSelection`（または `table.Subscribe`）を使ってください。

> [!NOTE]
> `manualPagination` を使っている場合、`getSelectedRowModel` API は現在のページの選択された行しか返さないことに注意してください。テーブルの行モデルは、渡された `data` をもとにしか行を生成できないからです。一方、行選択の状態には、`data` 配列にない行の ID が含まれていても問題ありません。

### 行選択の状態を管理する {#manage-row-selection-state}

アプリの別の場所から選択された行の ID を手軽に使いたい場合（たとえば、それを使って API を呼び出す場合）は、行選択の状態を自分で持つことができます。v9 で推奨される方法は、テーブルの `atoms` オプションに外部のアトムを渡すことです。アトムを使えばきめ細かな購読が保たれ、テーブルを持つコンポーネントを再レンダーさせずに、アプリのどこからでも選択の値を読めます。

```ts
import { useCreateAtom, useSelector } from '@tanstack/react-store'
import {
  useTable,
  tableFeatures,
  rowSelectionFeature,
  type RowSelectionState,
} from '@tanstack/react-table'

const features = tableFeatures({ rowSelectionFeature })

const rowSelectionAtom = useCreateAtom<RowSelectionState>({})

// subscribe to the atom wherever you need the value
const rowSelection = useSelector(rowSelectionAtom)

const table = useTable({
  features,
  //...
  atoms: {
    rowSelection: rowSelectionAtom, // selection APIs now update rowSelectionAtom
  },
})
```

v8 と同じ `state.rowSelection` と `onRowSelectionChange` を組み合わせるパターンも、引き続き使えます。単純な組み込みや v8 のコードを移行するときには便利ですが、外部のアトムほどきめ細かくはありません。詳しい比較は[テーブルの状態ガイド](./table-state)を参照してください。

```ts
const [rowSelection, setRowSelection] = useState<RowSelectionState>({})

const table = useTable({
  features,
  //...
  onRowSelectionChange: setRowSelection,
  state: {
    rowSelection,
  },
})
```

### 役に立つ行 ID {#useful-row-ids}

デフォルトでは、各行の行 ID は単に `row.index` です。行選択の機能を使うなら、もっと意味のある行の識別子を使いたくなるはずです。行選択の状態は行 ID をキーにしているからです。`getRowId` テーブルオプションに、各行の一意な行 ID を返す関数を指定できます。

```ts
const table = useTable({
  features,
  //...
  getRowId: (row) => row.uuid, // use the row's uuid from your database as the row id
})
```

こうすると、行を選択したときの行選択の状態は、次のようになります。

```json
{
  "13e79140-62a8-4f9c-b087-5da737903b76": true,
  "f3e2a5c0-5b7a-4d8a-9a5c-9c9b8a8e5f7e": false
  //...
}
```

次のような形にはなりません。

```json
{
  "0": true,
  "1": false
  //...
}
```

### 条件付きで行選択を有効にする {#enable-row-selection-conditionally}

行選択は、デフォルトですべての行で有効です。特定の行だけで行選択を有効にしたり、すべての行で無効にしたりするには、`enableRowSelection` テーブルオプションを使います。このオプションには真偽値か、より細かく制御するための関数を渡せます。

```ts
const table = useTable({
  //...
  enableRowSelection: (row) => row.original.age > 18, //only enable row selection for adults
})
```

行を選択できるかどうかを UI に反映させるには、チェックボックスなどの選択 UI で `row.getCanSelect()` API を使います。

### 単一行の選択 {#single-row-selection}

デフォルトでは、テーブルは複数の行を同時に選択できます。一度に1行だけ選択できるようにしたい場合は、`enableMultiRowSelection` テーブルオプションを `false` にして複数行の選択を無効にします。関数を渡して、ある行のサブ行について条件付きで複数行の選択を無効にすることもできます。

これは、チェックボックスの代わりにラジオボタンを使うテーブルを作るときに便利です。

```ts
const table = useTable({
  //...
  enableMultiRowSelection: false, //only allow a single row to be selected at once
  // enableMultiRowSelection: row => row.original.age > 18, //only allow a single row to be selected at once for adults
})
```

### サブ行の選択 {#sub-row-selection}

デフォルトでは、親の行を選択するとそのサブ行もすべて選択されます。サブ行の自動選択を無効にしたい場合は、`enableSubRowSelection` テーブルオプションを `false` にします。関数を渡して、ある行のサブ行について条件付きでサブ行の選択を無効にすることもできます。

```ts
const table = useTable({
  //...
  enableSubRowSelection: false, //disable sub-row selection
  // enableSubRowSelection: row => row.original.age > 18, //disable sub-row selection for adults
})
```

サブ行の選択は、すべて選択する API にも適用されます。親の行がサブ行の選択を禁止している場合、`table.toggleAllRowsSelected()` と `table.toggleAllPageRowsSelected()` はその親の子孫を飛ばします。また、`table.getIsAllRowsSelected()` と `table.getIsAllPageRowsSelected()` は、すべてが選択されているかを判断するときに、それらの子孫を無視します。

親の行を選択すると、親の ID と、選択できる子孫の ID が行選択の状態に書き込まれます。その後で子を選択解除しても、デフォルトでは親の ID は削除されません。状態の ID を文字どおりの選択として扱うテーブルもあるからです。行が選択解除されるたびに祖先の ID を削除するには、切り替え用の API に `deselectParents` オプションを渡してください。

```ts
row.getToggleSelectedHandler({ deselectParents: true })
// or
row.toggleSelected(false, { deselectParents: true })
```

### Shift による範囲選択 {#shift-range-selection}

`row.getToggleSelectedHandler()` は、デフォルトで Shift による範囲選択に対応しています。選択できる行を通常どおり操作すると、そこが起点（アンカー）になります。その後で別の行を Shift を押しながら選択すると、2つの行の間（両端を含む）がまとめて選択または選択解除されます。範囲全体の状態は、クリックしたチェックボックスの結果のチェック状態で決まり、クリックした端の行が次の Shift 操作の起点になります。

ハンドラーは、イベントに `event.shiftKey` か `event.nativeEvent.shiftKey` があれば Shift として認識します。範囲選択の動作を無効にしたり、イベントの判定方法を差し替えたりもできます。

React のチェックボックスの `onChange` イベントは、元になったクリックを `nativeEvent` として公開しています。そのため、次の例ではハンドラーが Shift 修飾キーを受け取れます。

```ts
const table = useTable({
  // ...
  enableRowRangeSelection: false,

  // For example, use the platform modifier instead of Shift:
  // isRowRangeSelectionEvent: event =>
  //   Boolean((event as React.MouseEvent).metaKey),
})
```

範囲選択は、フィルタリング、グループ化、ソート、展開を含めた、テーブルの現在の論理的な表示順に従います。クライアントサイドのページネーションでは、ページネーション前の完全な並び順を使うので、範囲がページをまたぐこともあります。手動（サーバーサイド）のページネーションでは、現在の `data` に読み込まれている行だけが対象になります。

デフォルトでは、サブ行の選択が有効なとき、範囲内にある親の行は、選択できる子孫を再帰的に切り替えます。表示順の範囲内に実際に存在する行だけを変更したい場合は、`selectChildren: false` を渡してください。

```tsx
<Checkbox
  checked={row.getIsSelected()}
  onChange={row.getToggleSelectedHandler({ selectChildren: false })}
/>
```

起点は、その行 ID が表示順に残っている限り、ソート、フィルタリング、グループ化、展開、ページネーション、データの更新をまたいで保持されます。フィルタリングやデータの差し替えで起点の行がなくなった場合、次の Shift 操作は通常の行の切り替えとして扱われ、そこが新しい起点になります。`resetRowSelection`、すべて選択するいずれかの API、`table.reset()` は起点をクリアします。`row.toggleSelected()` や `table.setRowSelection()` の直接呼び出しと、外部の制御された状態の変更は、起点を設定も移動もしません。

### 行選択の UI を描画する {#render-row-selection-ui}

TanStack Table は、行選択の UI をどう描画するかを決めません。チェックボックスでもラジオボタンでも、行そのものにクリックイベントを結び付けるだけでもかまいません。テーブルインスタンスには、行選択の UI を描画するのに役立つ API がいくつかあります。

#### 行選択の API をチェックボックスの入力につなぐ {#connect-row-selection-apis-to-checkbox-inputs}

TanStack Table には、チェックボックスの入力に直接つないで行選択を簡単に切り替えられるハンドラー関数があります。これらの関数は、他の内部 API を自動的に呼び出して行選択の状態を更新し、テーブルを再レンダーします。

行の選択を切り替えるチェックボックスの入力には、`row.getToggleSelectedHandler()` API をつなぎます。

すべての行の選択を切り替える「すべて選択」のチェックボックスの入力には、`table.getToggleAllRowsSelectedHandler()` または `table.getToggleAllPageRowsSelectedHandler` API をつなぎます。

これらのハンドラー関数よりも細かく制御したい場合は、いつでも `row.toggleSelected()` や `table.toggleAllRowsSelected()` API を直接使えます。他の状態のアップデーターと同じように、`table.setRowSelection()` API を呼んで行選択の状態を直接設定することもできます。ハンドラー関数は便利のために用意されているだけです。

```tsx
const columns = [
  {
    id: 'select-col',
    header: ({ table }) => (
      <Checkbox
        checked={table.getIsAllRowsSelected()}
        indeterminate={table.getIsSomeRowsSelected()}
        onChange={table.getToggleAllRowsSelectedHandler()} //or getToggleAllPageRowsSelectedHandler
      />
    ),
    cell: ({ row }) => (
      <Checkbox
        checked={
          row.getIsSelected() ||
          (row.getCanSelectSubRows() && row.getIsAllSubRowsSelected())
        }
        disabled={!row.getCanSelect()}
        indeterminate={row.getIsSomeSelected()}
        onChange={row.getToggleSelectedHandler()}
      />
    ),
  },
  //... more column definitions...
]
```

> [!NOTE]
> 行のチェックボックスにある `getCanSelectSubRows()` と `getIsAllSubRowsSelected()` の条件が意味を持つのは、サブ行のあるテーブルだけです。フラットなデータなら `row.getIsSelected()` だけで十分です。子が選択解除されたときに古い親の ID を取り除く `deselectParents` オプションも含めた完全なパターンは、展開のサンプルを参照してください。

#### 行選択の API を UI につなぐ {#connect-row-selection-apis-to-ui}

もっと単純な行選択の UI にしたい場合は、行そのものにクリックイベントを結び付けるだけでもかまいません。この使い方でも `row.getToggleSelectedHandler()` API が役立ちます。

```tsx
<tbody>
  {table.getRowModel().rows.map((row) => {
    return (
      <tr
        key={row.id}
        className={row.getIsSelected() ? 'selected' : null}
        onClick={row.getToggleSelectedHandler()}
      >
        {row.getVisibleCells().map((cell) => {
          return <td key={cell.id}>{/* */}</td>
        })}
      </tr>
    )
  })}
</tbody>
```
