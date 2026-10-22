---
title: データガイド
---

テーブルはデータから始まります。列定義と行は、データの形に左右されます。TanStack Table には、残りのテーブルのコードを型安全に、快適に書くための TypeScript の機能がいくつかあります。データと型を正しく設定すれば、TanStack Table はデータの形を推論し、列定義が正しく書かれていることを型で保証できます。

## TypeScript {#typescript}

TanStack Table のパッケージを使うのに TypeScript は必須ではありません。**_しかし_**、TanStack Table は、TypeScript での優れた開発体験がライブラリの大きな売りの1つだと感じられるように書かれ、構成されています。TypeScript を使わないと、優れた自動補完や型チェックの機能の多くを逃すことになります。これらは開発時間を短縮し、コードのバグも減らしてくれます。

### TypeScript のジェネリクス {#typescript-generics}

TypeScript のジェネリクスとは何か、どう動くのかを基本的に理解していると、このガイドがより分かりやすくなります。ただ、読み進めながらでも十分に身に付くはずです。TypeScript にまだ慣れていない方には、公式の [TypeScript ジェネリクスのドキュメント](https://www.typescriptlang.org/docs/handbook/2/generics.html)が役立つかもしれません。

### データの型を定義する {#defining-data-types}

`data` は、テーブルの行に変換されるオブジェクトの配列です。配列内の各オブジェクトは、（通常は）1行分のデータを表します。TypeScript を使う場合は、たいていデータの形を表す型を定義します。この型は、テーブル・列・行・セルの各インスタンスすべてのジェネリクスの型として使われます。TanStack Table の型や API の他の箇所では、このジェネリクスはふつう `TData` と呼ばれます。

たとえば、次のような配列でユーザーの一覧を表示するテーブルがあるとします。

```json
[
  {
    "firstName": "Tanner",
    "lastName": "Linsley",
    "age": 33,
    "visits": 100,
    "progress": 50,
    "status": "Married"
  },
  {
    "firstName": "Kevin",
    "lastName": "Vandy",
    "age": 27,
    "visits": 200,
    "progress": 100,
    "status": "Single"
  }
]
```

このとき、User（TData）型は次のように定義できます。

```ts
//TData
type User = {
  firstName: string
  lastName: string
  age: number
  visits: number
  progress: number
  status: string
}
```

この型で `data` 配列を定義すれば、後で列・行・セルなどを扱うときに、TanStack Table が多くの型を賢く推論してくれます。`data` の型が、文字どおり `TData` ジェネリクスの型として定義されているからです。`data` テーブルオプションに渡したものが、そのテーブルインスタンス全体の `TData` 型になります。後で列定義を書くときは、`data` の型と同じ `TData` 型を使うようにしてください。

```ts
//note: data needs a "stable" reference to prevent wasteful re-computation (more on this below)
const data: Array<User> = []
//or
const [data, setData] = React.useState<Array<User>>([])
//or
const data = ref<Array<User>>([]) //vue
//etc...
```

### 深いキーを持つデータ {#deep-keyed-data}

データがきれいでフラットなオブジェクトの配列でなくても大丈夫です。列を定義する段階で、アクセサーから深くネストしたデータにアクセスする方法があります。

`data` が次のような形だとします。

```json
[
  {
    "name": {
      "first": "Tanner",
      "last": "Linsley"
    },
    "info": {
      "age": 33,
      "visits": 100
    }
  },
  {
    "name": {
      "first": "Kevin",
      "last": "Vandy"
    },
    "info": {
      "age": 27,
      "visits": 200
    }
  }
]
```

型は次のように定義できます。

```ts
type User = {
  name: {
    first: string
    last: string
  }
  info: {
    age: number
    visits: number
  }
}
```

そして、列定義では accessorKey のドット記法か、単に accessorFn を使ってデータにアクセスできます。

```ts
const columns = [
  {
    header: 'First Name',
    accessorKey: 'name.first',
  },
  {
    header: 'Last Name',
    accessorKey: 'name.last',
  },
  {
    header: 'Age',
    accessorFn: (row) => row.info.age, //accessorFn receives the whole row object
  },
  //...
]
```

詳しくは[列定義ガイド](./column-defs)で説明しています。

> [!NOTE]
> JSON データの「キー」はたいてい何でもかまいませんが、`accessorKey` の中のピリオドはすべて深いキーのパスとして解釈されます。データのキーにピリオドそのものが含まれる場合は、代わりに `accessorFn` で読み取ってください。

### ネストしたサブ行のデータ {#nested-sub-row-data}

展開の機能を使う場合、データにネストしたサブ行が含まれるのはよくあることです。この場合、型は少し違った再帰的な型になります。

データが次のような形だとします。

```json
[
  {
    "firstName": "Tanner",
    "lastName": "Linsley",
    "subRows": [
      {
        "firstName": "Kevin",
        "lastName": "Vandy"
      },
      {
        "firstName": "John",
        "lastName": "Doe",
        "subRows": []
      }
    ]
  },
  {
    "firstName": "Jane",
    "lastName": "Doe"
  }
]
```

型は次のように定義できます。

```ts
type User = {
  firstName: string
  lastName: string
  subRows?: Array<User> //does not have to be called "subRows", can be called anything
}
```

ここで `subRows` は、`User` オブジェクトの省略可能な配列です。詳しくは[展開ガイド](../framework/react/guide/expanding)で説明しています。

### 形が分からないデータ {#data-of-unknown-shape}

データの形が前もって分からないため、行の型をまったく書けないこともあります（任意の API レスポンス、ユーザーがアップロードした CSV ファイル、ユーザーが設定できるレポートなど）。その場合は、行を汎用のレコードとして型付けします。

```ts
type DynamicRow = Record<string, unknown>

const data: Array<DynamicRow> = await fetchWhoKnowsWhat()
```

列ごとの値の推論はできなくなりますが、それ以外はすべてこれまでどおり動きます。この場合、列定義はハードコードせず、実行時にデータそのものから生成します。ソートやフィルタリングのための実行時のデータ型の判定も含めた完全なパターンは、列定義ガイドの[動的な列定義](./column-defs#dynamic-column-definitions)と、[動的な列のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/basic-dynamic-columns)（すべてのフレームワークアダプター向けにあります）を参照してください。

## データに「安定した」参照を持たせる {#give-data-a-stable-reference}

テーブルインスタンスに渡す `data` と `columns` の配列は、「安定した」参照を持たせてください。無駄な再計算や描画のバグを防ぐためです。

v9 では、テーブルの状態は TanStack Store のアトムに置かれ、テーブルインスタンスは一度しか作られません。描画のたびに新しい `data` や `columns` の参照を渡しても、それだけで v8 でおなじみの無限再レンダーループに陥ることはありません。しかし、行モデルや列の構造は `data` と `columns` の参照をもとにメモ化されているので、参照が不安定だと実際に次のような影響があります。

- **無駄な再計算。** `data` の参照が新しくなるとコア行モデルが無効になり、描画のたびにすべての行とセルのオブジェクトが一から作り直されます（ソート・フィルタリング・グループ化・ページネーションを適用した行モデルも、すべて一緒に再計算されます）。`columns` の参照が新しくなると、列とヘッダーの構造で同じことが起こります。大きなデータセットでは、深刻なパフォーマンスの問題になります。
- **自動リセットによる描画のループ。** 行が再計算されたときに状態を自動でリセットする機能は、今でも無限再レンダーループを引き起こすことがあります。たとえば、クライアントサイドのページネーションを有効にしていると、`autoResetPageIndex` は行モデルが再計算されるたびにページ番号をリセットします。`data` の参照が不安定だと、描画のたびに状態が更新され、その更新がまた新しい `data` の参照を伴う描画を引き起こします。

いずれにしても、`data` と `columns` の参照が安定していることは必須だと考えてください。

> [!NOTE]
> React Compiler がコンポーネントのコンパイルに成功すると、値や計算に安定した同一性を自動で与えられます。TanStack Table のサンプルでは、コンパイラーがなくても動くように、以下の明示的なパターンを残しています。手動のメモ化を外せる場面については、[React Compiler ガイド](../framework/react/guide/react-compiler)を参照してください。

方法は使っているフレームワークアダプターによって異なりますが、React では多くの場合、`React.useState` や `React.useMemo` などを使って、`data` と `columns` の両方のテーブルオプションが安定した参照を持つようにします。

```tsx
const fallbackData: Array<User> = [] //✅ GOOD: stable empty fallback for when your data can be undefined (e.g. while a query loads)
const features = tableFeatures({}) //✅ GOOD: define outside the component for a stable reference

export default function MyComponent() {
  //✅ GOOD: `columns` is a stable reference
  const columns = useMemo(
    () => [
      // ...
    ],
    [],
  )

  //✅ GOOD: `data` is a stable reference
  const [data, setData] = useState<Array<User>>(() => [
    // ...
  ])

  // Columns and data have stable references, so the table only recomputes when they actually change
  const table = useTable({
    features,
    columns,
    data, // from useState, so always defined; use `data ?? fallbackData` when your data can be undefined
  })

  return <table>...</table>
}
```

データに安定した参照を持たせる方法は、`React.useState` と `React.useMemo` だけではありません。データをコンポーネントの外で定義したり、Redux、Zustand、TanStack Query といったサードパーティの状態管理ライブラリを使ったりすることもできます。

何より避けるべきなのは、`useTable` の呼び出しと同じスコープで `data` 配列を定義することです。そうすると描画のたびに `data` 配列が定義し直され、テーブルは描画のたびにすべての行を作り直すことになります（自動リセットの機能が絡むと、無限にループすることもあります）。

```tsx
export default function MyComponent() {
  //❌ BAD: `features` is re-created on every render and re-applied to the table on every render
  const features = tableFeatures({})

  //😵 BAD: `columns` is redefined as a new array on every render, so the column and header structures are rebuilt on every render!
  const columns = [
    // ...
  ]

  //😵 BAD: `data` is redefined as a new array on every render, so every row is rebuilt on every render!
  const data = [
    // ...
  ]

  //❌ Columns and data are defined in the same scope as `useTable` without stable references
  const table = useTable({
    features,
    columns,
    data: data ?? [], //❌ Also bad because the fallback array is re-created on every render
  })

  return <table>...</table>
}
```

### データの変換をメモ化する {#memoize-data-transformations}

元のデータがすでに安定した参照を持っていても、インラインで変換するとその安定性は失われます。インラインで `data.filter()` を書くだけでも、描画のたびに新しい配列が作られます。

```tsx
export default function MyComponent() {
  //✅ GOOD (TanStack Query provides stable references to data automatically)
  const { data, isLoading } = useQuery({
    //...
  })

  const table = useTable({
    features,
    columns,
    //❌ BAD: This creates a new array on every render (destroys the stable reference)
    data: data?.filter((d) => d.isActive) ?? fallbackData,
  })

  return <table>...</table>
}
```

代わりに、データの変換は必ずメモ化してください。React では `useMemo` などでメモ化できます。

```tsx
export default function MyComponent() {
  //✅ GOOD
  const { data, isLoading } = useQuery({
    //...
  })

  //✅ GOOD: `filteredData` only gets a new reference when `data` changes
  const filteredData = useMemo(
    () => data?.filter((d) => d.isActive) ?? [],
    [data],
  )

  const table = useTable({
    features,
    columns,
    data: filteredData, // stable reference!
  })

  return <table>...</table>
}
```

取得したデータとの完全な組み込み例は、[TanStack Query と組み合わせたサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/with-tanstack-query)を参照してください。

## TanStack Table がデータを変換する仕組み {#how-tanstack-table-transforms-data}

このドキュメントの他の箇所では、TanStack Table がテーブルに渡された `data` をどう処理し、テーブルを作るのに使う行とセルのオブジェクトをどう生成するかを説明します。テーブルに渡した `data` を TanStack Table が書き換えることはありません。ただし、行やセルの実際の値は、列定義のアクセサーや、グループ化・集計といった[行モデル](./row-models)の変換によって変わることがあります。

## TanStack Table はどれくらいのデータを扱えるか {#how-much-data-can-tanstack-table-handle}

TanStack Table のクライアントサイドの行モデルは、大きなデータセットを扱えるように作られています。公式のサンプルには、もっと大規模な負荷テストも含まれています。実際の上限は、ペイロード、テーブルの機能、描画の方式、対象のハードウェアによって変わります。そのため、行数だけで決めず、実際に近いデータでテストしてください。

判断の枠組みの全体像と、データ処理・ページネーション・仮想化の違いについては、[クライアントサイドとサーバーサイドのガイド](./client-side-vs-server-side)を参照してください。
