---
id: table_getEndFooterGroups
title: table_getEndFooterGroups
---

```ts
function table_getEndFooterGroups<TFeatures, TData>(table): HeaderGroup<TFeatures, TData>[];
```

定義元: [features/column-pinning/columnPinningFeature.utils.ts:483](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.utils.ts#L483)

末尾の固定領域について、フッターグループを作ります。

フッターグループは、末尾のヘッダーグループを逆の順で使い回します。

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
const footerGroups = table_getEndFooterGroups(table)
```
