---
title: 展開（React）ガイド
---

## サンプル {#examples}

すぐに実装を見たい場合は、次の React のサンプルを参照してください。

- [展開](https://tanstack.com/table/latest/docs/framework/react/examples/expanding)

### 展開のセットアップ {#expanding-setup}

展開の機能を使うためのテーブルのセットアップ方法は次のとおりです。展開の機能を追加すると、関連する API が使えるようになります。クライアントサイドの展開を使う場合は、`expandedRowModel` も機能の後に設定してください。行モデルのスロットは型チェックされるためです。

```tsx
import {
  useTable,
  tableFeatures,
  rowExpandingFeature,
  createExpandedRowModel,
} from '@tanstack/react-table'

const features = tableFeatures({
  rowExpandingFeature,
  expandedRowModel: createExpandedRowModel(), // if using client-side expanding
  // manualExpanding: true, // if using manual server-side expanding
})

const table = useTable({
  features,
  columns,
  data,
})
```

## 展開機能（React）ガイド {#expanding-feature-react-guide}

展開は、特定の行に関連する追加の行データを表示したり隠したりできる機能です。階層構造のデータがあり、ユーザーに上位の階層から詳細へと掘り下げてもらいたい場合に役立ちます。また、行に関連する追加情報を表示したい場合にも便利です。

### 展開機能のさまざまな使い方 {#different-use-cases-for-expanding-features}

TanStack Table の展開機能には複数の使い方があります。以下ではそれぞれを説明します。

1. サブ行（子の行、集計行など）を展開する
2. 独自の UI（詳細パネル、サブテーブルなど）を展開する

### クライアントサイドの展開を有効にする {#enable-client-side-expanding}

クライアントサイドの展開機能を使うには、`rowExpandingFeature` と `expandedRowModel` のファクトリーを features に追加します。

```ts
import {
  useTable,
  tableFeatures,
  rowExpandingFeature,
  createExpandedRowModel,
} from '@tanstack/react-table'

const features = tableFeatures({
  rowExpandingFeature,
  expandedRowModel: createExpandedRowModel(),
})

const table = useTable({
  features,
  // other options...
})
```

展開されるデータには、テーブルの行を入れることも、表示したい任意のデータを入れることもできます。このガイドでは、両方の場合の扱い方を説明します。

### 展開データとしてのテーブルの行 {#table-rows-as-expanded-data}

展開される行は、親の行と同じ列構造を受け継ぐ子の行です。データオブジェクトに展開用の行データがすでに含まれている場合は、`getSubRows` 関数でその子の行を指定します。データオブジェクトに展開用の行データが含まれていない場合は、独自の展開データとして扱えます。これは次の節で説明します。

たとえば、次のようなデータオブジェクトがあるとします。

```ts
type Person = {
  id: number
  name: string
  age: number
  children?: Person[] | undefined
}

const data: Person[] = [
  {
    id: 1,
    name: 'John',
    age: 30,
    children: [
      { id: 2, name: 'Jane', age: 5 },
      { id: 5, name: 'Jim', age: 10 },
    ],
  },
  {
    id: 3,
    name: 'Doe',
    age: 40,
    children: [{ id: 4, name: 'Alice', age: 10 }],
  },
]
```

この場合、getSubRows 関数を使って、各行の children 配列を展開される行として返せます。これでテーブルインスタンスは、各行のどこにサブ行があるかを把握できます。

```ts
const table = useTable({
  features,
  getSubRows: (row) => row.children, // return the children array as sub-rows
  // other options...
})
```

> [!NOTE]
> `getSubRows` 関数は複雑にしてもかまいません。ただし、この関数はすべての行とすべてのサブ行に対して実行される点に注意してください。関数が最適化されていないと、処理が重くなるおそれがあります。非同期関数はサポートされていません。

### 独自の展開 UI {#custom-expanding-ui}

場合によっては、行の展開データのように、追加の詳細や情報を表示したいことがあります。その情報はテーブルのデータオブジェクトに含まれていることも、含まれていないこともあります。こうした行を展開する UI は、これまで「展開可能な行（expandable rows）」「詳細パネル（detail panels）」「サブコンポーネント（sub-components）」など、さまざまな名前で呼ばれてきました。

デフォルトでは、行インスタンスの API である `row.getCanExpand()` は、行に `subRows` がない限り false を返します。この動作は、テーブルインスタンスのオプションで独自の `getRowCanExpand` 関数を実装すると上書きできます。

```tsx
import { Fragment } from 'react'

//...
const table = useTable({
  features,
  getRowCanExpand: (row) => true, // Add your logic to determine if a row can be expanded. True means all rows include expanded data
  // other options...
})
//...
<tbody>
  {table.getRowModel().rows.map((row) => (
    <Fragment key={row.id}>
     {/* Normal row UI */}
      <tr>
        {row.getVisibleCells().map((cell) => (
          <td key={cell.id}>
            <table.FlexRender cell={cell} />
          </td>
        ))}
      </tr>
      {/* If the row is expanded, render the expanded UI as a separate row with a single cell that spans the width of the table */}
      {row.getIsExpanded() && (
        <tr>
          {/* span however many columns the expanded data needs if it does not share the parent row's columns */}
          <td colSpan={row.getAllCells().length}>
            {/* Your custom UI goes here */}
          </td>
        </tr>
      )}
    </Fragment>
  ))}
</tbody>
//...
```

### 展開された行の状態 {#expanded-rows-state}

アプリケーションのほかの場所で行の展開状態を参照したい場合は、`expanded` の状態のスライスを自分で管理できます。v9 で推奨される方法は、外部のアトムを `atoms` テーブルオプションで渡すことです。アトムは細かい粒度の購読を保ちます。そのため、テーブルを持つコンポーネントを再レンダーさせることなく、アプリのどこからでも展開状態の値を読み取れます。

```ts
import { useCreateAtom, useSelector } from '@tanstack/react-store'

const expandedAtom = useCreateAtom<ExpandedState>({})

// subscribe to the atom wherever you need the value
const expanded = useSelector(expandedAtom)

const table = useTable({
  features,
  // other options...
  atoms: {
    expanded: expandedAtom, // expanding APIs now update expandedAtom
  },
})
```

あるいは、v8 スタイルの `state.expanded` と `onExpandedChange` を組み合わせるパターンも引き続きサポートされています。単純な組み込みや v8 のコードを移行する場合には便利ですが、外部のアトムに比べると購読の粒度は粗くなります。詳しい比較は[テーブルの状態ガイド](./table-state)を参照してください。

```ts
const [expanded, setExpanded] = useState<ExpandedState>({})

const table = useTable({
  features,
  // other options...
  state: {
    expanded,
  },
  onExpandedChange: setExpanded,
})
```

ExpandedState 型は次のように定義されています。

```ts
type ExpandedState = true | Record<string, boolean>
```

ExpandedState が true の場合は、すべての行が展開されていることを意味します。レコードの場合は、ID がレコードのキーとして存在し、値が true の行だけが展開されます。たとえば展開状態が { row1: true, row2: false } であれば、ID が row1 の行は展開され、ID が row2 の行は展開されていないことを意味します。テーブルはこの状態を使って、どの行が展開されていて、サブ行（subRows）があればそれを表示すべきかを判断します。

### 展開された行を切り替える UI のハンドラー {#ui-toggling-handler-for-expanded-rows}

TanStack Table は、展開データを切り替えるための UI のハンドラーをテーブルに追加しません。ユーザーが行を展開したり折りたたんだりできるように、各行の UI に自分で追加する必要があります。たとえば、列定義の中にボタンの UI を追加できます。

```tsx
const columns = [
  {
    accessorKey: 'name',
    header: 'Name',
  },
  {
    accessorKey: 'age',
    header: 'Age',
  },
  {
    header: 'Children',
    cell: ({ row }) => {
      return row.getCanExpand() ? (
        <button
          onClick={row.getToggleExpandedHandler()}
          style={{ cursor: 'pointer' }}
        >
          {row.getIsExpanded() ? '👇' : '👉'}
        </button>
      ) : (
        ''
      )
    },
  },
]
```

### 展開の API {#expanding-apis}

行には、展開状態を読み取ったり切り替えたりするためのヘルパーがあります。

```tsx
row.getCanExpand()
row.getIsExpanded()
row.getIsAllParentsExpanded()
row.getToggleExpandedHandler()
row.toggleExpanded()
```

テーブルインスタンスには、テーブル全体の展開状態を読み取ったり切り替えたりするためのヘルパーがあります。

```tsx
table.getCanSomeRowsExpand()
table.getIsAllRowsExpanded()
table.getIsSomeRowsExpanded()
table.getExpandedDepth()
table.getToggleAllRowsExpandedHandler()
table.toggleAllRowsExpanded()
table.resetExpanded()
```

展開状態を直接更新するには `table.setExpanded` を使います。`table.resetExpanded()` は `initialState.expanded` に戻し、`table.resetExpanded(true)` は展開状態を空にします。

### 展開された行のフィルタリング {#filtering-expanded-rows}

デフォルトでは、フィルタリングは親の行から始まり、下の階層へと進みます。親の行がフィルターで除外されると、その子の行もすべて除外されます。この動作は `filterFromLeafRows` オプションで変更できます。有効にすると、フィルタリングは末端の（子の）行から始まり、上の階層へと進みます。そのため、子や孫の行のうち少なくとも1つがフィルターの条件を満たしていれば、親の行もフィルタリングの結果に含まれます。`maxLeafRowFilterDepth` オプションでは、フィルターが対象とする子の行の最大の深さを設定します。

```ts
const features = tableFeatures({
  columnFilteringFeature,
  rowExpandingFeature,
  filteredRowModel: createFilteredRowModel(),
  expandedRowModel: createExpandedRowModel(),
  filterFns,
})

//...
const table = useTable({
  features,
  getSubRows: (row) => row.subRows,
  filterFromLeafRows: true, // search through the expanded rows
  maxLeafRowFilterDepth: 1, // limit the depth of the expanded rows that are searched
  // other options...
})
```

### 展開された行のページネーション {#paginating-expanded-rows}

デフォルトでは、展開された行もテーブルのほかの行と一緒にページ分けされます（つまり、展開された行が複数のページにまたがることがあります）。この動作を無効にしたい場合は、`paginateExpandedRows` オプションを使います（無効にすると、展開された行は常に親と同じページに描画されます。その分、設定したページサイズより多くの行が描画されることになります）。

```ts
const table = useTable({
  features,
  // other options...
  paginateExpandedRows: false,
})
```

### 展開された行の固定 {#pinning-expanded-rows}

展開された行の固定は、通常の行の固定と同じように動作します。展開された行をテーブルの上端や下端に固定できます。行の固定について詳しくは、[行の固定ガイド](./row-pinning)を参照してください。

### 展開された行のソート {#sorting-expanded-rows}

デフォルトでは、展開された行もテーブルのほかの行と一緒にソートされます。

### 展開状態の自動リセット {#auto-reset-expanded-state}

グループ化の機能も使っている場合、`expanded` の状態は、グループ化された行モデルが計算し直されるたびに自動でリセットされます。たとえば `data` やグループ化の状態が変わったときです。このデフォルトの動作は `manualExpanding` が `true` のときには自動で無効になりますが、`autoResetExpanded` テーブルオプションに真偽値を明示的に指定すれば上書きできます。また、すべての自動リセットの動作をまとめて無効に（または有効に）する、グローバルな `autoResetAll` テーブルオプションもあります。

`autoResetExpanded: false` を設定するよくある理由は、テーブルを表示したままデータを編集する場合（たとえばセルのインライン編集）です。編集のたびに `data` が更新されて行モデルが計算し直されるため、何もしないとユーザーが展開していた行が折りたたまれてしまいます。ページネーションの機能も使っている場合は、`autoResetPageIndex: false` も組み合わせて、現在のページも保たれるようにしてください。

```ts
const table = useTable({
  features,
  // other options...
  autoResetExpanded: false, // keep expanded state when data changes
  // autoResetAll: false, // or turn off all auto resets at once
})
```

### 手動の展開（サーバーサイド） {#manual-expanding-server-side}

サーバーサイドで展開を行う場合は、manualExpanding オプションを true に設定して、行の手動展開を有効にできます。この場合、行の展開に `getExpandedRowModel` は使われず、展開は自分のデータモデルの中で行う必要があります。

```ts
const features = tableFeatures({ rowExpandingFeature })

const table = useTable({
  features,
  // other options...
  manualExpanding: true,
})
```
