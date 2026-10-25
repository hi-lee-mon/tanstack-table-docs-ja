---
id: isSubRowSelected
title: isSubRowSelected
---

```ts
function isSubRowSelected<TFeatures, TData>(row): boolean | "some" | "all";
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:1013](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L1013)

行の選択可能な子孫が、すべて・一部・まったく選択されていないのいずれかを返します。

この結果は、行選択の中間状態（indeterminate）の UI を動かすために使います。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`boolean` \| `"some"` \| `"all"`

## 例 {#example}

```ts
const selectedState = isSubRowSelected(row)
```
