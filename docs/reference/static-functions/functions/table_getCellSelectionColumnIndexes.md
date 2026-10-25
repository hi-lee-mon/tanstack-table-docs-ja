---
id: table_getCellSelectionColumnIndexes
title: table_getCellSelectionColumnIndexes
---

```ts
function table_getCellSelectionColumnIndexes<TFeatures, TData>(table): Record<string, number>;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:168](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L168)

列 ID から描画順のインデックスへのマップを作ります。

`columnOrderingFeature` がなくても検索結果がメモ化されたままになるよう、この機能が登録しています。その機能の静的関数 `getColumnIndexes` は呼ぶたびに4つのマップをすべて作り直すので、そのままだとセルごとの読み取りが O(列数) になってしまうためです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

`Record`\<`string`, `number`\>

## 例 {#example}

```ts
const index = table_getCellSelectionColumnIndexes(table)[columnId]
```
