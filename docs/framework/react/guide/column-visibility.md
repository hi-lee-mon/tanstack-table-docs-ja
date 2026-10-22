---
title: 列の表示切り替え（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React の例を参照してください。

- [列の表示切り替え](https://tanstack.com/table/latest/docs/framework/react/examples/column-visibility)

### 列の表示切り替えの準備 {#column-visibility-setup}

列の表示切り替え機能を使えるようにテーブルを準備する方法は次のとおりです。列の表示切り替え機能を追加すると、関連する API が有効になります。

```tsx
import {
  useTable,
  tableFeatures,
  columnVisibilityFeature,
} from '@tanstack/react-table'

const features = tableFeatures({ columnVisibilityFeature })

const table = useTable({
  features,
  columns,
  data,
})
```

## 列の表示切り替え（React）ガイド {#column-visibility-react-guide}

列の表示切り替え機能を使うと、テーブルの列を動的に隠したり表示したりできます。v9 でこの機能を有効にするには、`features` に `columnVisibilityFeature` を追加します。列の表示状態を動的に管理するための専用の `columnVisibility` 状態と API が用意されています。

### 列の表示状態 {#column-visibility-state}

`columnVisibility` 状態は、列 ID を真偽値に対応付けるマップです。マップに列 ID があり、その値が `false` の列は非表示になります。マップに列 ID がない場合や、値が `true` の場合は、その列は表示されます。

`columnVisibility` 状態を自分で管理する必要がある場合（たとえば、ユーザーの設定を保存しておきたい場合）、v9 で推奨される方法は、外部のアトムをテーブルの `atoms` オプションに渡すことです。外部アトムを使うと、アプリのどこからでもきめ細かく購読できます。また、テーブルを持つコンポーネントを再レンダーせずに、ほかのコードから表示状態を読み書きできます。

```tsx
import { useCreateAtom, useSelector } from '@tanstack/react-store'
import {
  useTable,
  tableFeatures,
  columnVisibilityFeature,
} from '@tanstack/react-table'
import type { ColumnVisibilityState } from '@tanstack/react-table'

const features = tableFeatures({ columnVisibilityFeature })

const columnVisibilityAtom = useCreateAtom<ColumnVisibilityState>({
  columnId1: true,
  columnId2: false, // hide this column by default
  columnId3: true,
})

const columnVisibility = useSelector(columnVisibilityAtom) // subscribe wherever it is needed

const table = useTable({
  features,
  //...
  atoms: {
    columnVisibility: columnVisibilityAtom,
  },
})
```

v8 と同じ `state.columnVisibility` と `onColumnVisibilityChange` を組み合わせる書き方も、引き続き使えます。簡単な連携や v8 のコードを移行するときには便利ですが、外部アトムに比べると購読の粒度は粗くなります。詳しい比較は[テーブルの状態ガイド](./table-state)を参照してください。

```tsx
const features = tableFeatures({ columnVisibilityFeature })

const [columnVisibility, setColumnVisibility] = useState<ColumnVisibilityState>(
  {
    columnId1: true,
    columnId2: false, // hide this column by default
    columnId3: true,
  },
)

const table = useTable({
  features,
  //...
  state: {
    columnVisibility,
    //...
  },
  onColumnVisibilityChange: setColumnVisibility,
})
```

また、列の表示状態をテーブルの外で管理する必要がなければ、`initialState` オプションで列の表示状態の初期値だけを設定することもできます。

> [!NOTE]
> `columnVisibility` を `initialState` と `state` の両方に渡した場合は、`state` による初期化が優先され、`initialState` は無視されます。`columnVisibility` は `initialState` と `state` のどちらか一方にだけ渡してください。

```tsx
const features = tableFeatures({ columnVisibilityFeature })

const table = useTable({
  features,
  //...
  initialState: {
    columnVisibility: {
      columnId1: true,
      columnId2: false, // hide this column by default
      columnId3: true,
    },
    //...
  },
})
```

### 列を隠せないようにする {#disable-hiding-columns}

デフォルトでは、すべての列を隠したり表示したりできます。特定の列を隠せないようにしたい場合は、その列の `enableHiding` 列オプションを `false` に設定します。

```tsx
const columns = [
  {
    header: 'ID',
    accessorKey: 'id',
    enableHiding: false, // disable hiding for this column
  },
  {
    header: 'Name',
    accessorKey: 'name', // can be hidden
  },
]
```

### 列の表示を切り替える API {#column-visibility-toggle-apis}

UI に列の表示切り替えのトグルを描画するときに役立つ、列の API メソッドがいくつかあります。

- `column.getCanHide` - `enableHiding` が `false` に設定された列の表示切り替えトグルを無効にするときに使います。
- `column.getIsVisible` - 表示切り替えトグルの初期状態を設定するときに使います。
- `column.toggleVisibility` - 列の表示・非表示を切り替えるときに使います。
- `column.getToggleVisibilityHandler` - `column.toggleVisibility` メソッドを UI のイベントハンドラーにつなぐためのショートカットです。

```tsx
const columnLabels: Record<string, string> = {
  firstName: 'First Name',
  lastName: 'Last Name',
}

{
  table.getAllColumns().map((column) => (
    <label key={column.id}>
      <input
        checked={column.getIsVisible()}
        disabled={!column.getCanHide()}
        onChange={column.getToggleVisibilityHandler()}
        type="checkbox"
      />
      {columnLabels[column.id] ?? column.id}
    </label>
  ))
}
```

> [!NOTE]
> `column.columnDef.header` はヘッダーを描画するためのテンプレートです。
> 文字列や JSX のほか、ヘッダーコンテキストを必要とする関数のこともあり、
> 実際のテーブルヘッダーを描画するときは `flexRender` で描画します。
> 一方、列の表示切り替えメニューで描画するのはふつうヘッダーオブジェクトではなく列です。
> また、非表示の列には有効なヘッダーコンテキストがないこともあります。
> そのため表示切り替えのトグルには、列 ID をキーにした独自のラベルのマップ、
> 型を付けた `columnDef.meta`（たとえば `column.columnDef.meta.label`）、
> `column.id` など、変わらないテキストのラベルを使うことをおすすめします。

### 列の表示状態を考慮するテーブル API {#column-visibility-aware-table-apis}

ヘッダー・本体・フッターのセルを描画するときに使える API はたくさんあります。`table.getAllLeafColumns` や `row.getAllCells` といった API もありますが、これらは列の表示状態を考慮しません。代わりに、`table.getVisibleLeafColumns` や `row.getVisibleCells` のような「visible」付きの API を使う必要があります。

```tsx
<table>
  <thead>
    <tr>
      {table.getVisibleLeafColumns().map((column) => ( // takes column visibility into account
        //
      ))}
    </tr>
  </thead>
  <tbody>
    {table.getRowModel().rows.map((row) => (
      <tr key={row.id}>
        {row.getVisibleCells().map((cell) => ( // takes column visibility into account
          //
        ))}
      </tr>
    ))}
  </tbody>
</table>
```

ヘッダーグループの API を使っている場合は、もともと列の表示状態が考慮されています。
