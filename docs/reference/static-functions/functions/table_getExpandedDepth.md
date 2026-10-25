---
id: table_getExpandedDepth
title: table_getExpandedDepth
---

```ts
function table_getExpandedDepth<TFeatures, TData>(table): number;
```

定義元: [features/row-expanding/rowExpandingFeature.utils.ts:250](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.utils.ts#L250)

展開された行 ID のうち、いちばん深い深さを計算します。

行 ID は `.` で分割されます。「すべて展開」の状態では現在の行モデルの展開できる行を走査し、明示的な展開状態ではその展開済み ID のキーを走査します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`number`

## 例 {#example}

```ts
const depth = table_getExpandedDepth(table)
```
