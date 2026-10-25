---
id: cell_getIsCovered
title: cell_getIsCovered
---

```ts
function cell_getIsCovered<TFeatures, TData, TValue>(cell): boolean;
```

定義元: [features/cell-spanning/cellSpanningFeature.utils.ts:425](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.utils.ts#L425)

他のセルの結合がこのセルを覆っているかどうかを判定します。

覆われたセルは描画してはいけません。内容と結合の属性は、覆っている側のセルが持ちます。

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

`boolean`

## 例 {#example}

```ts
const isCovered = cell_getIsCovered(cell)
```
