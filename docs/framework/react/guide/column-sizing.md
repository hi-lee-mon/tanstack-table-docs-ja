---
title: 列幅（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React のサンプルを参照してください。

- [列幅](https://tanstack.com/table/latest/docs/framework/react/examples/column-sizing)

### 列幅のセットアップ {#column-sizing-setup}

列幅の機能を使うためのテーブルの設定方法は次のとおりです。列幅の機能を追加すると、関連する API が使えるようになります。

```tsx
import {
  useTable,
  tableFeatures,
  columnSizingFeature,
} from '@tanstack/react-table'

const features = tableFeatures({ columnSizingFeature })

const table = useTable({
  features,
  columns,
  data,
})
```

## 列幅（React）ガイド {#column-sizing-react-guide}

列幅の機能を使うと、必要に応じて各列の幅を、最小幅・最大幅も含めて設定できます。

ユーザーが列のヘッダーをドラッグして列幅を動的に変えられるようにしたい場合は、[列幅の変更ガイド](./column-resizing)を参照してください。

### 列の幅 {#column-widths}

列には、デフォルトで次の寸法のオプションが設定されています。

```tsx
export const defaultColumnSizing = {
  size: 150,
  minSize: 20,
  maxSize: Number.MAX_SAFE_INTEGER,
}
```

これらのデフォルト値は、`tableOptions.defaultColumn` と個々の列定義の両方で上書きでき、この順に適用されます。

```tsx
const features = tableFeatures({ columnSizingFeature })

const columns = [
  {
    accessorKey: 'col1',
    size: 270, //set column size for this column
  },
  //...
]

const table = useTable({
  features,
  defaultColumn: {
    size: 200, // starting column size
    minSize: 50, // enforced during column resizing
    maxSize: 500, // enforced during column resizing
  },
  //...
})
```

列の「サイズ」はテーブルの状態に数値として保存されます。ふつうはピクセル単位の値として解釈しますが、これらの列幅の値を CSS のスタイルにどう結び付けるかは自由です。

ヘッドレスなユーティリティなので、列幅に関するテーブルのロジックは、実のところ状態の集まりにすぎません。それを自分のレイアウトにどう当てはめるかは自由です（上のサンプルでは、このロジックを2通りのスタイルで実装しています）。これらの幅の値は、さまざまな方法で適用できます。

- セマンティックな `table` 要素、または CSS の table 表示モードで表示される任意の要素
- `div/span` 要素、または table 以外の CSS 表示モードで表示される任意の要素
  - 幅を厳密に指定したブロックレベル要素
  - 幅を厳密に指定した絶対配置の要素
  - 幅をゆるく指定した Flexbox で配置する要素
  - 幅をゆるく指定した Grid で配置する要素
- そのほか、セルの幅をテーブルの構造に反映できるレイアウトの仕組みなら、実質的に何でもかまいません。

どの方法にもそれぞれ長所と短所、制約があり、ふつうはそれを UI ライブラリやコンポーネントライブラリ、デザインシステムが自分の考えで決めています。幸い、あなたが決める必要はありません 😉。

### 列幅の API {#column-sizing-apis}

レンダーに使う、計算済みのサイズやオフセットを読み取るには、列とヘッダーの API を使います。これらの値は、`columnSizing` の状態と、列定義のデフォルト値から求められます。

```tsx
column.getSize()
header.getSize()

column.getStart() // start offset in the current column flow
column.getStart('start')
column.getStart('center')
column.getStart('end')

column.getAfter() // end offset in the current column flow
column.getAfter('start')
column.getAfter('center')
column.getAfter('end')

column.resetSize()
```

テーブルインスタンスには、合計サイズを求めるヘルパーもあります。スクロールコンテナーを作るとき、固定した列ごとにテーブルを分割するとき、列幅を CSS 変数にするときに便利です。

```tsx
table.getTotalSize()
table.getStartTotalSize()
table.getCenterTotalSize()
table.getEndTotalSize()
```

列幅の状態を直接更新する必要がある場合は、`table.setColumnSizing` を使います。`table.resetColumnSizing` を使うと `initialState.columnSizing` にリセットされます。`true` を渡すと、機能のデフォルト値にリセットされます。

```tsx
table.setColumnSizing({
  firstName: 180,
  age: 80,
})

table.resetColumnSizing()
table.resetColumnSizing(true)
```

### 列幅の状態を管理する {#managing-column-sizing-state}

`columnSizing` の状態を自分で持ちたい場合（たとえば、ユーザーが設定した列幅を保存しておきたい場合）、v9 で推奨されるのは、外部のアトムをテーブルの `atoms` オプションに渡す方法です。外部のアトムを使うと、アプリのどこからでもきめ細かく購読できます。また、テーブルを持つコンポーネントを再レンダーさせずに、他のコードから列幅の状態を読み書きできます。

```tsx
import { useCreateAtom, useSelector } from '@tanstack/react-store'
import type { ColumnSizingState } from '@tanstack/react-table'

const features = tableFeatures({ columnSizingFeature })

const columnSizingAtom = useCreateAtom<ColumnSizingState>({})

const columnSizing = useSelector(columnSizingAtom) // subscribe wherever it is needed

const table = useTable({
  features,
  columns,
  data,
  atoms: {
    columnSizing: columnSizingAtom,
  },
})
```

v8 と同じ、`state.columnSizing` と `onColumnSizingChange` を組み合わせるパターンも引き続き使えます。単純な連携や v8 のコードを移行するときには便利ですが、外部のアトムほどきめ細かくはありません。詳しい比較は[テーブルの状態ガイド](./table-state)を参照してください。

```tsx
const features = tableFeatures({ columnSizingFeature })

const [columnSizing, setColumnSizing] = useState<ColumnSizingState>({})

const table = useTable({
  features,
  columns,
  data,
  state: {
    columnSizing,
  },
  onColumnSizingChange: setColumnSizing,
})
```
