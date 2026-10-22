---
title: カスタム機能（React）ガイド
---

## サンプル {#examples}

実装をすぐに見たい場合は、次の React のサンプルを参照してください。

- [カスタムプラグイン](https://tanstack.com/table/latest/docs/framework/react/examples/custom-plugin)

## カスタム機能（React）ガイド {#custom-features-react-guide}

このガイドでは、TanStack Table を独自の機能で拡張する方法を説明します。その過程で、TanStack Table v9 のコードベースがどのような構成で、どう動いているのかもあわせて見ていきます。

### TanStack Table は軽量であることを目指している {#tanstack-table-strives-to-be-lean}

TanStack Table には、ソート、フィルタリング、ページネーションなど、ライブラリに組み込まれたコア機能があります。これまで、さらに多くの機能を追加してほしいという要望を数多く受け取ってきました。よく考えられた PR をもらうこともあります。ライブラリの改善にはいつでも前向きですが、同時に TanStack Table を、ほとんどのユースケースで使われそうにないコードで膨らませず、軽量なライブラリのままにしておきたいとも考えています。実際の問題を解決する PR であっても、すべてをコアライブラリに取り込めるわけではなく、取り込むべきでもありません。TanStack Table でユースケースの9割は解決できるのに、あと少しだけ制御したいという開発者にとっては、もどかしいことかもしれません。

TanStack Table は、（少なくとも v7 以降は）高い拡張性を持つように作られてきました。使っているフレームワークのアダプター（`createTable`、`useTable` など）から返される `table` インスタンスは、プロパティや API を追加できる普通の JavaScript オブジェクトです。コンポジションを使って、独自のロジック、状態、API をテーブルインスタンスに追加することは以前から可能でした。[Material React Table](https://github.com/KevinVandy/material-react-table/blob/v2/packages/material-react-table/src/hooks/useMRT_TableInstance.ts) などのライブラリは、`useTable` フックを包む独自のラッパーフックを作るだけで、テーブルインスタンスに独自の機能を追加しています。

v9 の TanStack Table では、`features` オプション（`tableFeatures()` で作成）で、テーブルが使う機能を宣言します。これによりツリーシェイキングが効き、必要な機能のコードだけがバンドルされます。カスタム機能も、組み込みの機能とまったく同じ方法でテーブルインスタンスに追加できます。

> v9 では、機能はオプトイン（明示的に有効にする）方式です。カスタム機能も含め、テーブルが使う機能は `tableFeatures({ ... })` で宣言してください。

### TanStack Table の機能の仕組み {#how-tanstack-table-features-work}

TanStack Table のソースコードは、比較的シンプルだと言えるでしょう（少なくとも私たちはそう考えています）。各機能のコードはすべて、それぞれ独立したオブジェクト（ファイル）に分かれています。そこには、初期状態やデフォルトのテーブル・列のオプションを作るための初期化メソッドと、`table`、`header`、`column`、`row`、`cell` の各インスタンスに追加できる API メソッドが含まれています。

機能オブジェクトが持てるものは、すべて TanStack Table からエクスポートされている `TableFeature` 型で表せます。この型は、機能を作るのに必要な機能オブジェクトの形を表す TypeScript のインターフェースです。

```ts
export interface TableFeature {
  assignCellPrototype?: <
    TFeatures extends TableFeatures,
    TData extends RowData,
  >(
    prototype: Record<string, any>,
    table: Table_Internal<TFeatures, TData>,
  ) => void
  assignColumnPrototype?: <
    TFeatures extends TableFeatures,
    TData extends RowData,
  >(
    prototype: Record<string, any>,
    table: Table_Internal<TFeatures, TData>,
  ) => void
  assignHeaderPrototype?: <
    TFeatures extends TableFeatures,
    TData extends RowData,
  >(
    prototype: Record<string, any>,
    table: Table_Internal<TFeatures, TData>,
  ) => void
  assignRowPrototype?: <TFeatures extends TableFeatures, TData extends RowData>(
    prototype: Record<string, any>,
    table: Table_Internal<TFeatures, TData>,
  ) => void
  constructTableAPIs?: <TFeatures extends TableFeatures, TData extends RowData>(
    table: Table_Internal<TFeatures, TData>,
  ) => void
  initTableInstanceData?: <
    TFeatures extends TableFeatures,
    TData extends RowData,
  >(
    table: Table_Internal<TFeatures, TData>,
  ) => void
  getDefaultColumnDef?: <
    TFeatures extends TableFeatures,
    TData extends RowData,
    TValue extends CellData = CellData,
  >() => ColumnDefBase_All<TFeatures, TData, TValue>
  getDefaultTableOptions?: <
    TFeatures extends TableFeatures,
    TData extends RowData,
  >(
    table: Table_Internal<TFeatures, TData>,
  ) => Partial<TableOptions_All<TFeatures, TData>>
  getInitialState?: (initialState: Partial<TableState_All>) => TableState_All
  initCellInstanceData?: <
    TFeatures extends TableFeatures,
    TData extends RowData,
    TValue extends CellData = CellData,
  >(
    cell: Cell<TFeatures, TData, TValue>,
  ) => void
  initColumnInstanceData?: <
    TFeatures extends TableFeatures,
    TData extends RowData,
    TValue extends CellData = CellData,
  >(
    column: Column<TFeatures, TData, TValue>,
  ) => void
  initHeaderGroupInstanceData?: <
    TFeatures extends TableFeatures,
    TData extends RowData,
  >(
    headerGroup: HeaderGroup<TFeatures, TData>,
  ) => void
  initHeaderInstanceData?: <
    TFeatures extends TableFeatures,
    TData extends RowData,
    TValue extends CellData = CellData,
  >(
    header: Header<TFeatures, TData, TValue>,
  ) => void
  initRowInstanceData?: <
    TFeatures extends TableFeatures,
    TData extends RowData,
  >(
    row: Row<TFeatures, TData>,
  ) => void
  resetTableInstanceData?: <
    TFeatures extends TableFeatures,
    TData extends RowData,
  >(
    table: Table_Internal<TFeatures, TData>,
  ) => void
}
```

少しわかりにくいかもしれないので、それぞれのメソッドが何をするのかを順に見ていきましょう。

#### デフォルトのオプションと初期状態 {#default-options-and-initial-state}

<br />

##### getDefaultTableOptions {#getdefaulttableoptions}

テーブル機能の `getDefaultTableOptions` メソッドは、その機能のデフォルトのテーブルオプションを設定します。たとえば [Column Resizing](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.ts) 機能では、`getDefaultTableOptions` メソッドが `columnResizeMode` オプションのデフォルト値を `"onEnd"` に設定しています。

<br />

##### getDefaultColumnDef {#getdefaultcolumndef}

テーブル機能の `getDefaultColumnDef` メソッドは、その機能のデフォルトの列オプションを設定します。たとえば [Sorting](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.ts) 機能では、`getDefaultColumnDef` メソッドが列オプション `sortUndefined` のデフォルト値を `1` に設定しています。

<br />

##### getInitialState {#getinitialstate}

テーブル機能の `getInitialState` メソッドは、その機能のデフォルトの状態を設定します。たとえば [Pagination](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pagination/rowPaginationFeature.ts) 機能では、`getInitialState` メソッドが `pageSize` の状態のデフォルト値を `10` に、`pageIndex` の状態のデフォルト値を `0` に設定しています。

#### API を作るメソッド {#api-creators}

<br />

##### initTableInstanceData と resetTableInstanceData {#inittableinstancedata-and-resettableinstancedata}

`initTableInstanceData` は、1つのテーブルインスタンスに属する、変更可能でリアクティブでないデータに使います。たとえば、操作の起点（アンカー）や命令的に扱うキャッシュなどです。このメソッドは、テーブルオプション、状態のアトム、ストアが作られたあとに一度だけ実行されます。機能は登録順に1回の走査で処理され、各機能の初期化フックは、その機能の `constructTableAPIs` フックの直前に実行されます。そのため、フックの中では先に登録された機能のデータや API を前提にできます。

`resetTableInstanceData` は、`table.reset()` が実行されたときに、その一時的なデータを消去するために使います。リセットのフックは、テーブルが内部で持つ状態のアトムが `table.initialState` に戻されたあとに実行されます。テーブルの状態のスライスや外部で制御される状態はリセットしません。また、`table.reset()` で `initTableInstanceData` が再実行されることはありません。

API の割り当ては `constructTableAPIs` で行ってください。初期化とリセットのフックは、機能が持つデータのためのものです。

<br />

##### constructTableAPIs {#constructtableapis}

テーブル機能の `constructTableAPIs` メソッドは、`table` インスタンスにメソッドを追加することだけを担当します。このメソッドは、機能が持つテーブルインスタンスのデータがすべて初期化されたあとに実行されます。たとえば [Row Selection](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.ts) 機能では、`constructTableAPIs` メソッドが `toggleAllRowsSelected`、`getIsAllRowsSelected`、`getIsSomeRowsSelected` など、多くのテーブルインスタンスの API メソッドを追加しています。つまり、`table.toggleAllRowsSelected()` を呼ぶときは、`rowSelectionFeature` 機能がテーブルインスタンスに追加したメソッドを呼んでいることになります。

<br />

##### assignHeaderPrototype と initHeaderInstanceData {#assignheaderprototype-and-initheaderinstancedata}

テーブル機能の `assignHeaderPrototype` メソッドは、共有される `header` のプロトタイプにメソッドを追加します。たとえば [Column Sizing](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.ts) 機能は、`getStart` などのヘッダーインスタンスの API メソッドを追加しています。つまり、`header.getStart()` を呼ぶときは、列幅の機能が追加したメソッドを呼んでいることになります。`initHeaderInstanceData` メソッドは、共有のプロトタイプには置けない、ヘッダーごとのインスタンスデータやキャッシュのために使えます。このメソッドはヘッダーの構築中、サブヘッダーが設定される前、かつヘッダーがヘッダーグループに結び付けられる前に実行されます。ヘッダーはヘッダーグループが再計算されるたびに作り直されるため、作り直しのたびに再実行されます。

<br />

##### initHeaderGroupInstanceData {#initheadergroupinstancedata}

`initHeaderGroupInstanceData` メソッドは、ヘッダーグループごとのインスタンスデータのために使えます。ヘッダーグループには共有のプロトタイプがないため、インスタンスごとに拡張できるのはこのメソッドだけです。このメソッドは、ヘッダーグループの `depth`、`id`、要素がすべてそろった `headers` 配列が割り当てられたあとに実行され、ヘッダーグループが作り直されるたびに再実行されます。

<br />

##### assignColumnPrototype と initColumnInstanceData {#assigncolumnprototype-and-initcolumninstancedata}

テーブル機能の `assignColumnPrototype` メソッドは、共有される `column` のプロトタイプにメソッドを追加します。たとえば [Sorting](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-sorting/rowSortingFeature.ts) 機能は、`getNextSortingOrder`、`toggleSorting` などの列インスタンスの API メソッドを追加しています。つまり、`column.toggleSorting()` を呼ぶときは、行のソート機能が追加したメソッドを呼んでいることになります。`initColumnInstanceData` メソッドは、共有のプロトタイプには置けない、列ごとのインスタンスデータやキャッシュのために使えます。たとえば [Aggregation](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.ts) 機能は、このメソッドで列ごとの集計キャッシュを用意しています。

<br />

##### assignRowPrototype と initRowInstanceData {#assignrowprototype-and-initrowinstancedata}

テーブル機能の `assignRowPrototype` メソッドは、共有される `row` のプロトタイプにメソッドを追加します。`initRowInstanceData` メソッドは、共有のプロトタイプには置けない、行ごとのインスタンスデータやキャッシュのために使えます。たとえば [Row Selection](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.ts) 機能は、`toggleSelected` や `getIsSelected` などの行インスタンスの API メソッドを追加しています。

<br />

##### assignCellPrototype と initCellInstanceData {#assigncellprototype-and-initcellinstancedata}

テーブル機能の `assignCellPrototype` メソッドは、共有される `cell` のプロトタイプにメソッドを追加します。たとえば、列のグループ化の機能は `getIsGrouped` と `getIsPlaceholder` を、集計の機能は `getIsAggregated` を追加しています。`initCellInstanceData` メソッドは、共有のプロトタイプには置けない、セルごとのインスタンスデータやキャッシュのために使えます。セルは行と列の組み合わせごとに初めてアクセスされたときに遅延して作られ、キャッシュされます。そのため、このメソッドはセルのインスタンスごとに一度だけ実行されます。

### カスタム機能を追加する {#adding-a-custom-feature}

仮のユースケースを例に、カスタムのテーブル機能を作ってみましょう。ここでは、テーブルの「密度」（セルのパディング）をユーザーが変えられる機能をテーブルインスタンスに追加したいとします。

完全な実装は [custom-plugin](https://tanstack.com/table/latest/docs/framework/react/examples/custom-plugin) のサンプルを参照してください。ここでは、カスタム機能を作る手順を詳しく見ていきます。

#### ステップ1: TypeScript の型を用意する {#step-1-set-up-typescript-types}

TanStack Table の組み込みの機能と同じ完全な型安全性がほしいと仮定して、新しい機能のための TypeScript の型をすべて用意しましょう。新しいテーブルオプション、状態、テーブルインスタンスの API メソッドの型を作ります。

これらの型の名前は TanStack Table の内部で使われている命名規則に従っていますが、好きな名前を付けて構いません。この時点ではまだ TanStack Table に型を追加していません。追加は次のステップで行います。

```ts
// define types for our new feature's custom state
export type DensityState = 'sm' | 'md' | 'lg'
export interface TableState_Density {
  density: DensityState
}

// define types for our new feature's table options
export interface TableOptions_Density {
  enableDensity?: boolean
  onDensityChange?: OnChangeFn<DensityState>
}

// Define types for our new feature's table APIs
export interface Table_Density {
  setDensity: (updater: Updater<DensityState>) => void
  toggleDensity: (value?: DensityState) => void
}
```

#### ステップ2: TanStack Table の機能マップに機能を追加する {#step-2-add-the-feature-to-tanstack-tables-feature-maps}

TanStack Table は、`tableFeatures({ ... })` に渡されたキーをもとに、テーブルにどの機能の状態・オプション・API があるかを推論します。カスタム機能のキーを型安全にするには、宣言のマージ（declaration merging）を使って、エクスポートされている `Plugins`、`TableState_FeatureMap`、`TableOptions_FeatureMap`、`Table_FeatureMap` の各インターフェースにキーを追加します。

```ts
declare module '@tanstack/react-table' {
  interface Plugins {
    densityPlugin: TableFeature
  }

  interface TableState_FeatureMap {
    densityPlugin: TableState_Density
  }

  interface TableOptions_FeatureMap<
    TFeatures extends TableFeatures,
    TData extends RowData,
  > {
    densityPlugin: TableOptions_Density
  }

  interface Table_FeatureMap<
    TFeatures extends TableFeatures,
    TData extends RowData,
  > {
    densityPlugin: Table_Density
  }
}
```

この方法で機能を登録すると、TypeScript は `features` に `densityPlugin` を含むテーブルに限って、その機能の状態・オプション・API を推論できるようになります。

#### ステップ3: 機能オブジェクトを作る {#step-3-create-the-feature-object}

TypeScript の準備が済んだので、新しい機能の機能オブジェクトを作りましょう。ここで、テーブルインスタンスに追加するすべてのメソッドを定義します。

機能オブジェクトを正しく作れているかを確かめるために、`TableFeature` 型を使ってください。TypeScript の型が正しく用意できていれば、新しい状態・オプション・インスタンス API を持つ機能オブジェクトを作っても、TypeScript のエラーは出ないはずです。

```ts
export const densityPlugin: TableFeature = {
  // define the new feature's initial state
  getInitialState: (initialState) => {
    return {
      density: 'md',
      ...initialState, // must come last
    }
  },

  // define the new feature's default options
  getDefaultTableOptions: (table) => {
    return {
      enableDensity: true,
      onDensityChange: makeStateUpdater('density', table),
    }
  },
  // if you need to add a default column definition...
  // getDefaultColumnDef: () => {},

  // define the new feature's table instance methods
  constructTableAPIs: (table) => {
    assignTableAPIs('densityPlugin', table, {
      table_setDensity: {
        fn: (updater: Updater<DensityState>) => {
          const safeUpdater: Updater<DensityState> = (old) => {
            const newState = functionalUpdate(updater, old)
            return newState
          }
          return table.options.onDensityChange?.(safeUpdater)
        },
      },
      table_toggleDensity: {
        fn: (value?: DensityState) => {
          const safeUpdater: Updater<DensityState> = (old) => {
            if (value) return value
            return old === 'lg' ? 'md' : old === 'md' ? 'sm' : 'lg'
          }
          return table.options.onDensityChange?.(safeUpdater)
        },
      },
    })
  },

  // if you need to add row instance APIs...
  // assignRowPrototype: (prototype, table) => {},
  // initRowInstanceData: (row) => {},
  // if you need to add cell instance APIs...
  // assignCellPrototype: (prototype, table) => {},
  // initCellInstanceData: (cell) => {},
  // if you need to add column instance APIs...
  // assignColumnPrototype: (prototype, table) => {},
  // initColumnInstanceData: (column) => {},
  // if you need to add header instance APIs...
  // assignHeaderPrototype: (prototype, table) => {},
  // initHeaderInstanceData: (header) => {},
  // if you need to add header group instance data...
  // initHeaderGroupInstanceData: (headerGroup) => {},
}
```

#### ステップ4: テーブルに機能を追加する {#step-4-add-the-feature-to-the-table}

機能オブジェクトができたら、それを `tableFeatures()` の呼び出しに含め、その結果をテーブルインスタンスを作るときに `features` オプションに渡します。これで機能がテーブルインスタンスに追加されます。

```ts
const features = tableFeatures({ densityPlugin })

const table = useTable({
  features,
  columns,
  data,
  //..
})
```

#### ステップ5: アプリケーションで機能を使う {#step-5-use-the-feature-in-your-application}

機能がテーブルインスタンスに追加されたので、新しいインスタンス API、オプション、状態をアプリケーションで使えます。[custom-plugin のサンプル](https://tanstack.com/table/latest/docs/framework/react/examples/custom-plugin)では、`React.useState` と新しい `onDensityChange` オプションで `density` の状態を制御しています。

```tsx
const features = tableFeatures({ densityPlugin })

const [density, setDensity] = React.useState<DensityState>('md')

const table = useTable({
  features,
  columns,
  data,
  //...
  state: {
    density, // passing the density state to the table, TS is still happy :)
  },
  onDensityChange: setDensity,
})
//...
return (
  <td
    key={cell.id}
    style={{
      //using our new feature in the code
      padding: density === 'sm' ? '4px' : density === 'md' ? '8px' : '16px',
      transition: 'padding 0.2s',
    }}
  >
    <table.FlexRender cell={cell} />
  </td>
)
```

#### 必ずこの方法で作る必要があるのか {#do-we-have-to-do-it-this-way}

これは、TanStack Table の組み込みの機能と並べて独自のコードを統合するための新しい方法の1つにすぎません。上の例でも、`density` の状態を `React.useState` に保存し、`toggleDensity` のハンドラーを好きな場所に定義して、テーブルインスタンスとは別にコードの中で使うこともできました。テーブルインスタンスに深く統合せずに、TanStack Table と並べてテーブルの機能を作るのも、カスタム機能を作るうえでまったく問題のない方法です。ユースケースによっては、この方法が TanStack Table をカスタム機能で拡張する最もすっきりした方法になるとは限りません。
