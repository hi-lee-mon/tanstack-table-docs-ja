---
id: table_getHeaderGroups
title: table_getHeaderGroups
---

```ts
function table_getHeaderGroups<TFeatures, TData>(table): HeaderGroup<TFeatures, TData>[];
```

定義元: [core/headers/coreHeadersFeature.utils.ts:80](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/headers/coreHeadersFeature.utils.ts#L80)

現在の列ツリーについて、表示するヘッダーグループを作ります。

グループを作る前に、列の表示と固定を適用します。固定された列がなければ、固定の区分けを省いた速い経路を通ります。

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
const headerGroups = table_getHeaderGroups(table)
```
