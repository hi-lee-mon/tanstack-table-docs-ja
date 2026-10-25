---
id: TableOptions_Rows
title: TableOptions_Rows
---

定義元: [core/rows/coreRowsFeature.types.ts:107](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L107)

## 継承先 {#extended-by}

- [`TableOptions_Core`](TableOptions_Core.md)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getRowId? {#getrowid}

```ts
optional getRowId?: (originalRow, index, parent?) => string;
```

定義元: [core/rows/coreRowsFeature.types.ts:115](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L115)

各行の一意な ID を導き出すための関数です（省略可能）。指定しない場合は行のインデックスが使われます（入れ子の行は、祖先のインデックスを `.` でつないだもの、たとえば `index.index.index` になります）。
サーバーサイドの処理から来た個々の行を識別する必要がある場合は、この関数で、通信やあいまいさに左右されない意味のある ID（userId、taskId、データベースの ID フィールドなど）を返すことをおすすめします。

#### パラメーター {#parameters}

##### originalRow {#originalrow}

`TData`

##### index {#index}

`number`

##### parent? {#parent}

[`Row`](../type-aliases/Row.md)\<`TFeatures`, `TData`\>

#### 戻り値 {#returns}

`string`

#### 例 {#example}

```ts
getRowId: row => row.userId
```

***

### getSubRows? {#getsubrows}

```ts
optional getSubRows?: (originalRow, index) => readonly TData[] | undefined;
```

定義元: [core/rows/coreRowsFeature.types.ts:124](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.types.ts#L124)

各行のサブ行を取り出すための関数です（省略可能）。入れ子の行を使う場合は、この関数で行からサブ行のオブジェクト（または undefined）を返す必要があります。

#### パラメーター {#parameters-1}

##### originalRow {#originalrow-1}

`TData`

##### index {#index-1}

`number`

#### 戻り値 {#returns-1}

readonly `TData`[] \| `undefined`

#### 例 {#example-1}

```ts
getSubRows: row => row.subRows
```
