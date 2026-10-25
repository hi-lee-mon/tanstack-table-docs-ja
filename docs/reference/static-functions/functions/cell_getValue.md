---
id: cell_getValue
title: cell_getValue
---

```ts
function cell_getValue<TFeatures, TData, TValue>(cell): TValue;
```

定義元: [core/cells/coreCellsFeature.utils.ts:16](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.utils.ts#L16)

このセルが属する行と列から、セルのアクセサーの値を読み取ります。

これは `cell.getValue()` の裏にある単独の実装です。セルのプロトタイプのメソッドを呼ぶ代わりに、静的な API を import して使う場合に便利です。

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

`TValue`

## 例 {#example}

```ts
const value = cell_getValue(cell)
```
