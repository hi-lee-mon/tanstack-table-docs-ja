---
id: table_getStartFooterGroups
title: table_getStartFooterGroups
---

```ts
function table_getStartFooterGroups<TFeatures, TData>(table): HeaderGroup<TFeatures, TData>[];
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:461](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L461)

先頭の固定領域について、フッターグループを作ります。

フッターグループは、先頭のヘッダーグループを逆の順で使い回します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`HeaderGroup`](../../index/interfaces/HeaderGroup.md)\<`TFeatures`, `TData`\>[]

## 例 {#example}

```ts
const footerGroups = table_getStartFooterGroups(table)
```
