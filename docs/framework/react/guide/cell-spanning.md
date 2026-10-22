---
title: セル結合（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React のサンプルを参照してください。

- [セル結合](https://tanstack.com/table/latest/docs/framework/react/examples/cell-spanning)

### セル結合のセットアップ {#cell-spanning-setup}

セル結合の機能を使うためのテーブルのセットアップ方法は次のとおりです。セル結合の機能を追加すると、関連する API が使えるようになります。

```tsx
import {
  useTable,
  tableFeatures,
  cellSpanningFeature,
} from '@tanstack/react-table'

const features = tableFeatures({ cellSpanningFeature })

const table = useTable({
  features,
  columns,
  data,
})
```

## セル結合（React）ガイド {#cell-spanning-react-guide}

セル結合の機能は、隣り合うボディのセルを1つのセルとして描画します。素の HTML のテーブルやスプレッドシートで `rowspan` と `colspan` がセルを結合するのと同じです。行方向の結合はデータから導き出されます。結合を有効にした列で同じ値を持つ隣り合った行が、縦方向に広がる1つのセルにまとまります。列方向の結合は、全幅の集計行などのために行ごとに宣言します。

この機能は状態を持ちません。結合は実際に描画される行から毎回計算し直されます。そのため、ソート・フィルタリング・ページネーション・行の固定は、どの行が隣り合うかを変えるだけで、結合はそれに追従します。保存するものも、リセットするものもありません。

### 列ごとに行方向の結合を有効にする {#enable-row-spanning-per-column}

値に基づく行方向の結合を列で有効にするには、列定義に `spanRows` を指定します。

```tsx
const columns = [
  columnHelper.accessor('region', {
    spanRows: true, // adjacent rows with equal region values merge
  }),
]
```

`spanRows: true` を指定すると、値が同じ隣り合った行が結合されます。比較には `Object.is` を使います。デフォルトの比較では、null や undefined の値は結合されません。空欄が結合されたブロックは描画のバグに見えますし、意味の上で無関係な行をつなげてしまうためです。

結合の範囲（ラン）の区切りを自分で制御したい場合は、判定関数を渡します。ランは先頭の行を基準にします。候補となる各行は、ランの最初の行と比べて判定されます。この仕組みにより、ランは構造上、推移的な関係を保ちます。

```tsx
columnHelper.accessor('createdAt', {
  spanRows: ({ anchorValue, value }) =>
    sameMonth(anchorValue as Date, value as Date),
})
```

### 結合されたセルを描画する {#rendering-spanned-cells}

ほかのセルに覆われたセルは結合数として `0` を返し、描画側はそのセルを飛ばします。これは [`header.rowSpan`](../../../guide/headers#header-row-spanning) と同じ約束事です。

```tsx
{
  row.getVisibleCells().map((cell) => {
    const rowSpan = cell.getRowSpan()
    const colSpan = cell.getColSpan()

    // A span of 0 means the cell is covered by a cell above or to its left.
    // Skip it. Do not render `rowSpan={0}`: in HTML that means "span to the
    // end of the row group", which merges the cell down the entire tbody.
    if (rowSpan === 0 || colSpan === 0) return null

    return (
      <td key={cell.id} rowSpan={rowSpan} colSpan={colSpan}>
        {flexRender(cell.column.columnDef.cell, cell.getContext())}
      </td>
    )
  })
}
```

`cell.getIsCovered()` は同じ判定を手軽に行うためのメソッドです。結合数を別途必要としない場合は、`cell.getIsCovered() ? null : ...` と書くこともできます。

### 列方向の結合と集計行 {#column-spanning-and-summary-rows}

横方向の結合は、結合した内容を表示する列に `spanColumns` を指定して宣言します。結合数は行ごとに決まり、列が実際に描画される順序で数えられます。そのため、非表示の列は数に含まれず、列の並べ替えにも自動で対応します。

```tsx
columnHelper.accessor('label', {
  spanColumns: ({ row }) => (row.original.isSummary ? Infinity : 1),
})
```

使える幅より大きい値は、そのセルが属する固定領域の端までに切り詰められます。つまり `Infinity` は「自分の領域の残りすべて」を意味します。列方向の結合が、先頭側に固定された列・中央の列・末尾側に固定された列の境界をまたぐことはありません。

1つのセルが行と列の両方向に同時に結合される場合、結合されたブロックは長方形になります。基準となるセルは両方向の結合数を返し、長方形内のほかのセルは少なくとも一方の軸で `0` を返します。セルが縦方向のランに加わるのは、列方向の結合数が一致する場合だけです。そのため、全幅の集計行が上にあるデータのランに結合されることはありません。

### 結合とソート・フィルタリング・ページネーション {#spanning-and-sorting-filtering-and-pagination}

結合は最終的な行モデルから導き出され、保存されることはありません。そのため、行モデルが変わるたびに計算し直されます。

- ソートは行の隣り合い方を変えます。結合する列でソートすると同じ値がまとまり、ランが最も大きくなります。無関係な列でソートすると、たいていランはばらばらになります。
- フィルタリングは行を取り除きます。フィルターがランの途中の行を取り除くと、残った前後の行が隣り合って結合されます。
- ページネーションはランを切り取ります。ランがページの境界をまたぐことはありません。値が続いていても、次のページでは新しいセルが始まります。
- 固定された行は別のセクションに描画されるため、ランが固定セクションの境界をまたぐこともありません。

### セル結合を無効にする {#disable-cell-spanning}

```tsx
const table = useTable({
  features,
  columns,
  data,
  enableCellSpanning: false, // document-wide kill switch
})

columnHelper.accessor('status', {
  enableCellSpanning: false, // per-column opt out
})
```

### 結合されたセルを選択する {#selecting-merged-cells}

`cellSelectionFeature` はセル結合と組み合わせて使えます。両方の機能を登録すると、選択範囲の長方形は、接している結合セルをすべて完全に囲むように広がります。そのため、結合セルは常に全体が選択されているか、全体が選択されていないかのどちらかです。これは選択の除外にも当てはまり、結合セルの一部を除外すると結合セル全体の選択が解除されます。矢印キーによる移動では結合セルを1か所として扱い、`getSelectedCellCount()` は結合セルを1つと数え、`getSelectedCellIds()` は描画されるセルだけを返します。一方、`getSelectedCellRangesData()` は従来どおり、行優先の格子状のグリッド全体を返します。覆われたセルにも実際の値があるためです。

選択範囲の拡張は、選択が保存されるときではなく、選択範囲の境界が導き出されるときに行われます。ソート・ページ移動・`enableCellSpanning` の切り替えによって結合されるセルが変わっても、保存された角の位置は変わりません。導き出される選択範囲が、現在の結合に追従します。

### 既知の制限 {#known-limitations}

- 行の仮想化には特別な配慮が必要です。ランの基準となる行がスクロールして描画範囲の外に出ると、覆われていた行には何も描画されません。`table.getCellSpanIndex()` を読み取って基準となる行を見つけ、描画範囲の先頭に、範囲内に収めた結合セルを描画してください。
- グループ化された列では `spanRows` が無視されます。グループ化がすでに繰り返しの値をグループ行にまとめているためです。また、グループ行はどの列でもランに加わりません。
- フッターグループと `<tfoot>` の描画は、セル結合の影響を受けません。
