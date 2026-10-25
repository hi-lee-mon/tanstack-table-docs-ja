---
id: cell_getRowSpan
title: cell_getRowSpan
---

```ts
function cell_getRowSpan<TFeatures, TData, TValue>(cell): number;
```

定義元: [features/cell-spanning/cellSpanningFeature.utils.ts:366](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.utils.ts#L366)

このセルが結合する行の数を返します。

結合しない場合は `1`、上にある結合セルに覆われている場合は `0` です。`0` が「このセルを描画しない」を意味する `header.rowSpan` の決まりと同じです。

あえてメモ化していません。セルごとにメモ化すると、すべてのセルでクロージャーと依存関係の配列が作られ、テーブル単位の結合インデックスを2回引くだけの処理よりもコストがかかるためです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### cell {#cell}

[`Cell`](../../index/type-aliases/Cell.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

`number`

## 例 {#example}

```ts
const rowSpan = cell_getRowSpan(cell)
```
