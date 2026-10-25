---
id: cell_renderValue
title: cell_renderValue
---

```ts
function cell_renderValue<TFeatures, TData, TValue>(cell): any;
```

定義元: [core/cells/coreCellsFeature.utils.ts:35](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/cells/coreCellsFeature.utils.ts#L35)

このセルに描画する値を読み取ります。

アクセサーの値が null や undefined の場合は `table.options.renderFallbackValue` に置き換えます。`cell.renderValue()` と同じ動作です。

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

`any`

## 例 {#example}

```ts
const rendered = cell_renderValue(cell)
```
