---
title: 行の固定（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React のサンプルを参照してください。

- [行の固定](https://tanstack.com/table/latest/docs/framework/react/examples/row-pinning)

### 行の固定のセットアップ {#row-pinning-setup}

行の固定機能を使うためのテーブルのセットアップ方法を示します。行の固定機能を追加すると、関連する API が使えるようになります。

```tsx
import {
  useTable,
  tableFeatures,
  rowPinningFeature,
} from '@tanstack/react-table'

const features = tableFeatures({ rowPinningFeature })

const table = useTable({
  features,
  columns,
  data,
})
```

## 行の固定（React）ガイド {#row-pinning-react-guide}

行の固定を使うと、選んだ行を上端または下端の行領域にとどめ、残りの行を中央の領域に描画できます。

行の並び順を変える可能性のあるテーブルの機能は2つあり、次の順序で適用されます。

1. **行の固定** - 固定している場合、行は上端に固定された行、中央の（固定されていない）行、下端に固定された行に分けられます。
2. [ソート](./sorting)

### 行の固定を有効にする {#enable-row-pinning}

行の固定を使うには、`rowPinningFeature` を features に追加します。行の固定には行モデルのファクトリーが要らないので、テーブルで行モデルを使う他の機能を使っていない限り、`tableFeatures` に追加のスロットは必要ありません。

```tsx
import {
  rowPinningFeature,
  tableFeatures,
  useTable,
} from '@tanstack/react-table'

const features = tableFeatures({ rowPinningFeature })

const table = useTable({
  features,
  columns,
  data,
})
```

### 行の固定の状態 {#row-pinning-state}

`rowPinning` の状態は、行 ID を `top` と `bottom` の配列に保持します。

```tsx
type RowPinningState = {
  top: string[]
  bottom: string[]
}
```

`initialState.rowPinning` を使うと、最初から行を固定しておけます。

```tsx
const table = useTable({
  features,
  columns,
  data,
  initialState: {
    rowPinning: {
      top: ['0'],
      bottom: ['3'],
    },
  },
})
```

行の固定をテーブルインスタンスの外で管理する必要がある場合、v9 で推奨される方法は、テーブルの `atoms` オプションに外部のアトムを渡すことです。外部のアトムを使えば、アプリのどこからでもきめ細かく購読できます。また、テーブルを持つコンポーネントを再レンダーさせずに、他のコードから固定の状態を読み書きできます。

```tsx
import { useCreateAtom, useSelector } from '@tanstack/react-store'
import type { RowPinningState } from '@tanstack/react-table'

const rowPinningAtom = useCreateAtom<RowPinningState>({
  top: [],
  bottom: [],
})

const rowPinning = useSelector(rowPinningAtom) // subscribe wherever it is needed

const table = useTable({
  features,
  columns,
  data,
  atoms: {
    rowPinning: rowPinningAtom,
  },
})
```

v8 と同じ `state.rowPinning` と `onRowPinningChange` を組み合わせるパターンも、引き続き使えます。単純な組み込みや v8 のコードを移行するときには便利ですが、外部のアトムほどきめ細かくはありません。詳しい比較は[テーブルの状態ガイド](./table-state)を参照してください。

```tsx
const [rowPinning, setRowPinning] = useState<RowPinningState>({
  top: [],
  bottom: [],
})

const table = useTable({
  features,
  columns,
  data,
  state: {
    rowPinning,
  },
  onRowPinningChange: setRowPinning,
})
```

状態を直接更新するには `table.setRowPinning` を、`initialState.rowPinning` に戻すには `table.resetRowPinning` を使います。`resetRowPinning` に `true` を渡すと、固定された行の配列が両方とも空になります。

```tsx
table.setRowPinning({
  top: ['0', '2'],
  bottom: ['8'],
})

table.resetRowPinning()
table.resetRowPinning(true)
```

### 行の API で行を固定する {#pin-rows-with-row-apis}

各行には、固定できるかどうかの確認、固定位置の読み取り、固定位置の変更を行う API があります。

```tsx
row.getCanPin()
row.getIsPinned() // 'top', 'bottom', or false
row.getPinnedIndex()

row.pin('top')
row.pin('bottom')
row.pin(false)
```

これらの API を使って、固定を操作するコントロールを作れます。

```tsx
const columns = [
  {
    id: 'pin',
    header: 'Pin',
    cell: ({ row }) =>
      row.getCanPin() ? (
        <div>
          <button
            onClick={() => row.pin('top')}
            disabled={row.getIsPinned() === 'top'}
          >
            Top
          </button>
          <button onClick={() => row.pin(false)} disabled={!row.getIsPinned()}>
            Center
          </button>
          <button
            onClick={() => row.pin('bottom')}
            disabled={row.getIsPinned() === 'bottom'}
          >
            Bottom
          </button>
        </div>
      ) : null,
  },
  //...
]
```

`row.pin` API は `includeLeafRows` と `includeParentRows` のフラグも受け付けます。グループ化や展開をした行を固定するときに、関連する親の行や末端の行を一緒に動かすかどうかを決めるのに役立ちます。

### 行の固定に関するテーブルの API {#row-pinning-table-apis}

行の固定は、現在の行モデルを3つの行リストに分けます。

```tsx
table.getTopRows()
table.getCenterRows()
table.getBottomRows()
```

固定された行をテーブルの別のセクションに描画する場合は、これらの API を直接使ってください。

```tsx
<tbody>
  {table.getTopRows().map((row) => (
    <PinnedRow key={row.id} row={row} />
  ))}
  {table.getCenterRows().map((row) => (
    <TableRow key={row.id} row={row} />
  ))}
  {table.getBottomRows().map((row) => (
    <PinnedRow key={row.id} row={row} />
  ))}
</tbody>
```

固定された行が1つでもあるかを確認するには `table.getIsSomeRowsPinned()` を使います。位置を渡せば、特定の固定領域について確認できます。

```tsx
table.getIsSomeRowsPinned()
table.getIsSomeRowsPinned('top')
table.getIsSomeRowsPinned('bottom')
```

### 行の固定を無効にする {#disable-row-pinning}

デフォルトでは、すべての行を固定できます。`enableRowPinning` を使うと、テーブル全体で行の固定を無効にしたり、行ごとに判断したりできます。

```tsx
const table = useTable({
  features,
  columns,
  data,
  enableRowPinning: (row) => row.original.status !== 'archived',
})
```

### 固定された行を残す {#keep-pinned-rows}

`keepPinnedRows` はデフォルトで `true` です。そのため、固定された行は、本来ならフィルタリングやページネーションで中央の行から外れる場合でも、固定領域に表示されたままになります。

固定された行を、フィルタリングとページネーションを適用した現在の行モデルに含まれているときだけ描画したい場合は、`keepPinnedRows` を `false` にしてください。

```tsx
const table = useTable({
  features,
  columns,
  data,
  keepPinnedRows: false,
})
```
