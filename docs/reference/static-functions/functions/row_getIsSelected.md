---
id: row_getIsSelected
title: row_getIsSelected
---

```ts
function row_getIsSelected<TFeatures, TData>(row): boolean;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:571](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L571)

この行 ID が `state.rowSelection` で選択されているかどうかを判定します。

含まれない行 ID は、選択されていないものとして扱います。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const selected = row_getIsSelected(row)
```
