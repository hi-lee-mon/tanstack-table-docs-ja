---
id: row_getParentRow
title: row_getParentRow
---

```ts
function row_getParentRow<TFeatures, TData>(row):
  | Row<TFeatures, TData>
  | undefined;
```

定義元: [core/rows/coreRowsFeature.utils.ts:184](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.utils.ts#L184)

この行に直接の親があれば、それを探します。

親を探すときは、構造上の親についてはコア行モデルを先に見て、生成された親の行についてはページネーション前の行モデルを見ます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

  \| [`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>
  \| `undefined`

## 例 {#example}

```ts
const parent = row_getParentRow(row)
```
