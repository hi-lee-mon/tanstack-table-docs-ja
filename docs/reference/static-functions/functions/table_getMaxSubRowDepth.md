---
id: table_getMaxSubRowDepth
title: table_getMaxSubRowDepth
---

```ts
function table_getMaxSubRowDepth<TFeatures, TData>(table): number;
```

定義元: [core/rows/coreRowsFeature.utils.ts:159](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/rows/coreRowsFeature.utils.ts#L159)

コア行モデルで、構造上いちばん深い行の深さを返します。
ルートの行は深さ `0`、その直下のサブ行は深さ `1` で、以降も同様です。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`number`
