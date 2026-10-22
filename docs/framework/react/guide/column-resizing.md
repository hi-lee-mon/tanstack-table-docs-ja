---
title: 列幅の変更（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React のサンプルを参照してください。

- [列幅の変更](https://tanstack.com/table/latest/docs/framework/react/examples/column-resizing)
- [高速な列幅の変更](https://tanstack.com/table/latest/docs/framework/react/examples/column-resizing-performant)

### 列幅の変更のセットアップ {#column-resizing-setup}

列幅の変更の機能を使うためのテーブルのセットアップ方法は次のとおりです。列幅の変更は列幅の機能に依存しているので、`columnResizingFeature` より前に `columnSizingFeature` を追加してください。列幅の変更の機能を追加すると、関連する API が使えるようになります。

```tsx
import {
  useTable,
  tableFeatures,
  columnSizingFeature,
  columnResizingFeature,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnSizingFeature,
  columnResizingFeature,
})

const table = useTable({
  features,
  columns,
  data,
})
```

## 列幅の変更（React）ガイド {#column-resizing-react-guide}

TanStack Table には、テーブルの UI に列幅の変更を実装するための組み込みの状態と API が用意されています。UX やパフォーマンスに合わせて選べるオプションもさまざまです。

列幅の変更は、列幅の機能の上に成り立っています。初期の幅や最小・最大の幅を決めたいだけなら、[列幅のガイド](./column-sizing)を参照してください。

### 列幅の変更を有効にする {#enable-column-resizing}

列幅の変更を使うには、`columnSizingFeature` と、その後ろに `columnResizingFeature` を features に追加します。`column.getCanResize()` API はデフォルトですべての列で `true` を返します。`enableColumnResizing` テーブルオプションですべての列の列幅の変更を無効にすることも、`enableResizing` 列オプションで列ごとに無効にすることもできます。

```tsx
import {
  columnResizingFeature,
  columnSizingFeature,
  tableFeatures,
  useTable,
} from '@tanstack/react-table'

const features = tableFeatures({
  columnSizingFeature,
  columnResizingFeature,
})

const columns = [
  {
    accessorKey: 'id',
    enableResizing: false, // disable resizing for just this column
    size: 200, // starting column size
  },
  //...
]

const table = useTable({
  features,
  columns,
  data,
})
```

### 列幅の変更モード {#column-resize-mode}

デフォルトでは、列幅の変更モードは `"onEnd"` に設定されています。この場合、ユーザーが列幅の変更（ドラッグ）を終えるまで、`column.getSize()` API は新しい列幅を返しません。ユーザーが列幅を変更しているあいだは、たいてい小さな目印を UI に表示します。

React 版の TanStack Table アダプターでは、テーブルやページの複雑さによっては、列幅の変更を 60 fps で描画するのが難しい場合があります。そのため、ユーザーが列幅を変更するときのカクつきや遅れを避けるには、`"onEnd"` モードがデフォルトとして適しています。TanStack React Table で列幅の変更を 60 fps で描画できないわけではありませんが、そのためには追加のメモ化などのパフォーマンス最適化が必要になることがあります。

> 列幅の変更のパフォーマンスに関する高度なヒントは、[後述](#advanced-column-resizing-performance)します。

列幅の変更をすぐに描画に反映させるために、列幅の変更モードを `"onChange"` に変えたい場合は、`columnResizeMode` テーブルオプションを使います。

```tsx
const table = useTable({
  //...
  columnResizeMode: 'onChange', // change column resize mode to "onChange"
})
```

### 列幅の変更の方向 {#column-resize-direction}

デフォルトでは、TanStack Table はテーブルのマークアップが左から右に並ぶことを前提にしています。右から左に並ぶレイアウトでは、列幅の変更の方向を `"rtl"` に変える必要がある場合があります。

```tsx
const table = useTable({
  //...
  columnResizeDirection: 'rtl', // change column resize direction to "rtl" for certain locales
})
```

### 列幅の変更の API を UI につなぐ {#connect-column-resizing-apis-to-ui}

列幅の変更のドラッグ操作を UI につなぐのに役立つ API がいくつかあります。

#### 列幅の API {#column-size-apis}

列幅をヘッダーのセル、データのセル、フッターのセルに適用するには、次の API を使えます。

```ts
header.getSize()
column.getSize()
cell.column.getSize()
```

これらの幅をマークアップにどう適用するかは自由ですが、CSS 変数かインラインスタイルで列幅を適用するのが一般的です。

```tsx
<th
  key={header.id}
  colSpan={header.colSpan}
  style={{ width: `${header.getSize()}px` }}
>
```

ただし、[列幅の変更のパフォーマンスに関する高度な節](#advanced-column-resizing-performance)で説明するように、列幅をマークアップに適用するには CSS 変数を使うことも検討するとよいでしょう。

#### 列幅を変更する API {#column-resize-apis}

TanStack Table には、ドラッグ操作を簡単に実装するための、あらかじめ用意されたイベントハンドラーがあります。このイベントハンドラーは、内部の別の API を呼び出して列幅の状態を更新し、テーブルを再レンダーするための便利関数にすぎません。マウスとタッチの両方のイベントで、列幅の変更のドラッグ操作には `header.getResizeHandler()` をつなぎます。

```tsx
<ColumnResizeHandle
  onMouseDown={header.getResizeHandler()} // for desktop
  onTouchStart={header.getResizeHandler()} // for mobile
/>
```

#### 列幅の変更の状態を使った目印 {#column-resize-indicator-with-column-resizing-state}

TanStack Table は `columnResizing` という状態オブジェクトを管理しています。これを使って、列幅の変更中を示す目印の UI を描画できます。

```tsx
<ColumnResizeIndicator
  style={{
    transform: header.column.getIsResizing()
      ? `translateX(${table.state.columnResizing.deltaOffset ?? 0}px)`
      : '',
  }}
/>
```

`columnResizing` の状態には、ドラッグ中だけの一時的な情報が入ります。

```tsx
type columnResizingState = {
  columnSizingStart: Array<[string, number]>
  deltaOffset: null | number
  deltaPercentage: null | number
  isResizingColumn: false | string
  startOffset: null | number
  startSize: null | number
}
```

このドラッグ中の一時的な状態を自分で管理する必要はほとんどありません。管理する場合、v9 で推奨される方法は、外部のアトムをテーブルの `atoms` オプションに渡すことです。外部のアトムなら、アプリのどこでも細かい粒度で購読でき、テーブルを持つコンポーネントを再レンダーさせずに、他のコードから列幅の変更の状態を観察できます。

```tsx
import { useCreateAtom, useSelector } from '@tanstack/react-store'
import type { columnResizingState } from '@tanstack/react-table'

const columnResizingAtom = useCreateAtom<columnResizingState>({
  columnSizingStart: [],
  deltaOffset: null,
  deltaPercentage: null,
  isResizingColumn: false,
  startOffset: null,
  startSize: null,
})

const columnResizing = useSelector(columnResizingAtom) // subscribe wherever it is needed

const table = useTable({
  features,
  columns,
  data,
  atoms: {
    columnResizing: columnResizingAtom,
  },
})
```

v8 スタイルの `state.columnResizing` と `onColumnResizingChange` を組み合わせるパターンも、引き続き使えます。単純な連携や v8 のコードを移行するときには便利ですが、外部のアトムに比べると購読の粒度は粗くなります。詳しい比較は[テーブルの状態のガイド](./table-state)を参照してください。

```tsx
const [columnResizing, setColumnResizing] = useState<columnResizingState>({
  columnSizingStart: [],
  deltaOffset: null,
  deltaPercentage: null,
  isResizingColumn: false,
  startOffset: null,
  startSize: null,
})

const table = useTable({
  features,
  columns,
  data,
  state: {
    columnResizing,
  },
  onColumnResizingChange: setColumnResizing,
})
```

### 列幅の変更の API {#column-resizing-apis}

マウスやタッチのイベントを列幅の変更の処理につなぐには、`header.getResizeHandler()` を使います。列幅を変更するハンドルを描画するかどうかの判断には `column.getCanResize()` を、列幅の変更中の UI を描画するには `column.getIsResizing()` を使います。

```tsx
header.getResizeHandler()
column.getCanResize()
column.getIsResizing()
```

テーブルインスタンスは、列幅の変更中の一時的な状態を扱う API を `table.setColumnResizing` として公開しています。

```tsx
table.setColumnResizing((old) => ({
  ...old,
  deltaOffset: 12,
}))

table.resetHeaderSizeInfo()
table.resetHeaderSizeInfo(true)
```

### 列幅の変更のパフォーマンスに関する高度な話題 {#advanced-column-resizing-performance}

React で大きなテーブルや複雑なテーブルを作る場合、`"onChange"` モードで列幅を変更すると、ドラッグのフレームごとにテーブル全体が再レンダーされ、パフォーマンスが落ちることがあります。[高速な列幅の変更のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/column-resizing-performant)では、ドラッグを React のレンダーの経路から完全に切り離す方法を示しています。この方法なら、描画コストの高いセルを持つテーブルでも滑らかに動きます。

考え方は、ドラッグ中は列幅を React の状態として扱わないことです。

1. **テーブルのコンポーネントには、列幅の変更の状態を一切購読させません。** 定数を返すセレクター（例では `() => ({})`）を渡し、状態が変わってもテーブルを持つコンポーネントが再レンダーされないようにします。
2. **列幅は CSS 変数として命令的に書き込みます。** `useLayoutEffect` の中で `table.atoms.columnSizing` を購読し、`<table>` 要素に `--header-<id>-size` と `--col-<id>-size` の変数を直接設定します。セルは `width: calc(var(--col-firstName-size) * 1px)` のようにこれらの変数を参照するので、ブラウザーはフレームごとに React の処理をまったく挟まずに新しい幅を適用します。（コアの列幅変更ハンドラーは、すでにポインターイベントをアニメーションフレームごとに 1 回の更新にまとめています。）
3. **反応する必要のある少数の部分だけを、`table.Subscribe` の小さな島として切り出します。** 操作中のリサイザーのハイライトや、状態をリアルタイムに表示する部分は、それぞれ必要なスライスだけを購読します。そのため、ドラッグしても再レンダーされるのはそれらの小さな島だけで、テーブルの本体は再レンダーされません。

この方法は、以前の「列幅の変更中はテーブルの本体をメモ化する」という方法に代わるものです。本体は列幅の変更の状態を購読しなくなったので、メモ化する必要はありません。本体が再レンダーされるのは、データが変わったときだけです。
