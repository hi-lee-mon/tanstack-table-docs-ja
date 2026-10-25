---
id: row_toggleSelected
title: row_toggleSelected
---

```ts
function row_toggleSelected<TFeatures, TData>(
   row,
   value?,
   opts?): void;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:534](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L534)

この行を選択または選択解除します。

`value` を省略すると、行を切り替えます。`opts.selectChildren` が `false` の場合、サブ行の選択が無効な場合、行が単一選択にしか対応していない場合を除き、子の行も再帰的に選択されます。
この行を選択解除したときに祖先の行 ID も選択から取り除くには、`deselectParents: true` を渡してください。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

### value? {#value}

`boolean`

### opts? {#opts}

[`ToggleSelectedOptions`](../../index/interfaces/ToggleSelectedOptions.md)

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
row_toggleSelected(row)
row_toggleSelected(row, true)
row_toggleSelected(row, false)
row_toggleSelected(row, true, { selectChildren: false })
row_toggleSelected(row, false, { deselectParents: true })
```
