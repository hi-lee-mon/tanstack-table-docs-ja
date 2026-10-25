---
id: ColumnDef_CellSpanning
title: ColumnDef_CellSpanning
---

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:78](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L78)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](../type-aliases/CellData.md) = [`CellData`](../type-aliases/CellData.md)

## プロパティ {#properties}

### enableCellSpanning? {#enablecellspanning}

```ts
optional enableCellSpanning?: boolean;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:87](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L87)

テーブルがセル結合を許可していても、この列ではセル結合を無効にします。既定値は `true` です。

***

### spanColumns? {#spancolumns}

```ts
optional spanColumns?: number | ((context) => number);
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:102](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L102)

この列のセルを、行ごとに指定した数の列にわたって結合します。結合は自分の列から始まり、実際に描画される列の順で数えます。

`1` 以下を返すと結合しません。大きすぎる値は、そのセルが属する固定領域の端までに切り詰められるので、結合が先頭固定・中央・末尾固定の境界をまたぐことはありません。「自分の領域の残りすべて」にしたい場合は `Infinity` を渡してください。非表示の列は数えません。

#### 例 {#example}

```ts
{ accessorKey: 'label', spanColumns: ({ row }) => row.original.isSummary ? Infinity : 1 }
```

***

### spanRows? {#spanrows}

```ts
optional spanRows?: boolean | ((context) => boolean);
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:127](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L127)

この列で隣り合う行を、縦に結合した1つのセルにまとめます。

`true` を指定すると、この列の値が同じ（`Object.is`）行どうしを結合します。既定の比較では、null や undefined の値は結合されません。

述語関数を渡すと比較処理を丸ごと置き換え、`row` を `anchorRow` から始まる結合に加えるかどうかを決めます。null や undefined の値を結合してもかまいません。
この関数は、結合インデックスを作り直すたびに候補の行ごとに1回呼ばれ、呼び出しごとにコンテキストのオブジェクトを1つ作ります。処理は軽くしてください。

結合は常に実際に描画される行から計算し直されるので、ソート・フィルタリング・ページ送りで変わるのは、どの行が隣り合うかだけです。
結合は、ページの境界、固定された行のセクションの境界、行ツリー内での位置の変化、グループ行をまたぎません。この列がグループ化されている間は無視されます。

#### 例 {#example-1}

```ts
{ accessorKey: 'department', spanRows: true }
```
