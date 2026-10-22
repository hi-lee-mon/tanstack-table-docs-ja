---
title: クイックスタート
---

TanStack Table はヘッドレスなテーブルライブラリです。テーブルの状態とロジック（ソート、フィルタリング、ページネーション、選択など）を管理し、マークアップとスタイルは 100% あなたの手に委ねます。このページでは、インストールから React のテーブルを描画するところまでを進め、そのうえで最初の機能を追加する方法を紹介します。

## インストール {#installation}

```bash
npm install @tanstack/react-table
```

## 最初のテーブル {#your-first-table}

次のコンポーネントはこれだけで完結しています。React アプリに貼り付ければ、動くテーブルが表示されます。

```tsx
import { tableFeatures, useTable } from '@tanstack/react-table'
import type { ColumnDef } from '@tanstack/react-table'

// 1. Define the shape of your data
type Person = {
  firstName: string
  lastName: string
  age: number
}

// 2. Give your data a stable reference (module scope, useState, useQuery, etc.)
const data: Array<Person> = [
  { firstName: 'tanner', lastName: 'linsley', age: 24 },
  { firstName: 'tandy', lastName: 'miller', age: 40 },
  { firstName: 'joe', lastName: 'dirte', age: 45 },
]

// 3. New in v9: declare which features this table uses (none yet)
const features = tableFeatures({})

// 4. Define your columns
const columns: Array<ColumnDef<typeof features, Person>> = [
  {
    accessorKey: 'firstName', // accessorKey shorthand
    header: 'First Name',
    cell: (info) => info.getValue(),
  },
  {
    accessorFn: (row) => row.lastName, // accessorFn alternative with a custom id
    id: 'lastName',
    header: () => <span>Last Name</span>,
    cell: (info) => <i>{info.getValue<string>()}</i>,
  },
  {
    accessorKey: 'age',
    header: () => 'Age',
  },
]

export function PersonTable() {
  // 5. Create the table instance
  const table = useTable({
    key: 'person-table', // needed for devtools, omit if you don't want to use the devtools
    features,
    columns,
    data,
  })

  // 6. Render markup from the table instance APIs
  return (
    <table>
      <thead>
        {table.getHeaderGroups().map((headerGroup) => (
          <tr key={headerGroup.id}>
            {headerGroup.headers.map((header) => (
              <th key={header.id}>
                {header.isPlaceholder ? null : (
                  <table.FlexRender header={header} />
                )}
              </th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody>
        {table.getRowModel().rows.map((row) => (
          <tr key={row.id}>
            {row.getAllCells().map((cell) => (
              <td key={cell.id}>
                <table.FlexRender cell={cell} />
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  )
}
```

いくつか補足します。

- `tableFeatures({})` は、テーブルが使う省略可能な機能を宣言します。必要なものだけを登録すれば、バンドルを小さく保てるうえ、TypeScript がテーブルインスタンスに正確な型を付けられます。
- コア行モデルは常に自動で含まれます。機能ごとの行モデル（ソート、フィルタリング、ページネーション）は、必要になったときに features オブジェクトのスロットとして登録します。
- `table.FlexRender` は、列に定義した `header`、`cell`、`footer` を描画します。定義がただの値でも React コンポーネントでもかまいません。
- `key` オプションは、[TanStack Table Devtools](../../devtools) を使わないかぎり省略できます。Devtools は `key` でテーブルを識別します。テーブルを登録するには、`@tanstack/react-table-devtools` の `useTanStackTableDevtools(table)` を呼び出します。

列やフッターを増やした実行可能なバージョンは、[Basic useTable のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/basic-use-table)の全体を参照してください。

## 機能を追加する: ソート {#add-a-feature-sorting}

v9 では、機能はオプトイン（明示的に有効にする）方式です。列をソートできるようにするには、`tableFeatures` に `rowSortingFeature` とソート済み行モデルを登録し、ヘッダーのクリックハンドラーをつなぎます。

```tsx
import {
  createSortedRowModel,
  rowSortingFeature,
  sortFns,
  tableFeatures,
  useTable,
} from '@tanstack/react-table'

const features = tableFeatures({
  rowSortingFeature, // enables sorting APIs and state
  sortedRowModel: createSortedRowModel(), // client-side sorting
  sortFns,
})

export function PersonTable() {
  const table = useTable({
    key: 'person-table',
    features,
    columns,
    data,
  })

  return (
    <table>
      <thead>
        {table.getHeaderGroups().map((headerGroup) => (
          <tr key={headerGroup.id}>
            {headerGroup.headers.map((header) => (
              <th key={header.id}>
                {header.isPlaceholder ? null : (
                  <div
                    style={{
                      cursor: header.column.getCanSort()
                        ? 'pointer'
                        : undefined,
                    }}
                    onClick={header.column.getToggleSortingHandler()}
                  >
                    <table.FlexRender header={header} />
                    {{
                      asc: ' 🔼',
                      desc: ' 🔽',
                    }[header.column.getIsSorted() as string] ?? null}
                  </div>
                )}
              </th>
            ))}
          </tr>
        ))}
      </thead>
      {/* tbody unchanged from above */}
    </table>
  )
}
```

これで、ヘッダーをクリックするたびに昇順、降順、ソートなしが切り替わります。他の機能もすべて同じパターンです。`tableFeatures` に機能と、（あれば）その行モデルのファクトリーを登録し、機能がテーブル・列・行に追加する API を使います。カスタムのソート関数、複数列でのソート、列ごとのオプションについては、[ソートのガイド](./guide/sorting)と [ソートのサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/sorting)を参照してください。

## 次に読むもの {#where-to-go-next}

**テーブルの状態。** v9 では、テーブルの状態は TanStack Store のアトムで管理されています。たいていは自分で管理する必要はありません。開始時の値は `initialState` で設定し、`table.setSorting(...)` や `table.nextPage()` のような機能の API を呼び出します。状態スライスをアプリ側で持ちたい場合や、細かい粒度で購読したい場合は、[テーブルの状態のガイド](./guide/table-state)を読んでください。他のすべての土台になるガイドです。

**機能ごとのガイド。** 機能ごとにガイドがあります。たとえば[列フィルタリング](./guide/column-filtering)、[ページネーション](./guide/pagination)、[行選択](./guide/row-selection)、[列の表示切り替え](./guide/column-visibility)などです。

**組み立て可能なテーブル。** アプリ内の複数のテーブルで機能、行モデル、コンポーネントの約束事を共有する場合は、`createTableHook` で一度だけ定義します。

```tsx
const features = tableFeatures({
  rowSortingFeature,
  sortedRowModel: createSortedRowModel(),
  sortFns,
})

const { useAppTable, createAppColumnHelper } = createTableHook({ features })
```

事前に紐付けたセルやヘッダーのコンポーネントを含むパターン全体は、[組み立て可能なテーブルのガイド](./guide/composable-tables)を参照してください。

**例。** 基本的なテーブルから機能のデモまで、実行可能な [React のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/basic-use-table)を眺めると、想定されている使い方を最初から最後まで確認できます。
