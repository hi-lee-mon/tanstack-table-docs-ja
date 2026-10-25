---
id: row_getPinnedIndex
title: row_getPinnedIndex
---

```ts
function row_getPinnedIndex<TFeatures, TData>(row): number;
```

定義元: [features/row-pinning/rowPinningFeature.utils.ts:260](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-pinning/rowPinningFeature.utils.ts#L260)

固定領域の中で、この行の表示上のインデックスを探します。

固定されていない行は `-1` を返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`number`

## 例 {#example}

```ts
const index = row_getPinnedIndex(row)
```
