---
id: table_getFocusedCell
title: table_getFocusedCell
---

```ts
function table_getFocusedCell<TFeatures, TData>(table):
  | Cell<TFeatures, TData, any>
  | undefined;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:728](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L728)

アクティブなセル、つまり直近の操作のアンカーを返します。

フォーカスは保存せずに導き出します。スプレッドシートの考え方では、A1 から C5 までドラッグしてもアクティブなセルは A1 のままなので、アクティブな範囲のアンカーがそのままアクティブなセルになります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

  \| [`Cell`](../../index/type-aliases/Cell.md)\<`TFeatures`, `TData`, `any`\>
  \| `undefined`

## 例 {#example}

```ts
const cell = table_getFocusedCell(table)
```
