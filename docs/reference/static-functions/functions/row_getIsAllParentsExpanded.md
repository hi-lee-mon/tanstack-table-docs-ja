---
id: row_getIsAllParentsExpanded
title: row_getIsAllParentsExpanded
---

```ts
function row_getIsAllParentsExpanded<TFeatures, TData>(row): boolean;
```

定義元: [features/row-expanding/rowExpandingFeature.utils.ts:403](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-expanding/rowExpandingFeature.utils.ts#L403)

この行の祖先がすべて展開されているかどうかを判定します。

現在の行は対象にせず、親をさかのぼる連なりだけをたどります。

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
const parentsExpanded = row_getIsAllParentsExpanded(row)
```
