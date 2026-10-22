---
title: セル選択（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React のサンプルを参照してください。

- [セル選択](https://tanstack.com/table/latest/docs/framework/react/examples/cell-selection)

### セル選択のセットアップ {#cell-selection-setup}

セル選択の機能を使うためのテーブルの設定方法は次のとおりです。セル選択の機能を追加すると、関連する API が使えるようになります。

```tsx
import {
  useTable,
  tableFeatures,
  cellSelectionFeature,
} from '@tanstack/react-table'

const features = tableFeatures({ cellSelectionFeature })

const table = useTable({
  features,
  columns,
  data,
})
```

## セル選択（React）ガイド {#cell-selection-react-guide}

> [!NOTE]
> オプションの[セル結合](./cell-spanning)機能を登録している場合、選択範囲の長方形は、触れている結合セルを丸ごと囲むように広がります。そのため、結合セルは常に全体が選択されるか、全体が選択されないかのどちらかになります。

セル選択の機能は、スプレッドシートのような長方形の選択範囲を管理します。ユーザーはセルをクリックしたり、セルのまとまりをドラッグしたりして選択できます。Shift キーを押しながらクリックすると範囲を広げられ、Ctrl/Cmd キーを押しながらドラッグすると、開始したセルが選択済みかどうかに応じて長方形を追加または除外できます。よくあるユースケースをいくつか見ていきましょう。

### セル選択の状態を読み取る {#access-cell-selection-state}

セル選択の状態は、テーブルインスタンスがあらかじめ管理しています。選択範囲や、そこから派生した値は、いくつかの API で読み取れます。

- `table.state.cellSelection` - セル選択の状態をリアクティブに返します（`useTable` のセレクターで選択されたもの）
- `getSelectedCellCount()` - 選択されているセルの数を返します
- `getSelectedCellIds()` - 選択されているすべてのセルの ID を返します
- `getCellSelectionRowIds()` / `getCellSelectionColumnIds()` - 選択範囲にかかっている行と列を返します
- `getSelectedCellRangesData()` - 最終的に選択されている各領域の値を、行優先のグリッドとして返します

```ts
console.log(table.state.cellSelection) //get the cell selection state
console.log(table.getSelectedCellCount()) //3
console.log(table.getSelectedCellIds()) //['0_firstName', '0_lastName', '1_firstName']
console.log(table.getSelectedCellRangesData()) //[[['Tanner', 'Linsley'], ['Kevin', 'Vandy']]]
```

イベントハンドラーなど、レンダー以外のコードでは、`table.atoms.cellSelection.get()` で現在のスナップショットを読むこともできます。この読み取りではコンポーネントが以降の変更を購読しないため、レンダーの中では `table.state.cellSelection`（または `table.Subscribe`）を使ってください。

範囲を個々のセルに展開する API（`getSelectedCellIds`、`getSelectedCellRangesData`）はメモ化されており、呼ばれたときにだけ計算します。実際に呼ばない限りコストはかからないので、セルをハイライトするだけのテーブルが、大きな選択範囲を列挙するためのコストを払うことはありません。

### セル選択の状態の形 {#cell-selection-state-shape}

`CellSelectionState` は、範囲に対する操作を順番に並べた配列です。各範囲は、それを決める2つの角として保存されます。

```ts
type CellSelectionRange = {
  anchorRowId: string
  anchorColumnId: string
  focusRowId: string
  focusColumnId: string
  operation?: 'include' | 'exclude'
}

type CellSelectionState = Array<CellSelectionRange>
```

`anchor` の角は選択を始めた位置で、動きません。`focus` の角は、ドラッグ中や Shift で範囲を広げるときに動く側の角です。最小値・最大値で正規化した長方形ではなく両方の角を保存しているからこそ、Shift での範囲拡張や「アクティブセルだけの選択に戻す」操作が実現できます。

範囲は順番に適用されます。`operation` を省略した範囲は、後方互換性のために「含める」として扱われます。`exclude` の範囲は、それまでに作られた選択範囲からその長方形を差し引きます。このようにコンパクトな操作の記録として持つことで、「これらのセル以外をすべて選択する」といった操作でも、選択したセル1つにつき1エントリのマップを作らずに済みます。

### セル選択の状態を管理する {#manage-cell-selection-state}

アプリケーションの他の場所から選択範囲にアクセスしたい場合は、この状態を自分で持つこともできます。v9 で推奨されるのは、外部のアトムをテーブルの `atoms` オプションに渡す方法です。

```tsx
import { useCreateAtom } from '@tanstack/react-store'
import {
  useTable,
  tableFeatures,
  cellSelectionFeature,
  type CellSelectionState,
} from '@tanstack/react-table'

const features = tableFeatures({ cellSelectionFeature })

const cellSelectionAtom = useCreateAtom<CellSelectionState>([])

const table = useTable({
  features,
  columns,
  data,
  atoms: { cellSelection: cellSelectionAtom },
})
```

従来の、制御された状態のパターンも使えます。

```tsx
const [cellSelection, setCellSelection] = useState<CellSelectionState>([])

const table = useTable({
  features,
  columns,
  data,
  state: { cellSelection },
  onCellSelectionChange: setCellSelection,
})
```

> [!NOTE]
> ドラッグでは、ポインターがセルの境界を1つ越えるたびに変更が1回発生します。そのため、ドラッグ中は `onCellSelectionChange` が何度も呼ばれます。選択範囲をサーバーや URL と同期する場合は、デバウンスするか、`mouseup` のタイミングで確定させてください。

### 意味のある行 ID を使う {#useful-row-ids}

セル選択は行 ID と列 ID をキーにしています。そのため、行選択と同じ理由で、意味のある行 ID を使うことが重要です。`getRowId` テーブルオプションを使って、データの中の安定した値を選択のキーにしてください。

```ts
const table = useTable({
  features,
  //...
  getRowId: (row) => row.uuid, // use the row's uuid from your database as the row id
})
```

### 条件付きでセル選択を有効にする {#enable-cell-selection-conditionally}

セル選択は、デフォルトですべてのセルで有効です。`enableCellSelection` テーブルオプションを使うと、完全に無効にできます。関数を渡せば、セルごとに制御できます。

```ts
const table = useTable({
  //...
  enableCellSelection: (cell) => cell.row.original.age > 18, //only adults' cells are selectable
})
```

列定義の側で選択の対象から外すこともできます。チェックボックスの列や操作ボタンの列では、これがよく使われます。列で `false` を指定すると、テーブルオプションより優先されます。

```ts
columnHelper.accessor('actions', {
  enableCellSelection: false, //this column can never be selected
})
```

選択できないセルは、長方形がそのセルをまたいで描かれた場合でも飛ばされます。また、`moveCellSelection` はそのセルの列に止まらず、飛び越えて移動します。UI に選択用のハンドラーを付けるかどうかは、`cell.getCanSelect()` で判断してください。

### マウス操作 {#mouse-interactions}

マウス操作はすべて、2つのセルハンドラーで動きます。

- `cell.getSelectionStartHandler()` - `onMouseDown` に割り当てる
- `cell.getSelectionExtendHandler()` - `onMouseEnter` に割り当てる

```tsx
<td
  onMouseDown={cell.getSelectionStartHandler()}
  onMouseEnter={cell.getSelectionExtendHandler()}
>
  <table.FlexRender cell={cell} />
</td>
```

`mouseup` を自分で扱う必要はありません。開始ハンドラーがドキュメント全体に `mouseup` リスナーを付け、ドラッグが終わると外します。そのため、テーブルの外でポインターを離しても、ドラッグは正しく終了します。テーブルを別のドキュメント（iframe やポップアウトしたウィンドウなど）にレンダーしている場合は、そのドキュメントを `cell.getSelectionStartHandler(myDocument)` のように渡してください。

#### ドラッグでの選択 {#drag-selection}

セルを押し下げると、そのセル1つだけの新しい範囲が始まります。その後ポインターが入ったセルに合わせて、その範囲のフォーカスの角が動きます。ドラッグではなく明示的なクリックで選ばせたい場合は、`enableCellSelectionDrag: false` を設定してください。

#### Shift での範囲選択 {#shift-range-selection}

Shift キーを押しながらクリックすると、アクティブな範囲のアンカーの角は固定したまま、フォーカスの角がクリックしたセルに移ります。そのため、アクティブセルは選択を始めた位置にとどまり、スプレッドシートと同じ動きになります。

ハンドラーは、イベントに `event.shiftKey` か `event.nativeEvent.shiftKey` のどちらかがあれば、Shift が押されていると判断します。範囲選択の動作を無効にしたり、判定方法を差し替えたりできます。

```ts
const table = useTable({
  // ...
  enableCellRangeSelection: false,

  // For example, use the platform modifier instead of Shift:
  // isCellRangeSelectionEvent: event =>
  //   Boolean((event as React.MouseEvent).metaKey),
})
```

#### 複数の範囲 {#multiple-ranges}

選択されていないセルを Ctrl キーまたは Cmd キーを押しながらクリックすると、含める長方形が新しく追加されます。同じ修飾キーを押したまま選択済みのセルから操作を始めると、代わりに除外の範囲が追加されます。クリックならそのセルが選択から外れ、ドラッグなら長方形全体が差し引かれます。ドラッグが「含める」か「除外する」かはドラッグの開始時に決まります。除外のドラッグを縮めると、長方形から外れたセルは元の状態に戻ります。両方の動作を無効にするには `enableMultiCellRangeSelection: false` を設定します。修飾キーを変えるには `isMultiCellRangeSelectionEvent` を上書きします。

#### プログラムからの範囲操作 {#programmatic-range-operations}

`table.selectCellRange(range)` は、現在の選択範囲を置き換えます。`{ mode: 'include' }` を渡すと含める範囲を、`{ mode: 'exclude' }` を渡すと除外する範囲を末尾に追加します。以前からある `{ additive: true }` オプションは、include モードの非推奨の別名として残っています。両方を指定した場合は `mode` が優先されます。`table.getCellSelectionBounds()` は、操作の記録を解決し、常に同じ結果になる、互いに重ならない「含める」長方形の集まりにします。

### セル選択の UI をレンダーする {#render-cell-selection-ui}

選択されたセルをどう描画するかを、TanStack Table が決めることはありません。必要な情報は、次のセルの API ですべて得られます。

- `cell.getIsSelected()` - このセルがいずれかの範囲に含まれているかどうか
- `cell.getIsFocused()` - このセルがアクティブセルかどうか（除外されたアンカーは、選択されていなくてもフォーカスされることがあります）
- `cell.getSelectionEdges()` - どの辺が選択範囲の境界に接しているか
- `cell.getTabIndex()` - ロービング tabindex のための値。フォーカスされたセルでは `0`、それ以外では `-1`

`getSelectionEdges()` は `{ top, right, bottom, left }` を返します。各辺は、その方向の隣のセルが選択されていないときに `true` になります。これを使えば、各セルが隣のセルを調べなくても、選択範囲のまわりに1本の連続した枠線を描けます。離れた複数の長方形を合わせた範囲でも同じです。

```tsx
function getCellClassName(cell) {
  // most cells are unselected, so bail before asking for edges
  if (!cell.getIsSelected()) {
    return cell.getIsFocused() ? 'cell cell-focused' : 'cell'
  }

  const edges = cell.getSelectionEdges()

  return [
    'cell',
    'cell-selected',
    cell.getIsFocused() && 'cell-focused',
    edges.top && 'cell-edge-top',
    edges.right && 'cell-edge-right',
    edges.bottom && 'cell-edge-bottom',
    edges.left && 'cell-edge-left',
  ]
    .filter(Boolean)
    .join(' ')
}
```

> [!TIP]
> 枠線は `border` ではなく `box-shadow: inset ...` で描いてください。`border-collapse` のテーブルで border を太くすると、隣のセルと共有している罫線が太くなり、セルが選択されるたびに行の高さが変わってしまいます。box-shadow はレイアウトに影響しません。

### キーボード操作 {#keyboard-navigation}

セル選択の機能自体には、キーボード操作の処理は含まれていません。代わりに、命令的に呼び出せる API を公開しているので、[TanStack Hotkeys](https://tanstack.com/hotkeys) のような専用のライブラリから操作できます。

- `table.moveCellSelection(direction)` - 1つ隣のセルだけを選択した状態にする
- `table.extendCellSelection(direction)` - アンカーの角は固定したまま、アクティブな範囲のフォーカスの角を動かす
- `table.setFocusedCell(rowId, columnId)` - 指定した1つのセルだけを選択した状態にする
- `table.selectAllCells()` - 選択できるすべてのセルを選択する
- `table.resetCellSelection(true)` - 選択を解除する

`direction` は `'up'`、`'down'`、`'left'`、`'right'` のいずれかです。

```tsx
import { useHotkeys } from '@tanstack/react-hotkeys'

const gridRef = useRef<HTMLDivElement>(null)

useHotkeys(
  [
    { hotkey: 'ArrowUp', callback: () => table.moveCellSelection('up') },
    { hotkey: 'ArrowDown', callback: () => table.moveCellSelection('down') },
    { hotkey: 'ArrowLeft', callback: () => table.moveCellSelection('left') },
    { hotkey: 'ArrowRight', callback: () => table.moveCellSelection('right') },
    {
      hotkey: 'Shift+ArrowUp',
      callback: () => table.extendCellSelection('up'),
    },
    { hotkey: 'Mod+A', callback: () => table.selectAllCells() },
    { hotkey: 'Escape', callback: () => table.resetCellSelection(true) },
  ],
  { target: gridRef },
)
```

ホットキーの対象はドキュメント全体ではなく、グリッドの要素に限定してください。そうしないと、矢印キーや Escape キーが、ページ内の他の入力欄の操作まで横取りしてしまいます。

### 選択範囲をコピーする {#copying-a-selection}

`getSelectedCellRangesData()` は、`[regionIndex][rowIndex][columnIndex]` の順でインデックスを付けた生の値を返します。領域（region）とは、すべての「含める」「除外する」操作を適用したあとに残る、互いに重ならない長方形の1つ1つです。そのため、保存されている状態と1対1に対応するとは限りません。これをクリップボード用のテキストに変換する処理は、アプリケーションに任されています。区切り文字、`null` の表し方、引用符の付け方は、あなたにしか決められないからです。

```ts
function escapeTsvValue(value: unknown) {
  const text = value == null ? '' : String(value)
  const safeText =
    typeof value === 'string' && /^[\t\r ]*[=+@-]/.test(value)
      ? `'${text}`
      : text
  // spreadsheets expect a quoted field once it contains a delimiter, a newline,
  // or a quote, with inner quotes doubled
  return /["\t\n\r]/.test(safeText)
    ? `"${safeText.replace(/"/g, '""')}"`
    : safeText
}

function toTsv(ranges: Array<Array<Array<unknown>>>) {
  return ranges
    .map((grid) =>
      grid.map((row) => row.map(escapeTsvValue).join('\t')).join('\n'),
    )
    .join('\n\n')
}

navigator.clipboard.writeText(toTsv(table.getSelectedCellRangesData()))
```

### テーブルが変わったときの範囲の扱い {#how-ranges-survive-table-changes}

範囲は位置ではなく行 ID と列 ID を保存しているので、画面上の座標ではなく、角のセルそのものに追従します。

- **ソート、フィルタリング、列の並べ替え**では、角は固定されたまま、その間に何があるかが再計算されます。「行 A から行 B まで」の範囲は、ソートで間に入る行が変わっても、A から B までのままです。
- **列の固定**はレンダーの順序に反映されるので、列を固定しても長方形は見た目のうえで連続したままです。
- 角のある列を**非表示にする**と、その範囲は効力を失います。何も選択されているようには描画されませんが、範囲は状態に残り、列を再び表示すると元に戻ります。
- **ページネーション**では、ページに分ける前の順序に対して範囲が解決されます。そのため、範囲は複数のページにまたがることができ、どのページを見ていても正しくハイライトされます。

並べ替えによって、ユーザーが選んでいない列まで選択範囲が広がることがあります。そのため、列のレイアウトが変わったら選択を解除したいアプリケーションもあるでしょう。これはライブラリの利用者が決めることで、`useEffect` を1つ書けば実現できます。

```tsx
const isFirstLayout = useRef(true)

useEffect(() => {
  if (isFirstLayout.current) {
    isFirstLayout.current = false
    return
  }
  table.resetCellSelection(true)
}, [
  table.state.columnOrder,
  table.state.columnPinning,
  table.state.columnVisibility,
])
```

### セル選択をリセットする {#resetting-cell-selection}

`table.resetCellSelection()` は `initialState.cellSelection` に戻します。`true` を渡すと、初期状態を無視して選択を完全に解除します。

また、`data` が変わるたびに、選択は自動でリセットされます。新しいデータでは、範囲が指している行 ID が無効になるかもしれず、新しいデータがたまたま同じ ID を使っていれば、意図せずセルが選択し直されるかもしれないからです。この動作は `autoResetCellSelection: false` で無効にできます。ただし、`autoResetAll` はこの設定より優先されることに注意してください。

```ts
const table = useTable({
  //...
  autoResetCellSelection: false, //keep ranges across data changes
})
```

### table.Subscribe でパフォーマンスを上げる {#performance-with-tablesubscribe}

セル選択は、大きなテーブルを重く感じさせる原因になりやすい機能です。ドラッグ中は、ポインターがセルの境界を越えるたびに状態が更新されるからです。1,000 行・12 列のテーブルで素朴に実装すると、更新のたびに 12,000 個のセルが再レンダーされます。

セルごとの読み取り自体は軽い処理です。`cell.getIsSelected()` は、セルの行と列のインデックスを求め、選択範囲の境界をメモ化したキャッシュと比べるだけで、整数の比較が数回あるにすぎません。コストが大きいのは、React がテーブル内のすべてのセルを差分照合（reconcile）する部分です。

これには `table.Subscribe` を使います。そして、**どこに置くかが肝心です**。すぐに思いつくのは、`<tbody>` 全体を囲む置き方です。

```tsx
{
  /* every selection change re-renders every row */
}
;<table.Subscribe source={table.atoms.cellSelection}>
  {() => (
    <tbody>
      {table.getRowModel().rows.map((row) => (
        <tr key={row.id}>...</tr>
      ))}
    </tbody>
  )}
</table.Subscribe>
```

これでも動きますが、ドラッグで更新されるたびにテーブルの本体全体が再レンダーされます。代わりに、行ごとに購読を置き、その行の見た目を変えるものだけを返すセレクターを渡しましょう。`Subscribe` は内部で `useSelector` を使っているので、セレクターが返す値が変わらない行は再レンダーされません。

```tsx
<tbody>
  {table.getRowModel().rows.map((row) => (
    <table.Subscribe
      key={row.id}
      source={table.atoms.cellSelection}
      selector={(ranges) =>
        rowSelectionKey(
          ranges,
          table.getCellSelectionBounds(),
          row.getDisplayIndex(),
          row.id,
        )
      }
    >
      {() => (
        <tr>
          {row.getVisibleCells().map((cell) => (
            <td key={cell.id} className={getCellClassName(cell)}>
              <table.FlexRender cell={cell} />
            </td>
          ))}
        </tr>
      )}
    </table.Subscribe>
  ))}
</tbody>
```

セレクターは、行の描画を変えるものをすべて表現する必要があります。具体的には、その行のセルが範囲に含まれるかどうか、すぐ上とすぐ下の行が範囲に含まれるかどうか（これで上辺と下辺の枠線が決まります）、そしてその行がフォーカスされたセルを持っているかどうかです。

```ts
function rowSelectionKey(ranges, bounds, rowIndex, rowId) {
  const active = ranges[ranges.length - 1]
  let key =
    ranges.length > 0 && active.anchorRowId === rowId
      ? `f${active.anchorColumnId}`
      : ''

  for (const bound of bounds) {
    const self = rowIndex >= bound.minRowIndex && rowIndex <= bound.maxRowIndex
    const above =
      rowIndex - 1 >= bound.minRowIndex && rowIndex - 1 <= bound.maxRowIndex
    const below =
      rowIndex + 1 >= bound.minRowIndex && rowIndex + 1 <= bound.maxRowIndex

    if (self || above || below) {
      key += `|${self ? 1 : 0}${above ? 1 : 0}${below ? 1 : 0}:${bound.minColumnIndex}-${bound.maxColumnIndex}`
    }
  }

  return key
}
```

`table.getCellSelectionBounds()` はメモ化されているので、何行から呼ばれても、選択が変わるたびに1回しか計算されません。広がっていく範囲の途中にある行はキーが変わらないため、ドラッグを下に伸ばしても、再レンダーされるのは動いている境界にある2行だけで、全行ではありません。1,000 行のテーブルでは、これによってドラッグの更新1回あたりの時間が約 35 ミリ秒から約 10 ミリ秒に短縮されました。

このパターンについて、知っておくとよいことが2つあります。

**列のレイアウトはセレクターに含めないでください。** 列の固定、並べ替え、非表示によって行の描画内容は変わります。しかし、これらの状態はふつう `useTable` のセレクターにすでに含まれているので、親が再レンダーされ、いずれにせよ行は作り直されます。選択用のセレクターに加えても重複するだけです。

**`React.memo` よりこちらを使ってください。** メモ化した行コンポーネントは、`cell.getIsSelected()` のようなゲッターを通してセルのクラスを読みます。こうしたゲッターは、どの状態に依存しているかを React Compiler から隠してしまいます。目に見える入力が安定した `row` オブジェクトだけだと、コンパイラーは行のセルをキャッシュしてしまい、`React.memo` 自体は正しく再レンダーしていても、ハイライトがまったく動かなくなります。`table.Subscribe` なら、`useSelector` がコンパイラーの認識できる依存関係なので、この問題はそもそも起きません。詳しくは[ネストしたコンポーネントで Subscribe を使う](./react-compiler#use-subscribe-in-nested-components)を参照してください。

それでも足りないほど大きなテーブルなら、[仮想化](./virtualization)を使って、見えている行だけが DOM に存在するようにしてください。
