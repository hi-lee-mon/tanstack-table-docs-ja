---
id: createFacetedUniqueValues
title: createFacetedUniqueValues
---

```ts
function createFacetedUniqueValues<TFeatures, TData>(): (table, columnId) => () => Map<any, number>;
```

定義元: [features/column-faceting/createFacetedUniqueValues.ts:17](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/createFacetedUniqueValues.ts#L17)

ファセットによるフィルタリング向けに、メモ化されたファセットの一意な値のヘルパーを作成します。

返される関数は、テーブルの行モデルと関係するフィルターの状態からファセットのデータを導き出します。これにより、フィルターの UI で選択可能な値を表示できます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

## 戻り値 {#returns}

(`table`, `columnId`) => () => `Map`\<`any`, `number`\>
