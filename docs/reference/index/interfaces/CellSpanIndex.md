---
id: CellSpanIndex
title: CellSpanIndex
---

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:13](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L13)

現在描画されている行についての、テーブルのセル結合インデックスです。

Cell API がこれを読みます。Devtools や、結合の起点が描画中の範囲のどこにあるかを知る必要がある仮想化ライブラリのために公開されています。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### colSpans {#colspans}

```ts
colSpans: (Int32Array<ArrayBufferLike> | undefined)[];
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:23](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L23)

描画順の行位置ごとの列の結合数で、描画順の列位置をインデックスにしています。
ほとんどの行は空きになります。列の結合を宣言した行だけが配列を持ちます。保存された配列では、結合するセルが結合数を、覆われるセルが `0` を持ち、それ以外のセルは `1` を持ちます。

***

### columnIndexes {#columnindexes}

```ts
columnIndexes: Record<string, number>;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:27](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L27)

表示中の各列 ID に対する描画順のインデックスです。非表示の列は含まれません。

***

### rows {#rows}

```ts
rows: readonly Row<TFeatures, TData>[];
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:40](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L40)

このインデックスの元になった行を、描画順どおりに並べたものです。上に固定された行、（ページ分割された）中央の行、下に固定された行の順です。
セルを読むときはこれと比べて、古くなった行位置をはじきます。

***

### rowSpans {#rowspans}

```ts
rowSpans: Record<string, Int32Array>;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:34](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L34)

列 ID ごとの行の結合数で、描画順の行位置をインデックスにしています。
2行以上にわたる結合が1つでもできた列だけがここに入ります。列がない場合は、その列のどのセルもちょうど1行分です。保存された配列では、結合の起点の行が結合の長さを、覆われる行が `0` を持ちます。
