---
id: createFacetedRowModel
title: createFacetedRowModel
---

```ts
function createFacetedRowModel<TFeatures, TData>(): (table, columnId) => () => RowModel<TFeatures, TData>;
```

定義元: [features/column-faceting/createFacetedRowModel.ts:18](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/createFacetedRowModel.ts#L18)

メモ化されたファセット行モデルのファクトリーを作成します。

ファクトリーは関係するテーブルの状態のアトムとオプションを読み取り、テーブルの行モデルのパイプラインで使う行モデル関数を返します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md) = `any`

## 戻り値 {#returns}

(`table`, `columnId`) => () => [`RowModel`](../interfaces/RowModel.md)\<`TFeatures`, `TData`\>
