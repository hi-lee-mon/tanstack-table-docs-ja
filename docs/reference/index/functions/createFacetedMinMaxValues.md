---
id: createFacetedMinMaxValues
title: createFacetedMinMaxValues
---

```ts
function createFacetedMinMaxValues<TFeatures, TData>(): (table, columnId) => () => [number, number] | undefined;
```

定義元: [features/column-faceting/createFacetedMinMaxValues.ts:17](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/createFacetedMinMaxValues.ts#L17)

ファセットによるフィルタリング向けに、メモ化されたファセットの最小値・最大値ヘルパーを作成します。

返される関数は、テーブルの行モデルと関係するフィルターの状態からファセットのデータを導き出します。これにより、フィルターの UI で選択可能な値を表示できます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

## 戻り値 {#returns}

(`table`, `columnId`) => () => \[`number`, `number`\] \| `undefined`
